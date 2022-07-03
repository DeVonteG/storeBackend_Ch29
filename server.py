from flask import Flask

app = Flask("server")

@app.get("/")
def home():
    return "Hello from flask server"

@app.get("/test")
def test():
    return "This is just a test"

@app.get("/about")
def about_me():
    return "About me, My Name is DeVonte"


################################################################
################## API  Endpoints= Products ####################
################################################################

@app.get("/api/version")
def version():
    return "Running ver 1.0"







app.run(debug=True)
