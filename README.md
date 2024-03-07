AIRBNB CLONE (THE CONSOLE)
===============================

AirBnB Command Line Interface
------------------------------
Project Description
-----------------------
This project is a command-line interface (CLI) for managing AirBnB objects. 
It provides a set of commands to create, retrieve, update, and delete instances of various objects, such as users and places, within the AirBnB ecosystem.

Command Interpreter Description
The command interpreter, implemented in console.py, allows users to interact with the AirBnB objects using a set of commands. 
The available commands include:

quit/EOF: Exit the program.
help: Display help information.
create: Create a new instance of a specified class, save it, and print the unique identifier.
show: Print the string representation of an instance based on the class name and id.
destroy: Delete an instance based on the class name and id.
all: Print string representations of all instances based on the class name.
update: Update an instance based on the class name and id by adding or updating attributes


How to Use the console
==================================

.create: Create a new instance of a class.
(hbnb) create BaseModel

.show: Display the string representation of an instance.
(hbnb) show BaseModel 1234-1234-1234

.destroy: Delete an instance based on the class name and id.
(hbnb) destroy BaseModel 1234-1234-1234

.all: Print string representations of all instances
(hbnb) all BaseModel

.update: Update an instance's attributes.
(hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"

quit/EOF: Exit the program.
(hbnb) quit


AUTHORS
========
Leeon Kariuki Kamuti <kamutileeon@gmail.com>

