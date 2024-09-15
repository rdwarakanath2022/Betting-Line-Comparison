import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import torch
import numpy as np
from model import BettingModel

input_size = 82  
hidden_size = 128
num_layers = 2
dropout = 0.2
num_epochs = 200
learning_rate = 0.001
batch_size = 32

# Load the training data
input_data_train = pd.read_csv('input.csv')
output_data_train = pd.read_csv('output.csv')  # This might be used for supervised learning

print("Columns in input.csv:", input_data_train.columns)
print("Columns in output.csv:", output_data_train.columns)

# Define the ColumnTransformer based on the columns in your input.csv
column_transformer = ColumnTransformer(
    transformers=[
        ('team1', OneHotEncoder(sparse_output=False), ['team1']),
        ('team2', OneHotEncoder(sparse_output=False), ['team2']),
        # Add other transformers if needed
    ],
    remainder='passthrough'
)

# Fit the ColumnTransformer with the training input data
column_transformer.fit(input_data_train)

# Load the trained model
model = BettingModel(input_size, hidden_size, num_layers, dropout)
model.load_state_dict(torch.load('sports_betting_model.pth'))
model.eval()

# Prepare new input data
input_data_new = pd.DataFrame({
    'team1': ['Detroit Lions'],
    'team2': ['Minnesota Vikings'],
    'feature_1': [1],
    'feature_2': [1],
    'feature_3': [24.0],
    'feature_4': [10.0],
    'feature_5': [20.0],
    'feature_6': [21.8],
    'feature_7': [38.0],
    'feature_8': [24.0],
    'feature_9': [10.0],
    'feature_10': [38.0],
    'feature_11': [21.5],
    'feature_12': [20.0],
    'feature_13': [24.0],
    'feature_14': [38.0],
    'feature_15': [22.7],
    'feature_16': [20.0],
    'feature_17': [21.8],
    'feature_18': [10.0]
})










# Apply the same transformations as during training
prepared_data = column_transformer.transform(input_data_new).astype(np.float32)

# Convert to tensor
input_tensor = torch.tensor(prepared_data, dtype=torch.float32).unsqueeze(0)  # Add batch dimension

# Make prediction
with torch.no_grad():
    prediction = model(input_tensor)

# Convert to numpy array
prediction_np = prediction.numpy()
print(prediction_np)
