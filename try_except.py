my_dict = {"a": 1, "b": 2, "c": 3}

try:
    value = my_dict["a"]
except KeyError:
    print("Thay key does not exist!")
else:
    print("Everything is working perfect!")
