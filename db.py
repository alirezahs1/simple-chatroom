import json
import mysql.connector

DB_HOST     = 'localhost'
DB_NAME     = 'chatroom'
DB_USERNAME = 'root'
DB_PASSWORD = '12345678'

def db_conn():
    conn = mysql.connector.connect(
        host    = DB_HOST,
        user    = DB_USERNAME,
        passwd  = DB_PASSWORD,
        database= DB_NAME
    )
    return conn
    
conn = db_conn()
cursor = conn.cursor()

def jsonify(res):
    row_headers=[x[0] for x in cursor.description]
    json_data=[]
    for result in res:
        json_data.append(dict(zip(row_headers,result)))
    return json_data

def getRooms():
    cursor.execute("SELECT id, name FROM rooms")
    res = cursor.fetchall()
    return jsonify(res)

def insertRoom(name):
    sql = "INSERT INTO rooms (name) VALUES (%s)"
    cursor.execute(sql, (name,))
    conn.commit()

def insertMessage(room_id, username, body):
    sql = "INSERT INTO messages (room_id, username, body) VALUES (%s, %s, %s)"
    cursor.execute(sql, (room_id, username, body))
    conn.commit()

def getRoomMessages(room_id):
    sql = "SELECT username, body FROM messages WHERE room_id=%s" % room_id
    cursor.execute(sql)
    res = cursor.fetchall()
    return jsonify(res)