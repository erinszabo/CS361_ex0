
# Driver class with traits name, number and line
class Driver:
    def __init__(self, name, number, line):
        self.na = name
        self.nu = number
        self.li = line
    
    # getters for each trait
    def get_name(self):
        return self.na
    
    def get_num(self):
        return self.nu

    def get_line(self):
        return self.li

    # setter for line, so I can add " YEET!" if name == Lewis Hamilton
    def check(self):
        if self.na == "Lewis Hamilton":
            self.li = self.li + " YEET!"



# get info from file to create driver objects
# returns an array of driver objects
def get_info():
    file = open("drivers.txt", "r")
    drivers = [] # to store driver objects
    
    # populate drivers array with driver objects using file info 
    for i in range(19): # 20 drivers
        line = file.readline()  # the whole line is the "line"
        # split the line by the spaces
        parts = line.split()
        
        ### name = str(parts[0]) + " " + str(parts[1])  # first 2 words are the "name" of the driver
        ### ^ DELETE ME ^

        # easier to use just the last name
        name = str(parts[1]) # second word is last name
        
        num = parts[2]  # 3rd is the "number"

        ### TEST ###
        # print(f" line = {line} name = {name} \n num = {num} \n ")

        #create a driver object
        d = Driver(name, num, line)
        drivers.append(d)

    ### TEST ###
    # print(f"driver[0] name = {drivers[0].get_name()}")
    # print(f"driver[0] num = {drivers[0].get_num()}")
    # print(f"driver[0] line = {drivers[0].get_line()}")



    return drivers

# sorts drivers array in alphabetical order by last name
def name_sort(arr):
    arr.sort(key=lambda x: x.na)
    return arr

# sorts drivers array by number
def num_sort(arr):
    arr.sort(key=lambda x: int(x.nu))
    return arr


# prints the sorted list of drivers
def display(d_array):
    print("")
    print("2021 F1 Drivers")
    print("===============")
    for driver in d_array:
        print(driver.get_line(), end = '') # no new line
        # print(driver.get_num()) 
        # print(driver.get_name())

    return 