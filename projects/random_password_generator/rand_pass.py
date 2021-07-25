import string
import random

if __name__ == '__main__':
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    # taking input for lemngth of the password
    plen=int(input("Enter the length of your password"))
    if(plen <= 0 or plen >100):
        print("Enter valid length for the password")
    else:
        # empty list to store all letters from which we will generate the password
        s=[]
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        # generating the password using random module
        random.shuffle(s)
        print("\nYour password using random.shuffle  ")
        print("".join(s[0:plen]))
        print("\nusing random.shuffle")
        print("".join(random.sample(s,plen)))