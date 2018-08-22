from flask import Flask
from Modules.instantiation import CrmInsurnace

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/view")
def view():
    insurance = CrmInsurnace()
    insurance.view()

if __name__ == '__main__':
    app.run()