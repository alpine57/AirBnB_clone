#!/usr/bin/python3

import cmd
import re
from models import storage

class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def default(self, line):
        """Catch commands if nothing else matches then."""
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_EOF(self, line):
        """Handles End Of File character."""
        print()
        return True

    def do_quit(self, line):
        """Exits the program."""
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass

    def do_create(self, line):
        """Creates an instance."""
        if not line:
            print("** class name missing **")
            return

        classname = line.split()[0]
        if classname not in storage.classes():
            print("** class doesn't exist **")
            return

        new_instance = storage.classes()[classname]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance."""
        if not line:
            print("** class name missing **")
            return

        words = line.split()
        if len(words) < 2:
            print("** instance id missing **")
            return

        classname = words[0]
        instance_id = words[1]

        if classname not in storage.classes():
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(classname, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        if not line:
            print("** class name missing **")
            return

        words = line.split()
        if len(words) < 2:
            print("** instance id missing **")
            return

        classname = words[0]
        instance_id = words[1]

        if classname not in storage.classes():
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(classname, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances."""
        if line:
            classname = line.split()[0]
            if classname not in storage.classes():
                print("** class doesn't exist **")
                return

            instances = [str(obj) for obj in storage.all().values() if isinstance(obj, storage.classes()[classname])]
            print(instances)
        else:
            instances = [str(obj) for obj in storage.all().values()]
            print(instances)

    def do_update(self, line):
        """Updates an instance by adding or updating attribute."""
        if not line:
            print("** class name missing **")
            return

        words = line.split()
        if len(words) < 2:
            print("** instance id missing **")
            return

        classname = words[0]
        instance_id = words[1]

        if classname not in storage.classes():
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(classname, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(words) < 3:
            print("** attribute name missing **")
            return

        if len(words) < 4:
            print("** value missing **")
            return

        attribute = words[2]
        value = words[3]

        instance = storage.all()[key]
        setattr(instance, attribute, value)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

