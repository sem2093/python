import random

def main():
    print("Random Number Generator")
    x = input("Enter 'rn' to generate random number:")
    if x == "rn": 
        random_number = random.randint(1, 100)
        print(random_number)
    else: 
        print("Enter 'rn' to generate random number: ")
      
if __name__ == "__main__":
    main()
