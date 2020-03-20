import json
import os
import logging

class Entries():
    def __init__(self):
        self.path = "./local/user_data.json"
        self.startupCheck()

    def startupCheck(self):
        # check if file exists
        if os.access(self.path, os.R_OK):
            logging.info("  startupCheck: File exists")
        else:
            #TODO: create a new document
            with open(self.path, "w") as file:
                structure = []
                json.dump(structure, file)
            logging.warning("   startupCheck: user_data.json was created")

    def search_user(self, user_id, data):
        # returns matching dictionary
        return [element for element in data if element['id'] == user_id]
    
    def add_entry(self, data):

        user = data[0]
        record = data[1]

        with open(self.path, "r+") as file:
            json_file = json.load(file)
            file.seek(0)

            # search for
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
            print(" Info: New entry was added to user_data.json")

