

# day 4
# day 5
# Data Structure
# Dictionary Exercise

def list_dictionary():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    x = zip(keys, values)
    return dict(x)
# print(list_dictionary())

# return history
def history_channel():
    sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
                }
            }
        }
    }
    return sampleDict["class"]["student"]["marks"]["history"]
# print(history_channel())

def hero():
    super_hero = dict(name="Person A", hero_name="Super Person A", power="AAA power", origin="AAA")
    return super_hero
# print(hero())


def init_dictionary():
    employees = ['Kelly', 'Emma']
    defaults = {"designation": 'Developer', "salary": 8000}
    res = dict.fromkeys(employees,defaults)
    return res
# print(init_dictionary())


def extract_dictionary():
    sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

    # Keys to extract
    keys = ["name", "salary"]
    okey = {keys[0]:sample_dict[keys[0]], keys[1]:sample_dict[keys[1]]}
    return okey
# print(extract_dictionary())


def delete_dictionary():
    sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

    # Keys to extract
    keys = ["name", "salary"]
    sample_dict = {i: sample_dict[i] for i in sample_dict.keys() - keys}
    return sample_dict
# print(delete_dictionary())


def value_exists():
    sample_dict = {'a': 100, 'b': 200, 'c': 300}
    flag = False
    for i in sample_dict.values():
        if i==200:
            flag = True
    return flag
# print(value_exists())

def rename_key():
    sample_dict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New york"
    }
    sample_dict.pop("city")
    sample_dict["location"] = "Russia"
    return sample_dict
# print(rename_key())

def minimum_value():
    sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
    }
    a = list(sample_dict.values())
    return min(a)
# print(minimum_value())

def change_key_nested_dictionary():
    sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
    }
    sample_dict["emp3"].update({"salary":8500})
    return sample_dict
# print(change_key_nested_dictionary())