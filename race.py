# Driver class with traits name, number and line
class Driver:
    def __init__(self, name, number, line):
        self.na = name
        self.nu = number
        self.li = line
    
    # getters for each trait

    # setter for line, so I can add " YEET!" later if name == Lewis Hamilton




# get info from file to create driver objects
def get_info():
    # file_in = raw_input("driver file: ")
    file = open("drivers.txt", "r")
    for i in range(19): # 20 drivers
        driver = file.readline()
        # ..... continue later
        # print(driver, end = '') # no new line
    return