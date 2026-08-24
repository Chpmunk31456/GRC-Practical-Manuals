# Accessibility

The GRC Practical Manuals project is intended to be useful to people of different ages, abilities, backgrounds, languages, and income levels.

## Accessibility Goals

Repository documents should:

- Use plain language and define specialized terms
- Use a logical heading structure
- Use meaningful link text
- Avoid relying on color alone to communicate meaning
- Provide clear table headings and simple table structures
- Include alternative text for informative images
- Maintain readable contrast and text size
- Preserve a sensible reading order in Word and PDF editions
- Avoid unnecessary animation, flashing content, and decorative clutter

## Accessible Visual Learning

Follow the [project visual-learning standard](./VISUAL_LEARNING_STANDARD.md). A graphic must clarify a decision, workflow, mapping, timeline, hierarchy, data flow, or evidence-and-assurance relationship. It must not be included only as decoration.

Every informative graphic should:

- appear near the concept it explains;
- include localized labels and an accessible text explanation;
- preserve the same meaning when read without color;
- use a logical reading order and concise labels; and
- avoid simplifying a legal or technical obligation into a misleading rule.

The text explanation is part of the controlled content and must remain available in Markdown, Word, PDF, and other published formats.

## Review Workflow

When creating or revising a manual:

1. Review the source document’s headings, lists, tables, links, and image descriptions.
2. Use the accessibility checker available in the authoring application.
3. Confirm that keyboard navigation and reading order are logical.
4. Export the PDF with document tags and bookmarks when supported.
5. Test a sample with screen-reader or read-aloud software.
6. Correct the source document first, then regenerate derivative formats.
7. Record material accessibility changes in `CHANGELOG.md`.

Automated checks are useful but do not replace review by people with disabilities or users of assistive technology.

## Reporting an Accessibility Barrier

Open a GitHub issue and include:

- Manual and version
- File type
- Page or section
- Assistive technology or device, if relevant
- Description of the barrier
- Suggested correction, if known

Do not include private medical information.

## Alternative Formats

If a format is difficult to use, open an issue describing the format needed. The project is volunteer-led, so requests cannot be guaranteed, but accessibility needs will be considered in future revisions.
