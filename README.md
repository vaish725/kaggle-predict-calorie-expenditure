# Kaggle Predict Calorie Expenditure

This repository contains my solution for the Kaggle Playground Series S5E5 competition on predicting calorie expenditure based on physiological features.

## Project Overview

The goal of this competition was to predict calorie expenditure using features like duration, heart rate, body temperature, age, height, weight, and gender. The evaluation metric was Root Mean Squared Logarithmic Error (RMSLE).

## Repository Structure

```
📁 Project Structure
├── eda_step1.ipynb                     # Exploratory Data Analysis
├── preprocessing_step2.ipynb           # Data preprocessing
├── feature_engineering_step2b.ipynb    # Feature engineering (first iteration)
├── baseline_modelling_step3.ipynb      # Baseline models
├── xgboost_tuning_step4.ipynb          # XGBoost hyperparameter tuning
├── ensemble_models_step5.ipynb         # Model ensemble experiments
├── stacking_step5b.ipynb               # Stacking ensemble (first iteration)
├── shap_analysis_step6.ipynb           # SHAP feature importance analysis
├── feature_engineering_shap_step7.ipynb # Feature engineering informed by SHAP
├── xgboost_retrain_fe_v2_step7b.ipynb  # XGBoost with enhanced features
├── stacking_v2_meta_xgb.ipynb          # Meta-model stacking (final version)
├── assets/                             # Visualizations and images
├── datasets/                           # Data files
│   ├── submissions/                    # Model predictions
│   ├── train.csv                       # Original training data
│   ├── test.csv                        # Original test data
│   └── ...                             # Processed datasets
└── score_tracking/                     # Competition score records
```

## Methodology

My approach followed these key steps:

1. **Exploratory Data Analysis**: I examined distributions, correlations, and patterns in the data, noting that Duration, Heart Rate, and Body Temperature were highly correlated with calorie expenditure.

2. **Preprocessing**: I cleaned the data and encoded categorical features (Sex).

3. **Feature Engineering**: Created interaction features and polynomial features based on domain knowledge and correlations.

4. **Model Development**: 
   - Started with baseline models (Linear Regression, Random Forest)
   - Optimized XGBoost parameters through rigorous tuning
   - Explored ensemble approaches including averaging and stacking
   - Used SHAP values to guide further feature engineering

5. **Final Solution**: A stacked ensemble with XGBoost as the meta-learner on top of base models.

## Key Results

- Best single model: XGBoost with SHAP-guided feature engineering (RMSLE: 0.01712)
- Best ensemble: Stacked Meta-XGBoost (RMSLE: 0.01742)
- Feature importance: Duration, Heart Rate, and Body Temperature were the most influential predictors

## Technical Requirements

- Python 3.8+
- Libraries: pandas, numpy, scikit-learn, xgboost, lightgbm, matplotlib, seaborn, shap

## References

- RMSLE metric: [Understanding the metric RMSLE](https://www.kaggle.com/code/carlolepelaars/understanding-the-metric-rmsle)
- Ensemble Methods: Zhou, Z. H. (2012) "Ensemble Methods: Foundations and Algorithms"
- Stacking concept: Wolpert, D. H. (1992). "Stacked generalization"