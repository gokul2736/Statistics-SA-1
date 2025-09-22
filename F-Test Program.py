import numpy as np
from scipy.stats import f

#
# F-Test Real-Time Experiment
#

# Aim: To determine if there is a significant difference between the variances of two samples.
# Problem: Compare the production time consistency of two different machines.

# --- Data ---
machine1_times = np.array([12, 15, 14, 16, 13, 15, 14, 16, 15, 13])
machine2_times = np.array([11, 14, 13, 15, 12, 14, 13, 12, 14, 13])

# --- Calculations ---
# Calculate sample variances
var1 = np.var(machine1_times, ddof=1)
var2 = np.var(machine2_times, ddof=1)

# Ensure the larger variance is in the numerator for the F-statistic
if var1 > var2:
    F_stat = var1 / var2
    df1 = len(machine1_times) - 1
    df2 = len(machine2_times) - 1
else:
    F_stat = var2 / var1
    df1 = len(machine2_times) - 1
    df2 = len(machine1_times) - 1

# Find the critical F-value from the F-distribution for a two-tailed test
alpha = 0.05
F_critical = f.ppf(1 - alpha / 2, df1, df2)

# --- Output ---
print("--- F-Test Results ---")
print(f"Variance of Machine 1: {var1:.3f}")
print(f"Variance of Machine 2: {var2:.3f}")
print(f"F-statistic: {F_stat:.3f}")
print(f"Critical F-value (for alpha=0.05): {F_critical:.3f}")

# --- Conclusion ---
if F_stat > F_critical:
    print("\nResult: Reject null hypothesis. Variances are significantly different.")
else:
    print("\nResult: Fail to reject null hypothesis. Variances are similar.")
