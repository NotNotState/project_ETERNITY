import os
from itertools import islice
from functions.sinh import custom_sinh
from functions.arccos import arccos_taylor
from functions.logarithm import logarithm
from functions.exponent import exponent
from functions.ab_power_x import ab_power_x
from functions.mean_absolute_deviation import get_mad
from functions.standard_deviation import standard_deviation

class Answer_Package:
    def __init__(self, jump):
        self.answer = ''
        self.jump = jump

def single_input(operation, jump, sinh = True):
    print(f"entered sinh: with {operation}")
    answr_package = Answer_Package(jump)
    to_calculate = ''
    for i in operation:
        answr_package.jump += 1
        if i != ")":
            to_calculate += i
        else:
            break
    c = calc_obj()
    if sinh:
        
        answr_package.answer = custom_sinh(float(c.calculate(to_calculate)))
        print(f"sinh({to_calculate} = {answr_package.answer}")
    else:
        answr_package.answer = arccos_taylor(float(c.calculate(to_calculate)))
        print(f"arccos({to_calculate} = {answr_package.answer}")
    return answr_package

def list_function(operation, jump, function):
    print(f"entered {function} with {operation}")
    numbers = []
    brackets = ["("]
    current_number = ''
    answr_package = Answer_Package(jump)
    op_iter = iter(operation)
    c = calc_obj()
    for i in op_iter:
        answr_package.jump+=1
        if i==" ":
            pass
        else:     
            if i != ")" or (i == ")" and len(brackets) > 1): 
                print(f"\noperation: {operation}") 
                print(f"current: {i}")
                print(f"numbers: {numbers}")
                if i != ',':
                    current_number += i
                    if i == "(":
                        brackets.append(i)
                    if i == ")":
                        brackets.pop()
                # since we check commas, special checks for possible functions that also use commas
                    if i == "s" or i == "a":
                        pass
                    elif i == "e":
                        current_number = current_number[:-1]
                        answr_pkg_2 = c.get_answr_package(operation, "exp", 4, op_iter, i)
                        current_number += str(answr_pkg_2.answer)
                        answr_package.jump += answr_pkg_2.jump + 1
                    elif i == "l":
                        current_number = current_number[:-1]
                        answr_pkg_2 = c.get_answr_package(operation, "log", 4, op_iter, i)
                        current_number += str(answr_pkg_2.answer)
                        answr_package.jump += answr_pkg_2.jump + 1
                    elif i == "m":
                        current_number = current_number[:-1]
                        answr_pkg_2 = c.get_answr_package(operation, "mad", 4, op_iter, i)
                        current_number += str(answr_pkg_2.answer)
                        answr_package.jump += answr_pkg_2.jump + 1
                    elif i == "b":
                        current_number = current_number[:-2]
                        answr_pkg_2 = c.get_answr_package(operation, "abx", 3, op_iter, i)
                        current_number += str(answr_pkg_2.answer)
                        answr_package.jump += answr_pkg_2.jump + 1
                    elif i == "t":
                        current_number = current_number[:-2]
                        answr_pkg_2 = c.get_answr_package(operation, "std", 3, op_iter, i)
                        current_number += str(answr_package.answer)
                        answr_package.jump += answr_pkg_2.jump + 1
                    # since 's' is passed, must manually give the option of sin being found, even if it doesn't have commas
                    elif i == "i":
                        current_number = current_number[:-2]
                        answr_pkg_2 = c.get_answr_package(operation, "sinh", 4, op_iter, i)
                        current_number += str(answr_pkg_2.answer)
                        answr_package.jump += answr_pkg_2.jump + 1
                else:
                    final_number = c.calculate(current_number)
                    numbers.append(float(final_number))
                    current_number = ''
            else:
                break
    final_number = c.calculate(current_number)
    numbers.append(float(final_number))
    if function == "std":
        answr_package.answer = standard_deviation(numbers)
        print(f"std{numbers} = {answr_package.answer}")
    elif function == "mad":
        answr_package.answer = get_mad(numbers)
        print(f"mad{numbers} = {answr_package.answer}")
    elif function == "log":
        base = 10
        x = numbers[0]
        if len(numbers) == 2:
            base = float(numbers[1])
        answr_package.answer = logarithm(base, x)
        print(f"log{numbers} = {answr_package.answer}")
    elif function == "exp": 
        base = numbers[0]
        exp = numbers[1]
        answr_package.answer = exponent(base, exp)
        print(f"exp{numbers} = {answr_package.answer}")
    else:  # abx
        a = numbers[0]
        b = numbers[1]
        x = numbers[2]
        answr_package.answer = ab_power_x(a,b,x)
        print(f"abx{numbers} = {answr_package.answer}")
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
    return list_function(operation, 2, "log")

def exp(operation):
    return list_function(operation, 2, "exp")

def abx(operation):
    return list_function(operation, 1, "abx")

class calc_obj:

    def __init__(self):
        self.characters =["+", "-", "*","/","^","<","<=",">", ">=" , "==", "!=", "(", ")"]
        self.operators = []
        self.numbers = []
        self.final_answer = 0    

    # the jumps is the number of chars (numbers, operators, space, and letters of the function name) 
    # should be skipped since the function already calculated everything within its brackets.
    def get_answr_package(self, operation, function, jump, op_iter, i):
        answr_package = ''
        if function == "abx":
            answr_package = abx(operation[operation.index(i) + jump:])
        elif function == "exp":
            answr_package = exp(operation[operation.index(i) + jump:])
        elif function == "log":
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
        return answr_package


    # return priority of operator
    def converOperator(self, operator):
        return {
            '^': 1, '*': 2, '/': 2, '-': 3, '+': 3, '(': 4,  ')': 4, 
        }.get(operator, 5)

    # calculate the last two numbers and the respective operator. push answer intow numbers[]
    def execute(self):
        b = float(self.numbers.pop())
        a = float(self.numbers.pop())
        result = 0
        operator = self.operators.pop()
        result = {
            '^':pow(a,b), '+':a+b, '-':a-b, '*':a*b, '/':a/b
        }.get(operator, -1)
        self.numbers.append(result)
        print(f"executing: {a} {operator} {b} = {result}")

    def calculate(self, operation):
        # iter object. helps with jumping iteration
        op_iter = iter(operation)
        current_number = ''
        for i in op_iter:
            if i == " ":
                pass
            else:
                print(f"\noperation: {operation}")
                print(f"current: {i}")
                print(f"operators: {self.operators}")
                print(f"numbers: {self.numbers}")
                # both sin and std have s, so we'll ignore it for now, same for a in abx and arccos
                if i == "s" or i =="a":
                    pass 
                elif i == "b":
                    self.numbers.append(self.get_answr_package(operation, "abx", 3, op_iter, i).answer)
                elif i == "e":
                    self.numbers.append(self.get_answr_package(operation, "exp", 4, op_iter, i).answer)
                elif i == "l":
                    self.numbers.append(self.get_answr_package(operation, "log", 4, op_iter, i).answer)
                elif i == "m":
                    self.numbers.append(self.get_answr_package(operation, "mad", 4, op_iter, i).answer)
                elif i =="r":
                    self.numbers.append(self.get_answr_package(operation, "arccos", 6, op_iter, i).answer)
                elif i == "i":
                    self.numbers.append(self.get_answr_package(operation, "sinh", 4, op_iter, i).answer)
                elif i == "t":
                    self.numbers.append(self.get_answr_package(operation, "std", 3, op_iter, i).answer)
                elif i not in self.characters:
                    current_number += i
                else:
                    # reaching operator means a number has been fully recorded
                    if current_number != '':
                        self.numbers.append(current_number)
                        current_number = ''
                    if i == ")":
                        # loop execute until respective open bracket is found
                        while not self.operators[-1] == "(" :
                            self.execute();
                        # popping respective open bracket
                        self.operators.pop()
                    # checking if operator priority is respected (kinda forgot what len(op)==0 checks)
                    elif i == "(" or len(self.operators) == 0 or self.converOperator(self.operators[-1]) > self.converOperator(i):
                        # in case we want a negative number
                        if i == "-" and len(self.numbers) == 0:
                            self.numbers.append(0)
                        self.operators.append(i)
                    else:
                        # if the operator has lower priority, the one before will calculate first, before getting pushed
                        self.execute()
                        self.operators.append(i)
        if current_number != '':
            self.numbers.append(current_number)
        while len(self.operators) != 0:
            self.execute()
        self.final_answer = self.numbers.pop()
        print(f"\n{operation} = {self.final_answer}")
        return self.final_answer

# ===================================================================

    
# if __name__ == "__main__":
#     os.system('cls')
#     c = calc_obj()
#     with open('Input.txt', 'r') as file:
#         count = 1
#         for line in file:
#             print("\n================================")
#             print(f" {count})   {line}")
#             print("================================")
#             c.calculate(line.strip())
#             count+=1

#             # sinh(7) = 548.3161232732465
#             # sinh(56) = 1.045829748006498e+24
#             # std(11, 9, 10, 34) = 10.416333328
#             # log(4, 2) = 2
#             # exp(2,-3/4) = 0.594603
#             # abx(1.5, 3, -2) = 0.166666...
#             # arccos(-0.55) = 2.15316056466364
#             # mad(5, 12, 1, 0, 4, 22, 15, 3, 9) = 5.876543209876543

