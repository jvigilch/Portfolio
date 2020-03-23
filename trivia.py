from functools import wraps
import difflib


def decorator(generator):
    """Decorator function"""
    gen = generator()

    @wraps(generator)
    def wrapper(movie_char):
        """Wrapper function"""
        return f'Question {next(gen)} {movie_char}: '

    return wrapper


@decorator
def question_number():
    """Generates a question number generator"""
    i = 1
    while True:
        yield i
        i += 1


def get_questions(path):
    """Creates a generator that fetches lines from the path file"""
    with open(path) as fp:
        for line in fp:
            yield line.strip()


def grade_question(guess, answer):
    """Grades the guess according to the correct answer"""
    ratio = difflib.SequenceMatcher(None, guess, answer).ratio()
    if ratio >= .7:
        earned_points = 1
    else:
        earned_points = 0

    return earned_points


q_gen = get_questions('questions.txt')
points_total = 0
count = 0

print(f'{"Movie Trivia":*^30}\n\nYou will be given a character and you must respond with their movie:')

for q in q_gen:
    data = q.split(',')
    character, ans = data[0], data[1]
    prompt = question_number(character)
    guess = input(prompt)
    points_total += grade_question(guess, ans)
    count += 1

print(f'You scored {points_total} out of {count} questions')
