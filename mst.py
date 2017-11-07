import os
import platform
from random import randint


class Generator:
    """
    Generates x and y from range given by user.
    :param:min_value - lowest possible x and y value
    :param:max_value - biggest x and y value
    :param:quantity - amount of xs and ys to generate
    :param:correct_data - True if all params are correct
    :param:problems - list of problems eg. min_value < 0
    """
    def __init__(self):
        """Class constructor, controls flow of generating xs and ys"""
        self.min_value = 0
        self.max_value = 0
        self.quantity = 0
        self.filename = None
        self.correct_data = False
        self.problems = []

        while not self.correct_data:
            self.get_data()
            self.validate()

            if self.problems:
                clear_screen()
                for problem in self.problems:
                    print(problem)
            else:
                self.correct_data = True

    def get_data(self):
        """Get data from user"""
        self.min_value = int(input("Min value: "))
        self.max_value = int(input("Max value: "))
        self.quantity = int(input("Quantity: "))
        self.filename = input("Filename: ")

    def validate(self):
        """Basic validation. Check if passed data is correct"""
        if self.min_value < 0:
            self.problems.append("Min value cannot be lower than 0!")
        if self.max_value < 0:
            self.problems.append("Max value cannot be lower than 0!")
        if self.min_value > self.max_value:
            self.problems.append("Min value cannot be greater than max value!")
        if self.quantity <= 0:
            self.problems.append("Quantity cannot be 0 or lower!")
        if self.filename[-4:] != '.txt':
            self.filename += '.txt'

    def generate(self):
        """Actual generation and write to file"""
        with open(self.filename, 'w+') as file:
            for _ in range(self.quantity):
                rand_x = randint(self.min_value, self.max_value)
                rand_y = randint(self.min_value, self.max_value)
                file.write("{} {} \n".format(rand_x, rand_y))


def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def main():
    """Main function"""
    clear_screen()
    generator = Generator()
    generator.generate()
    print("Done!")


if __name__ == '__main__':
    main()