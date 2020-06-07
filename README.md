# python-flask-template-with-excel-upload

This is a template source code for uploading an excel (.xlsx) file with required data as input to automate task using python as a web application. This code can be further extended for specific task. 

# Run the project

There are two ways users can use this code.

1. **With Python enviroment**: Just run main_app.py *"python3 main_app.py"* and then from browser <localhost/ip-address:port> to use the code. 
Users required to create python environment in their host computers. Python3 is recommended since this code was developed in python3. 
<br><br>Install required packages: *"pip3 install package-name"
<br>  packages: **pandas, xlrd, flask**
 
2. **Use docker container**: Install docker software (and also, create user profile) and make sure it is running in the host environment. Then, run make-docker.sh(see below) and from browser <localhost:port> to use the code.
 <br><br> Run" "./make-docker.sh *web-app-name* *port-numnber*"
<br> Example: **"./make-docker.sh automate_task 5500"**
  <br> From browser: <localhost:5500 or http://ip-address:5500>
  
# Extending the Code

To extend the code for specific tasks:
1. Put your python scripts under **scripts** folder
2. Change/add titles, desciptions, action options, etc. in the html templates under **templates** folder.
3. In main_app.py, use your scripts for specific task under specific action.  
