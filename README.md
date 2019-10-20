# json-2.0-python
This is a wrapper around the *json* module, which uses *pickle* to store a wide variety of objects.

Json is a nice format, but it does not let you store a custom data type.
This module lets you store custom objects, which can be used in a wide variety of tasks.
For example, you cannot store a numpy array using json but using this module, you can.
Currently, it can only pickle dictionaries.
Here is an example on how to use this module.

```python
class User:

  def __init__(self, username, password, email):
    self.username = username
    self.password = password
    self.email = email
  
  def __repr__(self):
    return f'User({self.username})'
    
    
test_user = User("testing", 1234, 'testing@email.com')

# Let's say I want to store this test_user. So we can do:

import json2

dumped_data = json2.dumps({'User': test_user})

# if you want to load the dumped_data, you can use the loads method

json2.loads(dumped_data)

```
