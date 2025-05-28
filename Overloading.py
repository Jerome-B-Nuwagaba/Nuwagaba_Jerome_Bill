class Calculator:
    def add(self, *args):
        if not args:
            print("No numbers to add.")
        else:
            total = sum(args)
            print(f"Sum: {total}")
            
calc = Calculator()

calc.add(20, 23)
calc.add(11, 4, 16, 32)
calc.add()
calc.add(10)