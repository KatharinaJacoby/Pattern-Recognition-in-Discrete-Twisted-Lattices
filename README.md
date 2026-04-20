# Pattern Recognition in Discrete Twisted Lattices

> **Author:** Dr. Katharina Jacoby  
> **Date:** April 10, 2026 (Updated: April 18, 2026)  
---

## 🤝 A Note on Collaboration & Transparency

Welcome! This repository documents an ongoing, iterative journey into the scaling behavior of discrete photonic lattices with anti-periodic boundary conditions. 

Our goal here is **descriptive**: to carefully record numerical observations, document the evolution of our understanding, and share data that others might find useful. We enjoy finding reproducible patterns in specific discrete systems.

We believe science thrives on open dialogue. If you spot inconsistencies, have alternative interpretations, or wish to discuss the underlying physics, please reach out. We are happy to share our **source code** and simulation scripts upon request to facilitate independent verification and further exploration.

> **Note on Methodology and Tools**  
> This paper was assisted by Large Language Models (LLMs). They were used to assist with creating texts, formatting, literature search, verification of mathematical derivations, and scaffold code generation. All conceptual frameworks, ethical arguments, and editorial decisions are my own. In fact, trying to use an LLM for formatting and code scaffold—even under strict instructions—is exhausting. The helpful AI assistant constantly swaps my non-binary approach to a smooth binary one which sells or looks good for peer-review, which has made me question my life choices more than once and says a lot about today's bias in research. The bias of today's LLM is extremely strong and needs constant human intervention.

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

### Phase 4: Sensitivity Analysis — The "Smooth Twist" Test
To address the open question of whether the $\lfloor L/2 \rfloor$ dependence is a fundamental property of discrete lattices or an artifact of the boundary condition implementation, we replaced the **hard discontinuous twist** (`if dx > L/2: -1`) with smooth alternatives.

**Test 1: Smooth Cosine Twist (Euclidean Metric)**
*   **Modification:** Replaced the hard sign flip with `Twist = cos(2π · dx/side)`.
*   **Result:** The system became **immediately oscillatory** ($\rho < 0$) at $K=0$ for all lattice sizes ($L=2$ to $32$). No critical curvature $K_c$ could be defined. The product $K_c \times \lfloor L/2 \rfloor$ collapsed to zero everywhere.
*   **Data:** `scaling_results_torus_smooth_euclidean.csv`

**Test 2: Sensitivity Analysis (Linear Ramp & Weak Cosine)**
To confirm this wasn't an artifact of the specific cosine function, we tested two weaker smooth variants:
*   **Linear Ramp:** Smooth linear transition from +1 to −1.
*   **Weak Cosine:** Cosine scaled by 0.5 (range: −0.5 to +0.5).

| Twist Type | N=4 (L=2) | N=16 (L=4) | N=64 (L=8) | System State at K=0 |
| :--- | :--- | :--- | :--- | :--- |
| **Hard (Baseline)** | ρ > 0 | ρ > 0 | ρ > 0 | **Stable** |
| **Linear Ramp** | −0.789 | −0.685 | −0.516 | **Unstable** |
| **Weak Cosine (0.5×)** | −0.395 | −0.343 | −0.258 | **Unstable** |

*   **Result:** Even the weakest smooth twist destabilizes the system at $K=0$. No stable phase exists. No $K_c$ can be measured.

**Conclusion:** The $\lfloor L/2 \rfloor$ scaling pattern is **not a universal law** of discrete lattices. It is a direct consequence of the **hard, discontinuous boundary condition**. The pattern vanishes entirely when the boundary is smoothed, regardless of the smoothing function or its amplitude. The pattern exists only because the Hard system has a stable phase to transition from. The Smooth system has no stable phase, so the pattern vanishes.

---

## 🔍 Current Observations (High-Resolution Data, Hard Twist)

Based on the latest high-resolution runs (up to $N=1024$) with **Hard Twist** conditions:

### 1. The $\lfloor L/2 \rfloor$ Dependence (Conditional)
The critical curvature $K_c$ appears to scale with **$\lfloor L/2 \rfloor$** (the integer floor of half the lattice side), rather than the full side length $L$.
*   **Evidence:** Adjacent lattice sizes (e.g., $L=2$ and $L=3$) yield **identical** $K_c$ values within numerical precision ($10^{-8}$).
*   **Caveat:** This pattern is **strictly dependent** on the use of a hard, discontinuous anti-periodic boundary condition. It does not persist under smooth boundary implementations (see Phase 4).
*   **Interpretation:** The pattern arises from the interaction between the discrete grid geometry and the sharp discontinuity of the twist, likely related to how the grid resolves the "flip" at the Nyquist limit.

### 2. Metric-Dependent Scaling Constants
While the *scaling law* ($K_c \propto 1/\lfloor L/2 \rfloor$) holds for the hard twist, the specific constant of proportionality depends on the distance metric:
*   **Euclidean Metric:** Both Klein Bottle and Twisted Torus converge to a similar constant ($P \approx 1.11072$).
*   **Manhattan Metric:** The Twisted Torus converges to $P = \pi/4$.
*   **Open Question:** Is the Euclidean constant a universal feature of discrete twisted lattices with *hard* boundaries, or specific to our CME implementation?

---

## 📂 Data Availability

All raw simulation data is available in the `/data` directory for independent inspection.

**Directory Structure:**
*   `v1_coarse/`: Original data (contains grid artifacts; useful for historical context).
*   `v2_highres/`: Current best estimates using binary search ($10^{-8}$ tolerance).
    *   `scaling_results_klein_bottle_highres.csv`: Klein Bottle (Euclidean).
    *   `scaling_results_torus_euclidean_highres.csv`: Twisted Torus (Euclidean) – *Recommended for direct comparison.*
    *   `scaling_results_torus_manhattan_highres.csv`: Twisted Torus (Manhattan) – *For metric sensitivity analysis.*
*   `v3_sensitivity/`: Smooth Twist sensitivity analysis (April 18, 2026).
    *   `scaling_results_torus_smooth_euclidean.csv`: Smooth Cosine Twist results (all $K_c = 0$; system unstable at $K=0$).
    *   `sensitivity_test_terminal_output.txt`: Terminal output from the Linear Ramp and Weak Cosine tests.

**Scripts:**
*   **Sensitivity & Falsification Scripts (Update from April 18, 2026) are in the v3_sensitivity folder:**
    *   `smooth_twist_test.py`: Main test replacing the hard twist with a smooth cosine phase factor (Euclidean metric). Generates `scaling_results_torus_smooth_euclidean.csv`.
    *   `smooth_twist_sensitivity_test.py`: Comprehensive sensitivity analysis testing Linear Ramp and Weak Cosine twist variants to confirm system instability at K=0.

To ensure full reproducibility, the following Python scripts are available. Please email `k.jacoby at posteo de` to request access.

*   **Core Simulation Scripts:**
    *   `scaling_results_torus.py`: Original Twisted Torus simulation (Manhattan metric, coarse scan). *Historical reference only.*
    *   `scaling_results_klein_bottle.py`: Original Klein Bottle simulation (Euclidean metric, coarse scan). *Historical reference only.*
    *   `scaling_results_torus_high_resolution.py`: High-resolution Twisted Torus simulation (supports both Manhattan and Euclidean metrics, binary search).
    *   `scaling_results_klein_bottle_highres.py`: High-resolution Klein Bottle simulation (Euclidean metric, binary search, extended to N=1024).


**Reproducibility:**
Data is provided in standard CSV format. You can load these files in any data analysis environment (Python/pandas, R, Julia, etc.) to verify the statistics and create your own visualizations.

---

## 📄 Read the Full Story

*   **[Pattern Recognition in Discrete Twisted Lattices.md](./Pattern%20Recognition%20in%20Discrete%20Twisted%20Lattices.md)**: Formal manuscript with methodology, data, and conclusions. (Updated April 18, 2026)
*   **[Non-Tech Companion Guide: Understanding the Grid, the Glitch, and the Geometry.md](./Non-Tech%20Companion%20Guide%20Understanding%20the%20Grid%20the%20Glitch%20and%20the%20Geometry.md)**: Accessible version explaining the paper for non-math readers.
*   **[HISTORY.md](./history.md)**: Timeline of the research journey, including discovery of grid artifacts and the smooth twist falsification.

---

## 🌱 Let's Talk!

We view this work as a starting point for discussion. We are particularly interested in:
*   **Analytical Derivations:** Can anyone derive the $\lfloor L/2 \rfloor$ dependence specifically for **discontinuous** boundary conditions?
*   **Physical Interpretation:** What does the immediate instability under smooth twists imply for the physical modeling of anti-periodic systems? Is the hard twist a necessary idealization, or does it mask a deeper problem with the CME framework?
*   **Source Code Review:** We are happy to share our simulation scripts (including the smooth twist variants) with anyone interested in verifying the results or extending the study.

Please feel free to open an issue here in the repo or email me at **k.jacoby at posteo.de** to discuss, collaborate, or simply share your thoughts. I'll be updating this README periodically to keep everyone posted on new findings.

## 📧 Contact & Collaboration

Interested researchers are welcome to contact me for:
*   Access to further source codes (the sensitivity test scripts are in the v3_sensitivity folder).
*   Discussion of analytical derivations.
*   If you want to cite this paper, please go to https://philpeople.org/profiles/katharina-jacoby/publications
