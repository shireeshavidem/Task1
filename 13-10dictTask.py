# 1.Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

dictnry = {}
add_dict = {}
def update_dict(dictnry):
    for i in range(4):
       dictkeys = input("Enter your dictinary keys: ")
       dictvalues = input("Enter your dictionary values: ")
       dictnry[dictkeys] = dictvalues
    print(dictnry)
    K = input("Enter the key where you want to insert key: ")
    add_key = input("enter key: ")
    add_value = input("enter value: ")
    add_dict[add_key] = add_value
    new_dict = dict()
    for key in dictnry:
       new_dict[key] = dictnry[key]
       if key==K:
           new_dict.update(add_dict)
    print(new_dict)        
update_dict(dictnry)