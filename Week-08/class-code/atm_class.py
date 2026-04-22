correct_pin = 1010

class ATM:
    def __init__(self, atm_id, location, cash_available):
        self.atm_id = atm_id
        self._location = location                 # protected
        self.__cash_available = cash_available     ## private variable

    def verify_pin(self, user_pin):
        if user_pin == correct_pin:
            print("Login Successful!")
            return True
        else:
            return False

    def withdraw_cash(self):
        user_pin = int(input("Enter Pin : "))
        is_successful = self.verify_pin(user_pin)

        if is_successful:
            withdrawal_amount = int(input("Enter Amount : "))
            self.cash_available -= withdrawal_amount
            print("Withdrawal Successfull")
        else:
            print("Invalid Credintials")

    @property
    def cash_available(self):
        return self.__cash_available

    @cash_available.setter
    def cash_available(self, value):
        if isinstance(value, int):
            # self.__cash_available = value
            pass
        else:
            print("What are you doing with atm cash")



    