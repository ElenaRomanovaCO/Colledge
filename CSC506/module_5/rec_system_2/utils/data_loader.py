import sqlite3
import pandas as pd

def load_data():
    conn = sqlite3.connect('db/social_media.db')

    users = pd.read_sql_query("SELECT * FROM users", conn)
    posts = pd.read_sql_query("SELECT * FROM posts", conn)
    interactions = pd.read_sql_query("SELECT * FROM interactions", conn)

    conn.close()

    return users, posts, interactions

if __name__ == '__main__':
    users, posts, interactions = load_data()
    print(users.head())
    print(posts.head())
    print(interactions.head())
