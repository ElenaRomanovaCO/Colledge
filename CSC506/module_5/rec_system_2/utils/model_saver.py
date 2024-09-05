import pickle

def save_model(model, filename):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)
