class Bill:
    def calculate_total(self):
        print("Calculating base hospital bill")

class InpatientBill(Bill):
    def calculate_total(self):
        print("Calculating inpatient bill with room charges")

class OutpatientBill(Bill):
    def calculate_total(self):
        print("Calculating outpatient bill with consultation fees")
        
        
        
x = Bill()
x.calculate_total()
        
y = InpatientBill()
y.calculate_total()
        
z = OutpatientBill()
z.calculate_total()