def encode(password): # Madasin Garrison
    encoded_password = []
    for i in password:
        encoded_password.append(int(i) + 3)
    return encoded_password

def decode():#Evan, put your work here for decoding the password
    print("hold")

if __name__ == "__main__": #Madasin Garrison
    storage = [];
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n");
        print("Please enter an option:", end=' ');
        choice = input();
        if choice == "1":
            print("Please enter your password to encode:", end=' ')
            storage = encode(input())
            print("\nYour password has been encoded and stored!\n");
        elif choice == "2":
            decode();
        elif choice == "3":
            break
        else:
            print("Invalid selection")