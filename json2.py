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


# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def __repr__(self):
#         return f'User({self.username})'


# user = User("User", "testing321")
# dumped_user = dumps({"user": user})
# print(dumped_user)
# loaded_user = loads(dumped_user)
# print(loaded_user)
