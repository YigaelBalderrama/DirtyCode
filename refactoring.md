### Aclaration
It is recommended to check each refactoring looking at the commit where a refactoring ocurred and checking the code smell lines in a previous version from the refectoring commit. This is to avoid confusion as some code may change it's lines from version to version because of the refactoring.

### Code smell #1
* Smell:  "Naming matters"
* * Lines: 19, 20, 28, 34 & 38

* Refactoring: Changed the "iter" variable name to "menu_selection" to make it easy to understand.
* Lines: 19, 20, 28, 34 & 38

### Code smell #2
* Smell: "Naming matters". "t" is a bad name for the variable that saves the user text.
* * Lines: 16, 27 & 32

* Refactoring: Changed the "t" variable name to "user_text" to make it easy to understand.
* * Lines: 16, 27 & 32

### Code smell #3
* Smell: "Naming matters". "line" is a bad name for the variable that saves each console line content.
* * Lines: 23, 24 & 26

* Refactoring: Changed the "line" variable name to "console_line" to make it easy to understand.
* * Lines: 23, 24 & 26

### Code smell #4
* Smell: "Naming matters". "n" is a bad name for the variable that saves the txt file name.
* * Lines: 30, 31, 36 & 37

* Refactoring: Changed the "n" variable name to "file_name" to make it easy to understand.
* * Lines: 30, 31, 36 & 37

### Code smell #5
* Smell: "Big Method". The main() function is carrying al tasks
* * Lines: 31 to 37

* Refactoring: As a first step I moved all the code from the first IF statement into another function
* * Lines: Function call on line 37  |  Actual Method in lines 14 to 22

### Code smell #6
* Smell: "Big Method". The main() function is carrying al tasks
* * Lines: 33 to 37

* Refactoring: Continuing refactoring the main() code smell. I moved all the code from the second IF statement into another function
* * Lines: Function call on line 40  |  Actual Method in lines 24 to 30