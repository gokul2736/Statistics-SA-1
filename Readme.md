# Skill Assessment - 1 Statistical Tests in Python  
## NAME: MARKANDEYAN GOKUL  
## ROLL NO: 212224240086  


### This collection includes implementations for the following statistical tests:

- **T-Test** (`t-test.py`) - Compares the means of two independent groups.  
- **F-Test** (`f-test.py`) - Compares the variances of two independent groups.  
- **Z-Test** (`z-test.py`) - Tests a sample mean against a known population mean.  
- **Chi-Square Test** (`chisquare.py`) - Tests the goodness of fit for categorical data.  
- **One-Way ANOVA** (`onewayanova.py`) - Compares the means of three or more groups.  
- **Two-Way ANOVA** (`twowayanova.py`) - Tests the effect of two independent factors on a dependent variable.  
- **Latin Square Design ANOVA** (`latinsquare.py`) - Tests treatment effects while controlling for two blocking factors.  

---

### Prerequisites
- Python 3.7 or newer  
- Libraries: `numpy`, `scipy`, `pandas` (optional)  
- Basic understanding of statistical concepts and hypothesis testing  

---

## 1. T-Test
- **Aim:** Compare the average scores of two student groups.  
- **Case Statement:** A teacher wants to check if two teaching methods produce different results.  

### Algorithm:
1. Define datasets for Group A and Group B.  
2. Formulate hypotheses:  
   - H₀: μ₁ = μ₂ (both teaching methods equally effective)  
   - H₁: μ₁ ≠ μ₂ (there is a difference in effectiveness)  
3. Compute mean and standard deviation for both groups.  
4. Calculate pooled standard error:  
   \[
   SE = \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}
   \]  
5. Compute t-statistic:  
   \[
   t = \frac{\bar{x}_1 - \bar{x}_2}{SE}
   \]  
6. Compute degrees of freedom and p-value.  
7. Compare p-value with α = 0.05 to make a decision.  

### Program
```python
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

```
### Output:
<img width="878" height="243" alt="image" src="https://github.com/user-attachments/assets/1ac5d6a2-05b4-437f-b285-9d445752c307" />
 



## 2. F-Test
- **Aim:** Compare variances of two independent samples.  
- **Case Statement:** Compare production times from two machines to see if variability differs.  

### Algorithm:
1. Collect sample data for both machines.  
2. Compute sample variances \(s_1^2, s_2^2\).  
3. Compute F-statistic:  
   \[
   F = \frac{s_1^2}{s_2^2}
   \]  
4. Determine degrees of freedom: df1 = n1-1, df2 = n2-1.  
5. Compare F-statistic with critical F-values or calculate p-value.  
6. Draw conclusion based on α = 0.05.  

### Program
```python
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

```
### Output:
<img width="733" height="220" alt="image" src="https://github.com/user-attachments/assets/04f1c372-97ee-420a-aed9-9e1953249e8b" />
  



## 3. Z-Test
- **Aim:** Test whether a sample mean differs from a claimed population mean.  
- **Case Statement:** Verify if the average sugar content in soft drinks is less than 30g.  

### Algorithm:
1. Collect sample data.  
2. Formulate hypotheses:  
   - H₀: μ = 30  
   - H₁: μ < 30  
3. Compute sample mean and standard deviation.  
4. Calculate Z-statistic:  
   \[
   Z = \frac{\bar{x} - \mu}{s/\sqrt{n}}
   \]  
5. Compute p-value using standard normal distribution.  
6. Compare p-value with α = 0.05 to make a decision.  

### Program
```python
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

```

### Output:
<img width="821" height="183" alt="image" src="https://github.com/user-attachments/assets/adfb0852-f56f-4a4e-a811-6f491738e367" />



## 4. Chi-Square Test
- **Aim:** Determine if a categorical variable follows a specified distribution.  
- **Case Statement:** Test if a six-sided die is fair.  

### Algorithm:
1. Collect observed frequencies for each category.  
2. Compute expected frequencies (for fair die, all outcomes equally likely).  
3. Compute Chi-Square statistic:  
   \[
   \chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}
   \]  
4. Determine degrees of freedom: df = n_categories - 1.  
5. Compare Chi-Square statistic with critical value or p-value.  

### Program
```python
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

```

### Output:
<img width="647" height="191" alt="image" src="https://github.com/user-attachments/assets/19bd0e60-589b-4a18-aff2-0bf78efb75e6" />



## 5. One-Way ANOVA
- **Aim:** Compare means across multiple groups.  
- **Case Statement:** Evaluate the effect of three teaching methods on student scores.  

### Algorithm:
1. Collect data for all groups.  
2. Compute group means and overall mean.  
3. Compute Sum of Squares Between Groups (SSB):  
   \[
   SSB = \sum n_i (\bar{x}_i - \bar{x})^2
   \]  
4. Compute Sum of Squares Within Groups (SSW):  
   \[
   SSW = \sum \sum (x_{ij} - \bar{x}_i)^2
   \]  
5. Compute F-statistic:  
   \[
   F = \frac{MSB}{MSW} = \frac{SSB/df_{between}}{SSW/df_{within}}
   \]  
6. Compare with F-critical or p-value.  

### Program
```python
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

```

### Output:
<img width="999" height="163" alt="image" src="https://github.com/user-attachments/assets/861d3637-8cca-4062-aa06-d0d5f9c32875" />



## 6. Two-Way ANOVA
- **Aim:** Examine the effects of two factors and their interaction.  
- **Case Statement:** Study how teaching method and study environment affect student scores.  

### Algorithm:
1. Collect data for all factor combinations.  
2. Compute total sum of squares, factor sums of squares, interaction sum of squares, and error sum of squares.  
3. Compute degrees of freedom and Mean Squares (MS = SS/df).  
4. Compute F-statistics:  
   \[
   F_{Factor} = \frac{MS_{Factor}}{MS_{Error}}
   \]  
5. Compare with F-critical values or p-value.  

### Program
```python
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

```

### Output:
<img width="792" height="286" alt="image" src="https://github.com/user-attachments/assets/003006b8-a42f-486d-830c-e9a2762ee3db" />



## 7. Latin Square Design ANOVA
- **Aim:** Test treatment effects while controlling for two blocking factors.  
- **Case Statement:** Determine the effect of different fertilizers on crop yield while controlling for row (soil) and column (sunlight).  

### Algorithm:
1. Input Latin Square data (treatments × rows × columns).  
2. Compute row totals, column totals, treatment totals, and grand total.  
3. Compute sum of squares: SS_Total, SS_Row, SS_Column, SS_Treatment, SS_Error.  
4. Compute degrees of freedom and Mean Squares.  
5. Calculate F-statistic for treatment effect:  
   \[
   F_{Treatment} = \frac{MS_{Treatment}}{MS_{Error}}
   \]  
6. Compare with F-critical to make a decision.  

### Program
```python
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

```

### Output:
<img width="864" height="165" alt="image" src="https://github.com/user-attachments/assets/c4c4a56f-6aeb-44bc-b487-f3b0f2d31d24" />

## Installation and Setup

Follow these steps to set up the local environment.

### 1. Clone the Repository
```bash
git clone https://github.com/gokul2736/STATISTICS-SA-1
cd STATISTICS-SA-1
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv .venv
```
### 3. Install Required Libraries
```bash
pip install -r requirements.txt
```

### 4. How to Run the Programs
Example: Running the T-Test Program
```bash
python t-test.py
```
## The Result of the statistical test will be printed on terminal.
