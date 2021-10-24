import random



def flip_coin() : 
    if random.randint(0,1) == 1 : 
        return "H"  
    else :
        return "T"
    
def roll_dice() : 
    return random.randint(1,6)
    
def otp_pin() : 
   return "{:06}".format(random.randint(1, 999999))

def password_gen(length):
    s = ""
    for i in range(length):
        s = s + chr(random.randint(ord("A"), ord("Z"))) #ord() --> แปลงค่า string เป็น integer                                
    return s

def password_gen2(length):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-+"
    s = ""
    for i in range(length):
        s = s + random.choice(alpha)
    return s

def otp_password():
    hero_data = "0123456789"
    otp_str = ""
    for i in range(6):
        otp_str = otp_str + random.choice(hero_data)
    return otp_str
    

for i in range(10): 
    #print(flip_coin())
    #print(roll_dice(), end = " ")
    #print(otp_pin())
    print(otp_password())
    print(random.random())
    #print(password_gen2(10))
  
