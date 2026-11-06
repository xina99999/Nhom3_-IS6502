import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

class TestBuild(unittest.TestCase):
    def test_only_demo_page_is_published_and_version_matches(self):
        builder = Path(__file__).resolve().parent / 'build_site.py'
        with tempfile.TemporaryDirectory() as path:
            subprocess.run([sys.executable, str(builder)], cwd=path, check=True, env={**os.environ, 'GITHUB_SHA':'test-revision'})
            target = Path(path) / 'pr-flow-site'
            self.assertEqual({p.name for p in target.iterdir()}, {'index.html', 'version.json'})
            self.assertEqual(json.loads((target / 'version.json').read_text())['commit_sha'], 'test-revision')
            self.assertIn('test-revision', (target / 'index.html').read_text())
