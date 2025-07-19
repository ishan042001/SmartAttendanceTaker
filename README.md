# AttendanceTaker
About the project:
This application aims at automating the traditional attendance system where attendance is marked manually. This project involves building an attendance system that uses face recognition technology to mark a student as present or absent. Besides just helping to take attendance, it also enables the administrator to send emails to the parents of the absentees so that they know that their child is absent. This practice will help prevent students from bunking their classes.

Functionalities provided:
This application provides the following functionalities:
1.	See existing profiles
2.	Modify profile
3.	Delete profile
4.	Add a new profile
5.	Run scanner to record attendance
6.	View the list of present students along with their in-time.
7.	View the list of absentees
8.	See history
9.	Send mails to parents of the absentees
10.	 Reset the system

Tech stack used:
1.	HTML
2.	CSS
3.	JavaScript
4.	Python
5.	Django
6.	SQLite Database

Steps to run the project:
Follow these steps to run the project:
1.	Clone the repository
2.	Python version used 3.10.4
3.	Open settings.py and mention details like your email_host, email_port, email_host_user(your mail address) and email_host_password(your password). (This step is required if you want to access send mail functionality.)
![image](https://user-images.githubusercontent.com/76212203/170879838-8eca96b5-cffb-432d-845b-81ed33fc4418.png)

4.	Open view.py and add you email address the same that you mentioned in settings.py (This step is required if you want to access send mail functionality.)
![image](https://user-images.githubusercontent.com/76212203/170879851-1ebb2974-8d8c-4fea-8f9b-0bf436a8e3ad.png)

5.	Create a python virtual environment(recommended).
6.	Run pip install dlib-19.22.99-cp310-cp310-win_amd64.whl
7.	Run pip install face_recognition
8.	Run pip install -r req.txt
9.	Run python manage.py runserver
10.	Go to the browser and enter localhost:8000

