dict = {"Name":"Pushpa",
        "age":28,
        "sub":{"english":87,
               "Math":88,
               "physics":56}}
# print(dict.keys())
# print(list(dict.keys()))
# print(len(dict))
# print(dict.values())
# print(list(dict.values()))
pairs = list(dict.items())   # return the values as a tuple
print(pairs)
print(dict["Name"])
print(dict.get("Name")) #isse error nhi aata
dict.update({"city": "nagpur"}) 
print(dict)