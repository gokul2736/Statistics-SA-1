import numpy as np
from scipy.stats import f

#
# Two-Way ANOVA Real-Time Experiment
#

# Aim: To test the effects of two factors (and their interaction) on a dependent variable.
# Problem: Test the effect of teaching method and study environment on student scores.

# --- Data ---
data = {
    'A_Quiet': np.array([85, 88, 90]),
    'A_Noisy': np.array([78, 80, 79]),
    'B_Quiet': np.array([92, 94, 91]),
    'B_Noisy': np.array([81, 83, 82])
}
all_scores = np.concatenate(list(data.values()))
a = 2  # levels in factor 1 (Method: A, B)
b = 2  # levels in factor 2 (Environment: Quiet, Noisy)
n = len(data['A_Quiet']) # replications per cell
N = len(all_scores)

# --- Calculations ---
# Overall Mean and Total Sum of Squares (SST)
grand_mean = np.mean(all_scores)
SST = np.sum((all_scores - grand_mean)**2)

# Sum of Squares for Factor A (Method)
mean_A = np.mean(np.concatenate([data['A_Quiet'], data['A_Noisy']]))
mean_B = np.mean(np.concatenate([data['B_Quiet'], data['B_Noisy']]))
SSA = b * n * ((mean_A - grand_mean)**2 + (mean_B - grand_mean)**2)

# Sum of Squares for Factor B (Environment)
mean_Quiet = np.mean(np.concatenate([data['A_Quiet'], data['B_Quiet']]))
mean_Noisy = np.mean(np.concatenate([data['A_Noisy'], data['B_Noisy']]))
SSB = a * n * ((mean_Quiet - grand_mean)**2 + (mean_Noisy - grand_mean)**2)

# Sum of Squares for Error/Within (SSW)
SSW = sum(np.sum((d - np.mean(d))**2) for d in data.values())

# Sum of Squares for Interaction (SSAB)
SSAB = SST - SSA - SSB - SSW

# Degrees of Freedom
dfA = a - 1
dfB = b - 1
dfAB = (a - 1) * (b - 1)
dfW = N - (a * b)

# Mean Squares
MSA = SSA / dfA
MSB = SSB / dfB
MSAB = SSAB / dfAB
MSW = SSW / dfW

# F-statistics
F_Method = MSA / MSW
F_Environment = MSB / MSW
F_Interaction = MSAB / MSW

# Critical F-value (using df for main effects and error)
alpha = 0.05
F_critical = f.ppf(1 - alpha, dfA, dfW) # Using dfA, can also use dfB as they are same

# --- Output ---
print("--- Two-Way ANOVA Results ---")
print(f"F-Method: {F_Method:.3f}")
print(f"F-Environment: {F_Environment:.3f}")
print(f"F-Interaction: {F_Interaction:.3f}")
print(f"Critical F-value (for alpha=0.05): {F_critical:.3f}")

# --- Conclusion ---
print("\n--- Conclusions ---")
if F_Method > F_critical:
    print("Teaching Method effect: Reject null hypothesis (significant effect).")
else:
    print("Teaching Method effect: Fail to reject null hypothesis (no significant effect).")

if F_Environment > F_critical:
    print("Environment effect: Reject null hypothesis (significant effect).")
else:
    print("Environment effect: Fail to reject null hypothesis (no significant effect).")

if F_Interaction > F_critical:
    print("Interaction effect: Reject null hypothesis (significant effect).")
else:
    print("Interaction effect: Fail to reject null hypothesis (no significant effect).")
