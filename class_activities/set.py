# s1 = {1, 2, 3, 4, 5, 6}
# s2 = {4, 5, 6, 7, 8, 9}
# (s1.add(7))
# print(s1)
# # s1.interesction
# print(s1 & s2)
# # s1.union
# print(s1 | s2)
# # s1.update
# s1 |= s2
# print(s1)
#
# # s1.intersection_update
# s1 &= s2
# print(s1)
#
# s1.pop()
# print(s1)
#
# # difference between the two set
# print(s1 - s2)
#
# # difference_update
# s1 -= s2
# print(s1)
#
#
# # symmetric_difference
# print(s1 ^ s2)
#
# # symmetric_difference_update
# s1 ^= s2
# print(s1)
#
# # superset
# print(s1 >= s2)
#
# # subset
# print(s1 <= s2)


dict_play = {"name": "Tolani", "age": 32, "influenced": "Samson"}
print(dict_play.get("named", "Samson"))
print(dict_play.get("name"))
print(dict_play.pop("name"))
print(dict_play)
print(dict_play.popitem())

dict_play.update({"name": "Ademola"})
print(dict_play)

def get_first(s:str) -> str:
    return  s[0]

l = [get_first(val) for val in ["hello", "how", "are", "you"]]
print(l)