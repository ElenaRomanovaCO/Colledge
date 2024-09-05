import sys
import os
import random
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pickle
import numpy as np
import pandas as pd
from utils.data_loader import load_data


def recommend(user_id, num_recommendations=5):
    start_time = time.time()

    users, posts, interactions = load_data()
    load_time = time.time()
    print(f"Data loading time: {load_time - start_time:.2f} seconds")

    interaction_matrix = interactions.pivot_table(index='user_id', columns='post_id', values='interaction_type',
                                                  aggfunc='count', fill_value=0)
    pivot_time = time.time()
    print(f"Pivot table creation time: {pivot_time - load_time:.2f} seconds")

    # Print available user IDs
    available_user_ids = interaction_matrix.index.tolist()
    print("Available user IDs:", available_user_ids)

    # Check if the user_id exists in the interaction_matrix index
    if user_id not in interaction_matrix.index:
        raise ValueError(f"User ID '{user_id}' not found in the interaction matrix.")

    # Load the trained model
    model_load_start = time.time()
    with open('models/recommendation_model.pkl', 'rb') as file:
        nmf = pickle.load(file)
    model_load_time = time.time()
    print(f"Model loading time: {model_load_time - model_load_start:.2f} seconds")

    # Get user matrix
    user_matrix = nmf.transform(interaction_matrix)
    transform_time = time.time()
    print(f"User matrix transformation time: {transform_time - model_load_time:.2f} seconds")

    # Get predictions for the given user
    user_index = interaction_matrix.index.get_loc(user_id)
    user_preds = np.dot(user_matrix[user_index], nmf.components_)
    prediction_time = time.time()
    print(f"Prediction time: {prediction_time - transform_time:.2f} seconds")

    # Sort and get top recommendations
    post_indices = np.argsort(user_preds)[::-1][:num_recommendations]
    recommended_posts = interaction_matrix.columns[post_indices]
    sorting_time = time.time()
    print(f"Sorting and recommendation time: {sorting_time - prediction_time:.2f} seconds")

    recommendations = posts[posts['post_id'].isin(recommended_posts)]
    end_time = time.time()
    print(f"Total recommendation time: {end_time - start_time:.2f} seconds")

    return recommendations


if __name__ == '__main__':
    overall_start_time = time.time()

    # Load data to get available user IDs
    users, posts, interactions = load_data()
    available_user_ids = interactions['user_id'].unique()

    # Option 1: Choose a random user_id
    random_user_id = random.choice(available_user_ids)
    print(f"Randomly selected user ID: {random_user_id}")

    # Option 2: Choose a specific user_id by index (e.g., first user)
    specific_user_id = available_user_ids[0]  # You can modify the index here
    print(f"User ID selected by specific index: {specific_user_id}")

    # Choose which option to use for `user_id`
    selected_user_id = random_user_id  # Use either `random_user_id` or `specific_user_id`

    try:
        recommendations = recommend(user_id=selected_user_id, num_recommendations=5)
        print(f"Recommendations for user {selected_user_id}:")
        print(recommendations)
    except ValueError as e:
        print(e)

    overall_end_time = time.time()
    print(f"Total execution time: {overall_end_time - overall_start_time:.2f} seconds")