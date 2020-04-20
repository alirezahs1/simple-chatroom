# Simple Chatroom

## Installation
### 1. Clone this repository
```sh
git clone https://github.com/alirezahs1/simple-chatroom
```
## 2. Install requirements

    pip install -R requirements.txt
    
## 3. Import MySQL Database
Create a mysql database and import **chatroom.sql** file.
then, change file **/db.py**:

    DB_HOST = 'localhost'
    DB_NAME = *YOUR_DATABASE_NAME*
    DB_USERNAME = *YOUR_DATABASE_USERNAME*
    DB_PASSWORD = *YOUR_DATABASE_PASSWORD*
