#1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res_dict = dict(zip(keys, values))
print(res_dict)

#2
keys = ['Ten', 'Twenty', 'Thirty']

values = [10, 20, 30]

res_dict = dict()

for i in range(len(keys)):

  res_dict.update({keys[i]: values[i]})

print(res_dict)

#3
keys = ['Ten', 'Twenty', 'Thirty']

values = [10, 20, 30]

res_dict = dict()

for i in range(len(keys)):

  res_dict.update({keys[i]: values[i]})

print(res_dict)

#3
sample_dict = {
"name": "Kelly",
"age": 25,
"salary": 8000,
"city": "New york"}
keys = ["name", "salary"]
new = dict()
for k in keys:
  new.update({k: sample_dict[k]})
print(new)

#4
sample_dict = {
'Physics': 82,
'Math': 65,
'history': 75
}
print(min(sample_dict, key=sample_dict.get))

#5
sample_dict = {
'emp1': {'name': 'Jhon', 'salary': 7500},
'emp2': {'name': 'Emma', 'salary': 8000},
'emp3': {'name': 'Brad', 'salary': 6500}
}
sample_dict['emp3']['salary'] = 8500
print(sample_dict)