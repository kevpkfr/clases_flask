from flask import Flask


app= Flask(__name__)


@app.route('/kevinpinsag')
def Hello1():
    return 'Program 1 with flask by kevin pinsag'

@app.route('/')
def Hello2():
    return 'primero desarrollo de software yavirac'

#if__name__=="__main__":
    app.run(port=8080)
    
if __name__== '__main__':
    app.run(debug=True, port=8080)
    