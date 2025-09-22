import numpy as np
from scipy.stats import chi2

#
# Chi-Square Test Real-Time Experiment
#

# Aim: To determine if a six-sided die is fair using the Chi-Square goodness-of-fit test.
# Problem: Compare observed die roll frequencies with expected frequencies for a fair die.

# --- Data ---
observed = np.array([8, 10, 9, 12, 11, 10])

# --- Calculations ---
# Calculate expected frequencies for a fair die
total_rolls = np.sum(observed)
expected = np.full(6, total_rolls / 6)

# Compute the Chi-Square statistic
chi_square_stat = np.sum((observed - expected)**2 / expected)

# Determine degrees of freedom
df = len(observed) - 1

# Find the critical value from the Chi-Square distribution
alpha = 0.05
chi_square_critical = chi2.ppf(1 - alpha, df)

# --- Output ---
print("--- Chi-Square Test Results ---")
print(f"Chi-Square Statistic: {chi_square_stat:.3f}")
print(f"Degrees of Freedom: {df}")
print(f"Critical Chi-Square Value (for alpha=0.05): {chi_square_critical:.3f}")

# --- Conclusion ---
if chi_square_stat > chi_square_critical:
    print("\nResult: Reject null hypothesis. The die is not fair.")
else:
    print("\nResult: Fail to reject null hypothesis. The die is fair.")
