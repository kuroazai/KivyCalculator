# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:02:49 2019

@author: KuroAzai
"""
import Calculator


def LessThanSix(calc,ops):
    print(calc[1])
    if calc[1] == ops[0]:
        result = Calculator.Addition(calc[0],calc[2])
        print("Add" , result)
    elif calc[1] == ops[1]:
        result = Calculator.Subtraction(calc[0],calc[2])
        print("Sub" , result )
    elif calc[1] == ops[2]:
        result = Calculator.Multiplication(calc[0],calc[2])
        print("Mult" , result)
    elif calc[1] == ops[3]:
        result = Calculator.Division(calc[0],calc[2])
        print("Div" , result)
    else:
        print("404 Jutsu Not found nani ")
    return result
    

def GreaterThanSix(calc):
    pass

def calculate(calc):
    
    ops = ['+','-','*','/']
        
    # Using 0.429/ 0.43 we can find the number of operators that are within our list
    print("Number of operators" , round(len(calc) * 0.43)) 
    size = round(len(calc) * 0.43)
    print(size)
    
    #Step 1 
    
    '''
    Setting a variable that we will iterate over our Operators in our list.
    our operators will always be even numbers and our numbers will be odd numbers.
    so will be incremented by + 2 but for the initial operator is at index 1(2 - 1).
    ''' 
    n = 3
    #Initialise a vairable to store our result 
    result = 0 
    step = 0
    #Parameters for our Numbers 
    '''
    Our numbers will be on odd numbers(1,3,5...) . 
    our intial step will calculate the first 2 values then add the next value.
    calc = [5,'*',10, '+', 15, '+' ,20, '+', 25]
    With the above example after step one the 5th element will be added.
    so our Y variable will be 5 - 1 = 4 . Then we will the increment to increase it by +2
    '''
    y = 4
    print(len(calc))
    if len(calc) < 5 :
        print("less than")
        return LessThanSix(calc,ops)      
        
    #return "potato"
    while size > 0: 
        print("\nStep", step)
        #STEP 1 conditions 
        if step == 0 :
            if calc[1] == ops[0]:
                result = Calculator.Addition(calc[0],calc[2])
                print("Add" , result, calc[y])
            elif calc[1] == ops[1]:
                result = Calculator.Subtraction(calc[0],calc[2])
                print("Sub" , result )
            elif calc[1] == ops[2]:
                result = Calculator.Multiplication(calc[0],calc[2])
                print("Mult" , result)
            elif calc[1] == ops[3]:
                result = Calculator.Division(calc[0],calc[2])
                print("Div" , result)
            else:
                print("404 Jutsu Not found nani ", calc[n])

        else:
            if  calc[n] == ops[0]:
                result = Calculator.Addition(result,calc[y])
                print("Add", result , calc[y])               
            elif calc[n] == ops[1] :
                result = Calculator.Subtraction(result,calc[y])
                print("Sub", result )
            elif calc[n] == ops[2] :
                result = Calculator.Multiplication(result,calc[y])
                print("Mult", result)
            elif calc[n] == ops[3] :
                result = Calculator.Division(result,calc[y])
                print("Div", result)
            else:
                print("404 Jutsu Not found what", calc[n], "n =", n ) 
            y += 2
            n += 2
            
        size -= 1
        step += 1
    return result
