import random
length = input("Enter the length for your password")
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers ="0123456789"
string = lower + upper + numbers
password="".join(random.sample(string, int(length)))
print("password - "+ password)