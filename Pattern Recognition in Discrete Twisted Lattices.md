# Pattern Recognition in Discrete Twisted Lattices: A Descriptive Study of Scaling Behavior and Finite-Size Effects

**Author:** Dr. Katharina Jacoby  
**Date:** Updated: April 18, 2026 

> **⚠️ Important Note on Versions:**  
> This document has been updated to include the results of a **sensitivity analysis conducted on April 18, 2026**, which falsified the primary "robust" finding of the original April 10 manuscript.  
> *   **Deprecated Version (April 10)
> *   **Deprecated Version (March 2026)
> *   **Current Version:** This file. It documents the full evolution of the findings, including the final falsification.

---

## Abstract

This manuscript documents a re-evaluation of numerical scaling behaviors in discrete photonic lattices with anti-periodic boundary conditions ("twists"). In the initial study (March 2026), we noted a transition from finite-size deviation to a stable regime, with apparent "perfect" mathematical constants emerging. However, subsequent high-resolution analysis revealed these constants were artifacts of grid quantization.

Furthermore, we identified that the previously reported $\sqrt{2}$ ratio between the Klein Bottle and Twisted Torus topologies was an artifact of comparing different distance metrics (Manhattan for Torus, Euclidean for Klein Bottle). When both topologies are simulated using the **same Euclidean metric**, they converge to the **same** scaling product ($P \approx 1.11072$).

The primary observation in the high-resolution data was a step-wise dependence of the critical curvature $K_c$ on $\lfloor L/2 \rfloor$ rather than $L$. Within the tested range ($N=4$ to $N=1024$), this pattern held for both topologies and both metrics, suggesting a robust scaling law where the specific constant depends on the metric (Euclidean $\approx 1.1107$, Manhattan $\approx \pi/4$).

**However, subsequent sensitivity analysis (April 18, 2026) has revealed that this dependence is conditional.** When the hard, discontinuous boundary condition (instant sign flip) was replaced with smooth alternatives (linear ramp or cosine phase factor), the system became immediately oscillatory at $K=0$, and the $\lfloor L/2 \rfloor$ scaling pattern vanished entirely. This indicates that the observed scaling law is not a fundamental property of the discrete lattice, but a numerical artifact arising specifically from the interaction between the grid and the sharp discontinuity of the boundary condition.

These findings are presented as descriptive numerical observations specific to the Discrete Coupled Mode Equation (CME) framework. The study underscores the necessity of distinguishing between physical laws and methodological artifacts in computational topology. Full data, code, and the detailed falsification analysis are available in this repository.

---

## 1. Introduction

In continuous field theory, the critical curvature $K_c$ of a toroidal manifold is theoretically expected to scale inversely with the characteristic length $L$ ($K_c \propto 1/L$). When such a field is instantiated on a discrete grid, the interaction between the grid geometry (metric) and the global topology (the twist) introduces complexities absent in the continuous limit.

This study addresses a descriptive question: **How does the critical curvature $K_c$ numerically behave as the number of nodes $N$ increases, and does this behavior depend on the lattice dimension $L$ or a derived quantity?**

Crucially, this manuscript serves as a record of the numerical verification process. Initial observations prompted a re-examination of search algorithms and metric consistency. This re-evaluation led to the identification of grid quantization artifacts, the correction of a spurious topological ratio, and finally, the falsification of the "robust" scaling law through sensitivity testing.

---

## 2. Methodology

### 2.1 Model and System
*   **Framework:** Discrete Coupled Mode Equations (CME).
*   **System:** 2D Square Lattice with nearest-neighbor coupling.
*   **Topologies:**
    *   **Twisted Torus:** Anti-periodic boundary in one dimension ($x$).
    *   **Klein Bottle:** Anti-periodic boundary in both dimensions ($x, y$).

### 2.2 Numerical Precision and Metric Harmonization
A central component of this study was the verification of numerical stability and metric consistency.
1.  **Initial Scan:** Linear scans with coarse steps yielded values that appeared to match "perfect" rational constants.
2.  **Re-evaluation:** We implemented a **two-stage binary search** with a tolerance of $10^{-8}$. The "perfect" constants disappeared, revealing slight drifts.
3.  **Metric Harmonization:** We re-ran the Twisted Torus simulations using the **Euclidean metric** (matching the Klein Bottle script) to ensure a fair comparison. Previous comparisons had mixed Manhattan (Torus) and Euclidean (KB) metrics.
4.  **Sensitivity Testing (April 18):** We replaced the hard boundary condition with smooth alternatives (Linear Ramp, Cosine Phase) to test the robustness of the $\lfloor L/2 \rfloor$ pattern.

**Note:** All results presented in Sections 3.1–3.3 are derived from the high-resolution binary search method with **hard boundaries**. Section 3.4 presents the results of the sensitivity test.

### 2.3 Metrics
*   **Observed Critical Curvature ($K_c$):** The coupling strength where the system transitions from static to oscillatory (defined as Min_Rho < 0).
*   **Theoretical Target ($K_{target}$):** $K_{target} = 4\pi/L$.
*   **Correction Factor ($\alpha$):** $\alpha = K_c / K_{target}$.
*   **Scaling Product ($P$):** $P = K_c \times \lfloor L/2 \rfloor$.

---

## 3. Observations

### 3.1 The $\lfloor L/2 \rfloor$ Dependence (Hard Boundary)
The high-resolution data (with hard boundaries) indicates that $K_c$ does not vary continuously with $L$, but appears to remain constant for pairs of lattice sizes that share the same value of $\lfloor L/2 \rfloor$.

**Table 1: Paired $K_c$ Values (High-Resolution, Euclidean Metric, Hard Boundary)**
| L | $\lfloor L/2 \rfloor$ | $K_c$ (Klein Bottle) | $K_c$ (Twisted Torus) |
|---|---|---|---|
| 2 | 1 | 1.1107207 | 1.1107207 |
| 3 | 1 | 1.1107207 | 1.1107207 |
| 4 | 2 | 0.5553604 | 0.5553604 |
| 5 | 2 | 0.5553604 | 0.5553604 |

**Observation:** Adjacent lattice sizes with identical $\lfloor L/2 \rfloor$ values yield $K_c$ values that are identical within the limits of numerical precision ($10^{-8}$). This suggests that, numerically, the effective resolution of the twist boundary is determined by the integer floor of half the side length.

### 3.2 Product Stability and Metric Dependence
The product $P = K_c \times \lfloor L/2 \rfloor$ stabilizes to a near-constant value for each topology. However, the value of this constant depends on the distance metric used.

| Topology | Metric | Product $P$ (Mean) | Stability Observation |
|---|---|---|---|
| **Klein Bottle** | Euclidean | $1.1107207 \pm 10^{-7}$ | Highly stable |
| **Twisted Torus** | Euclidean | $1.1107207 \pm 10^{-7}$ | Highly stable (Matches KB) |
| **Twisted Torus** | Manhattan | $0.7853982 \pm 10^{-7}$ | Stable (Converges to $\pi/4$) |

**Critical Finding:** Under the Euclidean metric, the scaling products for the Klein Bottle and Twisted Torus are **identical**. The previously reported $\sqrt{2}$ ratio between topologies was an artifact of comparing a Manhattan-metric Torus to a Euclidean-metric Klein Bottle.

### 3.3 The $\sqrt{2}$ Ratio Re-evaluated
The ratio of scaling products between the two topologies is:
$$ \frac{P_{KB, \text{Eucl}}}{P_{Torus, \text{Eucl}}} \approx 1.0000 $$
$$ \frac{P_{KB, \text{Eucl}}}{P_{Torus, \text{Manh}}} \approx 1.4142 \approx \sqrt{2} $$

**Conclusion:** The $\sqrt{2}$ ratio is **not** a universal topological constant. It is a consequence of the specific combination of metrics used in the initial study. When metrics are harmonized, the ratio vanishes.

### 3.4 The Falsification: Sensitivity Analysis (April 18, 2026)
To determine if the $\lfloor L/2 \rfloor$ dependence was a fundamental property or an artifact of the **hard boundary condition**, we replaced the instant sign flip with smooth alternatives.

*   **Test 1: Linear Ramp Twist** (Smooth transition from +1 to -1).
*   **Test 2: Weak Cosine Twist** (Scaled cosine phase factor).

**Result:** In both smooth variants, the system became **immediately oscillatory** ($\rho < 0$) at $K=0$ for all lattice sizes ($L=2$ to $32$). No critical curvature $K_c$ could be defined. The $\lfloor L/2 \rfloor$ pattern vanished entirely.

**Conclusion:** The "robust" scaling law observed in Sections 3.1–3.3 is **not a fundamental property** of the discrete lattice. It is a **numerical artifact** arising specifically from the interaction between the grid and the sharp discontinuity of the hard boundary condition. When the boundary is smoothed, the system loses its stable phase, and the pattern disappears.

---

## 4. Discussion

### 4.1 The Nature of the "Perfect" Constants
The initial appearance of "perfect" constants in the March 2026 report was a cautionary example of grid quantization. The coarse search grid likely aligned with the true $K_c$ values in a manner that produced rational approximations indistinguishable from exact constants at low precision.

### 4.2 Interpretation of $\lfloor L/2 \rfloor$ and Grid Constraints
The observed dependence on $\lfloor L/2 \rfloor$ in the hard-boundary simulations suggests that the discrete grid perceives the twist boundary at a halved resolution. However, the **falsification** in Section 3.4 reveals that this perception is contingent on the **discontinuity** of the boundary. The grid does not "see" the twist at half resolution in a smooth system; it simply becomes unstable.

### 4.3 Metric Dependence vs. Topological Invariance
The fact that the scaling product $P$ changes with the metric indicates that the specific value of the constant is not a topological invariant. The **form** of the scaling law ($K_c \propto 1/\lfloor L/2 \rfloor$) is also not invariant; it is an artifact of the hard boundary implementation.

### 4.4 Limitations and Open Questions
*   **Simulation Specificity:** These observations are derived from a specific implementation of the Discrete Coupled Mode Equations.
*   **The Artifact Question:** Why does the hard boundary create this specific $\lfloor L/2 \rfloor$ pattern? Is it related to the Nyquist limit, or is it a purely numerical coincidence of the `if/else` logic?
*   **Smooth Systems:** What is the scaling behavior of the critical curvature in smooth systems? (Currently, no stable $K_c$ exists).

This work serves primarily as a descriptive record of these numerical patterns and the process of their falsification. Future research should focus on understanding why hard boundaries create these "phantom" laws and how to distinguish them from true physical phenomena.

---

## 5. Conclusion

This manuscript documents the evolution of observed numerical patterns in discrete twisted lattices:
1.  **Grid Artifacts:** Initial "perfect" constants were identified as numerical artifacts of low-resolution scanning.
2.  **Metric Artifacts:** The $\sqrt{2}$ ratio was an artifact of mixed metrics; under a unified Euclidean metric, both topologies converge to the same constant.
3.  **Boundary Artifacts:** The $\lfloor L/2 \rfloor$ scaling law was an artifact of the **hard, discontinuous boundary condition**. When smoothed, the pattern vanishes.

These findings underscore the necessity of distinguishing between physical laws and methodological artifacts in computational topology. The "robustness" of a pattern in a discrete simulation does not guarantee its universality; it may simply reflect the specific constraints of the implementation.

---

## Appendix: Data Availability

Raw simulation data supporting these observations is available in the repository:
*   `/data/v1_coarse/`: Original data (March 2026).
*   `/data/v2_highres/`: High-resolution data (April 10, 2026).
*   `/data/v3_sensitivity/`: Sensitivity analysis data (April 18, 2026).

The data is provided in standard CSV format to allow for independent verification of the statistical analysis. Source code is available upon request for collaborative verification.

**Contact:** k.jacoby@posteo.de
