# write your code here
def task(memory=0.0):
    """Stage 5"""
    memory = memory
    msg_0 = "Enter an equation"
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    msg_3 = "Yeah... division by zero. Smart move..."
    symbol = ["+", "-", "*", "/"]

    calc = input(msg_0 + "\n").split()
    x = validate_number(calc[0], memory)
    method = calc[1]
    y = validate_number(calc[2], memory)

    if not x or not y:
        if x == 0 or y == 0:
            pass
        else:
            print(msg_1)
            return task(memory)
    elif method not in symbol:
        print(msg_2)
        return task(memory)

    check(x, y, method)
    result = calculation(x, y, method)

    if result == ValueError:
        print(msg_3)
        return task(memory)

    print(float(result))

    memory = store_memory(memory, result)

    if continue_request():
        return task(memory)


def validate_number(number, memory):
    try:
        number = float(number)
    except ValueError:
        if number == "M":
            number = memory
        else:
            return False
    return number


def calculation(x, y, method):
    if method == "+":
        return x + y
    elif method == "-":
        return x - y
    elif method == "*":
        return x * y
    elif method == "/":
        if y == 0:
            return ValueError
        else:
            return x / y
    return None


def check(x, y, method):
    msg = ""
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if (x == 1 or y == 1) and method == "*":
        msg += msg_7
    if (x == 0 or y == 0) and (method == "+" or method == "-" or method == "*"):
        msg += msg_8
    if msg:
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    if 10 > v > -10 and v.is_integer():
        return True
    return False


def store_memory(memory, result):
    msg_4 = "Do you want to store the result? (y / n):"
    yes_or_no = input(msg_4 + "\n")
    if yes_or_no == "y":
        if check_easy_memory(result):
            memory = result  # memory += result in stages 1-4
    return memory


def check_easy_memory(number):
    msg_10 = "Are you sure? It is only one digit! (y / n)"
    msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
    msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
    if is_one_digit(number):
        answer = input(msg_10 + "\n")
        if answer == "y":
            answer = input(msg_11 + "\n")
            if answer == "y":
                answer = input(msg_12 + "\n")
                if answer == "y":
                    return True
    else:
        return True
    return False


def continue_request():
    msg_5 = "Do you want to continue calculations? (y / n):"
    continue_or_not = input(msg_5 + "\n")
    if continue_or_not == "y":
        return True
    return False


task()
