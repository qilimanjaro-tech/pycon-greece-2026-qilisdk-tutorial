# Setup: *Learn Quantum Computing with QiliSDK* (PyCon Greece 2026)

Please complete setup **before the session** and run `notebooks/00_setup.ipynb`. If its final cell shows a bar chart with two bars, `00` and `11`, each around 500 counts, you're ready.

You have two options: **local** or **Google Colab**. Either is fine; pick whichever you prefer.

---

## Option A: Local install (recommended if you have Python 3.11–3.13)

QiliSDK ships the **QiliSim** C++ simulator inside the wheel, so there is nothing to compile: `pip install qilisdk` just works on Windows, macOS, and Linux, and it pulls in everything the tutorial needs (numpy, scipy, matplotlib) as dependencies.

### A1: with venv + pip

```bash
# 1. (recommended) create a fresh virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. install QiliSDK (+ a notebook UI if you don't have one)
pip install "qilisdk==0.2.1" jupyterlab

# 3. launch Jupyter and open notebooks/00_setup.ipynb
jupyter lab
```

### A2: with uv

If you use [uv](https://docs.astral.sh/uv/), it handles the Python version for you (it downloads a
supported interpreter if yours is too old or too new):

```bash
uv venv --python 3.13
source .venv/bin/activate        # Windows: .venv\Scripts\activate
uv pip install "qilisdk==0.2.1" jupyterlab
jupyter lab
```

**Requirements:** Python **3.11, 3.12, or 3.13**. Check with `python --version`.

> **Why the pin?** Every notebook is verified against `qilisdk 0.2.1`, so install exactly that version. Newer releases exist and may behave differently. (The Colab "Run me first" cells pin this version for you.)

The base install is all you need: both notebooks, including the transpiler demo, run without any optional QiliSDK extras.

---

## Option B: Google Colab (zero local setup, needs internet)

Every tutorial notebook starts with a **"Run me first"** cell that installs QiliSDK automatically when
it is missing. On Colab you just:

1. Open the notebook in Colab (File → Upload notebook, or use the shared links we send).
2. Run the first cell (~1 min). It installs `qilisdk==0.2.1`.
3. Continue normally.

That same first cell is a **no-op locally** (if QiliSDK is already installed it does nothing), so the
notebooks are identical in both environments.

---

## Verify your environment

Run this anywhere (a cell, or `python -c`):

```python
import qilisdk
print(qilisdk.__version__)     # 0.2.1
print(qilisdk.about())         # full diagnostics: versions, system, QiliSim/QTensor import status
```

`notebooks/00_setup.ipynb` does this plus a 2-qubit Bell-circuit smoke test.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `pip` can't find a matching `qilisdk` wheel | Check `python --version` is 3.11–3.13; upgrade pip: `pip install -U pip`. |
| Import works but `0.0.0` version | The dist isn't fully installed. Reinstall in a clean venv. |
| `00_setup` reports a QiliSDK version other than 0.2.1 | Install the tested version: `pip install "qilisdk==0.2.1"`. |
| Plots don't show in Jupyter | Put `%matplotlib inline` at the top of the notebook (the tutorial notebooks already do). |
| Colab "restart session" prompt after install | Just re-run the cell; the install is cached for the session. |
| Anything else | Use Colab (Option B). It sidesteps all local-toolchain issues. |

Docs (EN / ES / CA): <https://qilimanjaro-tech.github.io/qilisdk/> · Source: <https://github.com/qilimanjaro-tech/qilisdk>
