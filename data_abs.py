class BankDetails:
    def __init__(self, acc_no, name, branch) -> None:
        self.acc_no = acc_no
        self.name = name
        self.branch = branch

    def display_details(self):
        print("Account Number:", self.acc_no)
        print("Account Holder Name:", self.name)
        print("Branch:", self.branch)

    def ifsc(self):
        print("IFSC code is 000001")

class Inher(BankDetails):
    def result(self):
        print(f"{self.acc_no}  {self.name}")

# Create an instance of Inher
obj = Inher("123456", "Archana", "Chennai")

# Call methods
obj.ifsc()
obj.display_details()
obj.result()