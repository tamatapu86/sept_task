# # dictionary_1 = {} 
# # print(type(dictionary_1))

# # dictionary_2 = {1:"rajesh",2:"ravi",3:"jahanavi"}
# # print(dictionary_2)
# # print(type(dictionary_2))

# # dictionary_3 = dict()
# # print(dictionary_3)
# # print(type(dictionary_3))

# # dictionary_1 = {
# #     "user1" : "user1@123",
# #     "user2" : "user2@123",
# #     "user3" : "user3@123",
# #     "user4" : "user4@123",
# #     1: "rajukumar",
# #     (1,2) : 123456,
# #     2: [1,2,3,4],
# #     3:{1:1234},
# # }
# # print(dictionary_1)



# #methods
# #clear method

# # dictionary_1 = {
# #     "user1" : "user1@123",
# #     "user2" : "user2@123",
# #     "user3" : "user3@123",
# #     "user4" : "user4@123",
# # }
# # dictionary_1.clear()
# # print(dictionary_1)

# # copy method
# # dictionary_1 = {
# #     "user1" : "user1@123",
# #     "user2" : "user2@123",
# #     "user3" : "user3@123",
# #     "user4" : "user4@123",
# # }
# # sample = dictionary_1.copy()
# # print(sample)
# # sample.clear()
# # print(sample)
# # print(dictionary_1)

# # items method
# # dictionary_1 = {
# #     "user1" : "user1@123",
# #     "user2" : "user2@123",
# #     "user3" : "user3@123",
# #     "user4" : "user4@123",
# # }
# # print(dictionary_1.items())
# # print(dictionary_1.values())

# #get method

# # dictionary_1 = {
# #     "user1" : "user1@123",
# #     "user2" : "user2@123",
# #     "user3" : "user3@123",
# #     "user4" : "user4@123",
# # }
# # print(dictionary_1.get("user1"))
# # print(dictionary_1["user1"])

# # dictionary_1 = {
# #     "user1" : "user1@123",
# #     "user2" : "user2@123",
# #     "user3" : "user3@123",
# #     "user4" : "user4@123",
# # }
# # print(dictionary_1.get("user5"))

# # dictionary_1 = {
# #     "user1" : "user1@123",
# #     "user2" : "user2@123",
# #     "user3" : "user3@123",
# #     "user4" : "user4@123",
# # }
# # dictionary_1.pop("user3")
# # print(dictionary_1)


# #=============update() method

# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }

# sample = { 
#     "user5" : "user5@123",
#     "user6" : "user6@123",
#     "user7" : "user7@123",
#     "user8" : "user8@123",

# }
# dictionary_1.update(sample)
# print(dictionary_1)

# Exercise 1:
# Dictionary Update
""" Write a Python script that updates a dictionary with a new key-value pair. """



# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# dictionary_1.update({"user4":"rajesh"})
# print(dictionary_1)

# Exercise 2: Dictionary Access
""" Write a Python script that accesses and prints the value associated with a specific
key in a dictionary. """

# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }

# print(dictionary_1.get("user4"))
# print(dictionary_1["user4"])

# Exercise 3: Dictionary Removal
""" Write a Python script that removes a key-value pair from a dictionary. """

# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }

# dictionary_1.pop("user3")
# print(dictionary_1)

# Exercise 4: Dictionary Keys
""" Write a Python script that prints all the keys present in a dictionary.  """
dictionary_1 = {
    "user1" : "user1@123",
    "user2" : "user2@123",
    "user3" : "user3@123",
    "user4" : "user4@123",
}
print(dictionary_1.keys())
print(dictionary_1.values())