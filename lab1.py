def hello ():
    print("ECSE3038 - Engineering Iot Systems")

def validatePassword(passwd):
     alnum=0
     nums = 0

    if len(passwd) > 7 and password.isalnum():
        for dig in psswd:
            try:
                if isinstance(int(dig), int):
                    nums += 1
            except:
                pass
        
        if nums > 1:
            return True
    
    return False
def sumUpToN(num):
    dig = 0

    if num > 1:
        for i in range(1, num+1):
            dig += i
    else:
        dig = -1

    return dig 
