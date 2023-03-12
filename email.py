# E-mail validation using String functions
email = input("Enter your E-mail : ")
k,j,m = 0,0,0 
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                       m = 1 
                if k == 1 or j == 1 or m == 1:
                    print("Wrong E-mail 5")
                else:
                    print("Right E-mail")
            else:
                print("Wrong E-mail 4")
        else:
            print("Wrong E-mail 3")
    else:
        print("Wrong E-mail 2")
else: 
    print("Wrong E-mail 1")

# E-mail Validation using RegEx
import re

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
# ^: startswith, ?: specified should be <=1, \w: search the string, {2,3}: indexing, $: endswith
user_email = input("Enter your E-mail : ")
 
if re.search(email_condition, user_email):
    print("Right E-mail")
else:
    print("Wrong E-mail")