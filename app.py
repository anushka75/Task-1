from flask import Flask, request

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        return 'Hi %s' % (request.form['username'])

    else:
        return '''<form action="/" method="post"></br>
        Username: <input name="username" type="text"/> </br> </br>
        <input value="Submit" type="submit" />
        </form> '''

if __name__=='__main__':
    app.run(port=8080)