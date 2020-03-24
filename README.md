# Climbing and Bouldering Tracking
Keep track of your boulder routes.

## Features 0.1
- 3 different scale types ("Fontainebleau-bloc", "Fontainebleau-trav", "Vermin-Scale")
- 4 dfifferent completion types ("Flash", "On-Sight", "Rotpunkt", "try" an unsuccessful attempt)
- choice between storage in local json or cloud mongodb


## Tasks (version 0.1):
- [x] grade & completion type mappings
- [x] local storage
- [x] connection to mongo
- [x] option a: input via script with mongodb 
- [x] option b: input via script with local storage
- [ ] set new standard scale type & convert scale types => **currently on hold**
- [ ] full test via script
- [ ] => update documentation in Github


# Next steps for version 0.2?
- [ ] add operations: update / delete records; update / delete user information; set new user?
- [ ] online/offline sync?
- [ ] web(pwa) integration? chatbot/voicebot integration?


# How to configure version 0.1?


## Setup Storage (MongoDB or Local)
TDB


## Setup of MongoDB
TDB


## Set Standard Scale Type
The scale type is defined in the config/options.json. Standard is "Fontainebleau-bloc".
```python
{
    "standard_scale" : "0"
}
```
It references to the array in config/mappings.json
```python
...
  "scale_type": {
        "name": [
            "fb-bloc",
            "fb-trav",
            "v-scale"
        ],
 ...
```

## Change Current User
TDB
