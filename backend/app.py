from flask import Flask, jsonify, Response, request, send_file, redirect, jsonify, render_template, make_response, flash
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token
from dotenv import load_dotenv
import os
import database as database
from google.oauth2 import id_token
from google.auth.transport import requests as gr

load_dotenv()

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
CORS(app)
JWTManager(app)


# @app.route('/')
# def start():
#     pass

@app.route('/login', methods = ['POST'])
def login():
    token = request.json["credential"]
    
    info = id_token.verify_oauth2_token(token, gr.Request(), os.getenv("GOOGLE_CLIENT_ID"))
    
    email = info["email"]
    
    if not email.endswith("@" + os.getenv("ALLOWED_DOMAIN")):
        return jsonify({"error": "School email required"}), 403
    
    access_token = create_access_token(identity=email)
    return jsonify({"token": access_token, "email": email, "name": info["name"]})


@app.route("/logout", methods=["POST"])
def logout():
    pass

@app.route('/map', methods=["GET"])
def map():
    pass

@app.route('/restaurant/{name}')
def getRestaurant(name):
    #user
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

    return render_template('restaurant.j2', name=name, address=address, cuisine=cuisine,
                           walk_time=walk_time, type=type, time_range=time_range,
                           price_range=price_range, mon_hrs=mon_hrs, tue_hrs=tue_hrs,
                           wed_hrs=wed_hrs, thu_hrs=thu_hrs, fri_hrs=fri_hrs,
                           sat_hrs=sat_hrs, sun_hrs=sun_hrs, reviews=reviews)


@app.route('/review', methods = ['POST'])
def update_review():
    name = request.form.get("name")
    user = request.form.get("user")
    rating = request.form.get("rating")
    comment = request.form.get("comment")

    if database.update_review(name, user, rating, comment):
        return redirect(f'/restaurant/{name}')

@app.route('/review', methods = ['DELETE'])
def delete_review():
    name = request.form.get("name")
    user = request.form.get("user")
    rating = request.form.get("rating")
    comment = request.form.get("comment")

    if database.delete_review(name, user, rating, comment):
        return redirect(f'/restaurant/{name}')

@app.route('/event', methods = ['POST'])
def create_event():
    pass

@app.route('/event', methods = ['PUT'])
def update_event():
    user = request.form.get("user")

    #figure out user role

@app.route('/event', methods = ['DELETE'])
def delete_event():
    pass

if __name__=='__main__':
    app.run(debug=True)