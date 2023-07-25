v1 = "first string"
v2 = "second string"

# we need to swap the values so that the value of v1 will become second string and v2 will become first string
# for that we need to take temp variables to store the value, if not the values of v1 and v2 will become same. In this way we no need to change the values everytime

# to execute first method, uncomment from line 8 - 14
# temp1 = v1  # we are assiging the value of v1 to temp1
# temp2 = v2  # we are assiging the value of v2 to temp2
# v1 = v2     # the v1 value will be second string
# v2 = temp1  # the v2 value will be first string

# print(v1)  # o/p - second string
# print(v2)  # o/p - first string

# we have 2 ways to solve this. First is by taking 2 temp variables. Second is to take only one temp variable

# second method - to execute first method, please uncomment from line 19 - 24
temp = v1  # we are assiging the value of v1 to temp
v1 = v2  # now the v1 value is equal to v2
v2 = temp # since the value is stored in temp, we are taking the value of v1 so that, it will print first string

print(v1)  # o/p - second string
print(v2)  # o/p - first string