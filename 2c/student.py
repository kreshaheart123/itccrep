class Student:

    # Complete the init
    def __init__(self):
        # Attributes of name, age, weight, height, and a list of grades for 5 subjects
        # Complete the __init__ method
        self.__name = None
        self.__age = None
        self.__weight = None
        self.__height = None
        self.__subjects = {
            "English": 0.0,
            "Filipino": 0.0,
            "Mathematics": 0.0,
            "Non-Verbal": 0.0,
            "Science": 0.0
        }

    # Declare getters and setters for all attributes (including individual subjects)

    # Then complete the following methods
    def getBMI(self) -> float:
        pass

    def getGPA(self) -> float:
        pass

    def __str__(self) -> str:
        """
        Prints the name of the student, their age, BMI, and grades in successive order.

        :return:
        """
        # Complete this method
        pass