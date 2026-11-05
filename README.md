# Regression Wow



A Python implementation of **Simple Linear Regression**, built from scratch using basic Python mathematics and Matplotlib.



The project aims to explore the mathematical foundations of linear regression while providing a practical tool for analyzing datasets, handling missing observations, estimating values, and visualizing results.



## Features



- Manual implementation of statistical functions.

- Calculation of mean, covariance, standard deviation, and Pearson's correlation coefficient.

- Simple linear regression using the least-squares method.

- Handling of missing observations (`ND`).

- Estimation of missing Y values using the regression model.

- Visualization of observed data, predicted values, and the regression line.

- Basic validation for datasets with no variation in X or Y.



## Requirements



- Python 3

- Matplotlib



Install the dependency with:



```bash

pip install -r requirements.txt

```



## How to use



Run the program:



```bash

python main.py

```



Enter your X and Y observations separately.



- Enter numerical values for observations.

- Enter `ND` when an observation is missing.

- Enter `...` to finish entering a dataset.



The program then cleans the data, matches corresponding observations, performs regression, and displays a visualization.



**Note:** The current development version contains hardcoded test datasets. Remove these assignments in `main.py` to enable interactive data collection.



## Mathematical foundations



### Descriptive statistics



The program implements:



**Arithmetic mean**

$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$

**Population covariance**

$COV(X,Y) = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})$

**Population standard deviation**

$\sigma_X = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2}$

**Pearson correlation coefficient**

$\rho_{XY} = \frac{COV(X,Y)}{\sigma_X \sigma_Y}$

### Simple linear regression



The program calculates the regression equation:


${\hat{y}} = a + b x$

Where:

$b = {\rho_{XY}} \frac{\sigma_Y}{\sigma_X}$

and 

$a = \bar{y} - b \bar{x}$


The regression line minimizes the sum of squared vertical residuals.



## Project structure



| File | Purpose |


| `main.py` | Statistical functions, data processing, regression, and visualization |

| `requirements.txt` | External Python dependencies |

| `.gitignore` | Files excluded from Git tracking |

| `README.md` | Project documentation |



## Current limitations



- Missing observations are matched using their original positions, but the current implementation also removes unmatched observations from the end of the longer dataset.

- Invalid inputs are converted into missing-data markers after displaying a warning.

- Only missing Y values are estimated.

- Correlation and the conventional coefficient of determination are undefined when either variable has zero variance.

- The program currently uses population standard deviation and covariance.

- Numerical stability for very large or very small values has not yet been addressed.

- Input validation and error handling are still under development.



## Future development



See the [Developer Notes](DEVELOPER_NOTES.md) and improvement roadmap for planned features.



---



**Regression Wow** is an educational project intended to explore the mathematics and programming concepts behind statistical regression.

