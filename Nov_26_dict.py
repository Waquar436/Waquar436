stud_info = {"name":"Amit",
            "age":10,
            "address":{
                "home address":"patna",
                "office address":"delhi"
            }}
print(stud_info["address"]["office address"])
print(stud_info["address"]["home address"])


#Dict from two list
keys = ["name","role","experience"]
values = ["Aman","SDET",6]
my_dict = dict(zip(keys,values))
print(my_dict)


#merge dict
dict1 = {"a":1,"b":2}
dict2 = {"c":3,"d":4}
print(dict1 | dict2)

#freq of char in a string
#input automation
#output "a":2,"u":1,"t":2,"o":2,"m":1,"i":1,"n:1

# user_inp = input("enter the value e.g automation")
# char_count = {}
# for char in user_inp:
#     char_count[char] = char_count.get(char,0)+1
# print(char_count)

#missing keys
dict1 = {"a":1,"b":2,"c":3}
dict2 = {"a":1,"b":2}
missing_key = set(dict1.keys() - dict2.keys())
print(missing_key)

#sort dict by values in desc order
my_dict = {"a":3,"b":1,"c":2}
print(my_dict.values())
print(max(my_dict.values()))
print(min(my_dict.values()))

#remove duplicate values from dict
#input my_dict1 = {"a":1,"b":2,"c":1,"d":3}
#ouput  {"a":1,"b":2,"d":3}

my_dict1 = {"a":1,"b":2,"c":1,"d":3}
unique_value = set()
result = {}
for key, value in my_dict1.items():
    if value not in unique_value:
        result[key] = value
        unique_value.add(value)
print(result)


#to check if two dict(say dict1, dict2)s r same
print(dict1 == dict2)

mylist = [1,2,2,3,4,5,5,6,7,8,8]
print(set(mylist))
