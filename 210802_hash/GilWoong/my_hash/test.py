from my_hashtable import MyHashtable

ht = MyHashtable(10)

ht.put(0, '0번')
ht.put(1, '1번')
ht.put(10, '10번')
# ht.put('길웅key', '길웅value')
# ht.put(8, '바뀜')

ht.print_table()

print(ht.get(0))
print(ht.get(1))
print(ht.get(10))
# print(ht.get(2))
# print(ht.get(10))
# print(ht.get(14))
# print(ht.get('길웅key'))
# print(ht.get(1))