import time

from caesar_cipher import menu_option_1


def display_menu():
    print("Menu:")
    print("1. Encrypt using Caesar Cipher")
    print("2. Encrypt using Mono alphabetic Cipher")
    print("3. Encrypt using Vigenère Cipher")
    print("4. Decrypt using Caesar Cipher")
    print("5. Decrypt using Mono alphabetic Cipher")
    print("6. Decrypt using Vigenère Cipher")
    print("0. Exit")


def menu_option_2():
    print("You selected Option 2")


def menu_option_3():
    print("You selected Option 3")


def menu_option_4():
    print("You selected Option 4")


def menu_option_5():
    print("You selected Option 5")


def menu_option_6():
    print("You selected Option 6")


def main():
    while True:
        time.sleep(2)  # make it sleep for 2 seconds so menu doesn't display automatically
        display_menu()
        choice = input("Please choose an option (0-6): ")

        if choice == '1':
            menu_option_1()
        elif choice == '2':
            menu_option_2()
        elif choice == '3':
            menu_option_3()
        elif choice == '4':
            menu_option_4()
        elif choice == '5':
            menu_option_5()
        elif choice == '6':
            menu_option_6()
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
