#!/usr/bin/env python3
"""
smooth_twist_sensitivity_test.py
Tests if the system can be stabilized by weakening the smooth twist.

Variants Tested:
1. Linear Ramp: Twist 
2. Weak Cosine: Twist 

"""

import numpy as np
import pandas as pd
import time

def calculate_distance_and_twist(coords, side, metric_type="euclidean", twist_mode="linear"):
    """
    Calculates distance and Twist based on the selected mode.
    """
    N = len(coords)
    D = np.zeros((N, N))
    Twist = np.ones((N, N))
    
    for i in range(N):
        for j in range(i + 1, N):
            dx_direct = abs(coords[i, 0] - coords[j, 0])
            dy_direct = abs(coords[i, 1] - coords[j, 1])
            
            # Wrapping for distance
            dx = dx_direct if dx_direct < (side - dx_direct) else (side - dx_direct)
            dy = dy_direct if dy_direct < (side - dy_direct) else (side - dy_direct)
            
            if metric_type == "manhattan":
                dist = dx + dy
            elif metric_type == "euclidean":
                dist = np.sqrt(dx**2 + dy**2)
            else:
                raise ValueError(f"Unknown metric type: {metric_type}")
            
            D[i, j] = D[j, i] = dist
            
            # --- TWIST LOGIC ---
            
            if twist_mode == "linear":
                if dx_direct < side / 2.0:
                    val = 1.0 - 4.0 * (dx_direct / side)
                else:
                    val = -1.0 + 4.0 * ((dx_direct - side/2.0) / (side/2.0))
                Twist[i, j] = val
                Twist[j, i] = val
                
            elif twist_mode == "weak_cosine":
                base = np.cos(2 * np.pi * (dx_direct / side))
                Twist[i, j] = 0.5 * base
                Twist[j, i] = 0.5 * base
            
            elif twist_mode == "shifted_cosine":
                pass

    return D, Twist

def calculate_correlation_matrix(N, K_eff, xi=10.0, metric_type="euclidean", twist_mode="linear"):
    side = int(np.sqrt(N))
    x = np.arange(side)
    y = np.arange(side)
    X, Y = np.meshgrid(x, y)
    coords = np.vstack([X.flatten(), Y.flatten()]).T
    
    D, Twist = calculate_distance_and_twist(coords, side, metric_type, twist_mode)
    
    G_matrix = np.cos(K_eff * D) * np.exp(-D / xi)
    C = G_matrix * Twist
    
    C = C + 0.1 * np.eye(N)
    
    std_devs = np.sqrt(np.diag(C))
    std_devs[std_devs == 0] = 1.0
    C_norm = C / np.outer(std_devs, std_devs)
    
    return C_norm, D

def find_min_rho(N, K_eff, xi=10.0, metric_type="euclidean", twist_mode="linear"):
    C_norm, D = calculate_correlation_matrix(N, K_eff, xi, metric_type, twist_mode)
    
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

def run_sensitivity_test():
    modes = ["linear", "weak_cosine"]
    sizes = [4, 16, 64]
    
    print("=" * 80)
    print("SENSITIVITY TEST: Can we stabilize the system?")
    print("=" * 80)
    
    for mode in modes:
        print(f"\n--- Testing Mode: {mode.upper()} ---")
        for N in sizes:
            L = int(np.sqrt(N))
            rho_0 = find_min_rho(N, 0.0, metric_type="euclidean", twist_mode=mode)
            print(f"N={N}, L={L}: Min_Rho at K=0 = {rho_0:.6f}")
            
            if rho_0 > 0:
                print(f"  >>> STABLE! System is static at K=0.")
                # Try to find K_c
                K_coarse = np.linspace(0.0, 2.0, 100)
                found = False
                for K in K_coarse:
                    if find_min_rho(N, K, metric_type="euclidean", twist_mode=mode) < 0:
                        print(f"  >>> Transition found at K ~ {K:.2f}")
                        found = True
                        break
                if not found:
                    print(f"  >>> No transition found up to K=2.0")
            else:
                print(f"  >>> UNSTABLE. System oscillates at K=0.")

if __name__ == "__main__":
    run_sensitivity_test()
