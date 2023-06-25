from haiku_generator import HaikuGenerator
from haiku_remixer import HaikuRemixer
from haiku_validator import HaikuValidator, HaikuStructureError

def main():
    haikus = [
        "An old silent pond\nA frog jumps into the pond—\nSplash! Silence again.",
        "Autumn moonlight—\nA worm digs silently\ninto the chestnut.",
        "Over the wintry\nforest, winds howl in rage\nwith no leaves to blow.",
    ]

    print("Welcome to the Haiku Tool!")
    while True:
        print("\nMenu:")
        print("1. Validate a Haiku")
        print("2. Generate a New Haiku")
        print("3. Save a Haiku")
        print("4. Remix an Existing Haiku")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            haiku = input("Enter a haiku for validation: ")
            validator = HaikuValidator(haiku)
            try:
                validator.validate_haiku()
                print("Valid haiku!")
            except HaikuStructureError as e:
                print("Invalid haiku:")
                print(e)

        elif choice == "2":
            generator = HaikuGenerator(haikus)
            new_haiku = generator.generate_haiku()
            print("Generated Haiku:")
            for line in new_haiku:
                print(line)

        elif choice == "3":
            haiku = input("Enter a haiku to save: ")
            with open("haikus.txt", "a") as file:
                file.write(haiku + "\n")
            print("Haiku saved successfully!")

        elif choice == "4":
            remixer = HaikuRemixer(haikus)
            remixed_haiku = remixer.remix_haiku()
            print("Remixed Haiku:")
            for line in remixed_haiku:
                print(line)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
