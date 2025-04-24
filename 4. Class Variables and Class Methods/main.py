class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        return cls.bank_name

# Branch 1
HBL_Branch_1 = Bank()
print(HBL_Branch_1.bank_name)
print(HBL_Branch_1.change_bank_name("HBL Bank 1"))

# Branch 2
HBL_Branch_2 = Bank() # Branch 2 will have the same bank name as Branch 1: "HBL Bank 1"
print(HBL_Branch_2.bank_name) # Changing 2 name so that it shows: "HBL Bank 2"
print(HBL_Branch_2.change_bank_name("HBL Bank 2"))

print("Printing Branch 1 again to show that the bank name has been changed to 'HBL Bank 2' by Branch 2.")
print(HBL_Branch_1.bank_name)

