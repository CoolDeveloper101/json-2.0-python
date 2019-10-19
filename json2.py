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
    b = {}
    for obj in data:
        o = data[obj]
        loaded_data = pickle.loads(bytes.fromhex(o))
        b[obj] = loaded_data
    return b


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'User({self.username})'


user = User("Ashwin", "testing321")
dumped_user = dumps({"user": user})
print(dumped_user)
loaded_user = loads(dumped_user)
print(loaded_user)
