# Research History: Pattern Recognition in Discrete Twisted Lattices

Welcome to the evolving story of this project. This document tracks our journey from initial curiosity to refined understanding. We believe that sharing the *process*—including the dead ends, corrections, and falsifications—is just as valuable as the final results.

---

## 📅 Timeline of Discoveries

### March 2026: The Initial Illusion
- **What we did:** Ran initial simulations using coarse linear scans.
- **What we saw:** "Perfect" mathematical constants appeared to emerge naturally ($\alpha_{KB} \approx 3/5\pi$, $\alpha_{Torus} \approx 80/199\pi$).
- **The feeling:** Exciting, but there was no clear ratio for the torus.
- **The Trap:** We mistook grid alignment for physical law.

### April 10, 2026: The First Correction (Grid & Metrics)
- **What we did:** Doubled down on precision, implementing a high-resolution binary search ($10^{-8}$ tolerance) and harmonizing distance metrics (Euclidean for both topologies).
- **What happened:** 
  1. The "perfect" constants vanished, revealing small drifts (Grid Quantization Artifacts).
  2. The previously reported $\sqrt{2}$ ratio between topologies **disappeared** when metrics were harmonized. Both converged to $P \approx 1.11072$.
- **The New Pattern:** In the refined data, a step-wise dependence on **$\lfloor L/2 \rfloor$** emerged. Adjacent lattice sizes ($L=2, 3$) shared identical $K_c$ values.
- **The Conclusion (at the time):** The $\lfloor L/2 \rfloor$ scaling law appeared robust across metrics and topologies. We published this as our primary finding, calling for an analytical basis.

### April 18, 2026: The Second Correction (The Smooth Twist Test)
- **The Question:** Is the $\lfloor L/2 \rfloor$ dependence a fundamental property of the lattice, or an artifact of the **hard, discontinuous boundary condition** (the instant sign flip) used in the code?
- **What we did:** We replaced the hard sign flip with **smooth boundary conditions** (Linear Ramp and Soft Cosine phase factors) to simulate a more physically realistic transition.
- **The Result:** 
  - The system became **immediately oscillatory** ($\rho < 0$) at $K=0$ for all lattice sizes.
  - No critical curvature $K_c$ could be defined.
  - The $\lfloor L/2 \rfloor$ scaling pattern **vanished entirely**.
- **The Falsification:** The "robust" law was not a universal truth. It was a **numerical artifact** arising specifically from the interaction between the discrete grid and the sharp discontinuity of the hard boundary.
- **The Lesson:** Observed scaling laws in discrete systems can be transient methodological artifacts. Distinguishing between physical laws and implementation artifacts is the core challenge of computational topology.

### April 29, 2026: Extended Scale Validation ($L=128$)
- **The Goal:** To test the stability of the scaling product $P$ and the $\lfloor L/2 \rfloor$ pattern at significantly larger scales, pushing the limits of the current implementation.
- **What we did:** Extended high-resolution simulations for both the Twisted Torus and Klein Bottle (Euclidean metric) up to **$L=128$** ($N=16,384$).
- **The Result:**
  - The scaling product $P \approx 1.11072$ remained **stable** for both topologies up to the maximum tested scale.
  - The $\lfloor L/2 \rfloor$ dependence held with high numerical precision ($10^{-8}$).
  - **Computational Reality:** Runtime increased non-linearly, with the $L=128$ run taking approximately **4,100 seconds** (~1.1 hours).
- **The Current Status:** Within the **specific CME implementation** used here, the scaling behavior is consistent across both topologies up to $L=128$. However, whether this constant is a universal feature of discrete twisted lattices or specific to this numerical scheme remains an open question.
- **The Next Step:** Analytical derivation is required to determine the underlying mechanism. Further empirical expansion (e.g., $L=256$) is currently limited by computational cost.

---

## 📂 Current Status
The project is in a phase of **ongoing research**.
**Full data (including extended runs to $L=128$) and the detailed falsification analysis are available in the repository.**

---

## 🤝 Join the Conversation
If you spot something we missed, have a different interpretation, or just want to chat about the physics, please reach out! We are happy to share our source code to help you verify these results or run your own variations.

**Email:** k.jacoby at posteo de
