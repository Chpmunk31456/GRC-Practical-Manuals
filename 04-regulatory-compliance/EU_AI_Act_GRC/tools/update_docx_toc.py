#!/usr/bin/env python3
"""Refresh DOCX table-of-contents fields through a running LibreOffice UNO service."""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import uno
from com.sun.star.beans import PropertyValue


def property_value(name: str, value: object) -> PropertyValue:
    item = PropertyValue()
    item.Name = name
    item.Value = value
    return item


def connect(port: int, attempts: int = 30, delay: float = 1.0):
    local_context = uno.getComponentContext()
    resolver = local_context.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", local_context
    )
    last_error: Exception | None = None
    for _ in range(attempts):
        try:
            return resolver.resolve(
                f"uno:socket,host=127.0.0.1,port={port};urp;StarOffice.ComponentContext"
            )
        except Exception as exc:  # UNO raises implementation-specific exceptions
            last_error = exc
            time.sleep(delay)
    raise RuntimeError(f"Unable to connect to LibreOffice UNO service: {last_error}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx")
    parser.add_argument("--port", type=int, default=2002)
    args = parser.parse_args()

    path = Path(args.docx).resolve()
    if not path.exists():
        raise FileNotFoundError(path)

    context = connect(args.port)
    service_manager = context.ServiceManager
    desktop = service_manager.createInstanceWithContext("com.sun.star.frame.Desktop", context)

    document = desktop.loadComponentFromURL(
        path.as_uri(),
        "_blank",
        0,
        (
            property_value("Hidden", True),
            property_value("ReadOnly", False),
        ),
    )
    if document is None:
        raise RuntimeError(f"LibreOffice could not open {path}")

    try:
        indexes = document.getDocumentIndexes()
        count = indexes.getCount()
        if count < 1:
            raise RuntimeError("DOCX contains no document index/TOC field to refresh")
        for index in range(count):
            indexes.getByIndex(index).update()
        document.calculateAll()
        document.store()
        print(f"Updated {count} document index(es) in {path}")
    finally:
        document.close(True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
