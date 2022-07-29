from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.secret_key = "itispassword"


# ==============Login page

@app.route("/")
@app.route("/home",methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        # return render_template("index.html")
        values = request.form.to_dict()
        if values["email"] == "praharsham@gmail.com" and values["password"] == "itispassword":
            # return "Login Successful"
            flash("Login Successful")
            return redirect(url_for("home"))
        else:
            flash("Invalid Credentials")
            return redirect(url_for("home"))
            # return "Login Failed <a href='/'>Try Again</a>"

@app.route("/users")
def users():
    return "Users Page"

@app.route("/products")
def products():
    return "Products Page"

@app.route("/orders")
def orders():
    return "Orders Page"

@app.route("/favourites")
def favourites():
    return "Favourites Page"


if __name__ == '__main__':
	app.run(debug=True,port=8000)