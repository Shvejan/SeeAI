from flask import Flask,request
from model_traffic_signs import predict_traffic_sign
import time
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, abort
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant, ChatGrant
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

from face_rec import register_new_face, identify
app = Flask(__name__)

twilio_account_sid = "ACfdfc075fe5d679fcc06afd3605d6766c"
twilio_api_key_sid = "SK0a46a880aceb5563dbe60f587b3dea8f"
twilio_api_key_secret = "KVHXCLIC3VbiAz2tX4cNci3qBRAIHDRm"
twilio_client = Client(twilio_api_key_sid, twilio_api_key_secret,
                       twilio_account_sid)



def get_chatroom(name):
    for conversation in twilio_client.conversations.conversations.stream():
        if conversation.friendly_name == name:
            return conversation

    # a conversation with the given name does not exist ==> create a new one
    return twilio_client.conversations.conversations.create(
        friendly_name=name)

@app.route('/videocall')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.get_json(force=True).get('username')
    if not username:
        abort(401)

    conversation = get_chatroom('My Room')
    try:
        conversation.participants.create(identity=username)
    except TwilioRestException as exc:
        # do not error if the user is already in the conversation
        if exc.status != 409:
            raise

    token = AccessToken(twilio_account_sid, twilio_api_key_sid,
                        twilio_api_key_secret, identity=username)
    token.add_grant(VideoGrant(room='My Room'))
    token.add_grant(ChatGrant(service_sid=conversation.chat_service_sid))

    return {'token': token.to_jwt(),
            'conversation_sid': conversation.sid}



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

@app.route("/traffic")
def traffic():
    print("functino calling ")
    return predict_traffic_sign()




if __name__=='__main__':
    app.run(host='0.0.0.0', port=3000)