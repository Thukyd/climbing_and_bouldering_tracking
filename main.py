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


##############################

import datetime
import time
import logging

######### MongoDB
import json
import pymongo
from pymongo import MongoClient

######### Local DB
# import json # duplicate Mongo
import os
import logging


# TODO: https://www.youtube.com/watch?v=rE_bJl2GAY8
# TODO: https://account.mongodb.com/account/login
###     Connection to MongoDB
class OptionMongoDb():
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

    def insert(self, data):
        self.collection.insert_one(
            data
        )

###     Connection to a local storage
class OptionLocalStorage():
    def __init__(self):
        self.path = "./local/user_records.json"
        self.startupCheck()

    def startupCheck(self):
        # check if file exists
        if os.access(self.path, os.R_OK):
            logging.info("  startupCheck: File exists")
        else:
            with open(self.path, "w") as file:
                structure = []
                json.dump(structure, file)
            logging.warning("   startupCheck: user_records.json was created")

    def search_user(self, user_id, data):
        # returns matching dictionary
        return [element for element in data if element['id'] == user_id]
    
    def add_entry(self, data):

        user = data[0]
        record = data[1]

        try: 
            with open(self.path, "r+") as file:
                json_file = json.load(file)
                file.seek(0)

                # search for user
                element = self.search_user(user["id"], json_file)

                # add new user
                if element == []:
                    # add record to user element
                    user["records"] = [record]
                    # add new user
                    json_file.append(user)
                # add new record entry 
                else: 
                    element[0]["records"].append(record)

                file.truncate()
                json.dump(json_file, file)
            print(" Info: New entry was added to user_records.json") 
        except RuntimeError:
            print("     Error: \n Could not add entry.")

###     Create Entries
#FIXME: Refactoring add Entry class 
class Operations():
    def __init__(self):
        self.mongo_storage = self.storage_config()
        self.current_user =  self.get_user()
        self.mappings = self.get_mapping()
        self.option = self.get_app_options()

    # check if mongoDB or local storage should be user
    def storage_config(self):
        with open("./mongo/configurations.json") as file:
            parsed = json.load(file)
            mongo_db_status = parsed["activated"]
        return mongo_db_status
    
    def get_use_mongo_status(self):
        return self.mongo_storage

    # check for current user
    def get_user(self):
        with open("./config/user_identity.json") as file:
            current_user = json.load(file)
        return current_user

    def set_user(self, data):
        with open("./config/user_identity.json", "w") as file:
            json.dump(data, file)

    def get_mapping(self):
        with open("./config/mappings.json") as file:
            mapping = json.load(file)
        return mapping

    def get_app_options(self):
        with open("./config/options.json") as file:
            options = json.load(file)
        return options

    def set_app_options(self):
        # TODO
        pass
        

    ################ Adding Entries
        
    def add_entry_mongo(self, record_input):
        # FIXME: Find a proper data model for mongodb
        # maybe going for referncing instead of embedded?
        #https://www.youtube.com/watch?v=4rhKKFbbYT4
        #  record = record_input
        # user = self.current_user
        # entry = {
        #     [user, record]
        # }
        # OptionMongoDb().insert(entry)
        pass

    def add_entry_local(self, record_input):
        record = record_input
        user = self.current_user
        OptionLocalStorage().add_entry([user, record])


###     Boulder Grades
class Grades():
    def __init__(self):
        # mapping based on this =>
            # https://www.bergzeit.de/magazin/bouldern-schwierigkeitsgrade-tabelle-umrechnung/
        self.scale_mapping = self.get_mapping()
        self.scale_type = self.scale_mapping["name"]
        self.grades = self.scale_mapping["grade"]

    def get_mapping(self):
        return Operations().get_mapping()["scale_type"]

    def set_scale_standard(self):
        # TODO => calls up local/options and changes this variable
        # expects an integer from 0 till 2
        
        pass

    def convert_grade(self, input_grade, output_scale):
        #TODO Scale type is from __init__
        pass

    #TODO OBSOLETE IN FUTURE?
    def set_route_grade(self, index):
        scale = Operations().get_app_options()["standard_scale"]
        current_grade = self.scale_mapping["grade"][index][scale]
        return current_grade

###     Boulder Completion Types
class CompletionType():
    def __init__(self):
        self.type = self.get_mapping()

    def get_mapping(self):
        return Operations().get_mapping()["completion_type"]

    def set_completion_type(self, index):
        return self.type[index]


class ConsoleInput():
    pass
    # def console(self):
    #     print("##################################\n")
    #     print("Allright, i need some information\n")
    #     print("Please tell the grade:\n") 
    #     print("TODO: FROM 0 TILL 21")

    #     input_grade = int(input())
    #     print("\nPlease tell me the type\n")
    #     print("(0) flash, (1) on-sight, (2) rotpunkt or (3) an unsuccesful try")
    #     input_type = int(input())
        
    #     ### local entry

    #     # entry_data = self.add_entry(input_grade, input_type)

    #     print(entry_data)

    # def form_entry(self, data):
    #     # information about user: currently static => TODO
       
    #     ## entry information
    #     record = {
    #         "timetamp" : data[0],
    #         "scale" : data[1],
    #         "grade" : data[2],
    #         "completion_type" : data[3],   
    #     }

    #     return [user, record]

    # def form_record(self, input_grade, input_type):
        
    #     # TODO: user data has to be added as well?!

    #     grade = Grades().set_route_grade(input_grade)
    #     completion_type = CompletionType().set_completion_type(input_type)
    #     timestamp = datetime.datetime.now().timestamp()
    #     scale = Grades().get_standard()
        
    #     record = [timestamp, scale, grade, completion_type]

    #     data = self.form_entry(record)

    #     # add to local record
    #     #FIXME => there is still a local entry which will be added. it should be neutral
    #         #local_record.Entries().add_entry(data)
    #     return data