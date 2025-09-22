import numpy as np
from scipy.stats import f

#
# One-Way ANOVA Real-Time Experiment
#

# Aim: To check for significant differences in means across three or more groups.
# Problem: Test if three different teaching methods result in different average student scores.

# --- Data ---
method1 = np.array([85, 90, 88, 86, 89])
method2 = np.array([78, 82, 79, 81, 77])
method3 = np.array([92, 88, 91, 95, 94])
all_data = [method1, method2, method3]

# --- Calculations ---
# Basic parameters
k = len(all_data)
n_total = sum(len(group) for group in all_data)
overall_mean = np.mean(np.concatenate(all_data))

# Sum of Squares Between Groups (SSB)
group_means = [np.mean(group) for group in all_data]
SSB = sum(len(group) * (mean - overall_mean)**2 for group, mean in zip(all_data, group_means))

# Sum of Squares Within Groups (SSW)
SSW = sum(sum((x - mean)**2 for x in group) for group, mean in zip(all_data, group_means))

# Degrees of Freedom
df_between = k - 1
df_within = n_total - k

# Mean Squares
MSB = SSB / df_between
MSW = SSW / df_within

# F-statistic
F_statistic = MSB / MSW

# Critical F-value
alpha = 0.05
F_critical = f.ppf(1 - alpha, df_between, df_within)

# --- Output ---
print("--- One-Way ANOVA Results ---")
print(f"F-statistic: {F_statistic:.3f}")
print(f"Critical F-value (for alpha=0.05): {F_critical:.3f}")

# --- Conclusion ---
if F_statistic > F_critical:
    print("\nResult: Reject null hypothesis. There is a significant difference between the teaching methods.")
else:
    print("\nResult: Fail to reject null hypothesis. No significant difference between teaching methods.")
