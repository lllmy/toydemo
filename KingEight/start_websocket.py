from flask import Flask,request
from geventwebsocket.websocket import WebSocket
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

import json

websocket_app = Flask(__name__)

user_socket_dict = {}

@websocket_app.route("/ws/<uid>")
def ws(uid):
    user_socket = request.environ.get("wsgi.websocket") #type:WebSocket
    user_socket_dict[uid] = user_socket
    print(len(user_socket_dict),user_socket_dict)
    while True:
        msg = user_socket.receive()
        print(msg)
        msg_dict = json.loads(msg) # {to_user:123,music:abc.mp3}
        to_user = msg_dict.get("to_user")
        to_user_socket = user_socket_dict.get(to_user)
        to_user_socket.send(msg_dict.get("music"))

if __name__ == '__main__':
    http_serv = WSGIServer(("0.0.0.0",9528),websocket_app,handler_class=WebSocketHandler)
    http_serv.serve_forever()