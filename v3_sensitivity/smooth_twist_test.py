#!/usr/bin/env python3
"""
smooth_twist_test.py
Scaling Study for the Twisted Torus Topology using a SMOOTH Phase Factor.
This tests if the pattern persists in the "harmonized" Euclidean regime.
"""

import numpy as np
import pandas as pd
import time

def calculate_manhattan_distance_and_twist_smooth(coords, side, metric_type="euclidean"):
    """
    Calculates distance with SMOOTH Twist.
    """
    N = len(coords)
    D = np.zeros((N, N))
    Twist = np.ones((N, N))
    
    for i in range(N):
        for j in range(i + 1, N):
            dx_direct = abs(coords[i, 0] - coords[j, 0])
            dy_direct = abs(coords[i, 1] - coords[j, 1])
            
            # Shortest path wrapping
            dx = dx_direct if dx_direct < (side - dx_direct) else (side - dx_direct)
            dy = dy_direct if dy_direct < (side - dy_direct) else (side - dy_direct)
            
            # METRIC SELECTION (Defaulting to Euclidean for this test)
            if metric_type == "manhattan":
                dist = dx + dy
            elif metric_type == "euclidean":
                dist = np.sqrt(dx**2 + dy**2)
            else:
                raise ValueError(f"Unknown metric type: {metric_type}")
            
            D[i, j] = D[j, i] = dist
            
            # SMOOTH TWIST (Same as before)
            smooth_phase = np.cos(2 * np.pi * (dx_direct / side))
            Twist[i, j] = smooth_phase
            Twist[j, i] = smooth_phase
                
    return D, Twist

def calculate_correlation_matrix(N, K_eff, xi=10.0, metric_type="euclidean"):
    side = int(np.sqrt(N))
    x = np.arange(side)
    y = np.arange(side)
    X, Y = np.meshgrid(x, y)
    coords = np.vstack([X.flatten(), Y.flatten()]).T
    
    D, Twist = calculate_manhattan_distance_and_twist_smooth(coords, side, metric_type)
    
    G_matrix = np.cos(K_eff * D) * np.exp(-D / xi)
    C = G_matrix * Twist
    
    C = C + 0.1 * np.eye(N)
    
    std_devs = np.sqrt(np.diag(C))
    std_devs[std_devs == 0] = 1.0
    C_norm = C / np.outer(std_devs, std_devs)
    
    return C_norm, D

def find_min_rho(N, K_eff, xi=10.0, metric_type="euclidean"):
    C_norm, D = calculate_correlation_matrix(N, K_eff, xi, metric_type)
    
    rho_values = []
    unique_dists = np.unique(D)
    
    for r in unique_dists:
        if r == 0:
            continue
        mask = (D == r)
        vals = C_norm[mask]
        if len(vals) > 0:
            rho_values.append(np.mean(vals))
    
    if len(rho_values) > 0:
        return np.min(rho_values)
    return 0.0

def find_critical_k_binary_debug(N, xi=10.0, metric_type="euclidean", tol=1e-8):
    # Debug check
    print(f"  [DEBUG] N={N}: Min_Rho at K=0: {find_min_rho(N, 0.0, xi, metric_type):.6f}")
    print(f"  [DEBUG] N={N}: Min_Rho at K=1: {find_min_rho(N, 1.0, xi, metric_type):.6f}")
    print(f"  [DEBUG] N={N}: Min_Rho at K=2: {find_min_rho(N, 2.0, xi, metric_type):.6f}")

    K_coarse = np.linspace(0.0, 2.0, 200)
    K_low = 0.0
    K_high = 2.0
    found_transition = False

    for K in K_coarse:
        min_rho = find_min_rho(N, K, xi, metric_type)
        if min_rho < 0:
            K_high = K
            found_transition = True
            break
        K_low = K

    if not found_transition:
        print(f"  [WARNING] N={N}: No transition found (Min_Rho never < 0). Returning None.")
        return None

    iterations = 0
    max_iter = 60

    while (K_high - K_low) > tol and iterations < max_iter:
        K_mid = (K_low + K_high) / 2.0
        min_rho = find_min_rho(N, K_mid, xi, metric_type)

        if min_rho < 0:
            K_high = K_mid
        else:
            K_low = K_mid
        iterations += 1

    return (K_low + K_high) / 2.0

def run_scaling_study_euclidean():
    sizes_L = [2, 3, 4, 5, 6, 8, 10, 16, 32]
    sizes_N = [L * L for L in sizes_L]
    results = []

    print("=" * 90)
    print(f"SCALING STUDY: TWISTED TORUS (EUCLIDEAN METRIC + SMOOTH TWIST)")
    print("Testing if pattern persists in the 'harmonized' regime.")
    print("=" * 90)

    for N in sizes_N:
        L = int(np.sqrt(N))
        print(f"\nProcessing L={L}, N={N}...")
        
        K_c = find_critical_k_binary_debug(N, metric_type="euclidean")
        
        if K_c is None:
            print(f"  Result: NO TRANSITION FOUND")
            results.append({"N": N, "L": L, "K_c": None, "Target_Kc": 4*np.pi/L, "Alpha": None})
        else:
            target_K = 4 * np.pi / L
            alpha = K_c / target_K
            print(f"  Result: K_c = {K_c:.6f}, Alpha = {alpha:.6f}")
            results.append({"N": N, "L": L, "K_c": K_c, "Target_Kc": target_K, "Alpha": alpha})

    # Save
    df = pd.DataFrame(results)
    df.to_csv('scaling_results_torus_smooth_euclidean.csv', index=False)
    print("\nResults saved to 'scaling_results_torus_smooth_euclidean.csv'")
    
    # Check pattern
    print("\n" + "=" * 90)
    print("PATTERN CHECK (Euclidean + Smooth Twist)")
    print("Does K_c * floor(L/2) stay constant?")
    print("=" * 90)
    for i, row in df.iterrows():
        if pd.notna(row['K_c']):
            prod = row['K_c'] * (row['L'] // 2)
            print(f"L={row['L']:2d}: K_c * floor(L/2) = {prod:.6f}")

if __name__ == "__main__":
    run_scaling_study_euclidean()
