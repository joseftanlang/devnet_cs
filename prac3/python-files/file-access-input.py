# File name to work with
obj = "devices.txt"

try:
    choice = int(input("Append for 1 and Read for 2: ").strip())
except ValueError:
    print("Invalid choice. Please enter 1 or 2.")
    exit(1)

if choice == 1:
    # Append mode
    userinput = input("What do you want to insert: ").strip()
    if userinput:  # Only write if not empty
        with open(obj, "a") as file:
            file.write(userinput + "\n")
        print("Item appended successfully.")
    else:
        print("Nothing to append.")

elif choice == 2:
    # Read mode
    try:
        with open(obj, "r") as file:
            lines = file.readlines()
            if lines:
                print("Contents of devices.txt:")
                for line in lines:
                    print(line.strip())
            else:
                print("File is empty.")
    except FileNotFoundError:
        print(f"File '{obj}' not found.")

else:
    print("Error: Choice must be 1 or 2.")

