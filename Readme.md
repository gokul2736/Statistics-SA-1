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

## 1. Independent T-Test
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

### Output:
*(Add your program output here)*  

---

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

### Output:
*(Add your program output here)*  

---

## 3. One-Sample Z-Test
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

### Output:
*(Add your program output here)*  

---

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

### Output:
*(Add your program output here)*  

---

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

### Output:
*(Add your program output here)*  

---

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

### Output:
*(Add your program output here)*  

---

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

### Output:
*(Add your program output here)*  
