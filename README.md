# Pattern Recognition in Discrete Twisted Lattices

> **Status:** 🚧 Active Research / Preliminary Findings  
> **Author:** Dr. Katharina Jacoby  
> **Date:** April 9, 2026  

---

## 📢 Scientific Transparency Note

This repository documents the **iterative process** of our research. We believe in full transparency regarding how our understanding of these discrete systems has evolved.

1.  **Initial Phase:** Early simulations suggested "perfect" mathematical constants.
2.  **Re-evaluation:** We discovered these were **numerical artifacts** caused by coarse search grids.
3.  **Current Phase:** High-resolution analysis has revealed a new scaling law ($\lfloor L/2 \rfloor$ dependence) and a potential universal ratio ($\sqrt{2}$).

**Note on Code:** The source code used to generate these results is proprietary and not included in this repository. However, the **raw data** and **analysis scripts** (Python notebooks for plotting) are provided to allow full reproducibility of the *results*.

---

## 📉 The Journey: From "Perfect" Constants to Grid Artifacts

### Phase 1: The Initial Observation
Using coarse-resolution linear scans, we initially observed what appeared to be **perfectly constant** correction factors ($\alpha$):
*   **Klein Bottle:** $\alpha \approx 0.1909859317$ ($3/5\pi$)
*   **Twisted Torus:** $\alpha \approx 0.1279637733$ ($80/199\pi$)

### Phase 2: The Re-evaluation
Suspecting these were numerical coincidences, we re-ran simulations with **high-resolution binary search** ($10^{-8}$ tolerance).
*   **Result:** The "constants" disappeared. The values shifted, and slight drifts appeared.
*   **Conclusion:** The original values were **grid quantization artifacts**.

| Topology | Coarse-Res $\alpha$ (Artifact) | High-Res $\alpha$ (Corrected) | Shift |
| :--- | :--- | :--- | :--- |
| **Klein Bottle** | $\approx 0.19099$ | $\approx 0.17678$ | $+0.0142$ |
| **Twisted Torus** | $\approx 0.12796$ | $\approx 0.12503$ | $+0.0029$ |

---

## 🔍 Current Hypotheses (High-Res Data)

With artifacts removed, new patterns have emerged:

### 1. The $\lfloor L/2 \rfloor$ Dependence
The critical curvature $K_c$ scales with **$\lfloor L/2 \rfloor$**, not $L$.
*   **Evidence:** Adjacent lattice sizes ($L=2,3$) share identical $K_c$ values.
*   **Implication:** The effective resolution of the twist boundary is half the lattice side length.

### 2. The Universal Ratio
The ratio of scaling products between topologies converges to **$\approx 1.414$**.
$$ \frac{(K_c \times \lfloor L/2 \rfloor)_{KB}}{(K_c \times \lfloor L/2 \rfloor)_{Torus}} \approx \sqrt{2} $$

---

## 📂 Data Availability

All raw simulation data is available in the `/data` directory.
*   `v1_coarse/`: Original data (contains artifacts, for historical reference).
*   `v2_highres/`: Corrected high-resolution data (current best estimate).

**Reproducibility:**
The data is provided in standard CSV format. We provide Jupyter notebooks in `/analysis` to reproduce all plots and statistical tests shown in the paper.

---

## 📄 Read the Full Story

*   **[Paper.md](./paper.md)**: The formal manuscript detailing the methodology, data, and conclusions.
*   **[HISTORY.md](./history.md)**: A detailed timeline of the research evolution and artifact discovery.

---

## 📧 Contact & Collaboration

Interested researchers are welcome to contact me for:
*   Access to my source codes.
*   Collaborative verification of the $\sqrt{2}$ hypothesis.
*   Discussion of analytical derivations.

**Email:** k.jacoby@posteo.de
