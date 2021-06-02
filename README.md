# Yupload
### Yupload is a simple example of how to upload files with flask
#### Clone the repository
```
$ git clone https://github.com/Mazzya/Yupload.git
```
If you don't want to clone it, you can download it directly from [here](https://github.com/Mazzya/Yupload/archive/refs/heads/master.zip).
#### Requirements
This project uses pipenv. 

It is necessary to have pipenv installed to be able to work with the project without any problem, to install it execute the following command:
```
$ pip install pipenv
```

To install all the necessary packages, run the following command at the console:
```
$ pipenv install -r requirements.txt
```
### How can I run the application?
It's very simple, from the application directory, open a console and run this command: 
```
$ python run.py 
```
### Where are my files kept?
All the files that you are going to upload are saved in a folder called <b>content</b>. This folder is next to the application files.
### On what port is the application running?
The default port is <b>3000</b>, but you can change it if you want in the ```run.py``` file.
### How can the web application be accessed?
You can access the web application with this url ```http://127.0.0.1:3000/```
