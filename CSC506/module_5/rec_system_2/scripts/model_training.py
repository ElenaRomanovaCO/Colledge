import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.decomposition import NMF
import numpy as np
from utils.data_loader import load_data
from utils.model_saver import save_model

def train_model():
    users, posts, interactions = load_data()

    # Create a user-item interaction matrix
    interaction_matrix = interactions.pivot_table(index='user_id', columns='post_id', values='interaction_type', aggfunc='count', fill_value=0)

    # Split data into training and testing sets
    train_data, test_data = train_test_split(interaction_matrix, test_size=0.2, random_state=42)

    # Apply NMF for collaborative filtering
    nmf = NMF(n_components=2, random_state=42)
    user_matrix = nmf.fit_transform(train_data)
    item_matrix = nmf.components_

    # Save the trained model
    save_model(nmf, 'models/recommendation_model.pkl')
    print(f"{nmf=}")

    # Calculate reconstruction error
    train_preds = np.dot(user_matrix, item_matrix)
    mse = mean_squared_error(train_data.values, train_preds)
    print(f'Model Training Completed. MSE: {mse}')

if __name__ == '__main__':
    train_model()
