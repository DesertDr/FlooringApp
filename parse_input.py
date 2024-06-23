# Handling user input, error handling, minimum and maximum values are given depending
# on parts of the room being measured. IE: number of doors (must have at least 1), number of cabinets (can be 0), etc
def parse_input(message, minimum_number, excessive_number):
    while True:
        excessive_number_bypass = False
        try:
            number = float(input(message))
        except ValueError:
            print('Invalid value: ValueError, Please enter a numerical value ')
            continue
        except NameError:
            print('Invalid value: NameError ')
            continue
        
        if number == 0 and minimum_number == 0:
            break
        if number < minimum_number:
            print(f"Please enter a number greater than {minimum_number}")
            continue
        if excessive_number == 0:
            break
        elif number > excessive_number:
            if YNBool_Converter(input('Are you sure, Y/N? \n> ')) == True:
                excessive_number_bypass = True
                break
            else:
                continue
        else:
            break
    return[number, excessive_number_bypass]