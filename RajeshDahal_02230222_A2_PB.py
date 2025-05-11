pokemon_binder = []  #this will hold the Pokemon cards

def input_int(prompt, min_val=None, max_val=None):
    """Prompt user for an integer input with optional range validation."""
    while True:
        try:
            val = int(input(prompt))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                raise ValueError()
            return val
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def pokemon_card_binder_manager():
    """
    Manage a virtual Pokémon card binder.
    Allows adding, viewing, and resetting card collection.
    """
    print("\n--- Pokemon Card Binder Manager ---")
    while True:
        print("\n1. Add Pokemon card")
        print("2. Reset binder")
        print("3. View current placements")
        print("4. Exit")
        choice = input_int("Enter choice: ", 1, 4)

        if choice == 1:
            name = input("Enter Pokemon card name: ").strip()
            if name:
                pokemon_binder.append(name)
                print(f"Added '{name}' to binder.")
            else:
                print("Card name cannot be empty.")
        elif choice == 2:
            pokemon_binder.clear()
            print("Binder reset.")
        elif choice == 3:
            print("Current cards in binder:")
            if pokemon_binder:
                for idx, card in enumerate(pokemon_binder, 1):
                    print(f"{idx}. {card}")
            else:
                print("Binder is empty.")
        elif choice == 4:
            break

if __name__ == "__main__":
    pokemon_card_binder_manager()
1