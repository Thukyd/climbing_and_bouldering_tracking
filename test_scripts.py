import local_record

############### TEST LOCAL RECORD ##############
# import datetime

# test_user_a = {
#     "id" : "123456789",
#     "surname" : "Mustermann",
#     "forename" : "Max"
# }
# test_user_b = {
#     "id" : "987654321",
#     "surname" : "Doe",
#     "forename" : "Jane"
# }
# ## entry information
# test_record_a = {
#     "timetamp" : datetime.datetime.now().timestamp(),
#     "grade" : "5+",
#     "completion_type" : "on-sight",
#     "scale" : 0
# }

# test_record_b = {
#     "timetamp" : datetime.datetime.now().timestamp(),
#     "grade" : "5+",
#     "completion_type" : "on-sight",
#     "scale" : 0
# }

# test_user_c = {
#     "id" : "44444444",
#     "surname" : "New",
#     "forename" : "User"
# }

# local_record.Entries().add_entry([test_user_a, test_record_a]) #NEW USER
# local_record.Entries().add_entry([test_user_b, test_record_a]) #ADD RECORD
# local_record.Entries().add_entry([test_user_a, test_record_b])
# local_record.Entries().add_entry([test_user_b, test_record_b])
# local_record.Entries().add_entry([test_user_b, test_record_a])
# local_record.Entries().add_entry([test_user_c, test_record_a]) #NEW USER WITH RECORD
############### TEST LOCAL RECORD ##############

############### TEST Console Input ##############

#import main



# main.CreateEntry().ask_console()
############### TEST Console Input ##############

############### TEST Mongo ##############

import main

print(main.Mongo().receive_credentials())



############### TEST Mongo ##############