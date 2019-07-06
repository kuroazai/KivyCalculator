# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 21:33:05 2019

@author: KuroAzai
"""

#credits to sergzah for a solution i used
import sys 
import re




def Addition(a,b):
    return a + b
    



def Subtraction(a,b):
    return a - b 



def Division(a,b):
    return a / b



def Multiplication(a,b):
    return a * b 




#First inital method allows for a string from kivy to processed Don't personally recommend it
def SingularMethod(string):
    #Imports to read stdout
    import numbers
    
    from io import StringIO
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    
    def fix(a,b):
        sa  = len(a)
        sb = len(b)
        if len(a) >= len(b):
            r = (sa - 1)  - sb
            b = b[0:sb-abs(r)]
            return b
        
    def removezero(a):
        s = len(a)
        a = a[1:s]
        return a
    
    #check if it's a number or not then add it as a number or operator
    a = re.split('\W+',string) 
    a = string.split()
    b = re.split('\d+', string) 
    s = string.replace(" ", "")
    b = re.split('\d+', string) 
    '''
    s = ""
    b = s.join(b)
    b = re.split('\.' , b)
    '''
    for x in b:
        x = x.split()
    Validate = ["+",'-','*','/']
    counter = 0
    for x in a :
        if x in Validate :
            del a[counter]
        counter += 1
    #New array of information ~ 
    values = a
    operation = []
    '''
    #Validate Number 
    for x in a : 
        print(x)
        #res = float(x).isnumeric()
        res = isinstance(x, numbers.Real)
        print(res)
        if res == True:
            values.append(x)
        else:
            pass
    '''
    #Validate our operators
    for x in b :
        x = x.lstrip()
        x = x.rstrip()
        if x in Validate:
            operation.append(x)            
        else:
            pass
    if len(operation) >= len(values) and len(values) > 1:
        operation = fix(operation,values)
    #Perform the operations 
    result = 0    
    try :
        i = 0     
        if len(values) <= 1 and len(operation) <= 1 or len(operation) <= 1 and len(values) <= 1:
            return string
        if len(values) == 1 and len(operation) == 1:
            result = str(operation[0] + str(values[0]))
            cmd = "print(" + result + ")"
            exec(cmd)
            
            sys.stdout = old_stdout
            b = redirected_output.getvalue()
            
            return b
        if len(values) <= 2:
            result = str(values[0]) + operation[i] + str(values[1])
            cmd = "print(" + result + ")"
            exec(cmd)
            
            sys.stdout = old_stdout # !
            b = redirected_output.getvalue()
            
            return b
        else:         
            for x in values:
                if i < len(operation):     
                    result = str(result) + str(x) + str(operation[i])
                else: 
                    result = str(result) + str(x)

                i += 1
        
        if float(result[:1]) == 0:
            result = removezero(result)
        cmd = "print(" + result + ")"
        exec(cmd)
    except Exception as e:
        e = "An error Has occured : " , e
        return e
    
    finally: # !
        sys.stdout = old_stdout # !
        b = redirected_output.getvalue()
        return b
        s = len(b) -1
        return b[s-1:s+2]
    
    #b =b[:1]
    
    #b = re.split('\W+',b) 
    s = len(b)-2
    print(b[s])
    return  b[s]

'''
a = "1 + 1 + 2 * 6 / 2"
b = (SingularMethod(a))
print(b)
'''
