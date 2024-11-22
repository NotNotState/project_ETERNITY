from functions.fancy_input import calculate


class Answer_Package:
    def __init__(self, jump):
        self.answer = ''
        self.jump = jump

def single_input(operation, jump, sinh = True):
    print(f"entered sinh:{sinh} with {operation}")
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
        print(f"sinh({to_calculate} = {answr_package.answer}")
    else:
        answr_package.answer = arccos_taylor(float(calculate(to_calculate)))
        print(f"arccos({to_calculate} = {answr_package.answer}")
    return answr_package

def list_function(operation, jump, function):
    print(f"entered {function} with {operation}")
    numbers = []
    brackets = ["("]
    current_number = ''
    answr_package = Answer_Package(jump)
    op_iter = iter(operation)
    for i in op_iter:
        if i==" ":
            pass
        else:
            print(f"\ncurrent: {i}")
            print(f"numbers: {numbers}")
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
        print(f"std{numbers} = {answr_package.answer}")
    elif function == "mad":
        answr_package.answer = get_mad(numbers)
        print(f"mad{numbers} = {answr_package.answer}")
    else:
        # log10
        base = 10
        x = numbers[0]
        if len(numbers) == 2:
            base = float(numbers[1])
        answr_package.answer = math.log(x, base)
        print(f"log{numbers} = {answr_package.answer}")
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