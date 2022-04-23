# Python-Django-Technical-Task

TASK1: Suppose you have two model with name user and customer. And customer are related to user with one to one relationship. You have to create a rest api view for create a customer.
Field of user are:- 
a) first_name
b) last_name
c) email
d) mobile no.
And field of customer are:-
a) profile number
Note:- email and mobile number are unique.

=> setup models.py file for user_data and customer data
=> then setting up serailizer.py, views.py file, & restapiframework as per requirement .
=> after final setup
=> running python manage.py runserver in cmd prompt
=>/users
input format->
{
"first_name": "**fname**",
"last_name": "**lname**",
"email": "**email**",
"mob_no": "**no.**"
}
and press POST to save the data, similar for /Customer.

TASK2: How to create a bundles of static files like css,js and images. And this static file should be minified when creating a bundle of it using webpack.

=> completed the task using gulpfile 
=> using webpack, it's completed just facing some error in it 
=> setup

TASK3: How to back up database (postgres) automatically at 2am in the morning and 
store it in a remote location like AWS s3 bucket storage
database name test1
database user test1
database password test

=> updated the detailed doc with code snippets(/task3), to backup the database automatically at 2am in AWS.
