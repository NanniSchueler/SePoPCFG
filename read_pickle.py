import pickle
import sys

# TODO Change path accordingly or change to parameter version
# path = sys.argv[1]
path = "./suggestion_list_hitlist.pkl"
with open(path, 'rb') as file:
    print(pickle.load(file))
