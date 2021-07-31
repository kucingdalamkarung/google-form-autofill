import random
import string


def generateLine(count):
    lines = []
    start = 0
    end = 5
    for i in range(count):
        child = [start, end]
        lines.append(child)
        start = start + 6
        end = end + 6

    return lines


def generateLineRadio(count):
    lines = []
    start = 0
    end = 1
    for i in range(count):
        child = [start, end]
        lines.append(child)
        start = start + 2
        end = end + 2

    return lines


def generateLineRadio2(count):
    lines = []
    start = 0
    end = 1
    for i in range(count):
        child = [start, end]
        lines.append(child)
        start = start + 5
        end = end + 5

    return lines


class Generator:
    @staticmethod
    def generateAge(min, max):
        return random.randint(min, max)

    @staticmethod
    def generateInitialName():
        letters = []
        for i in range(0, 2):
            letter = random.choice(string.ascii_letters)
            letters.append(letter)

        return "".join(letters).upper()

    @staticmethod
    def generateSemester():
        return random.randint(1, 8)

    @staticmethod
    def generateIPK():
        return f'{random.uniform(2.9, 4): .2f}'

    @staticmethod
    def generateAnswer(count):
        lines = generateLine(count)
        answers = []
        for i in range(count):
            randAnswer = random.randint(lines[i][0], lines[i][1])
            answers.append(randAnswer)

        return answers

    @staticmethod
    def generateAnswer2(count):
        lines = generateLineRadio(count)
        answers = []
        for i in range(count):
            randAnswer = random.randint(lines[i][0], lines[i][1])
            answers.append(randAnswer)

        return answers

    @staticmethod
    def generateAnswer3(count):
        lines = generateLineRadio2(count)
        answers = []
        for i in range(count):
            randAnswer = random.randint(lines[i][0], lines[i][1])
            answers.append(randAnswer)

        return answers
