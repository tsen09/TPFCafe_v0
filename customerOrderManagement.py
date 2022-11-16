from orderManagement import Order

class CustomerOrder(Order):
    """Child class from taking customer orders.
    Should act as User Interface."""

    #constructor function of class CustomerOrder
    def __init__(self):
        """Inherits every variable from classes Invoice and Order
        and updates invoice id to identify as Customer Invoice"""

        super().__init__()
        self._invoice_id = "C-" + self._invoice_id
        self._tax_amt = 0.0


    def amount_after_taxes(self, tax=5):
        """Updates invoice amount with appropriate tax amount.
        Tax amount comes from user. Default = 5%"""

        self._tax_amt = self._invoice_amount*(tax/100)
        print(f"Tax Amount: {self._tax_amt}\n")
        self._invoice_amount += self._tax_amt
        return 0


    def print_customer_order(self):
        """Prints the entire Invoice in appropriate format"""

        self.display_invoice_details()
        print("\n")
        self.display_closed_order()
        print(f"\nTax Amount: {self._tax_amt}")
        print(f"Net Amount Paid: {self._invoice_amount}")

        return 0

    def generate_customer_order(self):
        """Funtion to call all inherited and local methods
        of class CustomerOrder in appropriate sequence"""

        self.generate_order()
        self.amount_after_taxes()
        pay_back = self.process_payment()
        self.render_change(pay_back)
        print("\n\n")
        self.print_customer_order()

    def __str__(self):
        self.print_customer_order()
        return ""
    

if __name__ == "__main__":
    test0 = CustomerOrder()
    test0.generate_customer_order()


