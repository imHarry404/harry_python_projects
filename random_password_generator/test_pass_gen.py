import random
import string

if __name__ == '__main__':
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    plen=int(input("Enter the length of your passsowrd: "))
    if (plen<=0  or plen>100):
        print("Enter valid length for your password")
    else:
        s=[]
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        print("Your password type 1 is ")
        random.shuffle(s)        
        print("".join(s[0:plen]))
        print("Your password type 2 is ")
        print("".join(random.sample(s,plen)))
        

