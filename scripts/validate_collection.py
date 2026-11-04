"""Validate collection structure and exact preservation of the source snapshot."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'sources.json').read_text())
errors, names, hashes = [], [], {}
reference_count = 0
expected_skills = {item['name'] for item in manifest['skills']}
actual_skills = {p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')}
if actual_skills != expected_skills or len(actual_skills) != 20:
    errors.append('Skill inventory does not match the 20-source snapshot')
if (ROOT / 'SKILL.md').exists():
    errors.append('A root SKILL.md could shadow individual skills')
for item in manifest['skills']:
    directory = ROOT / 'skills' / item['name']
    skill_file = directory / 'SKILL.md'
    text = skill_file.read_text()
    parts = text.split('---', 2)
    try:
        assert text.startswith('---\n') and len(parts) == 3
        meta = yaml.safe_load(parts[1])
        name = meta['name']
        assert isinstance(name, str) and re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name)
        assert len(name) <= 64 and name == item['name']
        assert isinstance(meta['description'], str) and 0 < len(meta['description']) <= 1024
        assert not meta.get('metadata', {}).get('internal', False)
        names.append(name)
    except (AssertionError, KeyError, TypeError, yaml.YAMLError):
        errors.append(f'{skill_file.relative_to(ROOT)}: invalid or hidden skill frontmatter')
    expected_files = {f['path'] for f in item['files']}
    actual_files = {str(p.relative_to(directory)) for p in directory.rglob('*') if p.is_file()}
    if actual_files != expected_files:
        errors.append(f'{item["name"]}: source file inventory differs')
    for f in item['files']:
        path = directory / f['path']
        if not path.is_file():
            errors.append(f'Missing {path.relative_to(ROOT)}')
            continue
        data = path.read_bytes()
        digest = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        if digest != f['git_blob_sha']:
            errors.append(f'{path.relative_to(ROOT)}: source content changed')
        hashes.setdefault(digest, []).append(str(path.relative_to(ROOT)))
        if path.suffix != '.md':
            continue
        for target in re.findall(r'\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)', data.decode()):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or target.startswith('#'):
                continue
            relative = unquote(parsed.path)
            if not relative:
                continue
            reference_count += 1
            resolved = (path.parent / relative).resolve()
            if not resolved.is_relative_to(directory.resolve()) or not resolved.exists():
                errors.append(f'{path.relative_to(ROOT)}: missing or non-standalone reference {target}')
if len(set(names)) != len(names):
    errors.append('Duplicate skill names')
skill_hashes = [hashlib.sha256((ROOT / 'skills' / n / 'SKILL.md').read_bytes()).hexdigest() for n in names]
if len(set(skill_hashes)) != len(skill_hashes):
    errors.append('Duplicate SKILL.md content')
result = {'passed': not errors, 'skills': len(names), 'source_files': sum(len(s['files']) for s in manifest['skills']), 'local_markdown_references_checked': reference_count, 'duplicate_skill_names': len(names)-len(set(names)), 'duplicate_skill_bodies': len(skill_hashes)-len(set(skill_hashes)), 'repeated_supporting_file_groups': [v for v in hashes.values() if len(v)>1], 'errors': errors}
print(json.dumps(result, indent=2))
sys.exit(1 if errors else 0)
