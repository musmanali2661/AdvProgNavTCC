# Environment Setup

Software required by the curriculum: Google Chrome, Anaconda, Jupyter Notebook, Python, PyCharm.

## Option A: Anaconda (recommended for the lab)

1. Install Anaconda: https://www.anaconda.com/download
2. Create the course environment from the repo root:
   ```bash
   conda env create -f setup/environment.yml
   conda activate advprog-ai
   ```
3. Launch Jupyter:
   ```bash
   jupyter notebook
   ```

## Option B: pip / virtualenv

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r setup/requirements.txt
```

## Verify

```bash
python setup/check_env.py
```

## IDE

- PyCharm Community: https://www.jetbrains.com/pycharm/
- VS Code with the Python and Jupyter extensions also works.
