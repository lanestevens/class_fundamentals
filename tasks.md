## Introduction
A common requirement in data processing is moving data between disparate systems.  A pattern that evolved to address this
type of requirement is a three-step process:  Extract, Transform, and Load, or more commonly referred to by the acronym _ETL_.
In the extract step, data are retrieved from the source system.  In the transform step the data are reformatted or
modified in other ways in order to be compatible with the target system. The load step involves pushing the data into the target
system.

Python is well suited to all of these steps, but to make the most effective use of Python in this or to solve other complex
problems demands the effective use of the features and modules that are suited to the task at hand, and to pay attention to
the design of the system and the overall architecture into which it fits.

In this project, we will focus on the transform step of an ETL process.  You will build a Python _Class_ that will be used
to transform a source row from a CSV (comma-separated values format) file into a reformatted row for a target CSV file.  This
context and the supporting requirements will provide opportunities to better learn some fundamental features of the Python
language and software development techniques.
## Learning Objectives
  * Python Class construction and usage
  * Python Class initialization
  * Exceptions
  * String formatting
  * Application design
  * Refactoring
## Setup
## Tasks
### Task 1 - Create a Class
#### Step 1 - Create a file
#### Step 2 - Create an empty class
### Task 2 - Instance Initialization
#### Step 1 - Override initialization method
#### Step 2 - Check parameter type
#### Step 3 - Initialize state
### Task 3 - Validation
#### Step 1 - Create a validator method
#### Step 2 - Call the validator method from the initialization method
### Task 4 - Formatters
#### Step 1 - Default Formatter
#### Step 2 - US Currency Formatter
#### Step 3 - US Currency with thousands separators formatter
#### Step 4 - Integer formatter
#### Step 5 - Integer with thousands separator formatter
### Task 5 - The Main Event
#### Step 1 - Main formatter method
### Task 6 - Refactor
#### Step 1 - Refactor the validation method to be dynamic
