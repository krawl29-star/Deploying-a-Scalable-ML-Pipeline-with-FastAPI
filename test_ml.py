import pytest
from train_model import X_train, X_test
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import compute_model_metrics

# Implement the first test. 
def test_columns():
    """
    Tests training and test to ensure same number of columns
    """
    training_cols = x.train.shape[1]
    test_cols = x_test.shape[1]

    assert training_cols == test_cols # Should assert true


# Implements the second test. 
def test_randomforest():
    """
    Tests if the classifier model used is RandomForest
    """
    X = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([1, 2])

    model = train_model(X, y)
    assert isinstance(model, RandomForestClassifier) # Should assert true
    


# Implements the third test. 
def test_model_metrics():
    """
    Tests if the model metrics populate as anticipated 
    """
    y_true = [1, 0, 0, 1, 1, 0, 1, 0] 
    y_preds = [1, 0, 0, 1, 1, 0, 1, 0] 
    precision, recall, fbeta = compute_model_metrics(y_true, y_preds)
    
    assert fbeta is not None
    assert recall is not None
    assert precision is not None
