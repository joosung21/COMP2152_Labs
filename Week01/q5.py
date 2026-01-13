# Common Functions: Ask the user to input their age, and then save that input into the variable “userAge”.
# For the user input, add 22.Then print the following sentence followed by the value of userAge. 
# “Now showing the shop items filtered by age: 22”. Do not hard code the number 22.

userAge = int(input("Please enter your age: "))
userAge += 22
print("Now showing the shop items filtered by age: {}".format(userAge))