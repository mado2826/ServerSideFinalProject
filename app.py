from flask import Flask, jsonify, Response, request, send_file, redirect, jsonify, render_template, make_response, flash

app = Flask(__name__)
app.secret_key = 'skibiditoilet6767'

@app.route('/')
def start():
    pass

@app.route('/login')
def login():
    pass

@app.route("/logout", methods=["POST"])
def logout():
    pass

@app.route('/map')
def map():
    pass

@app.route('/review', methods = ['POST'])
def create_review():
    pass

@app.route('/review', methods = ['PUT'])
def update_review():
    pass

@app.route('/review', methods = ['DELETE'])
def delete_review():
    pass

@app.route('/event', methods = ['GET','POST'])
def create_event():
    pass

@app.route('/event', methods = ['PUT'])
def update_event():
    pass

@app.route('/event', methods = ['DELETE'])
def delete_event():
    pass

