import json
import pickle


def dumps(dictionary):
    pickled_dict = {}
    for obj in dictionary:
        pickled_obj = pickle.dumps(dictionary[obj]).hex()
        pickled_dict[obj] = pickled_obj
    return json.dumps(pickled_dict)


def loads(s):
    data = json.loads(s)
    result = {}
    for obj in data:
        hexed_obj = data[obj]
        loaded_data = pickle.loads(bytes.fromhex(hexed_obj))
        result[obj] = loaded_data
    return result
