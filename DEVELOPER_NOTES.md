# Developer Notes — Regression Wow

## 1. Project Overview

Regression Wow is a Python program that performs simple linear regression using user-provided X and Y data.

It calculates the regression equation, statistical measurements, and predicted Y values for observations with missing Y data. It also generates a visualization using Matplotlib.

The project is currently implemented in a single Python script.

### Dependencies
- `matplotlib`
- `math` (standard library)
- `os` (standard library)

---

## 2. Current Implementation

### Statistical Functions

| Function | Purpose |
|---|---|
| `ListPow2(A)` | Returns a list containing the squares of the elements of A. |
| `mean(A)` | Calculates the arithmetic mean. |
| `meanTwoVar(A, B)` | Calculates the mean of the element-wise products of two lists. |
| `COV(X, Y)` | Calculates population covariance. |
| `COV2(X, Y)` | Calculates covariance using the alternative formula. |
| `stddev(A)` | Calculates population standard deviation. |
| `coeffCorr(X, Y)` | Calculates the Pearson correlation coefficient. |
| `coeffCorr2(X, Y)` | Calculates correlation using the alternative covariance formula. |
| `clean(A)` | Converts valid inputs to floats and marks invalid inputs as missing data. |

### Regression Functions

**`reg(data)`**

Calculates the coefficients of the simple linear regression equation:

\[
\hat{y}=a+bx
\]

Where:
- `a` is the intercept.
- `b` is the slope.

The function uses the relationship between correlation, standard deviations, and the regression slope.

It also handles two special cases:
- If the standard deviation of X is zero, regression cannot be performed.
- If the standard deviation of Y is zero, it returns a horizontal regression line.

**`reg2(data)`**

An alternative implementation of regression using `COV2` and `coeffCorr2`.

This function is currently marked as unsafe and should not be used.

**`line(data, line)`**

Calculates predicted Y values for a collection of X values using the regression equation.

---

## 3. Current Data-Handling Workflow

The program currently follows these steps:

1. Collect X values from the user.
2. Collect Y values from the user.
3. Convert valid values to floats.
4. Identify missing or invalid values using `"ND"`.
5. Remove missing observations.
6. Attempt to match the sizes of the X and Y lists.
7. Perform regression on the remaining data.
8. Predict missing Y values.
9. Display statistical results.
10. Generate a scatter plot and regression line.

**Important:** The current data-cleaning implementation needs further work. In particular, removing values independently from X and Y can destroy the correspondence between observations.

See the known issues below.

---

## 4. Known Issues and Limitations

### 4.1 Data Alignment — High Priority

The most important current issue is the handling of missing data.

X and Y represent paired observations. Removing an element from one list must also account for the corresponding element in the other list.

Currently:
- Missing X values are removed independently.
- Missing Y values are removed separately.
- Removing X values before processing Y can shift the positions of subsequent observations.
- The final size-matching procedure removes extra values from the end, which does not necessarily preserve the correct pairs.

**Required improvement:**

Process X and Y together, preserving their original positions.

For each observation:
- Valid X and valid Y: include the pair in regression.
- Valid X and missing Y: retain X for Y prediction.
- Missing X and valid Y: exclude the pair from regression.
- Missing X and missing Y: exclude the pair.

The original observation order should be preserved throughout the process.

### 4.2 Input Termination

The input loops append the termination string `"..."` to the lists before stopping.

The `clean()` function subsequently treats this string as invalid data.

**Required improvement:** Check for the termination command before appending the input.

### 4.3 Index Zero Is Not Processed

The current missing-data removal loops use:

`range(len(X)-1, 0, -1)`

The loop does not include index zero.

Consequently, missing data at the first position can remain in the list.

**Required improvement:** Correct the loop boundaries or, preferably, replace the independent removal loops with paired observation processing.

### 4.4 Invalid Input Handling

The `clean()` function converts invalid values into `"ND"`.

This means that a typo or accidental input is treated as missing data.

**Possible improvement:**
- Normalize missing-data markers using `strip()` and `upper()`.
- Distinguish explicitly entered `"ND"` from other invalid inputs.
- Reject or request correction of unexpected values.
- Reject non-finite numbers such as NaN and infinity.

### 4.5 Prediction Dictionary

The `line()` function stores predictions in a dictionary using X values as keys.

If multiple observations have the same X value, earlier predictions are overwritten.

**Required improvement:** Consider storing predictions as a list of `(x, predicted_y)` pairs instead of a dictionary.

This also makes it easier to preserve the original observation order.

### 4.6 Insufficient Data

The program does not explicitly validate that enough valid observations exist before calculating statistical measurements.

**Required improvement:**
- Require at least two valid pairs for regression.
- Ensure X and Y have matching lengths.
- Handle empty datasets gracefully.
- Provide meaningful error messages.

### 4.7 Numerical Stability

The standard deviation function currently uses:

$\sigma=\sqrt{E[X^2]-E[X]^2}$

This formula is mathematically valid but can suffer from floating-point precision problems when dealing with large values that have small variation.

**Possible improvement:** Use a numerically more stable variance calculation.

---

## 5. Statistical Considerations

### Population vs. Sample Statistics

The current covariance and standard deviation calculations divide by \(n\), not \(n-1\).

Therefore, they calculate population covariance and population standard deviation.

This is internally consistent for the regression slope because both quantities use the same population denominator.

### Correlation Coefficient

The Pearson correlation coefficient is:

$r=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}$

Correlation is undefined when either variable has zero standard deviation.

The program currently handles this when displaying the correlation and coefficient of determination.

### Coefficient of Determination

The program calculates:


$R^2=r^2$

For ordinary simple linear regression with an intercept and nonconstant Y, this is equivalent to the usual coefficient of determination.

When Y is constant, the conventional coefficient of determination is undefined.

### Alternative Regression Formula

The regression slope can also be calculated directly:


$b=\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(X)}$


And the intercept:


$a=\bar{Y}-b\bar{X}$


This approach avoids calculating the correlation coefficient just to obtain the regression slope.

It is worth considering for a future implementation of `reg()`.

---

## 6. Technical Debt

The following areas should be reviewed during future refactoring:

- `reg2()` is unused and marked unsafe.
- `COV2()` and `coeffCorr2()` are currently only used by `reg2()`.
- `meanTwoVar()` is only used by `COV2()`.
- `ListPow2()` is only used by `stddev()`.
- The `line()` function uses a dictionary, which can lose duplicate X observations.
- Data collection, cleaning, regression, output, and visualization are all contained in one script.
- Error handling is limited and should be made more consistent.

These are not all immediate problems, but addressing them would improve maintainability.

---

## 7. Development Roadmap

### Priority 1 — Correctness and Reliability

- [ ] Fix positional data alignment.
- [ ] Fix the input termination behavior.
- [ ] Correct the index-zero handling issue.
- [ ] Validate matching X and Y lengths.
- [ ] Validate the number of usable observations.
- [ ] Improve invalid-input handling.
- [ ] Handle NaN and infinity.
- [ ] Preserve duplicate X values in predictions.

### Priority 2 — Statistical Improvements

- [ ] Improve numerical stability of standard deviation.
- [ ] Implement residual calculations.
- [ ] Calculate SSE (Sum of Squared Errors).
- [ ] Add residual visualization.
- [ ] Improve the statistical output.
- [ ] Review the alternative regression formula.

### Priority 3 — Software Engineering

- [ ] Remove unused and redundant functions.
- [ ] Separate data collection from statistical calculations.
- [ ] Separate visualization from regression logic.
- [ ] Introduce automated tests.
- [ ] Improve error messages.
- [ ] Organize the program into separate modules if necessary.

### Priority 4 — Additional Features

- [ ] Support importing data from CSV files.
- [ ] Allow users to save regression results.
- [ ] Add more regression diagnostics.
- [ ] Consider a graphical user interface.
- [ ] Explore multiple linear regression.

---

## 8. Development Philosophy

Regression Wow is intended to be more than a program that draws a regression line.

The goal is to build a reliable statistical tool while understanding the mathematics and computational methods behind it.

Whenever possible:
- Understand the mathematical reasoning before implementing a formula.
- Keep statistical calculations independent of user-interface code.
- Preserve the original data.
- Validate assumptions before performing calculations.
- Test edge cases, not only ordinary datasets.
- Prefer readable and maintainable code over unnecessary complexity.

**Last updated:** November 2026

**Status:** Early development — basic simple linear regression implemented; data handling and validation require further work.