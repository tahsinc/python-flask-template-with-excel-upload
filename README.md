# Automate-with-python-and-excel

This is a template source code for uploading an excel (.xlsx) file with required data as input to automate task using python as a web application. This code can be further extended for specific task. 

# Run the project

There are two ways users can use this code.

1. **With Python enviroment**: Just run main_app.py *"python3 main_app.py"* and then from browser <localhost/ip-address:port> to use the code. 
Users required to create python environment in their host computers. Python3 is recommended since this code was developed in python3. 
<br>Install required packages: *"pip3 install <package-name>"
<br>  packages: **pandas, xlrd, flask**
 
2. **Use docker container**: Install docker software (and also, create user profile) and make sure it is running in the host environment. Then, run make-docker.sh(see below) and from browser <localhost:port> to use the code.
 <br> *"./make-docker.sh <web-app-name> <port-numnber>"
<br> Example: **"./make-docker.sh automate_task 5500"**
  <br> From browser: <localhost:5500 or http://ip-address:5500>
