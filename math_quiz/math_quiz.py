import random


def generate_random_integer(min_value, max_value):
    """
    Generates a random integer within the specified range.

    Parameters:
    min_value (int): Minimum value of the range.
    max_value (int): Maximum value of the range.

    Returns:
    int: Random integer within the range.
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Chooses a random operator from addition, subtraction, or multiplication.

    Returns:
    str: A random operator.
    """
    return random.choice(['+', '-', '*'])


def create_math_problem(num1, num2, operator):
    """
    Creates a math problem and calculates the correct answer.

    Parameters:
    num1 (int): First number.
    num2 (int): Second number.
    operator (str): Operator to use in the problem.

    Returns:
    tuple: Problem as a string and the correct answer as an integer.
    """
    problem = f"{num1} {operator} {num2}"

    # Calculate answer based on operator
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:  # operator is '*'
        answer = num1 * num2

    return problem, answer


def math_quiz():
    """
    Starts a math quiz game with a series of random problems.
    """
    score = 0
    total_questions = 3  # Set a whole number for questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)  # Use an integer for range
        operator = generate_random_operator()

        problem, correct_answer = create_math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Error handling for non-integer input
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
