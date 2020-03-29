User-Activities
------------------------

It gives user's information and all of their activities.

sample Output:
[
    {
        "id": "W012A3CDE",
        "real_name": "Egon Spengler",
        "tz": "America/Los_Angeles",
        "activities": [
            {
                "start_time": " February 01 2020 10:30 AM ",
                "end_time": " February 01 2020 10:54 AM "
            },
            {
                "start_time": " March 01 2020 11:11 AM ",
                "end_time": " March 01 2020 02:00 PM "
            }
        ]
    },
    {
        "id": "IHURFMNA",
        "real_name": "Valerie Ward",
        "tz": "Africa/Addis_Ababa",
        "activities": [
            {
                "start_time": " March 09 2020 04:03 PM ",
                "end_time": " March 21 2020 06:00 PM "
            }
        ]
    },

Packages 
------------------------

- Python
- Django
- Django RestFramework
- Faker module 
- fatory_boy module

Tasks and Results
----------------------
1. Design a API to serve data in JSON format.

	localhost:8000/api/members-activity
	shows all the members and their activities returned as JSON object.

2. Build a custom management command to populate the database.
	
	--> pyhthon manage.py populate [num]
	num(integer type) = number of records to be made at time. This command can be used to populate the database's.
	
	factory_boy and faker module has been used to populate data with fake instances.
	
	

