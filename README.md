# Resume-Parser
Extract the data from resume using djnago rest api 

fallow this steps to run this project:

  create folder like project
  in /project

In /folder/

step 1: create virtual enviornment
    $ virtualenv -p python3 venv
    activate this virtualenvironment
    $ source venv/bin/activate

step 2 : download and extract git repo in that folder 
    $ https://github.com/palwesh/Resume-Parser.git (download this zip file and extract)
    $ cd Resume-Parser-master/
  
step 3 : configure packages (run this command)
   $ pip install Django==2.2
   $ pip install djangorestframework
   $ pip install pyresparser
   $ python -m spacy download en_core_web_sm
   $ python -m nltk.downloader words
   
   $ python manage.py makemigrations
   $ python manage.py migrate
  
step 4 : run project 
   $ python manage.py runserver
   
   resume upload api
   http://127.0.0.1:8000/upload/
   
   Open Postman and put this api
   http://127.0.0.1:8000/upload/
   
   {
    "id": 4,
    "name": "palwes sahu",
    "pdf": "/media/Resume/Shaktis_Resume_mJkihHi.pdf"
    }
    
    like this 
    name, pdf
    
 step 5 : data will stored in sqlite db in userProfile table
    login in djngo admin and check it
    
    
