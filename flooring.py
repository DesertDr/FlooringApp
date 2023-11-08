import logging

logging.basicConfig(
    level=logging.DEBUG,
    # filename='text.log',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug('Debug Mesage')
logging.info('Info Message')
logging.warning('Warning Message')
logging.error('Error Message')
logging.critical('Critical Message')

# communication functions
# NOTE: add file output functionality - sys log
# NOTE: ADD BLUTOOTH CAPABILITY - PyBluez

def YNBool_Converter(message):
    yes_no_bool = {
        'n': False,
        'no': False,
        'y': True,
        'ye': True,
        'yes': True
    }
    return yes_no_bool.get(message.lower(), False)


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

    def __init__(self, name):
        # super().__init__(self.name)
        self.name = name
        Home.add_room(self.name)
        print(Home.room_list)
        
    # def __str__(self) -> str:
    #     return super().__str__()
    
    # def measure(self):
    #     return f"{self.name}"
    
    def measure(self):
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
            
        cabinet_width = 1.75
        self.cabinet_fp = cabinet_width * self.cabinet_lf[0]
        self.trim = self.cabinet_lf[0] + cabinet_width * self.exposed_ends[0]
        
        self.area = width[0] * length[0] - no_of_bumps[0] * self.wall_width[0] - self.cabinet_fp
        self.baseboard = walls + bump_lf - self.transition - self.cabinet_lf[0]
        
        
    def list(self):
        pass
    
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
        else:
            print(f"\nThere are {Home.num_of_rooms} rooms on file.")
            print(f"Rooms measured: {Home.room_list}")
            
    def load_room(self):
        name_guess = input('\nChoose a room to view/change attributes ')
        if name_guess not in Home.room_list:
            print(f"{name_guess} is nto a room on the list ")
        if name_guess == 1:
            type(Home.room_list[1])
            x = vars(Home.room_list[1][0])
        if name_guess == 2:
            x = vars(Home.room_list[2][0])
        else:
            print(f"Please make a choice from the list ")
            print(Home.room_list)
            
    def rename(self, new_name):
        self.name = new_name
        
        
def main():
    print(f'\nWelcome to the flooring program ')
    while True:
        room_name = Room(input('\nPlease enter room name: '))
        room_name.measure()
        room_name.attributes()
        answer = YNBool_Converter(input('\nContinue measuring, Y/N?'))
        if answer == False:
            print(Home.room_list)
            input('\nChoose a room to view attributes: ')
            break
        else:
            print(room_name)
            room_name.load_room()
            continue
        
                               
if __name__ == '__main__':
    main()