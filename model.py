# Import necessary libraries
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Define hyperparameters
input_size = 82  
hidden_size = 128
num_layers = 2
dropout = 0.2
num_epochs = 70
learning_rate = 0.001
batch_size = 32

# Custom Dataset class for loading data from CSVs
class BettingDataset(Dataset):
    def __init__(self, input_csv, output_csv):
        # Load the CSV file
        input_data = pd.read_csv(input_csv)
        
        # Separate categorical and numerical columns
        categorical_columns = input_data.select_dtypes(include=['object']).columns
        numerical_columns = input_data.select_dtypes(exclude=['object']).columns

        # Create a column transformer that handles both numerical and categorical data
        self.column_transformer = ColumnTransformer(
            transformers=[
                ('num', 'passthrough', numerical_columns),
                ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)
            ]
        )

        # Apply the transformations and convert the data to numpy arrays
        # Convert the sparse matrix to a dense matrix using .toarray()
        self.feature_data = self.column_transformer.fit_transform(input_data).toarray().astype(np.float32)
        self.target_data = pd.read_csv(output_csv).apply(pd.to_numeric, errors='coerce').fillna(0).values.astype(np.float32)

    def __len__(self):
        return len(self.feature_data)

    def __getitem__(self, idx):
        features = self.feature_data[idx]
        target = self.target_data[idx]
        return torch.tensor(features, dtype=torch.float32), torch.tensor(target, dtype=torch.float32)

# Load dataset
input_csv = '/Users/rishabh/Betting-Line-Comparison/input.csv'
output_csv = '/Users/rishabh/Betting-Line-Comparison/output.csv'
dataset = BettingDataset(input_csv, output_csv)

# Split the dataset into train and validation sets
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])

# Create data loaders
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# Define the model
class BettingModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, dropout):
        super(BettingModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, dropout=dropout, batch_first=True)
        self.fc = nn.Linear(hidden_size, 2)

    def forward(self, x):
        h0 = torch.zeros(num_layers, x.size(0), hidden_size).to(x.device)
        c0 = torch.zeros(num_layers, x.size(0), hidden_size).to(x.device)
        out, _ = self.lstm(x, (h0, c0))
        out = out[:, -1, :]
        out = self.fc(out)
        return out

# Instantiate the model
model = BettingModel(input_size, hidden_size, num_layers, dropout)

# Define the Loss and Optimizer functions
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Training loop
for epoch in range(num_epochs):
    model.train()
    for features, target in train_loader:
        optimizer.zero_grad()
        features = features.unsqueeze(1)
        output = model(features)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

    model.eval()
    val_loss = 0
    with torch.no_grad():
        for features, target in val_loader:
            features = features.unsqueeze(1) 
            output = model(features)
            loss = criterion(output, target)
            val_loss += loss.item()

    val_loss /= len(val_loader)
    print(f'Epoch {epoch+1}/{num_epochs}, Validation Loss: {val_loss:.4f}')
    
torch.save(model.state_dict(), 'sports_betting_model.pth')
