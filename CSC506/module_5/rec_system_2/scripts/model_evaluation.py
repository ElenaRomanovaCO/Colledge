import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pickle
import numpy as np
import pandas as pd
from utils.data_loader import load_data

def recommend(user_id, num_recommendations=5):
    users, posts, interactions = load_data()
    interaction_matrix = interactions.pivot_table(index='user_id', columns='post_id', values='interaction_type', aggfunc='count', fill_value=0)

    # Check if the user_id exists in the interaction_matrix index
    if user_id not in interaction_matrix.index:
        raise ValueError(f"User ID '{user_id}' not found in the interaction matrix.")

    # Load the trained model
    with open('models/recommendation_model.pkl', 'rb') as file:
        nmf = pickle.load(file)

    # Get user matrix
    user_matrix = nmf.transform(interaction_matrix)

    # Get predictions for the given user
    user_index = interaction_matrix.index.get_loc(user_id)
    user_preds = np.dot(user_matrix[user_index], nmf.components_)

    # Sort and get top recommendations
    post_indices = np.argsort(user_preds)[::-1][:num_recommendations]
    recommended_posts = interaction_matrix.columns[post_indices]

    return posts[posts['post_id'].isin(recommended_posts)]

if __name__ == '__main__':
    try:
        recommendations = recommend(user_id='some_user_id', num_recommendations=5)
        print(recommendations)
    except ValueError as e:
        print(e)
