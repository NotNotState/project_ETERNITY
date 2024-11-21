import os
from itertools import islice
import math
from functions.sinh import custom_sinh
from functions.standard_deviation import standard_deviation
from functions.arccos import arccos_taylor
from functions.exponent import exponent
from functions.mean_absolute_deviation import get_mad
from functions.logarithm import logarithm

characters =["+", "-", "*","/","^","<","<=",">", ">=" , "==", "!=", "(", ")"]
operators = []
numbers = []
final_answer = 0

# the jumps is the number of chars (numbers, operators, space, and letters of the function name) 
# should be skipped since the function already calculated everything within its brackets.
def get_answr_package(operation, function, jump, op_iter, i):
    answr_package = ''
    if function == "log":
        answr_package = log(operation[operation.index(i) + jump:])
    elif function == "mad":
        answr_package = mad(operation[operation.index(i) + jump:])
    elif function == "arccos":
        answr_package = arccos(operation[operation.index(i) + jump:])
    elif function == "sinh":
        answr_package = sinh(operation[operation.index(i) + jump:])
    elif function == "std":
        answr_package = std(operation[operation.index(i) + jump:])
    # here is where the jumping happens
    next(islice(op_iter, answr_package.jump, answr_package.jump + 1), '')
    return answr_package.answer


# return priority of operator
def converOperator(operator):
    return {
        '^': 1, '*': 2, '/': 2, '-': 3, '+': 3, '(': 4,  ')': 4, 
    }.get(operator, 5)

# calculate the last two numbers and the respective operator. push answer intow numbers[]
def execute():
    b = float(numbers.pop())
    a = float(numbers.pop())
    result = 0
    operator = operators.pop()
    result = {
        '^':exponent(a,b), '+':a+b, '-':a-b, '*':a*b, '/':a/b
    }.get(operator, -1)
    numbers.append(result)
    print(f"{a}, {operator}, {b} == {result}")

def calculate(operation : str) -> float:
    # iter object. helps with jumping iteration
    op_iter = iter(operation)
    current_number = ''
    for i in op_iter:
        if i == " ":
            pass
        else:
            # both sin and std have s, so we'll ignore it for now
            if i == "s":
                pass 
            elif i == "l":
                numbers.append(get_answr_package(operation, "log", 4, op_iter, i))
            elif i == "m":
                numbers.append(get_answr_package(operation, "mad", 4, op_iter, i))
            elif i =="a":
                numbers.append(get_answr_package(operation, "arccos", 7, op_iter, i))
            elif i == "i":
                numbers.append(get_answr_package(operation, "sinh", 4, op_iter, i))
            elif i == "t":
                numbers.append(get_answr_package(operation, "std", 3, op_iter, i))
            elif i not in characters:
                current_number += i
            else:
                # reaching operator means a number has been fully recorded
                if current_number != '':
                    numbers.append(current_number)
                    current_number = ''
                if i == ")":
                    # loop execute until respective open bracket is found
                    while not operators[-1] == "(" :
                        execute()
                    # popping respective open bracket
                    operators.pop()
                # checking if operator priority is respected (kinda forgot what len(op)==0 checks)
                elif i == "(" or len(operators) == 0 or converOperator(operators[-1]) > converOperator(i):
                    # in case we want a negative number
                    if i == "-" and len(numbers) == 0:
                        numbers.append(0)
                    operators.append(i)
                else:
                    # if the operator has lower priority, the one before will calculate first, before getting pushed
                    execute()
                    operators.append(i)
    if current_number != '':
        numbers.append(current_number)
    while len(operators) != 0:
        execute()
    final_answer = numbers.pop()
    print(f"\n{operation} = {final_answer}")
    return final_answer

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Answer_Package:
    def __init__(self, jump):
        self.answer = ''
        self.jump = jump

def single_input(operation, jump, sinh = True):
    answr_package = Answer_Package(jump)
    to_calculate = ''
    for i in operation:
        answr_package.jump += 1
        if i != ")":
            to_calculate += i
        else:
            break
    if sinh:
        answr_package.answer = custom_sinh(float(calculate(to_calculate)))
    else:
        answr_package.answer = arccos_taylor(float(calculate(to_calculate)))
    return answr_package

def list_function(operation, jump, function):
    numbers = []
    brackets = ["("]
    current_number = ''
    answr_package = Answer_Package(jump)
    op_iter = iter(operation)
    for i in op_iter:
        answr_package.jump+=1
        if i != ")" or (i == ")" and len(brackets) > 1):  
            if i != ',' and i != "s":
                current_number += i
                if i == "(":
                    brackets.append(i)
                if i == ")":
                    brackets.pop()
            # since we check commas, special checks for possible functions that also use commas
            elif i == "s":
                pass
            elif i == "l":
                current_number += str((get_answr_package(operation, "log", 4, op_iter, i)))
            elif i == "m":
                current_number += str((get_answr_package(operation, "mad", 4, op_iter, i)))
            elif i == "t":
                current_number += str((get_answr_package(operation, "std", 3, op_iter, i)))
            # since 's' is passed, must manually give the option of sin being found, even if it doesn't have commas
            elif i == "i":
                current_number += str((get_answr_package(operation, "sinh", 4, op_iter, i)))
            else:
                final_number = calculate(current_number)
                numbers.append(float(final_number))
                current_number = ''
        else:
            break
    final_number = calculate(current_number)
    numbers.append(float(final_number))
    if function == "std":
        answr_package.answer = standard_deviation(numbers)
    elif function == "mad":
        answr_package.answer = get_mad(numbers)
    else:
        # log10
        base = 10
        x = numbers[0]
        if len(numbers) == 2:
            base = float(numbers[1])
        answr_package.answer = math.log(x, base)
        # answr_package.answer = logarithm(x, base)
    return answr_package


def sinh(operation):
    return single_input(operation, 2)

def arccos(operation):
    return single_input(operation, 5, False)

def std(operation):
    return list_function(operation, 1, "std")

def mad(operation):
    return list_function(operation, 2, "mad")

def log(operation):
    return list_function(operation, 4, "log")

    
if __name__ == "__main__":
    # os.system('cls')
    # with open('Input.txt', 'r') as file:
    #     count = 1
    #     for line in file:
    #         print("\n================================")
    #         print(f" {count}  -  {line}")
    #         print("================================")
    #         calculate(line.strip())
    #         count+=1
    test = "1+2+log(4,2)"
    print(calculate(test))
