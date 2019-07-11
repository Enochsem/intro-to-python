def getage():
    age=int(input("How old are you ")) 
    return age 

def getname():
    name=str(input("What is your name ")) 
    return name

age = getage()
name = getname()
print("your name is "+( name) +' and you are '+str(age) +" old ")


