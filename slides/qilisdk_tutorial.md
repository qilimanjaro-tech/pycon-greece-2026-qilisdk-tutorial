---
marp: true
size: 16:9
paginate: true
math: katex
title: Learn Quantum Computing with QiliSDK
footer: 'Learn Quantum Computing with QiliSDK · PyCon Greece 2026'
---

<style>
:root {
  --accent: #6c4cf1;
  --accent-soft: #f0eefb;
  --ink: #1c1c2e;
}
section {
  font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  font-size: 26px;
  color: var(--ink);
  padding: 56px 72px;
  background: #ffffff;
}
h1, h2 { color: var(--accent); font-weight: 700; line-height: 1.1; }
h1 { font-size: 1.9em; }
h2 { font-size: 1.4em; }
h3 { color: var(--ink); }
strong { color: var(--accent); }
a { color: var(--accent); text-decoration: none; }
ul, ol { line-height: 1.5; }
code {
  background: var(--accent-soft); color: #4326b3;
  padding: 2px 7px; border-radius: 5px; font-size: 0.86em;
}
pre { font-size: 0.78em; line-height: 1.35; }
table { font-size: 0.78em; }
th { background: var(--accent-soft); color: var(--accent); }
footer { color: #9a9ab0; font-size: 0.5em; }
section::after { color: #b6b6c8; font-weight: 600; }

section.lead { text-align: center; justify-content: center; }
section.lead h1 { font-size: 2.5em; margin-bottom: 0.1em; }
section.lead .sub { font-size: 1.15em; color: #55556e; }
section.lead .meta { font-size: 0.8em; color: #8a8aa0; margin-top: 1.4em; }

section.divider {
  background: linear-gradient(135deg, #6c4cf1 0%, #4326b3 100%);
  color: #fff; justify-content: center;
}
section.divider h1, section.divider h2, section.divider h3 { color: #fff; }
section.divider strong { color: #ffd866; }
section.divider .kicker { font-size: 0.8em; letter-spacing: .18em; text-transform: uppercase; opacity: .8; }
section.divider code { background: rgba(255,255,255,.18); color: #fff; }

.cap { font-size: 0.72em; color: #6a6a82; text-align: center; margin-top: 6px; }
.center { text-align: center; }
.small { font-size: 0.82em; }

.qrgrid { display: flex; gap: 40px; justify-content: center; align-items: flex-start; margin-top: 28px; }
.qrgrid > div { text-align: center; width: 300px; }
.qrgrid img { width: 280px; height: 280px; background: #fff; padding: 8px; border: 1px solid #e6e6ef; border-radius: 10px; }
.qrgrid .lbl { font-weight: 700; color: var(--accent); margin: 14px 0 4px; font-size: 0.95em; }
.qrgrid .url { font-size: 0.72em; line-height: 1.35; word-break: break-word; }
.qrgrid .url a { color: #55556e; }
</style>

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: '' -->

# Learn Quantum Computing with QiliSDK

<p class="sub">PyCon Greece 2026</p>

---

## Introduction

- **Vyron Vasileiadis** — Tech Lead at **Qilimanjaro Quantum Tech** · vyron@qilimanjaro.tech
- **Qilimanjaro** builds **analog quantum computers** and **multimodal data centers** and the software stack to run them.
- **QiliSDK** is that stack's open-source Python SDK, and your tool today: **digital** *and* **analog** quantum computing in one API along with the C++ **QiliSim** simulator.

---

## Why quantum computing?

- **Simulating molecules and materials** is the most natural fit for a quantum computer, because describing $n$ interacting quantum particles classically needs $2^n$ numbers while a quantum computer holds that state directly.
- **Combinatorial optimization** problems such as scheduling, routing, and portfolio selection can be rewritten as finding the lowest point of an energy landscape, which is exactly what a quantum annealer is built to minimize.
- **Machine learning** can use a quantum system as a feature map or sampler, because the probability distributions it produces are rich and hard for a classical computer to reproduce.
- **True randomness** comes almost for free, because the outcome of a quantum measurement is fundamentally unpredictable rather than produced by a deterministic algorithm.

---

## Quantum computing in 2026

- **Today's quantum computers are not general-purpose accelerators**, so they will not speed up everyday software or hold large datasets, because a few hundred qubits give only a few hundred classical bits when measured.
- **The hardware today** is noisy, small, and expensive, yet it is real, running, and improving every year.
- **A simulator on your laptop** is the practical way to learn, since it is exact and free at the scales this tutorial uses.
- **The code you write is not throwaway**, because the same program runs unchanged on real hardware once you have access.

---

<!-- Schedule slide, commented out — replaced by the Links & QR-codes slide below. Uncomment to restore.
## Schedule

| Part | Topic | Time |
| - | Introduction and setup check | 10 min |
| 1 | Foundations: qubits, states, measurement, entanglement | 25 min |
| 2 | Circuits / Digital Quantum Computing, ending with the transpiler | 45 min |
| - | Wrap-up and questions | 10 min |

90 minutes in total. Times are approximate, we flex with the room.
-->

## Links & QR codes

<!-- Add the QR code and link for this tutorial's repository here once it is published,
     as the first entry of the grid (the EuroPython deck used img/qr-tutorial.svg). -->

<div class="qrgrid">
<div>
<img src="img/qr-qilisdk.svg" alt="QR code for the QiliSDK GitHub repository" />
<div class="lbl">QiliSDK source</div>
<div class="url"><a href="https://github.com/qilimanjaro-tech/qilisdk">github.com/qilimanjaro-tech/qilisdk</a></div>
</div>
<div>
<img src="img/qr-docs.svg" alt="QR code for the QiliSDK documentation" />
<div class="lbl">Documentation</div>
<div class="url"><a href="https://qilimanjaro-tech.github.io/qilisdk">qilimanjaro-tech.github.io/qilisdk</a></div>
</div>
</div>

---

## Follow along

**Two ways to run everything, pick one:**

- **Local**: `pip install "qilisdk==0.2.1"` (Python 3.11–3.13), then open the notebooks.
- **Colab**: every notebook's first cell installs QiliSDK (pinned to `0.2.1`) automatically. Zero local setup.

**Right now:** open and run `notebooks/00_setup.ipynb`.
If its last cell prints counts like `{'00': ~500, '11': ~500}`, you're ready. ✅

> QiliSDK ships its C++ simulator **QiliSim** *inside* the wheel: nothing to compile.

---

## How we'll work

- **Coding-first.** These slides are a map; the real work is in the notebooks.
- Each part: a short **concept**, a live **code-along**, then **🧩 exercises**, each a small real problem.
- Notebooks come in two flavors:
  - `notebooks/…`: **attendee** version (blank `# TODO` cells)
  - `notebooks/solutions/…`: **completed**, with outputs
- Every snippet is **verified to run** against `qilisdk 0.2.1`.

> Stuck on an exercise? The solution is one folder away, but try first. 🙂

---

## What you'll build

- a **loaded quantum coin** whose odds are fixed by physics (Part 1);
- a **quantum dice roller** — true randomness you can trust (Part 2);
- a **shared secret for three parties**, made from entanglement (Part 2);
- a **circuit compiled onto a real chip**, with the cost of its wiring counted (Part 2).

Underneath it all: a working feel for qubits, measurement, gates, and circuits.

---

## The architecture

![h:500](img/overall.jpg)

---

## 30 seconds of notation

Quantum papers use **bra-ket** syntax: typed labels around vectors you already know from numpy.

- A **ket** $|\psi\rangle$ (read "ket psi") is a labeled complex **column vector**: $|0\rangle$ is `np.array([[1], [0]])`.
- A **bra** $\langle\psi|$ is its **conjugate transpose**, a row vector: `psi.conj().T`.
- Several qubits: $|01\rangle$ is shorthand for $|0\rangle \otimes |1\rangle$, the **tensor product** of the two kets: `np.kron(ket0, ket1)`.

That is every symbol today's math needs.

---

<!-- _class: divider -->

<p class="kicker">Part 1 · notebooks/01_foundations.ipynb</p>

# Foundations

### Qubits, superposition, and randomness you can trust

---

## Part 1: the ideas, in plain words

- A **qubit** is two complex numbers, its **amplitudes**: one weight for $|0\rangle$, one for $|1\rangle$. Think `np.array([a, b])` with unit length.
- **Measuring** samples one outcome with probability $|\text{amplitude}|^2$ (the **Born rule**) and destroys the superposition. No peeking twice.
- 2 qubits need 4 amplitudes: one for $|00\rangle$, one for $|01\rangle$, one for $|10\rangle$ and one for $|11\rangle$.
- $n$ qubits need $2^n$ amplitudes. That **memory wall** is why Feynman proposed quantum computers in the first place.
- But measurement returns only $n$ classical bits, so algorithms must **engineer interference**: wrong answers cancel, the right one survives.

---

## Part 1: the vocabulary and the API

- **Superposition**: several amplitudes nonzero at once. **Phase**: an amplitude's sign or angle, invisible on its own, decisive when paths interfere.
- **Entanglement**: correlated randomness between qubits that nobody else holds a copy of (the raw material for quantum key distribution).
- In code: `QTensor` holds states *and* operators.

---

## `QTensor`: the math object behind it all

![h:480](img/qtensor.jpg)

<!-- <p class="cap">Standard matrix ops · state factories (<code>ket</code>, <code>ghz</code>, <code>uniform</code>, …) · quantum-information primitives (partial trace, entropy, fidelity).</p> -->

---

<!-- _class: divider -->

<p class="kicker">Part 2 · notebooks/02_circuits.ipynb</p>

# Circuits & Digital Quantum Computing

### Interference, a quantum dice roller, and compiling for a real chip

---

## Part 2: the ideas, in plain words

- **Gates** are reversible matrix operations on the amplitude vector: the Hadamard gate $H$ creates superposition, the controlled-NOT (**CNOT**) entangles two qubits.
- A **circuit** is a program: an ordered list of gates applied to a fresh register of qubits.
- **Measurement** ends the program and hands back plain classical bits.
- **Sampling** repeats the whole measurement **nshots** times and averages the outcomes into a distribution; more shots pull it toward the exact answer. A simulator can give you both.

---

## Part 2: the one execution pattern

$$\texttt{Backend.execute(functional, readout)} \rightarrow \texttt{Result}$$

- **Functional** = *what* to run: `DigitalPropagation(circuit)` wraps your circuit.
- **Backend** = *where* to run: `QiliSim`, the built-in simulator. **Readout** = *what to measure*: samples, expectation values, or the exact state.
- A bare `Circuit` never executes. The wrapper keeps *what* cleanly separate from *where*.
- **One call, every backend.** The same three-part call runs on the simulator now and a real QPU later — you swap only the `Backend`.

---

## Part 2: from circuit to chip

- The **transpiler is a compiler**: instruction selection (your gates → the chip's native set) plus register allocation (your qubits → physical qubits).
- Real chips run only a small **native gate set** and connect only *some* qubit pairs, so an abstract circuit rarely fits as written.
- **SABRE** (SWAP-based Bidirectional heuristic search), a routing pass used by production compilers, inserts SWAPs so every two-qubit gate lands on physically connected qubits.
- Transpiling *multiplies* the gate count, and every extra gate is one more chance for noise to spoil the answer: the bridge from a clean circuit to a runnable one.

---

## The journey

**Loaded coin** → **dice roller** → **shared secret** → **compiled circuit**

A small set of primitives, composed and executed uniformly:

`QTensor` · `Circuit` · `Readout`
 → wrapped in a **Functional** (`DigitalPropagation`) → run by a swappable **Backend** (`QiliSim`).

> Every circuit today ran through one call: `backend.execute(functional, readout)`.

---

## Going further

The **3-hour version** of this tutorial (EuroPython 2026) picks up where we stop:

- **Analog** quantum computing: Hamiltonians, and scheduling talks by quantum annealing;
- **Variational algorithms**: a molecule's ground-state energy (VQE) and a quantum optimizer (QAOA);
- **Noise**: why real answers degrade, and how much gate error an answer survives;
- **Execution**: swapping backends, exporting circuits, and a quantum-reservoir forecaster.

[github.com/qilimanjaro-tech/europython2026-qilisdk-tutorial](https://github.com/qilimanjaro-tech/europython2026-qilisdk-tutorial)

---

<!-- _class: lead -->
<!-- _footer: '' -->

# Thank you! 🙏
