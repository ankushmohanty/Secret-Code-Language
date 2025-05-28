"""
Secret Code Language
This code is help you to code and decode your secret messages from your friends and families

"""
import os
import time
import random

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
         '1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*'
        ]


def random_aplha():
    random_char = []
    for i in range(3):
        random_char.append(alpha[random.randint(0,68)])
    
    return "".join(random_char)

def Coding(line):
    words = line.split(' ')
    new_words = []
    for word in words:
        if len(word)>=3:
            stnew = random_aplha() + word[1:]+ word[0] + random_aplha()
            new_words.append(stnew)
        else:
            new_words.append(word[::-1])
            
    print(" ".join(new_words)+ "\n")
    time.sleep(5)
    
    
    
def Decoding(line):
    words = line.split(' ')
    new_words = []
    for word in words:
        if len(word) < 3:
            new_words.append(word[::-1])
        else:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            new_words.append(stnew)
            pass
        
    print(" ".join(new_words)+ "\n")
    time.sleep(5)


os.system('cls')   
option = 1
while(option<3):
    option= int(input("1)Coding\n2)Decoding\n3)Exit\n"))
    time.sleep(1.5)
    os.system('cls')
    
    if option == 1:
        message = input("Enter your Message to Code:\n")
        time.sleep(1.5)
        os.system('cls')
        Coding(message)
    elif option == 2:
        message = input("Enter the Coded message to Decode:\n")
        time.sleep(1.5)
        os.system('cls')
        Decoding(message)
