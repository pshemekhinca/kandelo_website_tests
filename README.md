## Sample tests set for kandelo.eu website

---

Contains several sample test cases for three subpages.

Tests are ordered according to Page-object-model (POM) assumptions. 

---


### Table of Contents


- [Files Structure](#Files-Structure)
- [How To Run Tests](#How-To-Run-Tests)
- [Autho Info](#author-info)

---



#### Technologies

- pytest 6.2
- selenium 3.141
- allure-pytest==2.8.4


  
[Back to the Top ^](#Table-of-Contents)

---

### Files Structure

The project files should be ordered as below:


    
    test_kandelo
    |
    |--- configuration
    |    |---  drivers
    |    |     `---  chromedriver # not commited on gitHub
    |    |---  config_reader.py
    |    `---  configuration.json
    |
    |--- libs
    |    `---  allure-2.13.9 # not commited on github
    |    
    |--- results
    |    `---  files generated for allure report
    |  
    |--- screenshots
    |    `---  screenshots taken when test failed
    | 
    |--- src
    |    |---  pages
    |    |     |--- home_page.py
    |    |     |--- locators.py
    |    |     |--- main_page.py
    |    |     |--- page_factory.py
    |    |     |--- pages_header_menu.py
    |    |     `--- products_page.py
    |    | 
    |    |---  utils
    |    |     |--- screenshot_listener.py
    |    |     `--- wrappers.py
    |    | 
    |--- tests
    |    |---  pages
    |    |     |--- base_test_class.py
    |    |     |--- tests_home_page.py
    |    |     |--- test_main_page.py
    |    |     |--- test_pages_header_menu.py
    |    |     `--- test_products_page.py
    |    | 
    |    |---  test_data
    |    |     |--- web.json
    |    |     `--- web_reader.py
    |    | 
    |    `---  test_suites
    |          |--- testsuite_all_kandelo_tests.py
    |          |--- testsuite_sanity_tests.py
    |          `--- testsuite_smke_tests.py
    |
    `--- README.md

[Back to the Top ^](#Table-of-Contents)

---

###How To Run Tests
To run all tests, type:

```
pytest -v tests
```

or choosing specific file, add file path;

```
pytest -v tests/test_suites/testsuite_all_kandelo_tests.py 
```

- To screen Allure tests report, prepare report data:
```
python -m pytest tests/test_suites/testsuite_all_kandelo_tests.py --alluredir ./results
```
- then call to screen it in default web browser
```
libs/allure-2.13.9/bin/allure serve ./results  
```
[Back to the Top ^](#Table-of-Contents)

---

### Author Info

- Przemyslaw Hinca -> Github: [pshemekhinca](https://github.com/pshemekhinca)

[Back to the Top ^](#Table-of-Contents)
