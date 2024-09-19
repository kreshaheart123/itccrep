# Ranks determine the multiplication of salary of employees, and their tax
ranks = {
    "Intern": [0.75, 0.10],
    "Regular": [1, 0.12],
    "Manager": [1.5, 0.11],
    "Director": [2.015, 0.15],
    "Vice-President": [3.115, 0.175],
    "CEO": [5.05, 0.195]
}


class Employee:
    global ranks

    def __init__(self):
        # Complete this method
        # Has six attributes, name, age, weight, height, salary, and position
        self.__name = None
        self.__age = None
        self.__weight = None
        self.__height = None
        self.__salary = None
        self.__position = None
        pass

    # Declare getters and setters for every attribute above

    # Note that salary is <Regular Salary Value> * Ranks[Position][0]

    def bmi(self) -> float:
        """
        Computers the BMI of the Employee.
        :return:
        """
        pass

    def tax(self) -> float:
        """
            Computes the tax of the employee based on the following equation:
                Actual Salary * Ranks[Position][1]

        :return:
        """
        pass

    def __str__(self) -> str:
        """
            Prints the employee's name, age, BMI, position, and salary.

        :return:
        """
        pass
