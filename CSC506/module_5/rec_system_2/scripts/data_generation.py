import sqlite3
import random
import string
from faker import Faker

fake = Faker()


def generate_unique_string(length=8):
    """Generates a unique string of given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_data(user_num=100, post_num=50):
    users = []
    posts = []
    interactions = []

    for _ in range(user_num):
        user_id = generate_unique_string()
        users.append((user_id, fake.random_int(min=18, max=60), fake.city(), str(fake.words(nb=3))))

    for _ in range(post_num):
        post_id = generate_unique_string()
        posts.append((post_id, fake.sentence(), fake.text(), fake.word()))

    for user in users:
        for post in posts:
            like = random.choice([True, False])
            shared = random.choice([True, False])
            hashtag = fake.word()
            interactions.append((user[0], post[0], 'like' if like else 'none', shared, hashtag))

    return users, posts, interactions


def seed_dynamic_data(user_num=100, post_num=50):
    users, posts, interactions = generate_data(user_num, post_num)

    conn = sqlite3.connect('db/social_media.db')
    cursor = conn.cursor()

    cursor.executemany('INSERT INTO users (user_id, age, location, interests) VALUES (?, ?, ?, ?)', users)
    cursor.executemany('INSERT INTO posts (post_id, title, content, category) VALUES (?, ?, ?, ?)', posts)
    cursor.executemany('''
        INSERT INTO interactions (user_id, post_id, interaction_type, shared, hashtag) 
        VALUES (?, ?, ?, ?, ?)
    ''', [(u_id, p_id, 'like' if like else 'none', shared, hashtag) for u_id, p_id, like, shared, hashtag in
          interactions])

    conn.commit()
    conn.close()


if __name__ == '__main__':
    seed_dynamic_data(user_num=100, post_num=50)
