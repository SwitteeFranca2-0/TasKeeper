# TasKeeper
Taskeeper is a task management software cureently available as a console software.

The Authors of this projects are:
- Franca Chigoziem Uvere
- Precious Jacob Chiemeze
- OlaTomiwa OluwaNifemi Atoro-Tywo


## TasKeeper - *Console*
The console is used to create tasks and view them at the moment. It basically a test of the software in view.
The console makes use of a filestorage going by the name **tasks.json**. 

### Usage
The console is used in the terminal. To prevent any file errors, altering the *tasks.json* is discouraged unless you have technical kow-how on JSON files. Any **task.json** file had contained on the system prior to the first use of this console is advised to be removed or renamed. It is also advisable to run the **console.py** script in the **Taskeeper directory** to prevent any File I/O errors. 

Open the terminal and *cd* to the Taskeeper directory.

That is, on the terminal:

> `$ cd {path}/TasKeeper`

To run the script:

> `$ ./console.py`

You should see the following tet if the script was run successfully,

> `Welcome to Task-keeper`

> `Type in "help" or "classes" for better understanding of the program`

> `(taskeeper)`

To know the command present:

> `(taskeeper) help`

> ` `

> `Documented commands (type help <topic>):`

> `****************************************`

> `EOF  all  classes  create  destroy  quit  show  update`

> `'`

> `Undocumented commands:`

> `**********************`

> `help`

To understand each commands, type in **help {command}**

> `(taskeeper) help all`

> `USAGE: all <task class(optional)>`

The tasks are saved by their 'classes'. To get the **classes** of tasks

> `(taskeeper) classes`
