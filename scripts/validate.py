#!/usr/bin/env python3
"""Validate skill metadata, portable links, and optional UI metadata."""
import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


def validate(root):
    root = Path(root).resolve()
    errors = []
    skills = sorted((root / 'skills').glob('*/SKILL.md'))
    if not skills:
        errors.append('No skills/*/SKILL.md files found')
    for entry in skills:
        relative = entry.relative_to(root)
        content = entry.read_text()
        match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', content, re.S)
        if not match:
            errors.append(f'{relative}: missing YAML frontmatter')
            continue
        try:
            meta = yaml.safe_load(match.group(1))
        except yaml.YAMLError as error:
            errors.append(f'{relative}: invalid YAML: {error}')
            continue
        if not isinstance(meta, dict):
            errors.append(f'{relative}: frontmatter must be a mapping')
            continue
        name = meta.get('name', '')
        if (not isinstance(name, str) or len(name) > 64 or
                not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or name != entry.parent.name):
            errors.append(f'{relative}: name must match its directory and use lowercase hyphenated words')
        description = meta.get('description')
        if not isinstance(description, str) or not description.strip() or len(description) > 1024:
            errors.append(f'{relative}: description must contain 1–1024 characters')
        if re.search(r'\[TODO:|\bTBD\b', content):
            errors.append(f'{relative}: unfinished scaffold')
        ui = entry.parent / 'agents/openai.yaml'
        if ui.exists():
            try:
                data = yaml.safe_load(ui.read_text())
                interface = data['interface']
                if not 25 <= len(interface['short_description']) <= 64:
                    errors.append(f'{ui.relative_to(root)}: invalid short description length')
                if '$' + name not in interface['default_prompt']:
                    errors.append(f'{ui.relative_to(root)}: default prompt references the wrong skill')
            except (yaml.YAMLError, KeyError, TypeError) as error:
                errors.append(f'{ui.relative_to(root)}: invalid optional interface metadata: {error}')
    for document in root.rglob('*.md'):
        if any(part in {'.git', '.venv', 'node_modules'} for part in document.relative_to(root).parts):
            continue
        content = document.read_text()
        if re.search(r'/(?:Users|home)/[A-Za-z0-9_.-]+/', content):
            errors.append(f'{document.relative_to(root)}: machine-specific home path')
        for target in re.findall(r'\]\(([^\s)]+)\)', content):
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith('#'):
                continue
            destination = (document.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(root):
                errors.append(f'{document.relative_to(root)}: link escapes repository: {target}')
            elif not destination.exists():
                errors.append(f'{document.relative_to(root)}: missing linked file: {target}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        print('\n'.join(errors))
        return 1
    count = len(list((args.root / 'skills').glob('*/SKILL.md')))
    print(f'Validated {count} skills, optional UI metadata, and local Markdown links.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
