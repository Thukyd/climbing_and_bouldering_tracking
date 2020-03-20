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
import logging

# module to save entries locally
import local_record

######### MongoDB
import json
import pymongo
from pymongo import MongoClient


# TODO: https://www.youtube.com/watch?v=rE_bJl2GAY8
# TODO: https://account.mongodb.com/account/login
class Mongo():
    def __init__(self):
        self.collection = self.config()

    def config(self):
        with open("./mongo/configurations.json") as file:
            parsed = json.load(file)
            # config params
            param_connection = parsed["connection"]
            param_db_name = parsed["db_name"]
            param_collection = parsed["collection"]
            # set up connection
            cluster = MongoClient(param_connection)
            db = cluster[param_db_name]
            collection = db[param_collection]
        return collection

    def insert(self):
        # TODO: weiter ausbauen
        self.collection.insert_one(
            {"hallo":"Ballo3"}
        )

# convert boulder grade
class Grades():
    def __init__(self):
        # mapping based on this =>
            # https://www.bergzeit.de/magazin/bouldern-schwierigkeitsgrade-tabelle-umrechnung/
        self.grade_mapping = {
            "name" : ["fb-bloc", "fb-trav", "v-scale"],
            "grade": [
                [
                    "4",
                    "4",
                    "V0"
                ],
                [
                    "5",
                    "5",
                    "V1"
                ],
                [
                    "5+",
                    "6a",
                    "V2"
                ],
                [
                    "6a",
                    "6a+",
                    "V3"
                ],
                [
                    "6a+",
                    "6b",
                    "V4"
                ],
                [
                    "6b",
                    "6b+",
                    "V4"
                ],
                [
                    "6b+",
                    "6c",
                    "V5"
                ],
                [
                    "6c",
                    "6c+",
                    "V5"
                ],
                [
                    "6c+",
                    "7a",
                    "V6"
                ],
                [
                    "7a",
                    "7a+",
                    "V6"
                ],
                [
                    "7a+",
                    "7b",
                    "V7"
                ],
                [
                    "7b",
                    "7b+",
                    "V8"
                ],
                [
                    "7b+",
                    "7c",
                    "V9"
                ],
                [
                    "7c",
                    "7c+",
                    "V9"
                ],
                [
                    "7c+",
                    "8a",
                    "V10"
                ],
                [
                    "8a",
                    "8a+",
                    "V11"
                ],
                [
                    "8a+",
                    "8b",
                    "V12"
                ],
                [
                    "8b",
                    "8b+",
                    "V13"
                ],
                [
                    "8b+",
                    "8c",
                    "V14"
                ],
                [
                    "8c",
                    "8c+",
                    "V15"
                ],
                [
                    "8c+",
                    "9a",
                    "V16"
                ],
                [
                    "9a",
                    "> 9a",
                    "V17"
                ]
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



class CreateEntry():
    def __init__(self):
        pass
    
    def console_input(self):
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

    def form_entry(self, data):
        # information about user: currently static => TODO
        user = {
            "id" : "14785239",
            "surname" : "Bruchhagen",
            "forename" : "Heribert"
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
        
        record = [timestamp, scale, grade, completion_type]

        data = self.form_entry(record)

        # add to local record
        local_record.Entries().add_entry(data)
        return record
