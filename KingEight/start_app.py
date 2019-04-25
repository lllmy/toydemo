from flask import Flask,request,jsonify
from serv import content
from serv import get_anything
from serv import user_option
app = Flask(__name__)

app.register_blueprint(content.content_bp)
app.register_blueprint(get_anything.get_any)
app.register_blueprint(user_option.user_pb)

if __name__ == '__main__':
    app.run("0.0.0.0",9527,debug=True)