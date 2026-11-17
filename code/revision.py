# a= int(input("a: "))
# b= int(input("b: "))
# avg = (a+b)/2
# print(avg)
# movies = []
# movies.append(input("enter mov1: "))
# movies.append(input("enter mov2: "))
# movies.append(input("enter mov3: "))
# print(movies)

my_dict = {
    'name': 'pushpa',
    'sub':{'python':89,
        'c++':70,
        "c":67},
    'age' : 26,
    's': 'bairan'
}
# print(my_dict['name'])
# null_dict ={}
# print(my_dict['s'])
# my_dict['name'] = "My handsome man"
# my_dict['surname'] = 'i love you'
# print(my_dict['name'])
# print(my_dict['surname'])
# print(null_dict)
# print(my_dict['sub'])
# print(my_dict['sub']['python'])
# print(my_dict.keys())
# print(list(my_dict.keys()))
# print(type(my_dict))
# print(len(my_dict))
print(my_dict.items())
print(my_dict.pop('s'))