"""
The Invoice Management System for The Pepper Factory Cafe.
1. Generates New Invoice
2. Calculates change returned to customer
3. Takes customer tip into account
4. Sends day's revenue to revenueManagement
"""
from TPFCafeManagement import TPFCafe
from datetime import date


class Invoice(TPFCafe):
    """Invoice base class for Customer Invoice and Vendor Invoice
    Global Constant Attributes: _invoice_serial_no, _INR_denominations
    Instance Attributes: _invoice_id, _invoice_date, _invoice_status, _invoice_amount, _render_change
    """
   
    #class Invoice's global variables:
    _INVOICE_SERIAL_NO = 1
    _INR_DENOMINATIONS = (2000, 500, 200, 100, 50, 20, 10, 5, 2, 1)
    total_cash = 0.0        #should come from Revenue class

    #generates unique invoice ID
    def generate_invoice_id(self):
        """Automatically generates Invoice ID for each
        instance of class Invoice. To be used as Primary Key
        for Revenue database."""
        
        year = (date.today().year)%100
        month = date.today().month

        invoice_id = "TPF"+str(month).zfill(2)+str(year)+str(Invoice._INVOICE_SERIAL_NO).zfill(4)
        Invoice._INVOICE_SERIAL_NO += 1

        return invoice_id

    #constructor method for class Invoice
    def __init__(self):
        """Initialises every instance of this class with
        a few basic details"""

        super().__init__("The Pepper Factory Cafe")
        self._invoice_date = date.isoformat(date.today())
        self._invoice_id = self.generate_invoice_id()
        self._invoice_status = "Unpaid"
        self._invoice_amount = 0.0
        
    
    def process_payment(self):
        """Process payment by accepting payment for
        the Invoice and returns the amount
        to be paid back, if any"""

        print(f"Amount Payable: {self._invoice_amount}")
        #ensuring input is valid and payment is more than bill amount
        while True:

            _paid = self.get_money_input("Amount Paid: ")
            if _paid < self._invoice_amount:
                print(f"Amount Paid Less Than Bill Amount by {self._invoice_amount - _paid}. Try Again!")
            else:
                self._invoice_status = "Paid"
                break
            
        #calculating customer return amount
        _paid = float(_paid)
        result = round(abs(_paid-self._invoice_amount),2)
        to_pay_back = int(result)

        return to_pay_back

    
    def render_change(self, pay_back=0):
        """Takes an amount as input argument of class Integer
        and both prints and returns the INR denominations to be returned.
        Returned value is of class dictionary."""
        
        temp = pay_back
        #ensuring input amount is of class Interger
        if not type(pay_back) is int:
            raise ValueError("Ensure processed amount does not have decimal value")

        return_change = {key:0 for key in Invoice._INR_DENOMINATIONS}

        #calculating change to be rendered
        for i in Invoice._INR_DENOMINATIONS:
            while (pay_back - i) >= 0:
                return_change[i] += 1
                pay_back -= i
            
            if pay_back == 0:
                break
        
        #printing change to be rendered:
        final_amt = 0
        print("\nRender Change:")
        for key in return_change:
            if return_change[key] == 0:
                continue
            print(f"{key} notes: {return_change[key]}")
            final_amt += key*return_change[key]

        #ensuring final_amount is equal to pay_customer
        if not temp == final_amt:
            raise ValueError("Change total NOT matching Calculated Payment!!") 

        print(f"Total amount returned: {final_amt}")

        return return_change
    
    def display_invoice_details(self):
        """Prints Invoice details in order"""

        print(f"\n{self._name}")
        print(f"Invoice ID: {self._invoice_id}")
        print(f"Generated On: {self._invoice_date}")
        print(f"Invoice Status: {self._invoice_status}")
    
    def __str__(self):
        self.display_invoice_details()
        return ""



if __name__ == "__main__":
    
    print("Test Invoice 1:")
    test = Invoice()
    payback = test.process_payment()
    test.render_change(payback)
    test.display_invoice_details()
    print(test)

    print("Test Invoice 2:")
    test1 = Invoice()
    test1.generate_invoice()
    payback = test1.process_payment()
    test1.render_change(payback)
    test1.display_invoice_details()
    print(test1)


    



