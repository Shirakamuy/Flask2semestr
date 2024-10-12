from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"
@app.route("/home/")
def welcome_home():
    return "Welcome to Home"

if __name__ == '__main__':
    app.run(port=5000, debug=True)

    #static for css and image
    #templates for html