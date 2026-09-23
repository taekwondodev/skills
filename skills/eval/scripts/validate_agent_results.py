from __future__ import annotations

import json
import re
from pathlib import Path


def reject_constant(value: str) -> None:
    raise ValueError(f'Non-JSON constant: {value}')


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    failures: list[str] = []
    contracts = sorted(root.glob('*/references/result-contract.md'))
    formats: dict[str, Path] = {}
    examples = 0
    consumers: set[Path] = set()
    referenced: set[Path] = set()
    if not contracts:
        failures.append('no result contracts found')
    for path in contracts:
        text = path.read_text()
        version = re.search(r'^## Shape: ([a-z]+/\d+)$', text, re.M)
        if version is None:
            failures.append(f'{path.relative_to(root)}: missing format heading')
            continue
        name = version.group(1)
        if name in formats:
            failures.append(f'duplicate format {name}')
        formats[name] = path
        blocks = re.findall(r'```json\n(.*?)\n```', text, re.S)
        if not blocks:
            failures.append(f'{name}: no examples')
        for index, block in enumerate(blocks):
            try:
                value = json.loads(block, parse_constant=reject_constant)
                assert isinstance(value, dict) and value.get('format') == name
                if name != 'review/1':
                    assert value.get('status') in {'complete', 'partial', 'blocked'}
                    assert isinstance(value.get('limits'), list)
                examples += 1
            except (ValueError, AssertionError):
                failures.append(f'{name}: invalid example {index + 1}')

    paths = sorted(set(root.glob('*/SKILL.md')) | set(contracts))
    paths.extend(sorted(root.glob('*/references/runner-prompt.md')))
    for path in paths:
        text = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        targets = re.findall(r'\]\(([^)\s]+)\)', text)
        for target in targets:
            if '://' in target or target.startswith('#'):
                continue
            resolved = (path.parent / target.split('#')[0]).resolve()
            if not resolved.is_file():
                failures.append(f'{path.relative_to(root)}: missing {target}')
            if resolved in contracts:
                consumers.add(path)
                referenced.add(resolved)
        if '## Agent result' in text and not any(
            'result-contract.md' in target for target in targets
        ):
            failures.append(f'{path.relative_to(root)}: result section has no contract')

    for path in set(contracts) - referenced:
        failures.append(f'{path.relative_to(root)}: unreferenced contract')

    print(f'formats={len(formats)} examples={examples} consumers={len(consumers)} failures={len(failures)}')
    for failure in failures:
        print(failure)
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
