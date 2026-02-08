class BankAccount:
    def __init__(self, name , balance, pasw):
        self.name = name  #public
        self._balance = balance #protected ._
        self.__pasw = pasw # private .__  data mangling

    def get_balance(self): #getter
        return self._balance

    def set_balance(self, newBalance): #setter
        self._balance = newBalance

    def set__pasw(self, newPasw):
        self.__pasw = newPasw

acc1 = BankAccount("Rahul Kumar", 100_000, "Ab@23")
acc1.set_balance(200_000)
acc1.set__pasw("Ankita@123")
#print(acc1.name, acc1._balance, acc1._BankAccount__pasw)
print(acc1.name , acc1.get_balance() , acc1._BankAccount__pasw)
