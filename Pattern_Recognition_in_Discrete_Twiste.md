# Pattern Recognition in Discrete Twisted Lattices
## A Descriptive Study of Scaling Behavior and Finite-Size Effects

**Author:** Dr. Katharina Jacoby  
**Date:** March 26, 2026  

---

## Overview

This repository documents early numerical observations regarding the scaling behavior of discrete photonic lattices with anti-periodic boundary conditions ("twists"). Using a discrete Coupled Mode Equation (CME) framework, we are currently simulating two topological configurations: the **Twisted Torus** (single twist) and the **Klein Bottle** (double twist).

**Note:** The findings below are preliminary. The research is ongoing, and conclusions should be treated as hypotheses subject to further verification and analytical proof.

---

## Initial Observation: The "Perfect" Constant

Initial simulations using coarse-resolution linear scans (step sizes of 0.05 and 0.01) yielded what appeared to be perfectly constant correction factors ($\alpha$) across all tested lattice sizes for specific specs and set up, in this case the values were:

- **Klein Bottle:** $\alpha \approx 0.1909859317$
- **Twisted Torus:** $\alpha \approx 0.1279637733$

These values matched simple rational expressions involving $\pi$ to an unusually high degree of precision. While intriguing, the exactness we couldn't find a precise ratio for the torus. We ran simulations with a higher resolution for both the torus and the Klein Bottle.
---

## Re-evaluation: Suspected Grid Quantization Artifacts

To investigate, we re-ran the simulations using a higher-resolution two-stage binary search (tolerance $10^{-8}$). The results suggest that the "perfect" constants observed previously were likely **numerical artifacts** caused by the coarse search grids snapping to specific values.

| Topology | Coarse-Res $\alpha$ | High-Res $\alpha$ | Observation |
|----------|---------------------|-------------------|-------------|
| Klein Bottle | $\approx 0.19099$ | $\approx 0.17678$ | Significant displacement |
| Twisted Torus | $\approx 0.12796$ | $\approx 0.12503$ | Noticeable shift |

The high-resolution data reveals that $\alpha$ is not strictly constant but exhibits slight drifts. This suggests the original "constants" were coincidental alignments with the grid resolution rather than fundamental physical properties.

---

## Emerging Patterns: Hypotheses Under Investigation

With the artifact hypothesis in mind, we are currently analyzing the high-resolution data for underlying structures. Several tentative patterns have emerged, though they require further validation:

### 1. $\lfloor L/2 \rfloor$ Dependence
There is a strong indication that the critical curvature $K_c$ scales with the integer floor of half the lattice dimension, $\lfloor L/2 \rfloor$, rather than the raw dimension $L$ itself.
- **Observation:** Adjacent lattice sizes (e.g., $L=2$ and $L=3$) that share the same $\lfloor L/2 \rfloor$ value appear to yield identical $K_c$ values within our current precision.
- **Hypothesis:** The effective resolution of the twist boundary may be determined by $\lfloor L/2 \rfloor$.

### 2. Product Stability
The product $K_c \times \lfloor L/2 \rfloor$ appears to stabilize to a near-constant value for each topology, though small drifts are visible in the Torus data.
- **Klein Bottle:** Product $\approx 1.1107207$ (highly stable so far)
- **Twisted Torus:** Product $\approx 0.7856$ (shows minor drift)

### 3. Universal Ratio
A ratio between the scaling products of the two topologies appears to hover around **1.414**.
- **Current Estimate:** $\frac{(K_c \times \lfloor L/2 \rfloor)_{KB}}{(K_c \times \lfloor L/2 \rfloor)_{Torus}} \approx 1.414$
- **Question:** Is this exactly $\sqrt{2}$, or merely a numerical coincidence? This remains unproven.

---

## Current Status & Next Steps

The research is actively ongoing. Our immediate goals are:

1.  **Verification:** Extend simulations to larger lattice sizes ($N > 1024$) to confirm if the observed drifts converge or persist.
2.  **Analytical Derivation:** Attempt to derive the $\lfloor L/2 \rfloor$ dependence analytically to move beyond empirical observation.
3.  **Convergence Analysis:** Determine the exact limit of the scaling products as $L \to \infty$.
4.  **Metric Sensitivity:** Investigate whether these patterns hold under different grid metrics (e.g., Euclidean vs. Manhattan).

**Disclaimer:** The numerical values and patterns presented here are preliminary. They represent the current state of our investigation and are subject to change as further data is collected and analyzed. No definitive theoretical proof has been established yet.

---

## Data Availability

Raw simulation data and scripts are currently being curated. Interested researchers are welcome to contact the author for access to the datasets used in these preliminary runs.
