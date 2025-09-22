import numpy as np
from scipy.stats import f

#
# Latin Square Design ANOVA Real-Time Experiment
#

# Aim: To test the effect of a treatment while controlling for two blocking factors.
# Problem: Test the effect of four fertilizers on crop yield, controlling for soil and sunlight.

# --- Data ---
yields = np.array([
    [20, 22, 19, 21],  # Row 1
    [23, 20, 22, 21],  # Row 2
    [21, 23, 20, 22],  # Row 3
    [22, 21, 23, 20]   # Row 4
])

treatments = np.array([
    ['A', 'B', 'C', 'D'],
    ['B', 'C', 'D', 'A'],
    ['C', 'D', 'A', 'B'],
    ['D', 'A', 'B', 'C']
])
t = 4 # number of treatments/rows/columns

# --- Calculations ---
# Grand Total and Correction Factor (CF)
grand_total = np.sum(yields)
CF = grand_total**2 / (t * t)

# Sum of Squares Total (SST)
SST = np.sum(yields**2) - CF

# Sum of Squares for Rows and Columns
SS_Row = np.sum(np.sum(yields, axis=1)**2) / t - CF
SS_Column = np.sum(np.sum(yields, axis=0)**2) / t - CF

# Sum of Squares for Treatments
treatment_totals = {
    'A': np.sum(yields[treatments == 'A']),
    'B': np.sum(yields[treatments == 'B']),
    'C': np.sum(yields[treatments == 'C']),
    'D': np.sum(yields[treatments == 'D'])
}
SS_Treatment = sum(val**2 for val in treatment_totals.values()) / t - CF

# Sum of Squares for Error
SS_Error = SST - SS_Row - SS_Column - SS_Treatment

# Degrees of Freedom
df_Treatment = t - 1
df_Error = (t - 1) * (t - 2)

# Mean Squares
MS_Treatment = SS_Treatment / df_Treatment
MS_Error = SS_Error / df_Error

# F-statistic for Treatment
F_Treatment = MS_Treatment / MS_Error

# Critical F-value
alpha = 0.05
F_critical = f.ppf(1 - alpha, df_Treatment, df_Error)

# --- Output ---
print("--- Latin Square ANOVA Results ---")
print(f"F-statistic for Treatment: {F_Treatment:.3f}")
print(f"Critical F-value (for alpha=0.05): {F_critical:.3f}")

# --- Conclusion ---
if F_Treatment > F_critical:
    print("\nResult: Reject null hypothesis. Fertilizer type significantly affects crop yield.")
else:
    print("\nResult: Fail to reject null hypothesis. Fertilizer type does not significantly affect crop yield.")
