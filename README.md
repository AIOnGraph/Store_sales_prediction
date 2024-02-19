# Store Sales Prediction with XGBoost Regressor and Streamlit UI

## Overview

This project aims to predict store sales using the XGBoost Regressor model. The user interface (UI) is built using Streamlit, allowing users to interactively explore and make predictions based on input data.

## Data

The dataset used for training and prediction contains the following columns:

- `id`: Unique identifier for each data entry.
- `date`: Date of the sales record.
- `store_nbr`: Store number.
- `family`: Product family/category.
- `onpromotion`: Representing whether the product is on promotion.

Example rows from the dataset:

| id       | date       | store_nbr | family        | onpromotion |
|----------|------------|-----------|---------------|-------------|
| 1048544  | 2014-08-13 | 3         | BEAUTY        | 0           |
| 1048545  | 2014-08-13 | 3         | BEVERAGES     | 2           |
| 1048546  | 2014-08-13 | 3         | BOOKS         | 0           |
| 1048547  | 2014-08-13 | 3         | BREAD/BAKERY  | 0           |
| 1048548  | 2014-08-13 | 3         | CELEBRATION   | 0           |
| 1048549  | 2014-08-13 | 3         | CLEANING      | 3           |
| 1048550  | 2014-08-13 | 3         | DAIRY         | 0           |

## Model Training

The XGBoost Regressor is used to predict store sales based on the provided features. The model is trained on historical data to capture patterns and relationships between the input features and sales.

```python
from xgboost import XGBRegressor
# Code for model training...
