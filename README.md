# Pattern Recognition in Discrete Twisted Lattices

> **Status:** 🚧 Active Exploration / Descriptive Findings  
> **Author:** Dr. Katharina Jacoby  
> **Date:** April 10, 2026  

---

## 🤝 A Note on Collaboration & Transparency

Welcome! This repository documents an ongoing, iterative journey into the scaling behavior of discrete photonic lattices with anti-periodic boundary conditions. 

Our goal here is **descriptive**: to carefully record numerical observations, document the evolution of our understanding, and share data that others might find useful. We enjoy to find reproducible patterns in specific discrete systems.

We believe science thrives on open dialogue. If you spot inconsistencies, have alternative interpretations, or wish to discuss the underlying physics, please reach out. We are happy to share our **source code** and simulation scripts upon request to facilitate independent verification and further exploration.

---

## 📉 The Evolution of Our Understanding

This project has gone through several phases of refinement as we learned to distinguish between physical signals and numerical noise.

### Phase 1: The Initial Observation
Early simulations, using coarse-resolution linear scans, suggested the emergence of "perfect" mathematical constants for the correction factor $\alpha$:
*   **Klein Bottle:** $\alpha \approx 0.1909859317$
*   **Twisted Torus:** $\alpha \approx 0.1279637733$

### Phase 2: The Re-evaluation (Grid Artifacts)
Curious about the precision, we re-ran simulations using a **high-resolution binary search** (tolerance $10^{-8}$).
*   **Observation:** The "perfect" constants vanished. The values shifted slightly, revealing small but consistent drifts.
*   **Conclusion:** The initial values were likely **numerical artifacts** caused by the search grid aligning with specific data points.

### Phase 3: Metric Harmonization (New Insights)
To ensure a fair comparison, we re-ran the Twisted Torus simulations using the **same Euclidean metric** as the Klein Bottle (previously, the Torus used Manhattan distance).
*   **Surprising Result:** The previously hypothesized $\sqrt{2}$ ratio between topologies **disappeared** when the metric was harmonized. Both topologies converged to the *same* scaling product under Euclidean distance.
*   **Takeaway:** The ratio was likely an artifact of comparing different distance metrics, not a fundamental topological property.

---

## 🔍 Current Observations (High-Resolution Data)

Based on the latest high-resolution runs (up to $N=1024$), we have identified a robust pattern that holds across both metrics and topologies:

### 1. The $\lfloor L/2 \rfloor$ Dependence
The critical curvature $K_c$ appears to scale with **$\lfloor L/2 \rfloor$** (the integer floor of half the lattice side), rather than the full side length $L$.
*   **Evidence:** Adjacent lattice sizes (e.g., $L=2$ and $L=3$) yield **identical** $K_c$ values within numerical precision ($10^{-8}$).
*   **Interpretation:** This suggests the effective resolution of the twist boundary is constrained by the number of non-aliased distance shells, which corresponds to $\lfloor L/2 \rfloor$.
*   **Status:** This pattern is highly consistent in our data, though an analytical proof is still pending.

### 2. Metric-Dependent Scaling Constants
While the *scaling law* ($K_c \propto 1/\lfloor L/2 \rfloor$) seems robust, the specific constant of proportionality depends on the distance metric:
*   **Euclidean Metric:** Both Klein Bottle and Twisted Torus converge to a similar constant ($P \approx 1.11072$).
*   **Manhattan Metric:** The Twisted Torus converges to $P = \pi/4$.
*   **Open Question:** Is the Euclidean constant a universal feature of discrete twisted lattices, or specific to our Coupled Mode Equation (CME) implementation?

---

## 📂 Data Availability

All raw simulation data is available in the `/data` directory for independent inspection.

**Directory Structure:**
*   `v1_coarse/`: Original data (contains grid artifacts; useful for historical context).
*   `v2_highres/`: Current best estimates using binary search ($10^{-8}$ tolerance).
    *   `scaling_results_klein_bottle_highres.csv`: Klein Bottle (Euclidean).
    *   `scaling_results_torus_euclidean_highres.csv`: Twisted Torus (Euclidean) – *Recommended for direct comparison.*
    *   `scaling_results_torus_manhattan_highres.csv`: Twisted Torus (Manhattan) – *For metric sensitivity analysis.*

**Reproducibility:**
Data is provided in standard CSV format. You can load these files in any data analysis environment (Python/pandas, R, Julia, etc.) to verify the statistics and create your own visualizations.

---

## 📄 Read the Full Story

*   **[Paper.md](./paper.md)**: The formal manuscript detailing our methodology, data, and cautious conclusions. (Updated April 10, 2026)
*   **[HISTORY.md](./history.md)**: A timeline of our research journey, including the discovery of grid artifacts.

---

## 🌱 Let's Talk!

We view this work as a starting point for discussion. We are particularly interested in:
*   **Analytical Derivations:** Can anyone derive the $\lfloor L/2 \rfloor$ dependence from first principles?
*   **Alternative Implementations:** Does this pattern hold for different discretization schemes or metrics?
*   **Source Code Review:** We are happy to share our simulation scripts with anyone interested in verifying the results or extending the study.

Please feel free to email me at **k.jacoby@posteo.de** to discuss, collaborate, or simply share your thoughts. I'll be updating this README periodically to keep everyone posted on new findings.

## 📧 Contact & Collaboration

Interested researchers are welcome to contact me for:
*   Access to my source codes.
*   Collaborative verification of the $\sqrt{2}$ hypothesis.
*   Discussion of analytical derivations.

**Email:** k.jacoby@posteo.de
