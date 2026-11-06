"""Build an isolated public demonstration page; do not copy notebooks."""
import html
import json
import os
from pathlib import Path

revision = os.environ.get('GITHUB_SHA', 'local')
target = Path('pr-flow-site')
target.mkdir(exist_ok=True)
(target / 'version.json').write_text(json.dumps({'commit_sha': revision, 'environment': 'github-pages'}), encoding='utf-8')
(target / 'index.html').write_text('''<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Trang demo PR Flow</title><style>body{font:18px/1.6 system-ui;background:#f5f7fc;color:#17233b;margin:10vh auto;max-width:760px;padding:24px}main{background:white;padding:32px;border-radius:16px}code{overflow-wrap:anywhere}</style><main><h1>Trang thử nghiệm GitHub Actions</h1><p>Trang này dùng để thu thập dữ liệu cho bài tập Process Mining. Đây là môi trường demo.</p><p>Phiên bản thứ hai minh họa một thay đổi được đưa từ Pull Request qua kiểm thử đến triển khai.</p><p>Phiên bản: <code>''' + html.escape(revision) + '''</code></p><a href="version.json">Xem thông tin phiên bản</a></main></html>''', encoding='utf-8')
print('Built public demo page; no notebooks were copied.')
