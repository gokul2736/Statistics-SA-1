import numpy as np
from scipy import stats
import math

#
# T-Test Real-Time Experiment
#

# Aim: To test for a significant difference between the average marks of two groups.
# Problem: Compare the effectiveness of two teaching methods.

# --- Data ---
group_A = np.array([85, 78, 92, 88, 76, 81, 95, 89, 77, 84])
group_B = np.array([80, 74, 85, 90, 70, 79, 83, 82, 78, 75])

# --- Calculations ---
# Calculate means and standard deviations
mean_A, mean_B = np.mean(group_A), np.mean(group_B)
std_A, std_B = np.std(group_A, ddof=1), np.std(group_B, ddof=1)
n1, n2 = len(group_A), len(group_B)

# Calculate t-statistic using Welch's t-test formula (for unequal variances)
t_stat = (mean_A - mean_B) / math.sqrt((std_A**2 / n1) + (std_B**2 / n2))

# Calculate degrees of freedom using the Welch-Satterthwaite equation
df = (((std_A**2 / n1) + (std_B**2 / n2))**2) / \
     (((std_A**2 / n1)**2 / (n1 - 1)) + ((std_B**2 / n2)**2 / (n2 - 1)))

# Calculate the two-tailed p-value from the t-distribution
p_value = stats.t.sf(np.abs(t_stat), df) * 2

# --- Output ---
print("--- T-Test Results ---")
print(f"Mean of Group A: {mean_A:.2f}")
print(f"Mean of Group B: {mean_B:.2f}")
print(f"t-statistic: {t_stat:.3f}")
print(f"Degrees of Freedom: {df:.2f}")
print(f"P-value: {p_value:.6f}")

# --- Conclusion ---
alpha = 0.05
if p_value < alpha:
    print("\nResult: Reject H0 -> There is a significant difference between teaching methods.")
else:
    print("\nResult: Fail to Reject H0 -> No significant difference between teaching methods.")
