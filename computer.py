class Computer:
    # What attributes will it need?
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        # You'll remove this (pass) when you fill out your constructor
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?
    def update_price(self, new_price: int):
        self.price = new_price
        # return self.price
        

    def update_OS(self, operating_system: str):
        self.new_OS = self.operating_system
        return self.new_OS

    
# def main():
#     computer1= Computer("2019 MacBook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000)
#     print(computer1.refurbish(1,"newOS!"))

# if __name__ == "__main__": main()