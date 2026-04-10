# Pattern Recognition in Discrete Twisted Lattices: A Descriptive Study of Scaling Behavior and Finite-Size Effects

**Author:** Dr. Katharina Jacoby  
**Date:** April 10, 2026  

---

> **Publication Note:** This manuscript serves as a formal revision of the preliminary report *Pattern Recognition in Discrete Twisted Lattices* (Jacoby, March 2026). It incorporates high-resolution numerical data obtained via binary search and harmonized distance metrics (Euclidean) to correct previous observations regarding "perfect" constants and inter-topological ratios.

---

## Abstract

This manuscript documents a re-evaluation of numerical scaling behaviors in discrete photonic lattices with anti-periodic boundary conditions ("twists"). In the initial study (March 2026), we reported apparent "perfect" mathematical constants for the correction factor $\alpha$ and a $\sqrt{2}$ ratio between the Klein Bottle and Twisted Torus topologies. Subsequent high-resolution analysis using binary search (tolerance $10^{-8}$) and metric harmonization has revealed that these specific values were largely artifacts of search grid quantization and inconsistent distance metrics (Manhattan vs. Euclidean).

Using a refined Discrete Coupled Mode Equation (CME) framework, we present data for lattice sizes up to $N=1024$ ($L=32$). The primary robust finding is a step-wise dependence of the critical curvature $K_c$ on $\lfloor L/2 \rfloor$ rather than $L$. Specifically, adjacent lattice sizes sharing the same $\lfloor L/2 \rfloor$ value yield identical $K_c$ values within numerical precision. Furthermore, when both topologies are simulated using the Euclidean metric, they converge to the same scaling product $P = K_c \times \lfloor L/2 \rfloor \approx 1.11072$, contradicting the previously hypothesized universal $\sqrt{2}$ ratio. These findings suggest that the scaling behavior is governed by the interplay between the discrete grid resolution and the boundary condition, with the specific scaling constant depending on the chosen metric. No analytical proof is provided; these results are presented as descriptive numerical observations.

---

## 1. Introduction

In continuous field theory, the critical curvature $K_c$ of a toroidal manifold is theoretically expected to scale inversely with the characteristic length $L$ ($K_c \propto 1/L$). When such a field is instantiated on a discrete grid, the interaction between the grid geometry (metric) and the global topology (the twist) introduces complexities absent in the continuous limit.

This study addresses a descriptive question: **How does the critical curvature $K_c$ numerically behave as the number of nodes $N$ increases, and does this behavior depend on the lattice dimension $L$ or a derived quantity?**

Crucially, this manuscript serves as a record of the numerical verification process. Initial observations of "perfect" constants prompted a re-examination of the search algorithms. This re-evaluation led to the identification of grid quantization artifacts and the subsequent documentation of a more consistent, albeit complex, numerical pattern.

---

## 2. Methodology

### 2.1 Model and System
*   **Framework:** Discrete Coupled Mode Equations (CME).
*   **System:** 2D Square Lattice with nearest-neighbor coupling.
*   **Topologies:**
    *   **Twisted Torus:** Anti-periodic boundary in one dimension ($x$).
    *   **Klein Bottle:** Anti-periodic boundary in both dimensions ($x, y$).

### 2.2 Numerical Precision and Artifact Detection
A central component of this study was the verification of numerical stability through iterative refinement.
1.  **Initial Scan:** Linear scans with coarse steps were performed in the preliminary study. These yielded values that appeared to match "perfect" rational constants.
2.  **Re-evaluation:** Suspecting grid-induced bias, we implemented a **two-stage binary search** with a tolerance of $10^{-8}$.
3.  **Metric Harmonization:** To isolate topological effects, we ensured both topologies used the **Euclidean distance metric** for the revised analysis. The original Torus study used Manhattan distance; we re-ran these simulations with Euclidean distance for direct comparison.

**Note:** All results presented in this paper are derived from the high-resolution binary search method with Euclidean metric unless otherwise specified.

### 2.3 Metrics
*   **Observed Critical Curvature ($K_c$):** The coupling strength where the system transitions from static to oscillatory (defined as Min_Rho < 0).
*   **Theoretical Target ($K_{target}$):** $K_{target} = 4\pi/L$.
*   **Correction Factor ($\alpha$):** $\alpha = K_c / K_{target}$.
*   **Scaling Product ($P$):** $P = K_c \times \lfloor L/2 \rfloor$.

---

## 3. Observations

### 3.1 The $\lfloor L/2 \rfloor$ Dependence
The high-resolution data indicates that $K_c$ does not vary continuously with $L$, but appears to remain constant for pairs of lattice sizes that share the same value of $\lfloor L/2 \rfloor$.

**Table 1: Paired $K_c$ Values (High-Resolution, Euclidean Metric)**
| L | $\lfloor L/2 \rfloor$ | $K_c$ (Klein Bottle) | $K_c$ (Twisted Torus) |
|---|---|---|---|
| 2 | 1 | 1.11072073 | 1.11072073 |
| 3 | 1 | 1.11072073 | 1.11072073 |
| 4 | 2 | 0.55536037 | 0.55536037 |
| 5 | 2 | 0.55536037 | 0.55536037 |
| 6 | 3 | 0.37024024 | 0.37024024 |
| 8 | 4 | 0.27768019 | 0.27768019 |

**Observation:** Adjacent lattice sizes with identical $\lfloor L/2 \rfloor$ values yield $K_c$ values that are identical within the limits of numerical precision ($10^{-8}$). This suggests that, numerically, the effective resolution of the twist boundary is determined by the integer floor of half the side length.

### 3.2 Product Stability and Metric Dependence
The product $P = K_c \times \lfloor L/2 \rfloor$ stabilizes to a near-constant value for each topology within the tested range. However, the value of this constant depends on the distance metric used.

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

**Conclusion:** The $\sqrt{2}$ ratio is not a universal topological constant but a consequence of the specific combination of metrics used in the initial study. When metrics are harmonized, the ratio vanishes.

---

## 4. Discussion

### 4.1 The Nature of the "Perfect" Constants
The initial appearance of "perfect" constants in the March 2026 report was a cautionary example of grid quantization. The coarse search grid likely aligned with the true $K_c$ values in a manner that produced rational approximations indistinguishable from exact constants at low precision. The high-resolution re-evaluation was necessary to reveal the underlying, slightly drifting numerical behavior.

### 4.2 Interpretation of $\lfloor L/2 \rfloor$ and Grid Constraints
The observed dependence on $\lfloor L/2 \rfloor$ suggests that the discrete grid perceives the twist boundary at a halved resolution relative to the full lattice dimension $L$. This observation aligns with known constraints in lattice field theory, where the maximum representable momentum (the Nyquist limit) is bounded by $\lfloor L/2 \rfloor$ to avoid aliasing. 

While the mathematical basis for $\lfloor L/2 \rfloor$ as a momentum cutoff is established, its role as the primary scaling variable for critical curvature in photonic lattices appears to be a specific numerical feature of the CME framework tested here. The fact that this pattern holds for both topologies and both metrics suggests it is a fundamental property of the discrete grid's interaction with anti-periodic boundaries.

### 4.3 Metric Dependence vs. Topological Invariance
The fact that the scaling product $P$ changes with the metric (Euclidean $\approx 1.1107$ vs. Manhattan $\pi/4 \approx 0.7854$) indicates that the specific value of the constant is not a topological invariant. Instead, it reflects the geometric properties of the distance function used to define the lattice. The robustness of the $\lfloor L/2 \rfloor$ scaling law across metrics suggests that the *form* of the scaling is topological/grid-dependent, while the *coefficient* is metric-dependent.

### 4.4 Limitations and Open Questions
*   **Simulation Specificity:** These observations are derived from a specific implementation of the Discrete Coupled Mode Equations. Different discretization schemes or metrics may alter the scaling constants.
*   **Finite Range:** The largest tested lattice size is $N=1024$. While the $\lfloor L/2 \rfloor$ pattern is stable within this range, verification at larger scales is recommended.
*   **Analytical Gap:** Currently, there is no analytical proof linking the $\lfloor L/2 \rfloor$ momentum cutoff directly to the critical curvature $K_c$. Establishing this link would require deriving the dispersion relation for the twisted CME.
*   **Universality:** It is unknown whether similar scaling patterns emerge in other topological configurations or in 3D lattices.

This work serves primarily as a descriptive record of these numerical patterns. Future research should focus on bridging the gap between these empirical observations and the theoretical framework of discrete differential geometry.

---

## 5. Conclusion

This manuscript documents observed numerical patterns in discrete twisted lattices, specifically a transition from finite-size deviation to a stable regime governed by $\lfloor L/2 \rfloor$.

1.  **Grid Artifacts:** Initial "perfect" constants were identified as numerical artifacts of low-resolution scanning.
2.  **Observed Pattern:** The data suggests $K_c \propto 1/\lfloor L/2 \rfloor$ within the tested range, a pattern robust across metrics and topologies.
3.  **Metric Dependence:** The scaling product $P$ is metric-dependent. The previously hypothesized $\sqrt{2}$ ratio between topologies was an artifact of mixed metrics; under a unified Euclidean metric, both topologies converge to the same constant.

These findings are presented as descriptive records of numerical behavior. Future work should focus on deriving an analytical basis for the $\lfloor L/2 \rfloor$ dependence and verifying the scaling constants at larger scales.

---

## Appendix: Data Availability

Raw simulation data supporting these observations is available in the repository accompanying this manuscript:

**Repository:** https://github.com/KatharinaJacoby/discrete-twisted-lattices-patterns

*   `v2_highres/scaling_results_klein_bottle_highres.csv`
*   `v2_highres/scaling_results_torus_euclidean_highres.csv`
*   `v2_highres/scaling_results_torus_manhattan_highres.csv`

The data is provided in standard CSV format to allow for independent verification of the statistical analysis. Source code is available upon request for collaborative verification.

**Contact:** k.jacoby@posteo.de
