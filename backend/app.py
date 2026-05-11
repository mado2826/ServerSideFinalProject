from flask import Flask, jsonify, Response, request, send_file, redirect, jsonify, render_template, make_response, flash
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token
from dotenv import load_dotenv
import os
import database as database
from google.oauth2 import id_token
from google.auth.transport import requests as gr
import timedelta

load_dotenv()

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
CORS(app)
JWTManager(app)


@app.route('/')
def start():
    return send_file("index.html")

@app.route('/login', methods = ['POST'])
def login():
    token = request.json["credential"]
    
    info = id_token.verify_oauth2_token(token, gr.Request(), os.getenv("GOOGLE_CLIENT_ID"))
    
    email = info["email"]
    
    if not email.endswith("@" + os.getenv("ALLOWED_DOMAIN")):
        return jsonify({"error": "School email required"}), 403
    
    access_token = create_access_token(identity=email, additional_claims={"name": info["name"]})
    return jsonify({"token": access_token, "email": email, "name": info["name"]})


@app.route("/logout", methods=["POST"])
def logout():
    pass

@app.route('/map', methods=["GET"])
def map():
    return send_file("map.html")

@app.route('/restaurant/{name}')
@jwt_required()
def getRestaurant(name):
    user = get_jwt_identity()["name"]
    rating = database.avg_rating(name)
    address = database.get_address(name)
    cuisine = database.get_cuisine(name)
    walk_time = database.get_walk_time(name)
    type = database.get_type(name)
    time_range = database.get_time_range(name)
    price_range = database.get_price_range(name)
    mon_hrs = database.get_mon_hrs(name)
    tue_hrs = database.get_tue_hrs(name)
    wed_hrs = database.get_wed_hrs(name)
    thu_hrs = database.get_thu_hrs(name)
    fri_hrs = database.get_fri_hrs(name)
    sat_hrs = database.get_sat_hrs(name)
    sun_hrs = database.get_sun_hrs(name)
    reviews = database.get_reviews(name)
    events = database.get_events(name)

    return render_template('restaurant.j2', name=name, rating=rating, address=address, cuisine=cuisine,
                           walk_time=walk_time, type=type, time_range=time_range,
                           price_range=price_range, mon_hrs=mon_hrs, tue_hrs=tue_hrs,
                           wed_hrs=wed_hrs, thu_hrs=thu_hrs, fri_hrs=fri_hrs,
                           sat_hrs=sat_hrs, sun_hrs=sun_hrs, reviews=reviews, events=events, user=user)


@app.route('/review', methods = ['POST'])
@jwt_required()
def update_review():
    name = request.form.get("name")
    user = get_jwt_identity()["name"]
    rating = request.form.get("r")
    comment = request.form.get("c")

    if (rating != None and rating != ""):
        database.update_review(name, user, rating, comment)

@app.route('/review', methods = ['DELETE'])
@jwt_required()
def delete_review():
    name = request.form.get("name")
    user = get_jwt_identity()["name"]

    database.delete_review(name, user)

@app.route('/event', methods = ['POST'])
@jwt_required()
def create_event():
    name = request.form.get("name")
    user = get_jwt_identity()["name"]
    date = request.form.get("d")
    time = request.form.get("t")
    if (date != None and date != "" and time != None and time != ""):
        database.create_event(name, user, date, time)


@app.route('/event', methods = ['PUT'])
@jwt_required()
def update_event():
    id = request.form.get("id")
    user = get_jwt_identity()["name"]

    #figure out user role
    if (database.is_host(id, user)):
        date = request.form.get("d")
        time = request.form.get("t")
        if (date != None and date != "" and time != None and time != ""):
            database.update_details(id, date, time)
    else:
        database.toggle_guest(id, user)

@app.route('/event', methods = ['DELETE'])
@jwt_required()
def delete_event():
    id = request.form.get("id")
    user = get_jwt_identity()["name"]

    if (database.is_host(id, user)):
        database.delete_event(id)

if __name__=='__main__':
    app.run(debug=True)