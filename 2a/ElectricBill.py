charges = {
    "A" : 1.05, # 1 - 10 kWh
    "B" : 2.25, # 11 - 30 kWh
    "C" : 5.50, # 31 - 50 kWh
    "D" : 10.65 # 50+ kWh
}

class ElectricBill:

    def __init__(self):
        # Complete this method
        # The ElectricBill class has
        # 
        # Refers to amount of electricity consumed per kilowatt-hour 
        self.__rate = None
        # Prev refers to previously consumed kilowatts
        self.__prev = None
        # Curr refers to currently consumed kilowatts
        self.__curr = None
        pass

    # Create the getters and setters of all the attributes here

    # Then complete the following methods

    def vat(self) -> float:
        """
            Calculates the VAT based on charge.
        """
        pass

    def consumption(self) -> float:
        """
            Calculates total consumed kilowatts for this month.
        """
        pass

    def partial(self) -> float:
        """
            Calculates partial bill. This is the basic charge.
        """
        pass

    def bill(self) -> float:
        """
            Calculates final bill.
        """
        pass

    def __str__(self) -> str:
        """
            Prints the electric bill of the user. Includes rate, charge, previous, current, VAT, and bill.
        """
        pass