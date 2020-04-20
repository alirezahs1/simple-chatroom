import tornado.ioloop
import tornado.web
import tornado.websocket
from db import *
import json
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        rooms = getRooms()
        username = self.get_cookie("username") if self.get_cookie("username") else ''

        
        data = {
            'rooms' : getRooms(),
            'username': username
        }
        self.render("client/index.html", data=data)

    def post(self, *args, **kwargs):
        action = self.get_argument('action')
        if action=='join':
            username = self.get_argument('username')
            room_id  = self.get_argument('room_id')
            self.set_cookie("username", username)
            return self.redirect('/room/'+room_id+'/')
        elif action=='create_room':
            name  = self.get_argument('name')
            insertRoom(name)
            return self.get()
        

class RoomHandler(tornado.web.RequestHandler):
    def get(self, room_id):
        if self.get_cookie("username") != None:
            username = self.get_cookie("username")
        else:
            self.redirect('/')
            
        msgs = getRoomMessages(room_id)
        data = {
            'messages'  : json.dumps(msgs), 
            'room_id'   : room_id,
            'username'  : username
        }
        self.render("client/room.html",  data=data)
 
class SimpleWebSocket(tornado.websocket.WebSocketHandler):
    connections = set()
 
    def open(self):
        self.connections.add(self)
 
    def on_message(self, data):
        data = json.loads(data)
        insertMessage(data['room_id'], data['username'], data['body'])
        [client.write_message(data) for client in self.connections]
 
    def on_close(self):
        self.connections.remove(self)
 
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/room/([0-9-]+)/", RoomHandler),
        (r"/websocket", SimpleWebSocket),
        (r"/static/(.*)",tornado.web.StaticFileHandler, {"path": "./client"},),
    ])
 
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()