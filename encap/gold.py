class TreasureChest:
    def __init__(self):
        # Initialize an empty list to store the contents of the chest
        self.__contents = []

    def add_item(self, item):
        # Add an item to the chest
        self.__contents.append(item)
        print(f"Added {item} to the treasure chest!")

    def check_contents(self):
        # Check what's inside the chest
        print("Treasure Chest Contents:")
        for item in self.__contents:
            print(f"- {item}")

# Create a Treasure Chest
my_chest = TreasureChest()

# Try to access the contents directly (this will not work due to encapsulation)
# Uncomment the line below to see the error.
# print(my_chest.__contents)

# Add items to the chest
my_chest.add_item("Gold coins")
my_chest.add_item("Precious gems")

# Check the contents of the chest
my_chest.check_contents()
