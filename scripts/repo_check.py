from pathlib import Path
import nbformat
import re
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]

required = [
    REPO_ROOT / 'README.md',
    REPO_ROOT / 'requirements.txt',
    REPO_ROOT / '.gitignore',
    REPO_ROOT / 'notebooks' / '01_data_preprocessing.ipynb',
    REPO_ROOT / 'notebooks' / '02_eda_kpi_funnel_segments.ipynb',
    REPO_ROOT / 'notebooks' / '03_experiment_analysis.ipynb',
    REPO_ROOT / 'notebooks' / '04_uplift_modeling.ipynb',
    REPO_ROOT / 'data' / 'raw' / 'README.md',
    REPO_ROOT / 'data' / 'processed' / 'README.md',
]

missing = [str(p.relative_to(REPO_ROOT)) for p in required if not p.exists()]
if missing:
    print('Missing files:')
    for m in missing:
        print(' -', m)
    sys.exit(1)

bad_patterns = [r'C:\\Users\\', r'%pip install', r'!pip install']
issues = []
for nb_path in (REPO_ROOT / 'notebooks').glob('*.ipynb'):
    try:
        nb = nbformat.read(nb_path, as_version=4)
    except Exception as e:
        issues.append(f'{nb_path.name}: notebook parse failed ({e})')
        continue
    for cell in nb.cells:
        if cell.cell_type != 'code':
            continue
        src = cell.source
        for pat in bad_patterns:
            if re.search(pat, src):
                issues.append(f'{nb_path.name}: found disallowed pattern `{pat}`')

if issues:
    print('Notebook issues found:')
    for issue in issues:
        print(' -', issue)
    sys.exit(1)

print('Repo check passed.')
