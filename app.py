from flask import Flask, render_template, session

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/newtask")
def newTask():
    return render_template("newtask.html")

@app.route("/deletetask")
def deleteTask():
    return render_template("deletetask.html")

@app.route("/editask")
def editTask():
    return render_template("edittask..html")

if __name__ == '__main__':
    app.run(debug=True)