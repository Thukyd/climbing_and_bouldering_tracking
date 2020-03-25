#############################################
############       Boulder Tracker
############            V 0.1
############        @Thukyd, 2020
#############################################



import datetime
import time
import logging

# Needed for MongoDB
import json
import pymongo
from pymongo import MongoClient

# Needed for local JSON
# import json
import os
import logging

######### 
# Storage Option A: MongoDB Cloud
class OptionMongoDb():
    def __init__(self):
        self.collection = self.config()

    # sets up MongoDB connection
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

    # inserts records & user into DB
    def insert(self, data):
        self.collection.insert_one(
            data
        )

    # updates "user" documents with new "record" array 
    def add_record(self, user_id, record):
        self.collection.update_one({
            "_id" : user_id
        },
        {
            "$push" : {"records": record}
        })

    # checks if there is already an entry for this user
    def check_user_existance(self, user_id):
        # returns "find" returns mongo object that needs => needs to be handled in loops
        if self.collection.find({"_id" : user_id}).count() > 0: 
            return True
        else:
            return False

######### 
# Storage Option B: JSON in Local Folder
class OptionLocalStorage():
    def __init__(self):
        self.path = "./local/user_records.json"
        self.startupCheck()

    # check if file exists
    def startupCheck(self):
        # check if file exists
        if os.access(self.path, os.R_OK):
            logging.info("  startupCheck: File exists")
        else:
            with open(self.path, "w") as file:
                structure = []
                json.dump(structure, file)
            logging.warning("   startupCheck: user_records.json was created")

    # searches for user id
    def search_user(self, user_id, data):
        # returns matching dictionary
        return [element for element in data if element['_id'] == user_id]
    
    # adds a new user entry
    def insert(self, data):
        user = data[0]
        record = data[1]
        try: 
            with open(self.path, "r+") as file:
                json_file = json.load(file)
                file.seek(0)

                # search for user
                element = self.search_user(user["_id"], json_file)

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

######### 
# Basic Operations
class Operations():
    def __init__(self):
        self.mongo_storage = self.get_app_options()["mongo_db_activated"]
        self.option = self.get_app_options()["standard_scale"]
        self.current_user =  self.get_user()
        self.mappings = self.get_mapping()

     # return which scale type is used currently
    def get_app_options(self):
        with open("./config/options.json") as file:
            options = json.load(file)
        return options
    
    # checks if mongoDB is activated in options; otherwise the local storage is active
    def get_use_mongo_status(self):
        return self.mongo_storage

    # returns current user from config json
    def get_user(self):
        with open("./config/user_identity.json") as file:
            current_user = json.load(file)
        return current_user

    # sets a new user in config json
    def set_user(self, data):
        with open("./config/user_identity.json", "w") as file:
            json.dump(data, file)

    # returns scale type and competion type mapping
    def get_mapping(self):
        with open("./config/mappings.json") as file:
            mapping = json.load(file)
        return mapping

    # adds an entry in mongoDB    
    def add_entry_mongo(self, record_input):
        record = record_input
        user = self.current_user

        #TODO: THIS LOGIC BELLOW IS PART OF MONGODB OPERATIONS => 
        # cut & paste part bellow into OptionMongoDB, similar to add_entry_local
        # existing user? => add record
        if OptionMongoDb().check_user_existance(user["_id"]): 
            entry = record
            OptionMongoDb().add_record(user["_id"], record)
        # new user? => create user + record
        else:
            entry = user
            entry["records"] = [record]
            OptionMongoDb().insert(entry)

    # adds an entry in local folder  
    def add_entry_local(self, record_input):
        record = record_input
        user = self.current_user
        OptionLocalStorage().insert([user, record])

######### 
# Boulder Grades/Scale
class Grades():
    def __init__(self):
        # mapping based on this =>
            # https://www.bergzeit.de/magazin/bouldern-schwierigkeitsgrade-tabelle-umrechnung/
        self.scale_mapping = self.get_mapping()
        self.scale_type = self.scale_mapping["name"]
        self.grades = self.scale_mapping["grade"]

    # returns scale type mapping
    def get_mapping(self):
        return Operations().get_mapping()["scale_type"]

    # sets new scale type standard in options.json
    def set_scale_standard(self):
        # TODO => calls up local/options and changes this variable
        # expects an integer from 0 till 2
        pass

    # converts input into a scale
    def convert_grade(self, input_grade, output_scale):
        #TODO Scale type is from __init__
        pass

######### 
# Completion Types
class CompletionType():
    def __init__(self):
        self.type = self.get_mapping()

    # returns index mapping of completion types in mappings.json
    def get_mapping(self):
        return Operations().get_mapping()["completion_type"]

    # sets completion type based on mappings.json
    def set_completion_type(self, index):
        return self.type[index]