# Simple Chatroom
![enter image description here](http://uupload.ir/files/q3t0_screenshot_from_2020-04-20_04-58-40.png)
## Installation
### 0. Clone this repository
```sh
git clone https://github.com/alirezahs1/simple-chatroom
```
### 1. Install requirements
    pip install -R requirements.txt
    
### 2. Import MySQL Database
Create a mysql database and import **chatroom.sql** file.
then, change file **/db.py**:

    DB_HOST = 'localhost'
    DB_NAME = *YOUR_DATABASE_NAME*
    DB_USERNAME = *YOUR_DATABASE_USERNAME*
    DB_PASSWORD = *YOUR_DATABASE_PASSWORD*

## Serve
    python server.py

## Enjoy :)
![enter image description here](http://uupload.ir/files/549r_screenshot_from_2020-04-20_04-58-55.png)

#### Change port
you can change the port from end of **/server.py** file:

![enter image description here](http://uupload.ir/files/f1dc_screenshot_from_2020-04-20_05-10-42.png)