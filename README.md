# TasKeeper
Taskeeper is a task management software cureently available as a console software.

To view the Taskeeper website, please click [here](https://switteefranca2-0.github.io/)

The Authors of this project are:
- Franca Chigoziem Uvere
- Precious Jacob Chiemeze
- OlaTomiwa OluwaNifemi Atoro-Tywo


## TasKeeper - *Console*
The console is used to create tasks and view them at the moment. It basically a test of the software in view.
The console makes use of a filestorage going by the name **tasks.json**. 

### Usage
The console is used in the terminal. To prevent any file errors, altering the *tasks.json* is discouraged unless you have technical kow-how on JSON files. Any **task.json** file had contained on the system prior to the first use of this console is advised to be removed or renamed. It is also advisable to run the **console.py** script in the **Taskeeper directory** to prevent any File I/O errors. 

> Open the terminal and *cd* to the Taskeeper directory.

> That is, on the terminal:

 `$ cd {path}/TasKeeper`

> To run the script:

`$ ./console.py`

> You should see the following tet if the script was run successfully,

`Welcome to Task-keeper`

`Type in "help" or "classes" for better understanding of the program`

`(taskeeper)`

> To know the command present:

`(taskeeper) help`

` `

`Documented commands (type help <topic>):`

`****************************************`

`EOF  all  classes  create  destroy  quit  show  update`

`'`

`Undocumented commands:`

`**********************`

`help`

`(taskeeper)`
> To understand each commands, type in **help {command}**

`(taskeeper) help all`

`USAGE: all <task class(optional)>`

`(taskeeper)`

> The tasks are saved by their 'classes'. To get the **classes** of tasks

`(taskeeper) classes`
 
`There are 5 classes of tasks in this app. They are:` 

` -> Task: This can be used when the user doesn't feel the nedd to classify the task being inputed. `

` -> Home`

`-> Outdoor`

`-> School`

`-> Work`

`-> Create your tasks based on any of the five above`

`(taskeeper)`

> To create a task without a class(Please, use unserscores as spaces):

`(taskeeper) create Task Wash_Plate`


`[Task].`


`.......Name of task: Wash_Plate`

`.......Id: aa5df980-bb5a-11ed-b07b-00155d3a7fc6`
       
`.......Status: 0`

`.......Time Created: Day: 7 of Week: 9 of Year: 2023`

`(taskeeper)`

> The **status: 0** means ths task has not been completed. You can create a task with status too. Status should be either 1 or 0. **status: 1** means task has been completed.

> To create a 'Work' task with a status of 1:

`(taskeeper) create Work Read_Contract 1`

`[Work].`
 
 `.......Name of task: Read Contract`
 
 `.......Id: 8e294948-bb5c-11ed-b1be-00155d3a7fc6`
 
 `.......Status: 1`
 
 `.......Time Created: Day: 7 of Week: 9 of Year: 2023`
 
 `(taskeeper)`

> To view all tasks regardless of classes:

`(taskeeper) all`

`0 [Task].`

`.......Name of task: Wash_Plate`

`.......Id: aa5df980-bb5a-11ed-b07b-00155d3a7fc6`
        
`.......Status: 0`
        
`.......Time Created: Day: 7 of Week: 9 of Year: 2023`

`1 [Work].`

`.......Name of task: Read Contract`

`.......Id: 8e294948-bb5c-11ed-b1be-00155d3a7fc6`

`.......Status: 1`

`.......Time Created: Day: 7 of Week: 9 of Year: 2023`

`(taskeeper)`

> To view tasks of a particular class:

`(taskeeper) all Work`

`0 [Work].`

`.......Name of task: Read Contract`

`.......Id: 8e294948-bb5c-11ed-b1be-00155d3a7fc6`

`.......Status: 1`

`.......Time Created: Day: 7 of Week: 9 of Year: 2023`

`(taskeeper)`

> To update a task, get it's **id**:

`(taskeeper) update Work 8e294948-bb5c-11ed-b1be-00155d3a7fc6`

`[Work].`

`.......Name of task: Read Contract`

`.......Id: 8e294948-bb5c-11ed-b1be-00155d3a7fc6`

`.......Status: 1`

`.......Time Created: Day: 7 of Week: 9 of Year: 2023`

`update name or status, or both? `

> Let's update both information, i.e, both name and status of the task

`update name or status, or both? both`

`Name of task (use undercores instead of spaces): Sign_contract`

`Status of task: 1 or 0? 1`

`[Work].`

`.......Name of task: Sign contract`

`.......Id: 8e294948-bb5c-11ed-b1be-00155d3a7fc6`

`.......Status: 1`
        
`.......Time Created: Day: 7 of Week: 9 of Year: 2023`

`(taskeeper)`

> To delete a task, get the task's class and the task's id:

`(taskeeper) destroy Work 8e294948-bb5c-11ed-b1be-00155d3a7fc6`

`(taskeeper) `

> The task has been deleted.
> If any information id not imputed correctly, an error message is shown. For instance, deleting a task that doesn't exist.

`(taskeeper) destroy Work  8e294948`

`ID not found`

`(taskeeper) `

> or creating a task with a class that doesn't exist.

`(taskeeper) create Done Clean`

`***Invalid Task class`

`USAGE: create <name of class:`
                            `[Work, Outdoor, Home, School, or Task]> <name of task> <status(optional)>`

`(taskeeper) `

> To quit the program, use **ctrl + c** or:


`(taskeeper) quit`

`Are you sure?<yes/no, y/n> yes`

`Okay, bye!`

`$`

This is a break down of how to use taskeeper on the terminal. The development of the web_flask to make use of database storage is ongoing.

To view the Taskeeper website, please click [here](https://switteefranca2-0.github.io/)
# Thank You!