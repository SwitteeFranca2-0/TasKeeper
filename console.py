#!/usr/bin/python3
"""console fo rthe tas keeper using the cmd classs"""
import cmd
from models.home import Home
from models.school import School
from models.outdoor import Outdoor
from models.work import Work
from models.BaseModel import Task
from models import storage

class TaskKeeper(cmd.Cmd):
    """cmd class for the task keeper"""
    prompt = '(taskeeper) '
    ruler = '*'
    classes = {
        'Task': Task, 'Home': Home, 'Outdoor': Outdoor,
        'School': School, 'Work': Work
    }

    intro = 'Welcome to Task-keeper.\nType in "help" or "classes" for better understanding of the program'

    def do_EOF(self, line):
        """Implement end of file"""
        return True
    
    def emptyline(self):
        pass 

    
    def do_classes(self, line):
        """
            There are 5 classes of tasks in this app. They are:
            -> Task: This can be used when the user doesn't feel the nedd to classify the task being inputed.
            -> Home 
            -> Outdoor 
            -> School 
            -> Work
            Create your tasks based on any of the five above
        """
        return super().do_help('classes')
    #create a function that lists the classes of tasks. This function is basically a commentary, returning the do help function


    def default(self, line: str):
        print('Please, input a valid command')
        line = ""
        return cmd.Cmd.do_help(self, line)
        
    def do_help(self, arg: str):
        return super().do_help(arg)
    
    def do_quit(self, line):
        """quit the application"""
        ans = input('Are you sure?<yes/no, y/n> ')
        if ans not in ['yes', 'no', 'y', 'n']:
            print('Please, input yes or no or y or n')
        else:
            if ans == 'yes' or ans == 'y':
                print('Okay, bye!')
                exit()
            else:
                pass
    def parseLine(self, line: str):
        args = line.split(" ")
        return args

    def do_create(self, line):
        """USAGE: create <name of class:
                            [Work, Outdoor, Home, School, or Task]> <name of task> <status(optional)>"""
        
        args = self.parseLine(line)
        if not args:
            print('***Task name missing')
            return super().do_help('create')
        if args[0] not in TaskKeeper.classes.keys():
            print('***Invalid Task class\n')
            return super().do_help('create')
        if len(args) < 2:
            print('***Task name missing\n')
            return super().do_help('create')
        if len(args) > 2:
            try:
                obj = TaskKeeper.classes[args[0]](args[1], args[2])
                obj.save()
                print(obj)
            except ValueError:
                print('***Status should be either 0 or 1') #fix this part of code
        else:
            obj = TaskKeeper.classes[args[0]](args[1])
            obj.save()
            print(obj)
    
    def do_destroy(self, line):
        """Usage: Destroy <Task Class> <Task ID>"""
        args = self.parseLine(line)
        if not args:
            print('***Task name missing')
            return super().do_help('destroy')
        if args[0] not in TaskKeeper.classes.keys():
            print('***Invalid Task class\n')
            return super().do_help('destroy')
        if len(args) < 2:
            print('***Task ID missing\n')
            return super().do_help('destroy')
        objs = storage.all(TaskKeeper.classes[args[0]])
        key = args[0] + "." + args[1] 
        try:
            storage.delete(objs[key])
        except KeyError:
            print("ID not found")
    
    def do_all(self, line):
        """USAGE: all <task class(optional)>"""
        objs = storage.all().values()
        if line:
            if line in TaskKeeper.classes.keys():
                objs = storage.all(TaskKeeper.classes[line]).values()
            else:
                print('***class not found')
                line = ""
                return cmd.Cmd.do_help(self, line)
        id = 0
        for obj in objs:
            print(id, obj)
            id +=1
    
    def do_show(self, line):
        """USAGE: show <class> <id> """
        args = line.split(" ")
        if not line:
            print('***class is missing')
        if len(args) < 2:
            print('***Id missing')
        else:
            objs = storage.all(TaskKeeper.classes[args[0]])
            key = args[0] + "." + args[1]
            if key in objs.keys():
                print(objs[key])
            else:
                print("***Task not found")
    
    def do_update(self, line):
        """USAGE: update <class> <id>"""  
        args = line.split(" ")
        if not line:
            print('***class is missing')
        if len(args) < 2:
            print('***Id missing')
        else:
            objs = storage.all(TaskKeeper.classes[args[0]])
            key = args[0] + "." + args[1]
            if key in objs.keys():
                obj = objs[key]
                print(obj)
                c = input('update name or status, or both? ')
                if c.lower() == 'name':
                    obj.name = input('Name of task (use undercores instead of spaces): ').replace("_", " ")
                if c.lower() == 'status':
                    obj.status = input('Status of task: 1 or 0? ')
                if c.lower() == 'both':
                    obj.name = input('Name of task (use undercores instead of spaces): ').replace("_", " ")
                    obj.status = input('Status of task: 1 or 0? ')
                storage.save()
                print(obj)
            else:
                print("***Task not found")

if __name__ == '__main__':
    TaskKeeper().cmdloop()