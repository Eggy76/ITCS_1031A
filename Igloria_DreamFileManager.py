import os
import time

# Clear screen
os.system("cls")

# Function for typing effect
def typing(text, speed):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(speed)

# Welcome message
typing("Welcome to Simple File Manager\n", 0.05)

while True:
    typing("\nDo you want to continue?\n", 0.03)
    choice = input("Yes/No: ").lower()

    if choice == "yes":
        os.system("cls")

        typing("Loading...", 0.2)
        os.system("cls")

        # Menu function
        def show_menu():
            print("=================================")
            print("        SIMPLE FILE MANAGER      ")
            print("=================================")
            print("1 - Read Messages")
            print("2 - Add Message")
            print("3 - Rewrite File")
            print("4 - Exit")
            print("=================================")

        while True:
            show_menu()

            try:
                menu_choice = int(input("Choose: "))
            except:
                print("Invalid input")
                continue

            # READ FILE
            if menu_choice == 1:
                os.system("cls")

                print("Your Messages:\n")

                try:
                    with open("dreams.txt", "r") as file:
                        content = file.read()
                        print(content)
                except:
                    print("File not found.")

                back = input("\nBack to menu? (y/n): ").lower()

                if back == "y":
                    os.system("cls")

            # ADD MESSAGE
            elif menu_choice == 2:
                os.system("cls")

                new_message = input("Enter message: ")

                with open("dreams.txt", "a") as file:
                    file.write("\n" + new_message)

                print("Message added!")

                back = input("\nBack to menu? (y/n): ").lower()

                if back == "y":
                    os.system("cls")

            # REWRITE FILE
            elif menu_choice == 3:
                os.system("cls")

                new_text = input("Enter new file content: ")

                confirm = input(
                    "This will overwrite the file. Continue? (y/n): "
                ).lower()

                if confirm == "y":
                    with open("dreams.txt", "w") as file:
                        file.write(new_text)

                    print("File rewritten successfully!")

                elif confirm == "n":
                    print("Cancelled.")

                else:
                    print("Invalid input.")

                input("\nPress Enter to continue...")
                os.system("cls")

            # EXIT
            elif menu_choice == 4:
                exit_choice = input("Exit program? (y/n): ").lower()

                if exit_choice == "y":
                    print("Thank you for using the system!")
                    exit()

                os.system("cls")

            else:
                print("Invalid menu choice.")

    elif choice == "no":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid input.")
