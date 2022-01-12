#Basic Calculus, Edward Bowyer January 10 2022

def main():
    print("Welcome to the basic calculus calculator...")
    choice = int(input("Derivation(1) or Integration(2)?"))
    if choice == 1:
        derive()
    elif choice == 2:
        integrate()
    


def derive():  
    coef = int(input("Enter the coefficient: \n"))
    power = int(input("Enter the power: \n"))
    print("Problem is:", coef,"x^","(",power,")")
    if power != 0:
        solved = coef*power
        power = power-1
        print("Solution is:", solved,"x^","(",power,")")
    elif power == 0:
        solved = coef
        power = 0
        print("Solution is:", solved,"x^","(",power,")")
    
def integrate():
    coef = int(input("Enter the coefficient: \n"))
    power = int(input("Enter the power: \n"))
    print("Problem is:", coef,"x^","(",power,")")
    if power != -1:
        power = power+1
        solved = coef/power        
        print("Solution is:", solved,"x^","(",power,")")
    elif power == -1:
        solved = -coef
        power = 0
        print("Solution is:", solved,"x^","(",power,")")
        
        
main()