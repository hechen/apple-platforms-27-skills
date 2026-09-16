#!/usr/bin/env python3
"""Read selected Apple SDK metadata and public declaration context; no mutations."""
import argparse
from pathlib import Path
import subprocess
import sys


def command(*args):
    return subprocess.check_output(args, text=True, stderr=subprocess.STDOUT).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sdk', choices=['macosx', 'iphoneos', 'iphonesimulator'], default='macosx')
    parser.add_argument('--framework', help='Public framework name, such as SwiftUI')
    parser.add_argument('--symbol', help='Literal substring to locate, not a regular expression')
    parser.add_argument('--limit', type=int, default=8, help='Maximum declaration matches to print')
    args = parser.parse_args()
    if bool(args.framework) != bool(args.symbol):
        parser.error('--framework and --symbol must be supplied together')
    if args.limit < 1 or args.limit > 100:
        parser.error('--limit must be between 1 and 100')
    if args.framework and (not args.framework.replace('_', '').isalnum()):
        parser.error('--framework must be a framework name, not a path')
    try:
        print(command('xcodebuild', '-version'))
        sdk = Path(command('xcrun', '--sdk', args.sdk, '--show-sdk-path'))
        print('SDK:', args.sdk, command('xcrun', '--sdk', args.sdk, '--show-sdk-version'))
        print('Path:', sdk)
        if not args.framework:
            return 0
        base = sdk / 'System/Library/Frameworks' / (args.framework + '.framework')
        if not base.is_dir():
            print('Framework not present in this SDK.', file=sys.stderr)
            return 2
        interfaces = sorted(base.rglob('*.swiftinterface'))
        interfaces = [p for p in interfaces if '.private.' not in p.name and '.package.' not in p.name]
        # Prefer a native arm64 interface; Catalyst is a different target.
        native = [p for p in interfaces if 'macabi' not in p.name and p.name.startswith(('arm64-', 'arm64e-'))]
        candidates = native[:1] or interfaces[:1]
        # Some frameworks expose declarations through Clang headers/re-exports.
        candidates += sorted(p for p in base.rglob('*.h') if 'PrivateHeaders' not in p.parts)
        count = 0
        seen = set()
        for path in candidates:
            resolved = path.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            lines = path.read_text(errors='replace').splitlines()
            for index, line in enumerate(lines):
                if args.symbol not in line:
                    continue
                print(f'\n{path}:{index + 1}')
                for n in range(max(0, index - 10), min(len(lines), index + 3)):
                    print(f'{n + 1}: {lines[n]}')
                count += 1
                if count >= args.limit:
                    print('\nMatch limit reached; narrow the symbol or increase --limit.')
                    return 0
        if not count:
            print('No match in the inspected public interface/headers. Check re-exported modules and Apple documentation; absence here is not proof of API absence.')
            return 1
        print('\nContext can omit enclosing availability attributes. Inspect the enclosing declaration and compile the target before relying on availability.')
        return 0
    except (OSError, subprocess.CalledProcessError) as error:
        print(f'Unable to inspect SDK: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
