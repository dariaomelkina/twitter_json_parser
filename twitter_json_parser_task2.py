import json


def read_file(path):
    """
    () -> dict
    Return data from json file.
    """
    with open(path) as file:
        data1 = file.read()
    data = json.loads(data1, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None,
                      parse_constant=None,
                      object_pairs_hook=None)
    return data


def check(data, key):
    """
    (dict) -> dict/list/str/int/float
    Searches for the given key in data and returns it's value.
    >>> check({'1': 1, '2': 'b'}, '2')
    'b'
    """
    if key in data.keys():
        return data[key]


def func_for_dict(x):
    """
    (dict) -> dict/tuple/list/str/int/float
    Return requested value of the dictionary, or itself.
    """
    question = input('Your answer is a dictionary, do you want to access a certain key?(Y/N) ')
    if question == 'Y':
        available_keys1 = list(x.keys())
        print('Available keys:', available_keys1)
        key = input('Which key are you interested in? ')
        x = check(x, key)
        return x
    else:
        return x, 0


def func_for_lst(x):
    """
    (list) -> dict/tuple/list/str/int/float
    Return requested value of the list, or itself.
    """
    length = len(x)
    print('Your answer contains dictionaries, its length = ', length)
    question = input('Do you want to access a certain elemet in the list?(Y/N) ')
    if question == 'Y':
        ind = int(input('Which element do you want?(number) ')) - 1
        x = x[ind]
        available_keys1 = list(x.keys())
        print('Available keys:', available_keys1)
        key = input('Which key are you interested in? ')
        x = check(x, key)
        return x
    else:
        return x, 0


def func_for_dict_in_dict(x):
    """
    (dict) -> dict/tuple/list/str/int/float
    Return requested dictionary from the dictionary, requested value or itself.
    """
    lst = []
    num = 0
    for i in list(x.values()):
        if type(i) == dict:
            lst.append(list(x.keys())[list(x.values()).index(i)])
            num += 1
    print('Your answer contains dictionaries, number of dictionaries = ', num)
    question1 = input('Do you want to access a certain dictionary?(Y/N) ')
    if question1 == 'Y':
        print("These are keys for other dictionaries: ", lst)
        el = input('Which dictionary do you want?(key for access) ')
        x = x[el]
        return x
    else:
        while type(x) == dict:
            x = func_for_dict(x)
        return x


if __name__ == "__main__":
    try:
        print("This program parses json file with information about account's friends, got with Twitter API.")
        given_path = input("Please, enter the path to json file: ")
        given_data = read_file(given_path)
        available_keys = list(given_data.keys())
        print('Available keys:', available_keys)
        given_key = input('Which key are you interested in? ')
        answer = check(given_data, given_key)
        while (type(answer) != tuple) and (("<class 'dict'>" in list(map(lambda x: str(type(x)), answer))) or
                                           ((type(answer) == dict) and
                                            ("<class 'dict'>" in list(map(lambda x: str(type(x)), answer.values())))) or
                                           (type(answer) == dict)):
            while (type(answer) != tuple) and (type(answer) != dict) and \
                    "<class 'dict'>" in list(map(lambda x: str(type(x)), answer)):
                answer = func_for_lst(answer)
            while (type(answer) != tuple) and (type(answer) != list) and \
                    "<class 'dict'>" in list(map(lambda x: str(type(x)), answer.values())):
                answer = func_for_dict_in_dict(answer)
            while (type(answer) != tuple) and (type(answer) != list) and \
                  (type(answer) == dict) and "<class 'dict'>" not in list(map(lambda x: str(type(x)), answer.values())):
                answer = func_for_dict(answer)
        print('Here is your answer: ', answer)
    except:
        print('Please, your input should follow the rules of the program.')
