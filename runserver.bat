@echo START virtualenv
@echo OFF
START  /B ..\hello\Scripts\activate 
@echo START Server
python manage.py runserver
