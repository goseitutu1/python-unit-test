# python-unit-test

2. $ pip install nose  .Run the command to install nose.

3. $ pip install nose-cov  .Run the command to install coverage plugin.

4. $ pip install mock  .Run the command to install mock package inside your virtual environment.

5. $ pip install requests  .Run the command to install requests package inside your virtual environment.


Inside the code directory, there is a test file 'item_resources_test.py', which contains the test case for the resource file 'item_resource.py'.

Test case is written in python which uses unittest package with Nose and coverage plugins. 

You can execute the test by running this command "nosetests --with-coverage item_resources_test.py" in the terminal of your editor after setting up python environment and installing unittest package with Nose and Coverage plugins.

This test has a coverage of 93% with 2 miss. 

Search the file name "item_resources.py" from the output after excuting the test file to verify the test coverage. 
