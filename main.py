#### Verson 0.1 
# - backend logic only - no database & gui
# - only bouldering
# 1. track route
#   a) set Rotpunkt /On Sight / Flash / try without success
#        https://de.wikipedia.org/wiki/Begehungsstil#Gebr%C3%A4uchliche_Begehungsstile
#   b) set grade in current measurment and convert to standard measurement
#       https://en.wikipedia.org/wiki/Grade_(climbing)
#       https://www.mountainproject.com/international-climbing-grades
# 2. see all results
# a) todays result
# b) former days results


# self.grade_mapping = {
#             "name" : ["fb-bloc", "fb-trav", "v-scale"],
#             "grade": {
#                 0:  ["4", "4", "V0"],
#                 1:  ["5"],
#                 2:  ["5+"],
#                 3:  ["6a"],
#                 4:  ["6a+"],
#                 5:  ["6b"],
#                 6:  ["6b+"],
#                 7:  ["6c"],
#                 8:  ["6c+"],
#                 9:  ["7a"],
#                 10: ["7a+"],
#                 11: ["7b"],
#                 12: ["7b+"],
#                 13: ["7c"],
#                 14: ["7c+"],
#                 15: ["8a"],
#                 16: ["8a+"],
#                 17: ["8b"],
#                 18: ["8b+"],
#                 19: ["8c"],
#                 20: ["8c+"],
#                 21: ["9a"]
#             }


##############################

import datetime
import time

# convert boulder grade
class Grades():
    def __init__(self):
        # mapping based on this =>
            # https://www.bergzeit.de/magazin/bouldern-schwierigkeitsgrade-tabelle-umrechnung/
        self.grade_mapping = {
            "name" : ["fb-bloc", "fb-trav", "v-scale"],
            "grade": [
                ("4", "4", "V0"),
                ("5"),
                ("5+"),
                ("6a"),
                ("6a+"),
                ("6b"),
                ("6b+"),
                ("6c"),
                ("6c+"),
                ("7a"),
                ("7a+"),
                ("7b"),
                ("7b+"),
                ("7c"),
                ("7c+"),
                ("8a"),
                ("8a+"),
                ("8b"),
                ("8b+"),
                ("8c"),
                ("8c+"),
                ("9a")

            ]
        }
        self.standard_grade = 00 # sets standard to "fb-bloc"

    def get_standard(self):
        return self.standard_grade

    def print_standard(self):
        return self.grade_mapping["name"][self.get_standard()]

    def change_grade_system(self): 
        # TODO
        pass

    def set_route_grade(self, index):
        scale = self.get_standard()
        current_grade = self.grade_mapping["grade"][index][scale]
        return current_grade

############# TEST
print()
print(f"My standard scale is {Grades().print_standard()}.") # returns "fb-bloc" 
print(f"The current grade is {Grades().set_route_grade(0)}") # returns "5+"


class CompletionType():
    def __init__(self):
        self.type = {
            0: "flash",
            1: "on-sight",
            2: "rotpunkt",
            3: "try"
        }
    
    def set_completion_type(self, index):
        return self.type[index]

############# TEST
print(f"The completion typ is {CompletionType().set_completion_type(0)}") # returns flash

class CreateEntry():
    def __init__(self):
        pass
    
    def ask_console(self):
        print("##################################\n")
        print("Allright, i need some information\n")
        print("Please tell the grade:\n") 
        print("TODO: FROM 0 TILL 21")

        input_grade = int(input())
        print("\nPlease tell me the type\n")
        print("(0) flash, (1) on-sight, (2) rotpunkt or (3) an unsuccesful try")
        input_type = int(input())
        
        # print out inputs
        print_out = self.add_entry(input_grade, input_type)
        print()
        print(f"I added '{print_out[3]}' with the grade '{print_out[2]}'.")
        print(f"    Scale:  {Grades().print_standard()}")
        timestamp = print_out[0]
        print(f"    Date:   {time.ctime(timestamp)}")
        print()

    def formt_json(self, data):
        # information about user: currently static => TODO
        user = {
            "id" : "123456789",
            "surname" : "Mustermann",
            "forename" : "Max"
        }
        ## entry information
        record = {
            "timetamp" : data[0],
            "scale" : data[1],
            "grade" : data[2],
            "completion_type" : data[3],
            
        }

        return [user, record]

    def add_entry(self, input_grade, input_type):
        grade = Grades().set_route_grade(input_grade)
        completion_type = CompletionType().set_completion_type(input_type)
        timestamp = datetime.datetime.now().timestamp()
        scale = Grades().get_standard()
        return [timestamp, scale, grade, completion_type]



############# TEST 
CreateEntry().ask_console()
