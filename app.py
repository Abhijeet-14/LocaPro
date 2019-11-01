from flask import Flask, render_template,request, session

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/First_page", methods=["POST"])
def welcome():
    name=request.form.get("name")
    password=request.form.get("password")
    return render_template("First_page.html", name=name , password=password)

if __name__ == "__main__":
    app.run()
