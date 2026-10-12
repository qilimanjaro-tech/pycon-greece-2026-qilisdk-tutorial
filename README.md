# Learn Quantum Computing with QiliSDK

Material for the PyCon Greece 2026 hands-on tutorial **Learn Quantum Computing with QiliSDK**: a 90-minute session on the foundations of quantum computing and digital circuits, from qubits and measurement to compiling a circuit for a real chip.

This is a shorter version of the [EuroPython 2026 tutorial](https://github.com/qilimanjaro-tech/europython2026-qilisdk-tutorial), which continues with analog computing, variational algorithms, noise, and execution on hardware.

## Where everything is

| Path | What it is |
|------|------------|
| [Setup](#setup) | Installation instructions for pip, uv, or Google Colab. Start here. |
| [`notebooks/`](notebooks/) | Two tutorial notebooks (`01_foundations`, `02_circuits`) with exercises for attendees to complete. |
| [`notebooks/solutions/`](notebooks/solutions/) | The same notebooks with exercises solved and outputs included. |
| [`slides/`](slides/) | The Marp slide deck (`qilisdk_tutorial.md`, pre-rendered `qilisdk_tutorial.html`) and its diagrams in `slides/img/`. |
| [`scripts/embed_diagrams.py`](scripts/embed_diagrams.py) | Copies the SVG diagrams from `slides/img/` into the notebooks, which embed them so they work in Colab. Run it after editing a diagram. |

## Setup

Use **Python 3.11–3.14** and **QiliSDK 0.3.0**, the version used to verify these examples. You can run the notebooks locally or in Google Colab. QiliSDK includes the QiliSim simulator and the numerical and plotting dependencies needed for both lessons; no optional extras or quantum hardware are required.

Before the session, open [`notebooks/01_foundations.ipynb`](notebooks/01_foundations.ipynb) and run its first two code cells. The first installs QiliSDK if it is missing and should print `QiliSDK 0.3.0`; the second imports the tools used in the lesson. Both should finish without errors.

### Local installation

Check your Python version with `python --version`. From the repository root, create a virtual environment and install QiliSDK and JupyterLab:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows Command Prompt: .venv\Scripts\activate
pip install "qilisdk==0.3.0" jupyterlab
jupyter lab
```

If you use [uv](https://docs.astral.sh/uv/), it can create the environment with Python 3.13, downloading the interpreter if needed:

```bash
uv venv --python 3.13
source .venv/bin/activate  # Windows Command Prompt: .venv\Scripts\activate
uv pip install "qilisdk==0.3.0" jupyterlab
jupyter lab
```

In JupyterLab, open `notebooks/01_foundations.ipynb` and run the cells in order. QiliSDK provides prebuilt packages for supported Windows, macOS, and Linux systems, so installing a compatible package requires no compilation.

### Google Colab

1. Open `notebooks/01_foundations.ipynb` in Colab using **File → Upload notebook**.
2. Run the first code cell and wait for installation to finish.
3. Continue through the notebook in order, completing the exercises as you reach them.

Each lesson, including its solution version, starts with the same installation cell. It also works locally and leaves an existing QiliSDK installation unchanged, so check that it reports version `0.3.0`. If Colab requests a restart, restart the session and rerun the notebook from the top. Colab requires an internet connection while you work.

### Troubleshooting

For version and import diagnostics, run this in a notebook cell:

```python
import qilisdk
print(qilisdk.__version__)  # expected: 0.3.0
print(qilisdk.about())     # versions, system information, and component import status
```

| Symptom | What to check |
|---------|---------------|
| pip cannot find a matching QiliSDK package | Check that Python is 3.11–3.14 and that pip can access PyPI. Upgrade pip with `pip install -U pip`. |
| The notebook reports a different QiliSDK version | Run `%pip install "qilisdk==0.3.0"` in a notebook cell, restart the kernel, and rerun from the top. |
| QiliSim or QTensor fails to import, or the version is `0.0.0` | Reinstall in a fresh virtual environment and open the notebook using that environment. |
| Plots do not appear | Check for errors in the plotting cell and run the notebook's `%matplotlib inline` cell. |
| Local setup still fails | Try Colab or ask the instructor for help with the full error message. |

Documentation (English, Spanish, and Catalan): <https://qilimanjaro-tech.github.io/qilisdk/> · Source: <https://github.com/qilimanjaro-tech/qilisdk>
