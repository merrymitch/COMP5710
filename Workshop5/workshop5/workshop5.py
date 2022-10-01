'''
Author: Akond Rahman 
Sep 09, 2022 
Code needed for Workshop 5 
'''

from ast import operator
import random 


def simpleCalculator(v1, v2, operation):
    print('The operation is:', operation)
    valid_ops = ['+', '-', '*', '/', '%']
    res = 0 
    if operation in valid_ops:
        if operation=='+':
            res = v1 + v2 
        elif operation=='-':
            res = v1 - v2 
        elif operation=='*':
            res = v1 * v2 
        elif operation=='/':                
            res = v1 / v2 
        elif operation=='%':                
            res = v1 % v2 
        print('After calculation the result is:' , res) 
    else: 
        print('Operation not allowed. Allowable operations are: +, -, *, /, %')
        print('No calculation was done.') 
    return res 


def checkNonPermissiveOperations(): 
    # operation_ = '=' 
    # op_list = [ x for x in range(100) ]
    # for op_ in op_list:
    operation_ = "../../../../../../../../../../../etc/passwd%00"
    simpleCalculator( 100, 1,  operation_  ) 
    print('='*100)

def fuzzValues():
    # Error 1
    #simpleCalculator( 100, 0, "/" )

    # Error 2
    #simpleCalculator( 420, "a", "/" )

    # Error 3
    #simpleCalculator( 999, None, "+" )

    # Error 4
    #simpleCalculator( 1111, "åß∂ƒ©˙∆˚¬…æ", "-" )

    # Error 5
    #val1 = {}
    #val1['value'] = 7
    #simpleCalculator( val1, 1, "%" )

    # Error 6
    #simpleCalculator( "333", 9, "+" )

    # Error 7
    val_list = [ x for x in range(100) ]
    simpleCalculator( val_list, 1, "%" )


def simpleFuzzer(): 
    # Complete the following methods 
    fuzzValues()
    #checkNonPermissiveOperations() 


if __name__=='__main__':
    # val1, val2, op = 100, 1, '+'

    # data = simpleCalculator(val1, val2, op)
    # print('Operation:{}\nResult:{}'.format(  op, data  ) )

    simpleFuzzer()