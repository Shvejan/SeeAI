from flask import Flask,request
import time

from face_rec import register_new_face, identify
app = Flask(__name__)

@app.route("/find")
def hello_world():

    name=identify()
    if(name=="unknown"):
        return "unknown"

    return "It's "+name


@app.route("/register")
def register():
    name=request.args.get("name").split(" ")[-1]
    register_new_face(name)
    return name+"'s face registered"


if __name__=='__main__':
    app.run(host='0.0.0.0', port=3000)