#!/usr/bin/env python3

class CreditCard:
    surcharge = 0.1
    def __init__(self, customer_name, customer_credit_card_no, balance):
        self.customer_name = customer_name
        self.customer_credit_card_no = customer_credit_card_no
        self.balance = balance
      
    def check_balance(self):
         return self.balance
    
    def make_payment(self, payment):
        if payment < 0 :
            raise ValueError("Payment can not be in negative") 
        self.balance = self.balance - payment
        return self.balance
    
    def print_customer_info(self):
        #print(" customer details : {0} , {1}, {2}".format(self.customer_name, self.customer_credit_card_no, self.balance))
        print(f" customer details : {self.customer_name}, {self.customer_credit_card_no}, {self.balance}")

card = CreditCard("aashu", 3359 , 1000)
card.print_customer_info()
card.make_payment(150)
card.print_customer_info()
card.make_payment(-10)
card.print_customer_info()

