from flask import Flask, render_template
import turbo_flask as tf


app = Flask(__name__)
turbo = tf.Turbo(app)

@app.route('/')
def hello_world():
    return render_template("index.html", page_val="index", link="/2")

@app.route('/2')
def second_route():
    return render_template("index.html", page_val="the second one!", link="/")