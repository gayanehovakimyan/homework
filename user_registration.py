def decorator(func):
    def wrapper(*args,**kwargs):
        user_name=func()
        if len(user_name)<5 or len(user_name)>20:
            print("Username should be between 5 and 20 characters long. ") 
            return
        for i in user_name:
            if not i.isalnum():
                print("Username should contain only alphanumeric characters. ")
                return
        res_name=['root','admin']
        if user_name in res_name:
            print("Username cann't be reserved word like: root, admin .")
            return
        return user_name
    return wrapper

@decorator
def name_val():
    return input("Enter a username:")
try:
    result = name_val()
except ValueError as e:
    print(e)
else:
    print(result)

    
    
    
def decorator2(func):
    def wrapper(*args,**kwargs):
        email_val=func()
        if '@' in email_val and '.' in email_val:
            shnikic_araj,shnikic_heto=email_val.split('@')
            ketic_araj,ketic_heto=shnikic_heto.split('.')
            if len(shnikic_araj)>0 and  len(ketic_araj)>0 and len(ketic_heto)>=2:
                return True
            else:
                print("Error.")
            return False
        else:
            print("Invalid email validation: ")
            return False
        
    return wrapper

@decorator2
def email():
    return input("Enter your email:")
try:
    result=email()
except ValueError as e:
    print(e)
else:
    print(result)

    
def decorator3(func):
    def wrapper(*args,**kwargs):
        phone_num=func()

        if phone_num[0] != '+':
            print("Phone number should start with '+': ")
            return
        for i in phone_num[1::]:
            if not i.isdigit():
                print("Phone number should contain only digit.")
                return 
        return phone_num
    return wrapper

@decorator3
def phone():
    return input("Enter your phone number:")
try:
    result = phone()
except ValueError as e:
    print(e)
else:
    print(result)






def decorator4(func):
    def wrapper(*args,**kwargs):
        psw=func()
        if len(psw)<8:
            print("Password should be at least 8 characters long:")
            return
        if not any(i.isupper() for i in psw):
            print("Will contain at least 1 uppercase letter.")
            return
        if not any(j.lower() for j in psw):
            print("Will contain at least 1 lowercase letter.")
            return
        if not any(char.isdigit() for char in psw):
            print("Will contain at least 1 digit.")
            return
        special_char='!@#$%^&*'
        if not any(char in special_char for char in psw):
            print("Wil contain one of the speciaal characters '@#$%^&*' :")
            return
        return psw
    return wrapper 
@decorator4
def pasww():
    return input("Enter your password:")
try:
    result=pasww()
except ValueError as ax:
    print(ax)
else:
    print(result)

    


def decorator5(func):
    def wrapper(*args,**kwargs):
        rep=func()
        repeat=input("Repeat your password again:")
        if rep != repeat:
            print('Wrong repetition.')
            return
        return rep
    return wrapper
    
@decorator5
def repetition():
    return input("Please repeat your password:")
try:
    result=repetition()
except ValueError as k:
    print(k)
else:
    print(result)


