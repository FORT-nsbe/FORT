from flask import Flask, request
from dotenv import load_dotenv
import bot
import os
import requests


from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        return "I'm a simple GroupMe bot built with Python, I take and save pictures shared in a group chat"
    else: # issue response to the received post request (message)
        response = request.get_json()
        if(response['text'].startswitch('Fort Alert')):
            print('Awesome')
        print(response['text'])
  
        return 'good'    

if __name__ == '__main__':
    print('Listening..')
    app.run()
