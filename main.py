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
### Design: https://www.mongodb.com/blog/post/building-with-patterns-a-summary?utm_campaign=Int_EM_ONB_FT1a_10_19_WW&utm_source=Eloqua&utm_medium=email&utm_term=Designing%20a%20MongoDB%20schema%20for%20Atlas
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

    def add_record(self, user_id, record):
        self.collection.update_one({
            "_id" : user_id
        },
        {
            "$push" : {"records": record}
        })

    def check_user_existance(self, user_id):
        # returns "find" returns mongo object that needs => needs to be handled in loops
        if self.collection.find({"_id" : user_id}).count() > 0: 
            return True
        else:
            return False

    def find_entry(self, user_id):
        return self.collection.find({"_id": user_id})

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
        return [element for element in data if element['_id'] == user_id]
    
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
        record = record_input
        user = self.current_user

        # existing user? => add record
        if OptionMongoDb().check_user_existance(user["_id"]): 
            entry = record
            OptionMongoDb().add_record(user["_id"], record)
            # TEST BEGIN
            user_id = user["_id"]
            print(f"{user_id} existiert bereits. Neuer Record hinzugefügt")
            # TEST END
        # new user? => create user + record
        else:
            entry = user
            entry["records"] = [record]
            OptionMongoDb().insert(entry)
            # TEST BEGIN
            user_id = user["_id"]
            print(f"Neue Nutzer mit der ID {user_id} angelegt")
            # TEST END

    def add_entry_local(self, record_input):
        record = record_input
        user = self.current_user
        OptionLocalStorage().insert([user, record])


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