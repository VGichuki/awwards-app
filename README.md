# Awwards-app
## Author 
>[Vivian-Gichuki]
# Description 
This is a Django application where a user can rate and post different projects.
##  Live Link 
 Click [View Site](https://awwardsapp21.herokuapp.com/)  to visit the site
## User Story 
* View different projects that interest them
* Search for different projects
* Rate a project according to design, content and usability.
## Setup and Installation 
To get the project .......
##### Cloning the repository: 
 ```bash
https://github.com/VGichuki/awwards-app
```
##### Navigate into the folder and install requirements 
 ```bash
cd Picture-Globe pip install -r requirements.txt
```
##### Install and activate Virtual 
 ```bash
- python3 -m venv virtual - source virtual/bin/activate
```
##### Install Dependencies 
 ```bash
 pip install -r requirements.txt
```
##### Setup Database 
  SetUp your database User,Password, Host then make migrate
 ```bash
python manage.py makemigrations pictures
 ```
 Now Migrate
 ```bash
 python manage.py migrate
```
##### Run the application 
 ```bash
 python manage.py runserver
```
##### Running the application 
 ```bash
 python manage.py server
```
##### Testing the application 
 ```bash
 python manage.py test
```
Open the application on your browser `127.0.0.1:8000`.
## Technology used 
* [Python3.8]
* [Django]
* [Heroku]
## Known Bugs
* The profile page doe not entail the users account details.
* The rating and total scores of a project are not functional.
* Tests are not running.
## License
* *MIT License:*
* Copyright (c) 2021 **Vivian Gichuki**
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.