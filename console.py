#!/usr/bin/env python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User  # Import the User class

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User"]  # Include User class in valid classes

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def help_quit(self):
        print("Exit the program")

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        return True

    def help_EOF(self):
        print("Exit the program")

    def do_create(self, arg):
        """Creates a new instance of a class, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        try:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        try:
            obj = storage.get(class_name, obj_id)
            print(obj)
        except Exception as e:
            print("**", e)

    def do_destroy(self, arg):
        """Deletes an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        try:
            obj = storage.get(class_name, obj_id)
            obj.delete()
            storage.save()
        except Exception as e:
            print("**", e)

    def do_all(self, arg):
        """Prints all instances"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        objs = storage.all(class_name)
        print([str(obj) for obj in objs.values()])

    def do_update(self, arg):
        """Updates an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        try:
            obj = storage.get(class_name, obj_id)
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            setattr(obj, attr_name, attr_value)
            storage.save()
        except Exception as e:
            print("**", e)

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        count = len(storage.all(class_name))
        print(count)

    def do_all_instances(self, arg):
        """Prints all instances of a class"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        objs = storage.all(class_name)
        print([str(obj) for obj in objs.values()])

if __name__ == '__main__':
    HBNBCommand().cmdloop()

