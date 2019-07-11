def calculate():
    string=(input("please enter an opration "))
    a=int(input("enter a number "))
    b=int(input("enter another number "))
    
    add = a+b
    subtruct = a-b
    multiply = a*b
    divide = a/b
    if string == "add":
        print("the answer is "+str(add))
    elif string == "subtruct":
        print("the answer is "+str(subtruct))
    elif string == "multiply":
         print("the answer is "+str(multipy))
    elif string == "divide":
        print("the answer is "+str(divide))
    else:
        print("please try again")
    

calculate()