"""Validate notebook files without executing code or uploading notebook content."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
notebooks = sorted(root.glob('**/*.ipynb'))
if not notebooks:
    raise SystemExit('No notebooks found')
for path in notebooks:
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data.get('cells'), list) or data.get('nbformat') != 4:
        raise SystemExit(f'Invalid notebook structure: {path.relative_to(root)}')
    print('OK:', path.relative_to(root))
print(f'Validated {len(notebooks)} notebooks; code cells were not executed.')
