import pickle

# TODO Change path accordingly
path = "./suggestion_list_hitlist.pkl"
with open(path, 'rb') as file:
    print(pickle.load(file))
