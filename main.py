from flask import Flask


app= Flask(__name__)


@app.route('/')
def Hello1():
    return 'Program 1 with flask by kevin pinsag'