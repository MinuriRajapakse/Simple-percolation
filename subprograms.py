import random

# Create a function
def createRandomNums():
    "This function will automatically create random numbers and spaces"
    probability_NO = 0.1
    if (random.random() < probability_NO):
        return " "
    else:
        return random.randint(10,99)


# Create a function
def createSubLists(random_values,no_of_sublists):
    "This function will create sublists"
    sub_lists=[]
    result=[]
    for i in random_values:
        sub_lists+=[i]
        if (len(sub_lists)==no_of_sublists):
            result+=[sub_lists]
            sub_lists=[]
    if sub_lists:
        result+=[sub_lists]
    return result
