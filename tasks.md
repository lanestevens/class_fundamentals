## Introduction
A common requirement in data processing is moving data between disparate systems.  A pattern that evolved to address this
type of requirement is a three-step process:  Extract, Transform, and Load, or more commonly referred to by the acronym _ETL_.
In the extract step, data are retrieved from the source system.  In the transform step the data are reformatted or
modified in other ways in order to be compatible with the target system. The load step involves pushing the data into the target
system.

Python is well suited to each of these three data-migration steps, but to make the most effective use of Python in this or
to solve other complex problems demands the effective use of the features and modules that are suited to the task at hand, and
to pay attention to the design of the system and the overall architecture into which it fits.

In this project, we will focus on the transform step of an ETL process.  You will build a Python _class_ that will be used
to transform a source row from a CSV (comma-separated values format) file into a reformatted row for a target CSV file.  This
context and the supporting requirements will provide opportunities to better learn some fundamental features of the Python
language and software development techniques.
## Learning Objectives
  * Python class construction and usage
  * Python class initialization
  * Exceptions
  * String formatting
  * Application design
  * Refactoring
## Setup
  * Create a python 3 virtual environment
```bash
python -m venv my_project
```
  * Change to the virtual environment directory
```bash
cd my_project
```
  * Activate the virtual environment
    * Mac/Linux
```bash
source bin/activate
```
    * Windows
```bash
Scripts\activate
```
  * Clone the project repository as a child of the virtual environment directory.  So, the directory structure will be ./my_project/class_fundamentals
```bash
git clone <project url>
```
  * Change to the project repository directory
```bash
cd class_fundamentals
```
  * Install required modules
```bash
pip install -r requirements.txt
```
  * Start tests
```bash
ptw -- -x -vv
```

### Windows
  * Create a python 3 virtual environment
```bash
python -m venv my_project
```
  * Change to the virtual environment directory
```bash
cd my_project
```
  * Activate the virtual environment
```bash
Scripts\activate
```
  * Clone the project repository as a child of the virtual environment directory.  So, the directory structure will be ./my_project/class_fundamentals
```bash
git clone <project url>
```
  * Change to the project repository directory
```bash
cd class_fundamentals
```
  * Install required modules
```bash
pip install -r requirements.txt
```
  * Start tests
```bash
ptw -- -x -vv
```

## Tasks
### Task 1 - Create a Class
#### Step 1 - Create a file
The first step is to create a file named fmt.py in the src directory of your project root.  To get the failing
test to pass, it is enough to create an empty file.
#### Step 2 - Create an empty class
In this step we create an empty class in order to get the test to pass.  There are three options for specifying the class and
all three are equivalent in terms of this project.  The first pattern omits the parentheses for class inheritance.  The second
provides an empty parenthesized inheritance, and the third inherits from the _object_ class.  The default class in Python 3 is
the _object_ class, hence the three implementations achieve equivalent results.

```python
class MyClass:
    pass

class MyClass():
    pass
    
class MyClass(object):
    pass
```

The name of the class is important because it is intended to be a public class available for inclusion in other code.

__Requirement:__  The name of the class shall be CsvFormatter.

In the empty file that you have created, choose one of the three syntax options above and create the class with the correct
name in order to get the next failing test to pass.

### Task 2 - Instance Initialization
An empty class isn't going to do much for us in terms of the problem we are trying to solve.  A good place to start is to
customize the class instance initialization method to perform tasks that will place the class instance into a known state.

Upon creation, the CsvFormatter class will need to accept a map of format specifiers that indicate how columns of the source
records are to be formatted to create the output record.

The instance initialization method in a Python class is the \_\_init\_\_ method.  When defining a method in a Python class,
the first parameter is a reference to the class instance.  By convention this is named _self_.  Additional parameters are
provided following the _self_ parameter.

A Python method is defined in the same way that a Python function is defined except that a method is defined within
the class definition.
#### Step 1 - Override initialization method
In order to get the next failing test to pass, we need to define an \_\_init\_\_ method in the CsvFormatter class.  This can
be an empty method that will be evolved through subsequent tests.

__Requirement:__  The class instantiation shall accept exactly one parameter which must be a dictionary.  The keys of the
dictionary will be column names and the values will be the name of the format specifier to be used for that column.

I have chosen _format\_map_ as the name of this parameter.  This specific name is exposed to the users of the class in help
strings and _Exception_ messages.  In this case, the code wouldn't require a specific parameter name, but for the sake of
consistency, and due to the fact that it is exposed to the user of the class, we will treat the name _format\_map_ as a
requirement.

```python
class CsvFormatter:
    def __init__(self, format_map):
        pass
```
#### Step 2 - Check parameter type
As noted in the previous step, the parameter must be of type dictionary.  In order to get the next failing test to pass,
we need to raise a _TypeError_ exception in the case where the supplied parameter is not a dictionary.  At this point in
the development of the initialization method, we are not going to concern ourselves with whether the contents of the
dictionary are valid.

There are various ways to check the type of an item.  In this instance we only need to support dictionaries and so it will be
sufficient to confirm that the parameter passed is an instance of _dict_ using the _isinstance_ function.

If we determine that the type is not a dictionary, then we will signal that to the caller by raising an _Exception_.  The use
of an _Exception_ will cause the error to continue to propagate up the call stack until it is caught.  If it is not caught by
application code, then it will cause python to cease execution due to an uncaught exception.

The advantages of using an _Exception_ to signal to the caller is that we don't have to define a protocol for communicating the
failure to the caller, and if the caller does not wish to deal with failures, then the _Exception_ can propagate until it reaches
the code that is prepared to deal with it.

In this project, we will also provide a description of why the _Exception_ is being raised.  The descriptions will be part of
the project requirements and so the specific verbiage of the description will be provided as part of each requirement where
an _Exception_ is being raised.

__Requirement:__  The message included with the _Exception_ that is raised when the passed parameter is not a dictionary is:

The format\_map parameter provided to instantiate the class must be a dictionary

The following is an example of code that will check the type of the _format\_map_ parameter and raise an _Exception_.  Code
similar to this will be required to get the next failing test to pass.

```python
        if not isinstance(format_map, dict):
            raise TypeError('The format_map parameter provided to instantiate the class must be a dictionary')
```
#### Step 3 - Initialize state
In order to keep the value of the format\_map for subsequent usage it must become part of the state of the _CsvFormatter_
class.  One way to accomplish this is to create an attribute that is part of the instance and set the value of the attribute
to the value of the parameter that was passed.

__Requirement:__  The name of the instance attribute will be _format\_map_.  The only reason that the name of this is being
specified as a requirement is so to support the tests.

The following is a statement that would follow the type check in the \_\_init\_\_ method.  On the left side of the assignment
we create a new attribute on self and assign the value of the passed format\_map parameter.
```python
        self.format_map = format_map
```

At this point, your \_\_init\_\_ method should look something like the following:
```python
class CsvFormatter:
    def __init__(self, format_map):
        if not isinstance(format_map, dict):
            raise TypeError('The format_map parameter provided to instantiate the class must be a dictionary')
        self.format_map = format_map
```
### Task 3 - Validation
We have validated the type of the format\_map, but we haven't validate the contents of the format\_map.  We will use
a new method to validate that all of the format specifiers indicated are supported by our _CsvFormatter_ class.  Once
we have created the validator method, we can call the method from the \_\_init\_\_ method and signal an error when
we encounter unsupported format specifiers.
#### Step 1 - Create a validator method
For this project, we will use a method to validate the values in the format\_map dictionary.  We will use a leading underscore
in the name of the method to signal to users of the _CsvFormatter_ class that the method is protected and is intended for
use only within the class.

__Requirement:__  The name of the validator method shall be _\_verify\_map_, and will take as a parameter the format\_map.
Since this is intended to be a protected method of the class, it normally wouldn't matter what we called it - aside from the
normal importance of clear and unambiguous names.  In this case, the tests make an assumption about the name of the method, so
we need the code to match that assumption.

__Requirement:__  The supported format specifiers shall be:  _default_, _us\_currency_, _thousands\_us\_currency_,
_thousands\_integer_, and _integer_.

__Requirement:__  This method will raise a _ValueError_ if one or more unsupported format specifiers is found.

__Requirement:__  The message included with the raised exception will include the unsupported format specifiers in alphabetical
order.  Multiple unsupported format specifiers will be separated by ",\<space\>" and only one instance of each unsupported
format specifier will be listed in the message.  The message shall be:

Invalid format specifier(s) in map:\<space\>\<space\>\<alphabetical list of unsupported format specifiers\>

__Requirement:__  If no unsupported format specifiers are found, then the method returns _None_.  The default action for a
function or method without a return statement is to return _None_.

There is nothing that we can do to validate the column names, so only the format specifiers will be validated.

The following illustrates a valid and an invalid format\_map.
```python
valid = {'column1': 'default', 'column2': 'us_currency'}
invalid = {'column1': 'default', 'column2': 'unknown'}
```

To get the next three failing tests to pass, the method must exist, it must correctly detect unsupported format specifiers,
and it must correctly detect valid format\_maps.

```python
    def _verify_map(self, format_map):
        valid_formats = {'default', 'us_currency', 'thousands_us_currency', 'thousands_integer', 'integer'}
        invalid_formats = set([])
        for value in format_map.values():
            if not value in valid_formats:
                invalid_formats.add(value)
        
        if invalid_formats:
            format_names = ', '.join(sorted(invalid_formats))
            raise ValueError('Invalid format specifier(s) in map:  {:s}'.format(format_names))
```

For consideration:
  * Why was the set data type used in the implementation of this method?
  * What does the join method on strings do?
  * What does the values method on dictionaries do?

#### Step 2 - Call the validator method from the initialization method
Now that we have a method that will correctly validate a format\_map dictionary, we need to finish the \_\_init\_\_
method by validating the input.  Adding a call to the _\_verify\_map_ method will accomplish this and cause the next
failing test to pass.

```python
        self._verify_map(format_map)
```

### Task 4 - Formatters
For this next task, we'll create the 5 formatter methods that implement that supported formats.  With the exception of the
default formatter which only has 2 tests, the other formatter methods have 3 tests each:  the method must exist, it must
correctly raise a ValueError if the input value is not valid for the format specified, and a test for a successful format.
#### Step 1 - Default Formatter
__Requirement:__  This is a method that accepts one parameter.

__Requirement:__  This returns the input value unmodified.

__Requirement:__  The name of this method is _\_fmt\_default_

```python
    def _fmt_default(self, val):
        return val
```
#### Step 2 - US Currency Formatter
__Requirement:__  This is a method that accepts one parameter

__Requirement:__  This returns the value as a float with a precision of 2 decimal places preceded by a $ character.

__Requirement:__  The name of this method shall be _\_fmt\_us\_currency_

__Requirement:__  This method shall raise a ValueError if the input value does not represent a valid float.

```python
    def _fmt_us_currency(self, val):
        try:
            the_float = float(val)
            return '${:.2f}'.format(the_float)
        except (ValueError, TypeError) as e:
            raise ValueError('The value "{:s}" is not valid for the us_currency formatter'.format(str(val)))
```

#### Step 3 - US Currency with thousands separators formatter
__Requirement:__  This is a method that accepts one parameter

__Requirement:__  This returns the value as a float with a precision of 2 decimal places preceded by a $ character and with
thousands separated by a , character.

__Requirement:__  The name of this method shall be _\_fmt\_thousands\_us\_currency_

__Requirement:__  This method shall raise a ValueError if the input value does not represent a valid float.

```python
    def _fmt_thousands_us_currency(self, val):
        try:
            the_float = float(val)
            return '${:,.2f}'.format(the_float)
        except (ValueError, TypeError) as e:
            raise ValueError('The value "{:s}" is not valid for the thousands_us_currency formatter'.format(str(val)))
```
Considerations:
  * How is the comma separator formatting controlled?

#### Step 4 - Integer formatter
__Requirement:__  This is a method that accepts one parameter

__Requirement:__  This returns the value as an integer.  This will remove leading zeros and spaces.

__Requirement:__  The name of this method shall be _\_fmt\_integer_

__Requirement:__  This method shall raise a ValueError if the input value does not represent a valid float.

```python
    def _fmt_integer(self, val):
        try:
            the_integer = int(val)
            return '{:d}'.format(the_integer)
        except (ValueError, TypeError) as e:
            raise ValueError('The value "{:s}" is not valid for the integer formatter'.format(str(val)))

```

#### Step 5 - Integer with thousands separator formatter
__Requirement:__  This is a method that accepts one parameter

__Requirement:__  This returns the value as an integer with commas separating thousands.  This will remove leading zeros and spaces.

__Requirement:__  The name of this method shall be _\_fmt\_thousands\_integer_

__Requirement:__  This method shall raise a ValueError if the input value does not represent a valid float.

```python
    def _fmt_thousands_integer(self, val):
        try:
            the_integer = int(val)
            return '{:,d}'.format(the_integer)
        except (ValueError, TypeError) as e:
            raise ValueError('The value "{:s}" is not valid for the thousands_integer formatter'.format(str(val)))
```
Considerations
  * How is the thousands comma separator controlled?

### Task 5 - The Main Event
The main point of this class is to take rows of csv data and transform them into new rows based on the specified formatting
on a column-by-column basis.  Each row is represented by a dictionary where the column name is the key and the value at that
key is the corresponding value of that column in the row.  This method will be called for each row of data in a csv file.

For this project, the method will return a tuple of two values.  The first value is a list of the column headers for the
columns that had formatting exceptions raised.  The second value is the modified row.  Any row with a formatting exception
will remain unchanged from the input row, and all of the other values will be modified according to the rules specified
in the format\_map.

Any column that does not include a format specifier will have the default rule applied.  The default rule will leave the value
unchanged.

This is a flexible approach to error handling.  With this, the caller can take any of several actions when an error occurs.
For example, the offending row could be written to an error file, a notice of the exception could be written and the
partially modified row could be written to the output, etc.
#### Step 1 - Main formatter method
__Requirement:__  This method shall be named _format_.

__Requirement:__  This method shall leave the input dictionary unchanged and will return a copy of the input with the format
modifications.

__Requirement:__  This method shall return a tuple where the first element is a list of the column names where formatting
exceptions occurred and the second element is the modified record.

__Requirement:__  Any input columns without formatting specifications shall use the default format rule.

```python
    def format(self, record):
        if not isinstance(record, dict):
            raise TypeError('The record parameter must be a dictionary')

        new_record = {}
        failed_formats = []
        for key in record.keys():
            try:
                new_record[key] = getattr(self, '_fmt_{:s}'.format(self.format_map.get(key, 'default')))(record[key])
            except ValueError as e:
                failed_formats.append(key)
                new_record[key] = record[key]
        return sorted(failed_formats), new_record
```

Considerations:
  * How does the statement the try block that determines the new value work?
### Task 6 - Refactor
As we gain some experience with a new development effort we may recognize that there are some improvements that can be
made to the way that a component was designed, or even improvements to the overall application architecture.  In the
case of this project, we are maintaining a list of format methods, and so should we add support for other formats it will
be necessary to also update the _\_verify\_map_ method.

The final task is to refactor the _\_verify\_map_ method to use introspection of the _CsvFormatter_ class to determine
what the supported format specifiers are.
#### Step 1 - Refactor the validation method to be dynamic
In order to get the final failing test to pass, we must revise the _\_verify\_map_ method to compare the specified format
specifiers to against the methods of the class to determine if the specifier is valid or not.

```python
    def _verify_map(self, format_map):
        invalid_formats = set([])
        for value in format_map.values():
            if not hasattr(self, '_fmt_{:s}'.format(value)):
                invalid_formats.add(value)

        if invalid_formats:
            format_names = ', '.join(sorted(invalid_formats))
            msg = 'Invalid format specifier(s) in map:  {:s}'.format(format_names)
            raise ValueError(msg)
```

### Conclusion
#### Example data
There is a script in the scripts directory that can be run to process the sample data using the _CsvFormatter_ class you
have created.
  * Example 1 has bad entries in the map and illustrates how an application might respond to bad data.
  * Example 2 has one good row and one bad row.  The script will write the good rows to stdout and the bad rows to stderr.


```bash
# Illustrates a response to invalid map entries
python scripts/csvfmt.py -m examples/example_1_map.csv
# Will display the good row
python scripts/csvfmt.py -m examples/example_2_map.csv < examples/example_2.csv 2> /dev/null
# Will display the bad row
python scripts/csvfmt.py -m examples/example_2_map.csv < examples/example_2.csv > /dev/null
```

#### Final Solution

```python
# Implements a class to modify the format of input data to produce output data.

class CsvFormatter:
    def __init__(self, format_map):
        """
        Validate and initialize the format_map
        """
        if not isinstance(format_map, dict):
            raise TypeError('The format_map parameter provided to instantiate the class must be a dictionary')
        self._verify_map(format_map)
        self.format_map = format_map

    def _verify_map(self, format_map):
        """
        Validates the format_map looking for unknown format specifiers.  The format
        specifiers are considered to be valid if the instance has a method with a
        name that matches the pattern _fmt_<format_specifier>.
        """
        invalid_formats = set([])
        for value in format_map.values():
            if not hasattr(self, '_fmt_{:s}'.format(value)):
                invalid_formats.add(value)

        if invalid_formats:
            format_names = ', '.join(sorted(invalid_formats))
            msg = 'Invalid format specifier(s) in map:  {:s}'.format(format_names)
            raise ValueError(msg)
        
    def _fmt_default(self, val):
        """
        This formatter returns the value unmodified.
        """
        return val

    def _fmt_us_currency(self, val):
        """
        This formatter returns the value formatted as US currency.
        """
        try:
            the_float = float(val)
            return '${:.2f}'.format(the_float)
        except (ValueError, TypeError) as e:
            raise ValueError('The value "{:s}" is not valid for the us_currency formatter'.format(str(val)))

    def _fmt_thousands_us_currency(self, val):
        """
        This formatter returns the value formatted as US currency with a comma as the thousands separator
        """
        try:
            the_float = float(val)
            return '${:,.2f}'.format(the_float)
        except (ValueError, TypeError) as e:
            raise ValueError('The value "{:s}" is not valid for the thousands_us_currency formatter'.format(str(val)))

    def _fmt_integer(self, val):
        """
        This formatter returns the value formatted as an integer.
        """
        try:
            the_integer = int(val)
            return '{:d}'.format(the_integer)
        except (ValueError, TypeError) as e:
            raise ValueError('The value "{:s}" is not valid for the integer formatter'.format(str(val)))

    def _fmt_thousands_integer(self, val):
        """
        This formatter returns the value formatted with commas separating the thousands.
        """
        try:
            the_integer = int(val)
            return '{:,d}'.format(the_integer)
        except (ValueError, TypeError) as e:
            raise ValueError('The value "{:s}" is not valid for the thousands_integer formatter'.format(str(val)))
        
    def format(self, record):
        """
        Applies the formatting rules to the specified record.
        """
        if not isinstance(record, dict):
            raise TypeError('The record parameter must be a dictionary')

        new_record = {}
        failed_formats = []
        for key in record.keys():
            try:
                new_record[key] = getattr(self, '_fmt_{:s}'.format(self.format_map.get(key, 'default')))(record[key])
            except ValueError as e:
                failed_formats.append(key)
                new_record[key] = record[key]
        return sorted(failed_formats), new_record
```
