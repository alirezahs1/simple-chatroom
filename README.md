# Simple Chatroom
![enter image description here](https://filebin.net/4o04wfjt5kupa4u3/Screenshot_from_2020-04-20_04-58-40.png?t=i4j43v7h)
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
![enter image description here](https://filebin.net/4o04wfjt5kupa4u3/Screenshot_from_2020-04-20_04-58-55.png?t=i4j43v7h)

#### Change port
you can change the port from end of **/server.py** file:

![enter image description here](https://filebin.net/kqq5azpys0e9n4d2/Screenshot_from_2020-04-20_05-10-42.png?t=uypz7dvh)