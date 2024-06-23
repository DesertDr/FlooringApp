# Logging functionality: Experimental
# import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     # filename='text.log',
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# logging.debug('Debug Mesage')
# logging.info('Info Message')
# logging.warning('Warning Message')
# logging.error('Error Message')
# logging.critical('Critical Message')

# Communication functions: Future
# NOTE: add file output functionality - sys log
# NOTE: ADD BLUTOOTH CAPABILITY - PyBluez

# Simple Yes/No Boolean Converter
def YNBool_Converter(message):
    yes_no_bool = {
        'n': False,
        'no': False,
        'y': True,
        'ye': True,
        'yes': True
    }
    return yes_no_bool.get(message.lower(), False)

# Handling user input, error handling, minimum and maximum values are given depending
# on parts of the room being measured. IE: number of doors (must have at least 1), number of cabinets (can be 0), etc
def Parse_input(message, minimum_number, excessive_number):
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


class Home():
    room_list = []
    num_of_rooms = 0
    
    def __init__(self) -> None:
        self.name = __name__
        # self.room_list = []
        # self.num_of_rooms = 0
        pass
        
    def add_room(room_name):
        Home.num_of_rooms += 1
        Home.room_list.append(room_name)
        
        
class Room():
    
    name: str
    
    wall_width = [5 / 12, 0]
    excess = 1.1
    diagonal_excess = 1.2
    heringbone_excess = 1.3
    max_doors = 12
    max_door_width = 20
    max_cabinet_sections = 8
    max_cabinet_lf = 30
    max_exposed_ends = 8
    kitchen_half_cabinet = 1.5
    bathroom_short_cabinet = 1.25
    cabinet_width = 1.75

    def __init__(self, name):
        # super().__init__(self.name)
        self.name = name
        Home.add_room(self.name)
        print(Home.room_list)
        
    # def __str__(self) -> str:
    #     return super().__str__()
    
    # def measure(self):
    #     return f"{self.name}"

    # Measure room: Take input on basic dimensions and details, IE: width, length, number of doors, cabinet sections, etc.
    def measure(self):
        # The extra parameters provided to Parse_input are the minimum and maximum values for the input: 0 for max = no max.
        width = Parse_input('\nRoom width: ', 0, 0)
        length = Parse_input('Room length: ', 0, 0)
        
        walls = (width[0] + length[0]) * 2
        
        no_of_bumps = Parse_input('Bumped in walls: ', 0, 0)
        if no_of_bumps[0] == 0:
            bump_depth = [0, 0]
        else:
            bump_depth = Parse_input('Wall depth: ', 0, 0)
            
        bump_lf = bump_depth[0] * no_of_bumps[0] * 2
        self.transition = 0
        
        doors = Parse_input('Number of doors: ', 0, self.max_doors)
        if doors[0] == 0:
            door_width = [0, 0]
        else:
            for n in range(0, int(doors[0])):
                door_width = Parse_input(
                    f'Door {n + 1} width: ', 0, self.max_door_width)
                doors.append(door_width[0])
                self.transition = self.transition + door_width[0]
                
        cabinet_sections = Parse_input('Number of cabinet sections: ', 0, self.max_cabinet_sections)
        if cabinet_sections[0] <= 0:
            self.cabinet_lf = [0, 0]
            self.exposed_ends = [0, 0]
        else:
            self.cabinet_lf = Parse_input('Cabinet linear footage: ', 0, self.max_cabinet_lf)
            self.exposed_ends = Parse_input('Exposed cabinet ends: ', 0, self.max_exposed_ends)

        # Cabinet width default is 1 Foot 9 inches    
        self.cabinet_fp = self.cabinet_width * self.cabinet_lf[0]
        self.trim = self.cabinet_lf[0] + self.cabinet_width * self.exposed_ends[0]
        
        self.area = width[0] * length[0] - no_of_bumps[0] * self.wall_width[0] - self.cabinet_fp
        self.baseboard = walls + bump_lf - self.transition - self.cabinet_lf[0]
        
        
    def list(self):
        pass
    
    # Attributes printing and list room/s measured
    def attributes(self):
        print(f"{self.name} measurements: ")
        if self.cabinet_fp > 0:
            print(f"Figures are shown with 10% excess, besides cabinet footprint")
        else:
            print(f"Figures are shown with 10% excess")
        if self.area > 0:
            print(round(self.area * self.excess, 2), ' sq.ft. flooring')
        if self.baseboard > 0:
            print(round(self.baseboard * self.excess, 2), ' feet of baseboard')
        if self.transition > 0:
            print(round(self.transition * self.excess, 2), ' feet of transition')
        if self.cabinet_fp > 0:
            print(round(self.cabinet_fp, 2), ' sq. ft. cabinetry')
        if self.trim > 0:
            print(round(self.trim * self.excess, 2), ' feet of cabinet trim')
        if Home.num_of_rooms == 1:
            print(f"\nThere is {Home.num_of_rooms} room on file.")
            print(f"Room measured: {Home.room_list}")
        else:
            print(f"\nThere are {Home.num_of_rooms} rooms on file.")
            print(f"Rooms measured: {Home.room_list}")

    # Load room function, Choose from list
    def load_room(self):
        name_guess = input('\nChoose a room to view/change attributes ')
        if name_guess not in Home.room_list:
            print(f"{name_guess} is not a room on the list ")
        if name_guess == 1:
            type(Home.room_list[1])
            room_name = vars(Home.room_list[1][0])
        if name_guess == 2:
            room_name = vars(Home.room_list[2][0])
        else:
            print(f"Please make a choice from the list ")
            print(Home.room_list)
            
    def rename(self, new_name):
        self.name = new_name
        
# Returns True or False as to whether to continue measuring, prints room list on continue | Refactored 6/16/2024
def end_measure():
        answer = YNBool_Converter(input('\nContinue measuring, Y/N?'))
        if answer == False:
            return False
        else:
            print(Home.room_list)
            return True
        
# Main Function
def main():
    print(f'\nWelcome to the flooring program ')
    Run = True
    room_name = Room(input('\nPlease enter room name: '))
    while Run == True:
        room_name.load_room()
        room_name.measure()
        room_name.attributes()
        Run = end_measure()
        
                               
if __name__ == '__main__':
    main()