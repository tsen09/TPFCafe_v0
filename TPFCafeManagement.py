
class TPFCafe(object):
    """Base class for the whole TPF Cafe Management System.
    Contains code that will be frequently used by all TPF subclasses."""

    def __init__(self, name):
        "Initialising the name of the restaurant"
        self._name = name

    def get_string_input(self, message="Enter String: "):
        """Takes keyboard input from user of type string.
        Verifies if user input is empty and
        requests user to try again if true.
        Returns the string given by user."""

        while True:
            user_input = input(message)
            if user_input == "":
                print("Invalid Input. Try Again!!")
            else:
                return user_input
        
        
    
    def get_money_input(self, message="Enter Value: "):
        """Takes keyboard input from user for money-related inputs.
        Verifies if input value is valid. Raises error message, if not,
        and asks user to input again. Returns float type of user input."""
        
        while True:
            user_input = self.get_string_input(message)
            try:
                user_input = float(user_input)
            except:
                print("Invalid Input. Try Again!")
            else:
                return user_input
        
        
    
    def get_quantity_input(self, message="Enter Quantity: "):
        """Takes keyboard input from user for quantity-related inputs.
        Verifies if input value is an Integer. Raises error message, if not,
        and asks user to input again. Returns int type of user input."""
        
        while True:
            user_input = self.get_string_input(message)
            if not user_input.isdigit():
                print("Invalid Quantity. Try Again!!")
            else:
                return int(user_input)


#test runs
if __name__ == "__main__":
    test0 = TPFCafe()
    test_string = test0.get_string_input("Enter test string input: ")
    test_value = test0.get_money_input("Enter test money input: ")
    test_quantity = test0.get_quantity_input("Enter test quantity input: ")

    print(f"\nEntered Value: {test_string}")
    print(f"Entered Value: {test_value}")
    print(f"Entered Quantity: {test_quantity}")
