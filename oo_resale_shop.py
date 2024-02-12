from computer import Computer
class ResaleShop:
    """
    
    """
    # What attributes will it need?
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, item_id, inventory):
    # You'll remove this when you fill out your constructor
        self.item_id = 0
        self.inventory = {}
    # What methods will you need?
    def buy(self, computer: Computer): 
        """
    
        """
        self.item_id += 1
        self.inventory[self.item_id] = computer
        return self.item_id
  
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def update_price(self,item_id: int, new_price: int):
        if self.item_id in self.inventory:
            computer = self.inventory[self.item_id] 
            computer.update_price(new_price)
            self.inventory[self.item_id] = computer
        else:
            print("Item", item_id, "not found. Cannot update price.")
        
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
        # For each item
            for item_id in self.inventory:
            # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id].description}')
        else:
            print("No inventory to display.")

    def refurbish(self, item_id: int, new_os: str):
        if item_id in self.inventory:
            computer = self.inventory[item_id]
            if item_id in self.inventory:
                computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

        if new_os is not None:
            computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", self.item_id, "not found. Please select another item to refurbish.")

# def main():
#     computer1 = Computer("2019 MacBook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000)
#     computer2 = Computer("2020 MacBook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000)
#     resale = ResaleShop(3,{})
#     print(resale.buy(computer1))
#     print(resale.buy(computer2))
#     resale.sell(1)
#     resale.update_price(2,24, computer1)
#     resale.print_inventory()
# if __name__ == "__main__": main()