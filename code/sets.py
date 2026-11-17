# sets are collection of unordered item & all the item are unique and immutable (set mutable hota he pr iske elements immutable hote he)
# we can store int ,str, float,tuple, boolean in it be. list and dictionary ko isme store nahi kara sakte.


# s = set()
# print(s)
# print(type(s))


# methods of sets(set.add,remove,clear,pop, union,intersection)
s1 = {1,4,2,4,3,5,5,5,"world","world"} # duplicate value ko ignore karta he or inko sorted krk return karega
s2 = {3,2,5,7,6,12,23}
# method performs
s1.add(6)
s1.add((4,5,6,8,9))
s1.remove(4)
s1.pop()
#print(s.clear())
print(s1.union(s2))
print(s1.intersection(s2))

print(s1)
print(type(s1))
print(len(s1))