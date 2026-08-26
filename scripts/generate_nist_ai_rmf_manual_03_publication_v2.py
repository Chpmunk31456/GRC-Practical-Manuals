#!/usr/bin/env python3
"""Manual 03 publication generator with semantic graph layout.

This wrapper replaces the first-pass linear Mermaid rendering with a layered
layout that preserves branch/fan-out relationships and visible feedback edges.
All document generation and QA logic remains in the controlled base generator.
"""

from __future__ import annotations

import re
from collections import defaultdict, deque
from pathlib import Path

from PIL import Image, ImageDraw

import generate_nist_ai_rmf_manual_03_publication as base


def parse_graph(block: str):
    labels: dict[str, str] = {}
    order: list[str] = []
    edges: list[tuple[str, str, str]] = []

    node_re = re.compile(
        r"\b([A-Za-z][A-Za-z0-9_]*)\s*(?:\[\[|\[|\(|\{)\s*[\"']?(.+?)[\"']?\s*(?:\]\]|\]|\)|\})"
    )
    edge_re = re.compile(
        r"\b([A-Za-z][A-Za-z0-9_]*)\b\s*(?:-->|---|-.->|==>)\s*(?:\|([^|]*)\|\s*)?([A-Za-z][A-Za-z0-9_]*)\b"
    )

    for raw in block.splitlines():
        line = raw.strip()
        if not line or line.startswith(("flowchart", "graph", "%%")):
            continue
        for match in node_re.finditer(line):
            node_id = match.group(1)
            label = re.sub(r"<br\s*/?>", " ", match.group(2), flags=re.I)
            label = base.clean_inline(label.strip("\"' "))[:180]
            if node_id not in labels:
                order.append(node_id)
            labels[node_id] = label
        for match in edge_re.finditer(line):
            src, edge_label, dst = match.group(1), (match.group(2) or "").strip(), match.group(3)
            edges.append((src, dst, base.clean_inline(edge_label)))
            for node_id in (src, dst):
                if node_id not in labels:
                    labels[node_id] = node_id
                    order.append(node_id)

    if not order:
        order = ["FLOW"]
        labels["FLOW"] = "AI risk-management relationship"
    return order, labels, edges


def layered_positions(order: list[str], edges: list[tuple[str, str, str]]):
    outgoing: dict[str, list[str]] = defaultdict(list)
    indegree = {node: 0 for node in order}
    for src, dst, _ in edges:
        if src == dst:
            continue
        outgoing[src].append(dst)
        if dst in indegree:
            indegree[dst] += 1

    roots = [node for node in order if indegree.get(node, 0) == 0]
    if not roots:
        roots = [order[0]]

    depth = {root: 0 for root in roots}
    queue = deque(roots)
    visits = defaultdict(int)
    while queue:
        src = queue.popleft()
        for dst in outgoing.get(src, []):
            if dst not in depth:
                depth[dst] = depth[src] + 1
                queue.append(dst)
            elif depth[dst] <= depth[src] and visits[dst] == 0:
                # Treat feedback/cycle edges as return relationships rather than
                # forcing the target below its source.
                pass
            visits[dst] += 1

    last_depth = max(depth.values(), default=0)
    for node in order:
        if node not in depth:
            last_depth += 1
            depth[node] = last_depth

    layers: dict[int, list[str]] = defaultdict(list)
    for node in order:
        layers[depth[node]].append(node)
    return depth, dict(sorted(layers.items()))


def render_mermaid_memory_graphic(block: str, out_path: Path, title: str) -> str:
    order, labels, edges = parse_graph(block)
    depth, layers = layered_positions(order, edges)

    width = 1900
    margin_x = 90
    margin_top = 160
    row_gap = 90
    box_h = 150
    layer_count = max(layers) + 1 if layers else 1
    height = max(650, margin_top + layer_count * (box_h + row_gap) + 100)
    canvas = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(canvas)
    title_font = base.font(34, bold=True)
    body_font = base.font(26)
    small_font = base.font(20)
    edge_font = base.font(18, bold=True)
    draw.text((margin_x, 48), title[:100], fill="black", font=title_font)

    positions: dict[str, tuple[int, int, int, int]] = {}
    for layer, nodes in layers.items():
        count = len(nodes)
        available = width - 2 * margin_x
        slot = available / max(1, count)
        box_w = int(min(820, max(360, slot - 45)))
        y = margin_top + layer * (box_h + row_gap)
        for idx, node in enumerate(nodes):
            cx = int(margin_x + slot * (idx + 0.5))
            x1 = cx - box_w // 2
            x2 = cx + box_w // 2
            positions[node] = (x1, y, x2, y + box_h)

    # Edges first, so boxes remain legible on top of lines.
    right_lane = width - 35
    feedback_index = 0
    for src, dst, edge_label in edges:
        if src not in positions or dst not in positions:
            continue
        a, b = positions[src], positions[dst]
        sx, sy = (a[0] + a[2]) // 2, a[3]
        tx, ty = (b[0] + b[2]) // 2, b[1]
        if depth.get(dst, 0) > depth.get(src, 0):
            mid_y = sy + max(20, (ty - sy) // 2)
            draw.line([(sx, sy), (sx, mid_y), (tx, mid_y), (tx, ty)], fill="#333333", width=4)
            draw.polygon([(tx, ty), (tx - 12, ty - 20), (tx + 12, ty - 20)], fill="#333333")
            if edge_label:
                label_x = int((sx + tx) / 2) + 8
                draw.text((label_x, mid_y - 24), edge_label[:45], fill="#333333", font=edge_font)
        else:
            # Feedback/cycle edge: route outside the node field so the return
            # relationship is explicit and never looks like a forward step.
            lane = right_lane - feedback_index * 25
            feedback_index += 1
            start = (a[2], (a[1] + a[3]) // 2)
            end = (b[2], (b[1] + b[3]) // 2)
            draw.line([start, (lane, start[1]), (lane, end[1]), end], fill="#555555", width=3)
            draw.polygon([(end[0], end[1]), (end[0] + 18, end[1] - 10), (end[0] + 18, end[1] + 10)], fill="#555555")
            draw.text((lane - 120, min(start[1], end[1]) + 8), "feedback", fill="#555555", font=small_font)

    for node in order:
        x1, y1, x2, y2 = positions[node]
        draw.rounded_rectangle((x1, y1, x2, y2), radius=18, outline="black", width=3, fill="#f6f6f6")
        label_lines = base.wrap_text(draw, labels[node], body_font, (x2 - x1) - 70)
        line_h = 33
        total_h = line_h * len(label_lines)
        yy = y1 + (box_h - total_h) // 2
        for line in label_lines:
            bbox = draw.textbbox((0, 0), line, font=body_font)
            xx = x1 + ((x2 - x1) - (bbox[2] - bbox[0])) // 2
            draw.text((xx, yy), line, fill="black", font=body_font)
            yy += line_h
        draw.text((x1 + 12, y1 + 8), node, fill="#555555", font=small_font)

    canvas.save(out_path, format="PNG", optimize=True)
    return (
        f"Memory graphic: {title}. Diagram contains {len(order)} labeled nodes and "
        f"{len(edges)} directed relationships. Branches are shown in shared horizontal "
        "layers and feedback relationships are routed separately."
    )


base.render_mermaid_memory_graphic = render_mermaid_memory_graphic

if __name__ == "__main__":
    raise SystemExit(base.main())
