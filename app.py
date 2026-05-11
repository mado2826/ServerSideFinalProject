from flask import Flask, jsonify, Response, request, send_file, redirect, jsonify, render_template, make_response, flash
import database
import redis

app = Flask(__name__)
app.secret_key = 'skibiditoilet6767'

r = redis.Redis()

@app.route('/')
def start():
    pass

@app.route('/login')
def login():
    pass

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
    id = request.form.get("id")
    user = request.form.get("user")

    #figure out user role
    if (database.is_host()):
        date = request.form.get("date")
        time = request.form.get("time")
        database.update_details(id, date, time)
    else:
        database.toggle_guest(id, user)

@app.route('/event', methods = ['DELETE'])
def delete_event():
    pass