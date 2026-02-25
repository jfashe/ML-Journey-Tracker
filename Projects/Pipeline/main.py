# Imports
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split #flashcards?
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Loading Data
data = pd.read_csv("vehicle_emissions.csv")
data.head()
data.info()

# Create features and target variables
# Split Categorial and Numerical Features
# Combine the pipelines
# Split into training and testing
# Train and predict model
# Evaluate model accuracy