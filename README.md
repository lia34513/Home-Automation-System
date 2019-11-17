# Parity_Home_Automation

This repository contains the code required to setup the data models for a home automation system.
It is built using Django (Python-based API framework as the back-end), SQLite3 (persistent storage), and Python3.

# Local Installation

- Install Python3 and Django
- Setup the SQLite3: `python3 manage.py makemigrations`, `python3 manage.py migrate'
- Run the Server: `python3 manage.py runserver`
- Input `http://127.0.0.1:8000/`+API in the Browser or Use Postman with `GET` commend becuase address contains all input

# Database

- Table: home_automation
    - Fields: 
        - id: Integer, Primary key
        - roomtype: String, Not Null
        - light_status: Integer, Values: `0` is off and `1` is on
        - temperature_degree: Float
        - thermostat_status: String, Values: `off`, `cool`, `heat`, `fan-on`, `auto`
# API End Points

- `admin/initial`
    - Create initial rooms into home_automation(database)
    - Add three rooms with their roomtypes(`bedroom`, `livingroom`, `bathroom`) and unique id
    - Set light_status, temperature_degree, thermostat_status to Null
    - Output: json file
        - Wrong Message or Success Message with list of database
        
    
- `admin/addroom?roomtype=X&lightstatus=Y&temperature=Z&thermostatstatus=M`

    - Create your own room, assign new unique id to the room
    - Provide value for `roomtype`
    - `lightstatus`,`temperature`,`thermostatstatus` optional to set a value
    - URL examples: 
        - `admin/addroom?roomtype=kitchen`
        - `admin/addroom?roomtype=garage&lightstatus=1&temperature=20&thermostatstatus=off`
        - `admin/addroom?roomtype=bedroom&lightstatus=0`
    - Output: json file
        - Wrong Message or Success Message with list of database
        
- `admin/clear`
    - Delete all data in the home_automation table
    - Output: json file
        - Success Message with list of database
        
- `admin/list`
    - Show all data in the home_automation table
    - Output: json file
        - list of database
    
- `admin/light?id=X&value=Y`
    - Change the light status for the room with id
    - `id` must exist in the home_automation table
    - `value` must be `0` or `1`
    - URL examples:
        - `admin/light?id=1&value=0`
    - Output: json file
        - Wrong Message or Success Message with list of database

- `admin/temperature?id=X&value=Y`
    - Change the temperature degree for the room with id
    - `id` must exist in the home_automation table
    - `value` must be a number
    - URL examples:
        - `admin/temperature?id=1&value=20`
    - Output: json file
        - Wrong Message or Success Message with list of database

- `admin/thermostat?id=X&value=Y`
    - Change the thermostat status for the room with id
    - `id` must exist in the home_automation table
    - `value` must be `off`, `cool`, `heat`, `fan-on` or `auto`
    - URL examples:
        - `admin/thermostat?id=1&value=heat`
    - Output: json file
        - Wrong Message or Success Message with list of database
        
   
