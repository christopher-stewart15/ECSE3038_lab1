def hello ():
    print("ECSE3038 - Engineering Iot Systems")


def validatePassword(passwd):
     alnum=0
     nums = 0

    if len(passwd) > 7 and password.isalnum():
        for val in psswd:
            try:
                if isinstance(int(val), int):
                    nums += 1
            except:
                pass
        
        if nums > 1:
            return True
    
    return False