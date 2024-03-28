from abc import ABC, abstractmethod
class bank_details:
    def __init__(self,acc_no,name,branch) -> None:
        self.acc_no = acc_no
        self.name = name
        self.branch = branch

    @abstractmethod
    def display_details(self):
        print("Account Number:", self.acc_no)
        print("Account Holder Name:", self.name)
        print("Branch:", self.branch)
    @abstractmethod
    def ifsc(self):
        print("Ifsc code is 000001")

class inher(bank_details):
    def result(self):
        print(f"{self.acc_no} says {self.name} {self.branch}")
obj = inher("123456","Archana","chennai")
obj.result()



