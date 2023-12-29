import prob
from fractions import Fraction

def main():
    curr_input_val = input("Enter amount of values: ")
    vals_num = int(curr_input_val)
    print("Entering value, format: \"U\" is undetermined, \"T\" is true, \"F\" is false")
    vals = []
    for i in range(vals_num):
        curr_input_val = input(f"Enter {i}th value: ")
        curr_input_val = curr_input_val.upper()
        if curr_input_val == "T":
            vals.append(True)
        elif curr_input_val == "F":
            vals.append(False)
        else:
            vals.append(None)
    
    curr_input_val = input("Enter amount of clauses: ")
    clauses_num = int(curr_input_val)
    print("Entering literals, format: Optional not (!) followed by the index of the value")
    vars = []
    negateds = []
    for i in range(clauses_num):
        clause_vars = []
        clause_negateds = []
        for j in range(3):
            curr_input_val = input(f"Enter {j}th literal for {i}th clause: ")
            if curr_input_val.startswith("!"):
                clause_negateds.append(True)
                curr_input_val = curr_input_val.replace("!", "")
            else:
                clause_negateds.append(False)
            var = int(curr_input_val)
            if var < 0 or var >= vals_num:
                print("Out of range")
                exit()
            clause_vars.append(int(curr_input_val))
        vars.append(clause_vars)
        negateds.append(clause_negateds)
    
    expected_satisifed = prob.expected(vals, vars, negateds)
    expected_satisifed_fraction = Fraction(expected_satisifed).limit_denominator()
    print(f"The expected num of satisifed clauses = {expected_satisifed} = {expected_satisifed_fraction.numerator}/{expected_satisifed_fraction.denominator}")
    expected_satisifed_rate = expected_satisifed/clauses_num
    expected_satisifed_rate_fraction = Fraction(expected_satisifed_rate).limit_denominator()
    print(f"The expected num of satisifed clauses/{clauses_num} = expected_satisifed_rate = {expected_satisifed_rate_fraction.numerator}/{expected_satisifed_rate_fraction.denominator}")
if __name__ == "__main__":
    main()