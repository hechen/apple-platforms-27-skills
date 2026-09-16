# Contributing

Contributions should improve a concrete development decision, fix a verified API mistake, or make the same instructions work reliably across agents.

## Technical changes

- Link the relevant Apple documentation and identify the SDK/platform version.
- Distinguish compile-time availability, linked-SDK behavior, runtime availability, hardware support, and service eligibility.
- Preserve existing app behavior, deployment targets, and file formats unless a requested migration requires a change.
- Keep `SKILL.md` focused. Put substantial optional detail in a linked reference and avoid copying entire manuals.
- When correcting a beta-era name or behavior, show the current declaration or a focused compile reproduction.

## Portability

- Keep core workflows independent of any agent's proprietary tool names or invocation syntax.
- Preserve standard `name` and `description` frontmatter, relative resource links, and sibling skill names.
- Host-specific metadata must stay optional. Don't add required MCP servers or provider accounts merely to read a skill.
- Document installation tests separately from real agent activation or end-to-end app tests.
- Do not add personal paths, credentials, private project references, or local installation receipts.

## Validate locally

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s tests -v
```

On a Mac with the relevant 27 SDKs, also run:

```sh
bash scripts/check-sdk.sh
```

The portable checks validate packaging and references. The Swift probe covers selected APIs, not every framework mentioned in the collection. New executable helpers should have meaningful success/failure checks. For Markdown-only corrections, avoid tests that merely assert the wording you just wrote.
