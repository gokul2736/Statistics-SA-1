import numpy as np
import math

#
# Z-Test Real-Time Hypothesis Testing
#

# Aim: To test if a sample mean is significantly less than a claimed population mean.
# Problem: Test if the average sugar content in soft drinks is less than the claimed 30g.
# Note: A Z-test assumes the population standard deviation is known.

# --- Data ---
claimed_mean = 30
sample_data = np.array([28.5, 29.2, 30.1, 29.5, 28.9, 29.0, 29.4, 28.7, 29.1, 28.8])
# For a true Z-test, this would be given. We'll assume it's known.
population_std_dev = 0.5

# --- Calculations ---
sample_mean = np.mean(sample_data)
n = len(sample_data)

z_stat = (sample_mean - claimed_mean) / (population_std_dev / math.sqrt(n))

# Custom function to calculate p-value from Z-statistic (area to the left)
def normal_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

p_value = normal_cdf(z_stat) # One-tailed test

# --- Output ---
print("--- Z-Test Results ---")
print(f"Sample Mean: {sample_mean:.2f}")
print(f"Z-statistic: {z_stat:.3f}")
print(f"P-value: {p_value:.6f}")

# --- Conclusion ---
alpha = 0.05
if p_value < alpha:
    print("\nResult: Reject H0 -> The average sugar content is significantly less than 30g.")
else:
    print("\nResult: Fail to Reject H0 -> No strong evidence that the sugar content is less than 30g.")
