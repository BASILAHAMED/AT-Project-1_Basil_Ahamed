AT Project 1
System Description

The OrangeHRM System is a web based manages employee photos. Employees can add or change their own photos and Human Resources can add or change everyone's photos. 
The system produces lists of photos by different selection criteria. Its photos will be used by manyother systems in the company. 
The photos are stored in a configurable file structure and the photo location is pointed to by a file system. 
This release only includes employee photos name and address and social security information and not any of the other information planned for later.

Test Cases include
1.Test Cases dealing the with login - 02
2.Test Cases dealing the with PIM - 03
Total 05 

Folder Description
There are two Folders,
1.Test_Codes # It consists of Test Files (i.e. test_login, test_pim)
2.Test_Data # It consists of Test Data's (i.e. username, password, XPATH, ID, etc.,)


COMMAND TO RUN A TEST FILE
--------------------------

pytest -v -s --capture=sys --html=C:\Users\test_result.html
pytest -v -s --capture=sys --html=C:\Users\sbasi\Automation\Try\Python-Automation-Professional-Coding-main\reports\test_basil.html