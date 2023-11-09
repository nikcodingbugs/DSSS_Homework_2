import random


def random_int(min_val: int, max_val: int):
    """
    Random choice of a value between two boundaries.

    Args:
        min_val (int): The lower boundary for the random value.
        max_val (int): The upper boundary for the random value.

    Returns:
        int: A random value in the defined range.
    """
    try:
        return random.randint(min_val, max_val)
    # The boundary values are converted to int
    except ValueError:
        print("The values for random_int have to be integers! They will be cut from the decimal point.")
        return random.randint(int(min_val), int(max_val))

def random_operator():
    """
    Random choice between the operators +, - and *.

    Returns:
        str: A random operator out of +, - or *.
    """
    return random.choice(['+', '-', '*'])


def calculation(num1, num2, operator):
    """
    The addition, subtraction or multiplication of two values.
    The calculation depends on the given variable "operator".

    Args:
        num1 (int): The first number on the left side of the calculation.
        num2 (int): The second number on the right side of the calculation.
        operator (str): The type of calculation (+, - or *).

    Returns:
        str: The math problem for visualisation.
        int: The result of the calculation.
    """    
    problem = f"{num1} {operator} {num2}"
    # Defining the right calculation for each operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return problem, result

def math_quiz():
    """
    Math quiz with 10 random questions, which have to be answered on the terminal.
    In the end, the score will be shown.
    """
    score = 0
    total_questions = 10

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = random_int(1, 10)
        num2 = random_int(1, 6)
        operator = random_operator()

        # Math problem is calculated and shown on the terminal
        # The script waits for an input of type int
        problem, correct_answer = calculation(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        try: 
            user_answer = int(input("Your answer: "))
            # User earns one point for a correct answer
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print(f"The answer has to be from type int. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
