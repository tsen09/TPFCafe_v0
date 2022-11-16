from invoiceManagement import Invoice

class Order(Invoice):
    """Class Order of The Pepper Factory Cafe
    to manage and execute both Customer and Vendor orders.
    Base Class for class CustomerOrder and VendorOrder.
    """
    
    #constructor method for Order
    def __init__(self):
        """Inherits all class variables from Invoice
        and assigns an empty dictionary to accept order"""
        super().__init__()
        self._order = {}         #empty dictionary to store orders
        self._item_serial_no = 1
        self._amt_before_tax = 0.0   

    
    def reset_order(self):
        """Function to reset present order and
        start fresh again.
        """
        self._order = {}         #reinitialising _order to empty dictionary without updating Invoice ID
        self._item_serial_no = 1
             


    def add_item(self):
        """Function to add one item to the order dictionary.
        Returns a List of [item, quantity, price]
        of type [str, int, float].
        """
        
        #accepting item input
        item = self.get_string_input("\nInput Item: ")    #to be verified with database

        #input item quantity
        quantity = self.get_quantity_input("Enter Quantity: ")

        #input price - REMOVE LATER
        price = self.get_money_input("Input Item Price: ")      #to come from menu database

        return [item, quantity, price]


    def place_order(self):
        """Function to build the _order dictionary for
        a particular table.
        """

        flag = "y"

        while flag.lower() == "y":
            
            order = self.add_item()         #Adding at least 1 order
            self._order.update({self._item_serial_no: order})
            self._item_serial_no += 1

            flag = self.get_string_input("\nAdd Another Order (Y/N): ").lower()

            if not flag == "y":
                break               #passing control back to display_order
        
        return 0
        

    def close_order(self):
        """Closes present active order.
        Calculates net bill amount based on items ordered.
        Updates self._invoice_amount defined in Invoice class
        and returns the total bill amount before taxes."""

        for key in self._order:
            self._order[key].append(self._order[key][-1]*self._order[key][-2])
            self._amt_before_tax += self._order[key][-1]
        
        self._invoice_amount = self._amt_before_tax
        return 0                #passing control back to display_order


    def display_closed_order(self):
        """displays closed order in user-friendly format"""
        print("Item         Quantity        Rate        Cost")
        for key in self._order:
            print(f"{self._order[key][0]}           {self._order[key][1]}           {self._order[key][2]}           {self._order[key][3]}")

        print(f"\nTotal Amount Payable Before Taxes: {self._amt_before_tax}")

        return 0


    def display_order(self):
        """Displays current active order. Prompts
        user to type "Close" to close order or "Add" 
        to keep adding to existing order."""

        #printing current order
        if not self._order:
            print("Current Order Status is Empty. Consider Adding Items!")
        else:
            print("Item         Quantity")
            for key in self._order:
                print(f"{self._order[key][0]}          {self._order[key][1]}")
        
        #prompting user for input regarding further action
        print("\nType Add to keep adding items to this order.")
        print("Type Close to close this order and generate Invoice.")

        while True:
            flag = self.get_string_input("Add/Close?:").lower()
            if not (flag == "add" or flag == "close"):
                print("Invalid Input. Try Again!!")
            elif flag == "add":
                self.place_order()
                return True
            else:
                self.close_order()
                return False



    def generate_order(self):
        """Function to execute all methods of class Order
        in the correct sequence."""
        self.place_order()

        #logic to keep order active until closed by user
        while True:
            flag = self.display_order()

            if flag == False:        #means user wanted to close order
                break      
        
        self.display_closed_order()
        return 0
    

#tests for class Order
if __name__ == "__main__":
    test0 = Order()
    test0.generate_order()
    






    
