from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Auto Blogger is Running!'

if __name__ == "__main__":
    app.run()
