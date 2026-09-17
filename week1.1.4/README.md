# Two Machine Learning Models with Scikit-learn

## Overview

This project is part of the Skillset Go AI/ML Week 1 practical tasks.

The objective is to build and evaluate two supervised machine learning models using Scikit-learn:

1. A regression model
2. A classification model

## Tools Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Google Colab

## Regression Model

A regression model is trained for a numerical prediction task.

The workflow includes:

* Loading the dataset
* Separating features and target
* Splitting the data into training and testing sets
* Training the model
* Making predictions
* Evaluating predictions

### Regression Metrics

The regression model is evaluated using:

* MAE
* RMSE
* R²

## Classification Model

A classification model is trained for a categorical prediction task.

The workflow includes:

* Loading the dataset
* Separating features and target
* Preprocessing the input data
* Splitting the data into training and testing sets
* Training the classification model
* Making predictions
* Evaluating the predictions
* Inspecting incorrect predictions

### Classification Metrics

The classification model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

## Error Analysis

Incorrect predictions are inspected to understand where the model makes mistakes and what types of cases may be difficult for the model.

## Reproducibility

The notebook documents the dataset, preprocessing, model setup, evaluation metrics, and important assumptions required to reproduce the work.

## Notebook

The complete implementation is available in:

`Week_1_1_4_ML_Models.ipynb`

## What I Learned

I learned the basic supervised machine learning workflow from preparing the data to training, prediction, and evaluation.

I learned that regression and classification are different types of problems and require different evaluation metrics.

I also learned how to inspect incorrect predictions instead of focusing only on the final performance scores.

## Challenges

The main challenge was understanding the difference between regression and classification workflows.

Another challenge was selecting and interpreting the appropriate evaluation metrics and understanding incorrect predictions.

## What I Would Improve

I would improve the models by testing additional suitable algorithms and comparing their performance with the baseline models.

I would also perform more detailed error analysis and experiment with preprocessing choices while keeping the evaluation procedure consistent.
