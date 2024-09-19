# SDET2024 UI task

Application for testing the **[BankingProject UI](https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager)**

### Testcases
* **Add Customer**  
    Generate a 10-digit `Post Code` number  
    Generate `First Name` based on `Post Code`:
    - every two digits is a letter number of the alphabet (0 - "a", 1 - "b", etc.)
    - if the number is greater than 25, then 26 is 0, 27 is 1, etc.

- **Sort Customers by First Name**

* **Delete the Customer with the name length closest to the average**  
    Determine the average name length  
    Find `Customer` with the name length closest to the average  
    Delete this `Customer`
***


## Requirements
To use the application, you must have [Python 3](https://www.python.org/downloads/) 
and [Allure](https://allurereport.org/docs/install/) installed on your operating system.  
`Python` (tested to work with 3.10.14)  
`Allure` (tested to work with 2.30.0)

**Python packages**
* `allure-pytest` (tested to work with 2.13.5)  
* `beautifulsoup4` (tested to work with 4.12.3)  
* `selenium` (tested to work with 4.23.0)  
* `pytest` (tested to work with 8.3.1)  
* `pytest-xdist` (tested to work with 3.6.1)  
* `rstr` (tested to work with 3.2.2)  
* `selenium` (tested to work with 4.23.0)  
* `lxml` (tested to work with 5.2.2)  

**Note:** The packages can be installed by running `python3 -m pip install -r requirements.txt`
***


## Run `run_task_ui.py` to test the BankingProject
The `pytest-xdist` plugin extends `pytest` to speed up test execution,  
and `allure-pytest` is used for visualizing the results of a test run.

### First `pytest` runs 3 test cases in parallel
```
pytest tests/ -n 3 --alluredir=allure-results --clean-alluredir
```

### An `environment.properties` file is then created with information about the environment
```
os_platform = Linux
os_release = 6.8.0-40-generic
os_version = Ubuntu 24.04 LTS
python_version = Python 3.10.14
```

### Finally, `allure` converts the test results into an HTML report
```
allure generate allure-report --clean --single-file allure-results
```

### And opens it in default browser
```
webbrowser.open('index.html')
```
***


### Files and directories:
- `allure-report/index.html` allure report
- `allure-results/` test results directory  
**Note:** These directories will be created after running `run_task_ui.py`

* `tests/` test modules
* `data.py` form data generator script
* `locators.py` locators module
* `pages.py` web pages module
* `requirements.txt` required packages
* `run_task_ui.py` ui testing script
