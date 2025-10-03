# Project_WiDS2023

## Abstract
This project addresses the **WiDS 2023 Challenge** by developing and evaluating machine learning models for predictive analytics.  
The pipeline includes **exploratory data analysis (EDA)**, **data preprocessing**, **feature engineering**, and **hyperparameter optimization using Optuna**.  
Among all tested algorithms, **XGBoost** achieved the best performance, evaluated using **Root Mean Square Error (RMSE)** as the primary metric.

---

## Methodology

### 1. Data Preprocessing
- Handled missing values through imputation strategies.  
- Encoded categorical variables using suitable encoding techniques.  
- Normalized numerical variables where appropriate.  

### 2. Feature Engineering
- Constructed additional variables to capture hidden patterns.  
- Selected the most relevant features to reduce redundancy.  

### 3. Model Development
- Several models were initially explored for benchmarking (e.g., Random Forest, LightGBM and catBoost).  

- **XGBoost was chosen as the main model** due to its superior performance.  
- Hyperparameter tuning was conducted using **Optuna**, leveraging Bayesian optimization techniques to minimize RMSE.  

### 4. Evaluation
- The **Root Mean Square Error (RMSE)** was used as the primary evaluation metric, as it directly reflects prediction error magnitudes.  
- Cross-validation was applied to ensure robustness and reduce overfitting.  

---

## Results
- **Best Performing Model:** XGBoost  
- **Optimization Framework:** Optuna (automated hyperparameter search)  
- **Evaluation Metric:** RMSE  
- Comparative model (catBoost, Random Forest, LightGBM) yielded higher RMSE and were therefore not selected.  

---

## Reproducibility
- All experiments are documented in Jupyter Notebooks under `notebooks/`.  
- Core functionalities for preprocessing, optimization, and evaluation are modularized in `src/`.  
- Trained models and prediction outputs are saved in `outputs/`.  

---

## Future Work
- Explore advanced ensemble techniques to complement XGBoost.  
- Investigate deep learning approaches (e.g., Neural Networks) for comparison.  
- Apply fairness-aware analysis to detect and mitigate potential biases.  
- Deploy the optimized XGBoost model in a production environment for real-world use cases.  

--- 