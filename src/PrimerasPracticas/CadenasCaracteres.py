'''
Created on 11 jun. 2019

@author: pietrodeocre
'''

if __name__ == '__main__':
    
    email = "elemail@hot@mail.com"
    
    if(email.count("@") == 1 and email.find('@', 0, len(email)) == email.rfind('@', 0, len(email))):
        print("El email es correcto")
    else:
        print("El email no es correcto")

    print(email.find("@", 0, len(email)))
    print(email.rfind("@", 0, len(email)))
    
    pass
