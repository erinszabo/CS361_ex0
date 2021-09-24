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
def get_info():
    # file_in = raw_input("driver file: ")
    file = open("drivers.txt", "r")
    for i in range(19): # 20 drivers
        driver = file.readline()
        # ..... continue later
        # print(driver, end = '') # no new line
    return