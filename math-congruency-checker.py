import tkinter as tk

def main():
    print("This program checks if two numbers are congruent.")
    running = True
    while running == True:
        print("Enter the first number: ")
        a = int(input())
        print("Enter the second number: ")
        b = int(input())
        print("Enter the modulus: ")
        m = int(input())

        if (a - b) % m == 0:
            print("The numbers are congruent. The remainder is " + str(a % m) + ".")
        else:
            print("The numbers are not congruent. The remainder of " + str(a) + " is " + str(a % m) + " and the remainder of " + str(b) + " is " + str(b % m) + ".")

        print("Would you like to check another set of numbers? (y/n)")
        answer = input()
        if answer == "n":
            running = False
            print("Program terminated.")
    return

def main_with_UI():
    print("Program started.")
    root = tk.Tk()
    root.title("Math Congruency Checker")
    root.geometry("480x360")
    print("tkinter initielized.")

    tk.Label(root, text="Enter the first number: ").grid(row=0)

main()
