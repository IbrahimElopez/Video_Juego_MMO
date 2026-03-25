# Welcome message
print("Welcome to the game!")
print("Please select and customize your character.\n")

# Character options using dictionaries
hair_options = {
    1: "Short",
    2: "Long",
    3: "Curly"
}

skin_colors = {
    1: "White",
    2: "Gold",
    3: "Dark"
}

genders = {
    1: "Male",
    2: "Female"
}

shirts = {
    1: "Red shirt",
    2: "Blue shirt",
    3: "Black shirt"
}

pants = {
    1: "Jeans",
    2: "Shorts",
    3: "Joggers"
}

# Function to create player (manual selection)
def create_character(name):
    print(f"\nCreating {name}...\n")

    print("Choose hair style:")
    for key, value in hair_options.items():
        print(key, "-", value)
    hair = hair_options[int(input("Enter option: "))]

    print("\nChoose skin color:")
    for key, value in skin_colors.items():
        print(key, "-", value)
    skin = skin_colors[int(input("Enter option: "))]

    print("\nChoose gender:")
    for key, value in genders.items():
        print(key, "-", value)
    gender = genders[int(input("Enter option: "))]

    print("\nChoose shirt:")
    for key, value in shirts.items():
        print(key, "-", value)
    shirt = shirts[int(input("Enter option: "))]

    print("\nChoose pants:")
    for key, value in pants.items():
        print(key, "-", value)
    pant = pants[int(input("Enter option: "))]

    character = {
        "Name": name,
        "Hair": hair,
        "Skin": skin,
        "Gender": gender,
        "Shirt": shirt,
        "Pants": pant
    }

    return character


# Create characters
player = create_character("Player")

# Show results
print("\n--- CHARACTER SUMMARY ---")
print("\nPlayer:", player)