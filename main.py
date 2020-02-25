from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"
    
@app.route("/test")
def testing():
    return "Hello world!"
    

if __name__=='__main__':
    app.run('0.0.0.0', port=8080, debug=True)
