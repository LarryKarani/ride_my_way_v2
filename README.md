

[![Coverage Status](https://coveralls.io/repos/github/larryTheGeek/ride_my_way_v2/badge.svg?branch=master)](https://coveralls.io/github/larryTheGeek/ride_my_way_v2?branch=master)

Ride-my App is a carpooling application that provides drivers with the ability to create ride oﬀers and passengers to join the available ride oﬀers.

**Getting Started**

1. Clone the repository to your machine; *https://github.com/LarryTheGeek/ride_my_way_v2.git
2. Open the repo with an IDE of your choice as a project.

**Prerequisites**

_ Python 3
_ Virtual environment.
_ Flask
_ flask rest-plus
_ Postman
- Browser of your choice

**Setup**

1. Open cmd. In the root directory folder;
2. Run the command: virtualenv venv -p python3.6, to create a virtual 
3. environment with the name venv. Folder with the name venv will created. 

**windows**

_ Activate the virtual environment by moving to the Script directory i.e. cd venv\Scripts, and running 
activate.

**linux and mac**

 _ Activate the virtual environment by running the command: source /venv/bin/activate
 
**Application Requirements**


_ The application requirements are clearly listed in the requirents.txt document.
_ To install them run the following cmd command:
_ pip install -r requirements.txt

**End-Points**


_ GET	api/v1/rides	Get all Rides

_ GET	api/vi/rides/{ride_id}	Get a specific ride

_ DELETE	api/v1/rides/{ride_id}	Delete ride

_ POST	api/v1//rides	Add a ride

_ POST	api/v1/rides/{ride_id}/requests	Request to join a ride

_ PUT	api/v1/rides/{ride_id}	Edit ride details

_ POST	api/v1/users	Register users

_ POST	api/v1/users	Get all users

_ DELETE	api/v1/users/{username}	Delete a user

The above endpoints can be tested by Postman.

**Running Of Tests**

Running of tests can be done by using pytest and unittest. run

**Version Control**

_This was done by GitHub

**Github link**

https://github.com/larryTheGeek/ride_my_way_v2

Heroku
...

**Author**

Larry Karani

**License**

This project is licensed under the MIT License
