#!/usr/bin/env python3
"""Module for HBNB command interpreter"""
import cmd
import importlib
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB project"""
    
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def update_valid_classes(self):
        """Update the list of valid classes dynamically"""
        module_names = storage.get_all_classes()
        self.valid_classes = [name for name in module_names]

    def do_create(self, arg):
        """Create a new instance, save it, and print the id"""
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.valid_classes:
            self.update_valid_classes()
            if arg not in self.valid_classes:
                print("** class doesn't exist **")
                return

        try:
            new_instance = eval(f"{arg}()")
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            self.update_valid_classes()
            if args[0] not in self.valid_classes:
                print("** class doesn't exist **")
                return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            print(objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            self.update_valid_classes()
            if args[0] not in self.valid_classes:
                print("** class doesn't exist **")
                return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            del objects[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        objects = storage.all()

        if not args:
            print([str(objects[key]) for key in objects])
            return

        if args[0] not in self.valid_classes:
            self.update_valid_classes()
            if args[0] not in self.valid_classes:
                print("** class doesn't exist **")
                return

        print([str(objects[key]) for key in objects if key.split('.')[0] == args[0]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            self.update_valid_classes()
            if args[0] not in self.valid_classes:
                print("** class doesn't exist **")
                return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        instance = objects[key]
        attribute_name = args[2]
        attribute_value = args[3]

        try:
            """Casting attribute value to the attribute type"""
            attribute_type = type(getattr(instance, attribute_name))
            casted_value = attribute_type(attribute_value)

            """Updating the attribute"""
            setattr(instance, attribute_name, casted_value)
            instance.save()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

