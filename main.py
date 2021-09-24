
import race as r


if __name__ == '__main__':
    drivers = r.get_info()
    
    r.display(drivers)  # FOR TESTING, DELETE LATER

    # sort by name
    r.display(drivers) 

    drivers = r.num_sort(drivers)  # sort by number
    r.display(drivers) 

