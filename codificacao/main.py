from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def produto():
    return render_template("produtos.html")

if __name__=="__main__":
    app.run(debug=True)