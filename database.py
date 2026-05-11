import sqlite3
import json

''' Creates table to store restaurant information and reviews, if not already created'''
def database_init():

    __db = sqlite3.connect("restaurants.db")

    table_restaurants = 'CREATE TABLE IF NOT EXISTS restaurants (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE, address TEXT, cuisine TEXT, walk_time TEXT, type TEXT, time_range TEXT, price_range TEXT, mon_hrs TEXT, tue_hrs TEXT, wed_hrs TEXT, thu_hrs TEXT, fri_hrs TEXT, sat_hrs TEXT, sun_hrs TEXT);'
    __db.execute(table_restaurants)
    table_reviews = 'CREATE TABLE IF NOT EXISTS reviews (id INTEGER PRIMARY KEY AUTOINCREMENT, restaurant TEXT, user TEXT NOT NULL, rating INTEGER CHECK (rating >= 1 AND rating <= 5), comment TEXT);'
    __db.execute(table_reviews)
    table_events = 'CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY AUTOINCREMENT, restaurant TEXT, host TEXT, guest_list TEXT, date TEXT, time TEXT);'
    __db.execute(table_events)

    __db.commit()
    __db.close()

'''
    Adds all data to the restaurant table, if not already in table
        
    @return True if data insertion successful
'''
def database_fill() -> bool:
    table_insert = "INSERT INTO restaurants (name, address, cuisine, walk_time, type, time_range, price_range, mon_hrs, tue_hrs, wed_hrs, thu_hrs, fri_hrs, sat_hrs, sun_hrs) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"

    #Sanitation process
    #Give SQL command and tuple
    __db = sqlite3.connect("restaurants.db")
    try:
        __db.execute(table_insert, ('Alpaca Chicken', '703 9th St', 'Peruvian', '16 min', 'Fast Casual', '10-20 mins', '$5-15', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm'))
        __db.execute(table_insert, ("Banh's Cuisine", '750 9th St', 'Vietnamese', '14 min', 'Sit-Down', '30-60 mins', '$10-20', '11am-8pm', '11am-8pm', '11am-8pm', '11am-8pm', '11am-8pm', '11am-8pm', 'Closed'))
        __db.execute(table_insert, ("Bruegger's Bagels", '626 9th St', 'Bagels', '16 min', 'Fast Casual', '10-20 mins', '$5-10', '6am-2pm', '6am-2pm', '6am-2pm', '6am-2pm', '6am-2pm', '6am-2pm', '6am-2pm'))
        __db.execute(table_insert, ('Chicken Bee', '810 9th St Ste 129', 'Korean', '10 min', 'Fast Casual', '10-20 mins', '$10-20', 'Closed', '11:30am-9pm', '11:30am-9pm', '11:30am-9pm', '11:30am-9pm', '11:30am-9pm', '12pm-9pm'))
        __db.execute(table_insert, ('Chipotle Mexican Grill', '737 9th St', 'Mexican', '13 min', 'Fast Casual', '10-20 mins', '$10-15', '10:45am-10pm', '10:45am-10pm', '10:45am-10pm', '10:45am-10pm', '10:45am-10pm', '10:45am-10pm', '10:45am-10pm'))
        __db.execute(table_insert, ('Cloche Coffee', '721 Broad St Ste 116', 'Coffee', '13 min', 'Cafe', '15-30 mins', '$5-10', '7am-7pm', '7am-7pm', '7am-7pm', '7am-7pm', '7am-7pm', '7am-7pm', '7am-7pm'))
        __db.execute(table_insert, ('Common Market Durham', '1821 Green St', 'Sandwiches', '9 min', 'Cafe', '10-20 mins', '$10-15', '7am-8pm', '7am-10pm', '7am-10pm', '7am-10pm', '7am-10pm', '8am-10pm', '8am-8pm'))
        __db.execute(table_insert, ('Cosmic Cantina', '1920 Perry St', 'Mexican', '16 min', 'Fast Casual', '10-25 mins', '$5-15', '11am-4am', '11am-4am', '11am-4am', '11am-4am', '11am-4am', '11am-4am', '11am-4am'))
        __db.execute(table_insert, ("Dain's Place", '754 9th St', 'American', '13 min', 'Sit-Down / Bar', '45-90 mins', '$10-20', '11am-12am', '11am-12am', '11am-12am', '11am-12am', '11am-12am', '11am-12am', '11am-12am'))
        __db.execute(table_insert, ("Devil's NY Pizzeria", '742 9th St', 'Pizza', '14 min', 'Fast Casual', '5-15 mins', '$5-15', '11am-10pm', '11am-10pm', '11am-10pm', '11am-10pm', '11am-10pm', '11am-10pm', '11am-10pm'))
        __db.execute(table_insert, ("Elmo's Diner", '776 9th St', 'Diner', '12 min', 'Sit-Down', '30-60 mins', '$10-20', '7am-3pm', '7am-3pm', '7am-3pm', '7am-3pm', '7am-3pm', '7am-3:30pm', '7am-3:30pm'))
        __db.execute(table_insert, ('Happy + Hale', '703B 9th St', 'Healthy Bowls', '16 min', 'Fast Casual', '10-20 mins', '$10-20', '8am-8pm', '8am-8pm', '8am-8pm', '8am-8pm', '8am-8pm', '8am-8pm', '8am-8pm'))
        __db.execute(table_insert, ('Harris Teeter', '2107 Hillsborough Rd', 'Grocery', '14 min', 'Grocery', '10-30 mins', '$5-20', '6am-11pm', '6am-11pm', '6am-11pm', '6am-11pm', '6am-11pm', '6am-11pm', '6am-11pm'))
        __db.execute(table_insert, ('Hops and Flower', '2014 Hillsborough Rd', 'Sandwiches', '12 min', 'Fast Casual', '5-15 mins', '$10-15', '8am-8pm', '8am-8pm', '8am-8pm', '8am-8pm', '8am-8pm', '8am-8pm', '8am-8pm'))
        __db.execute(table_insert, ('International Delights', '740 9th St', 'Mediterranean', '14 min', 'Fast Casual', '10-20 mins', '$5-15', 'Closed', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm', '12pm-9pm', '12pm-9pm'))
        __db.execute(table_insert, ('Juju Durham', '737 9th St #210', 'Asian Fusion', '13 min', 'Sit-Down', '45-90 mins', '$15-30', '11am-2pm, 5-9pm', '11am-2pm, 5-9pm', '11am-2pm, 5-9pm', '11am-2pm, 5-9pm', '11am-2pm, 5-9pm', '11am-2pm, 5-9pm', '5-9pm'))
        __db.execute(table_insert, ("Jimmy John's", '701 9th St', 'Sandwiches', '16 min', 'Fast Casual', '5-15 mins', '$5-15', '10am-10pm', '10am-10pm', '10am-10pm', '10am-10pm', '10am-10pm', '10am-10pm', '10am-10pm'))
        __db.execute(table_insert, ('Kabab and Curry Durham', '716 9th St', 'Indian', '15 min', 'Sit-Down', '20-45 mins', '$10-20', '11:30am-10pm', '11:30am-10pm', '11:30am-10pm', '11:30am-10pm', '11:30am-10pm', '11:30am-10pm', '11:30am-10pm'))
        __db.execute(table_insert, ('Kiichi Ramen', '730 9th St', 'Japanese', '14 min', 'Sit-Down', '30-60 mins', '$10-20', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm'))
        __db.execute(table_insert, ('Koi Sushi & Hibachi', '607 Broad St', 'Japanese', '18 min', 'Sit-Down', '45-90 mins', '$15-35', '11am-3pm, 4-9:30pm', '11am-3pm, 4-9:30pm', '11am-3pm, 4-9:30pm', '11am-3pm, 4-9:30pm', '11am-3pm, 4-10pm', '11am-10pm', '11am-9:30pm'))
        __db.execute(table_insert, ('Lime & Lemon Indian Grill', '811 9th St', 'Indian', '10 min', 'Sit-Down', '45-90 mins', '$15-25', '11:30am-9pm', '11:30am-9pm', '11:30am-9pm', '11:30am-9pm', '11:30am-9:30pm', '11:30am-9:30pm', '11:30am-9pm'))
        __db.execute(table_insert, ('Locopops', '2618 Hillsborough Rd', 'Ice Cream', '22 min', 'To-Go', '5-15 mins', '$5-10', '12pm-9pm', '12pm-9pm', '12pm-9pm', '12pm-9pm', '12pm-9pm', '12pm-9pm', '12pm-9pm'))
        __db.execute(table_insert, ('The Loop Restaurant', '1116 Broad St', 'American', '2 min', 'Sit-Down', '30-60 mins', '$10-20', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm'))
        __db.execute(table_insert, ('Mad Hatter Cafe + Bakeshop', '1802 W Main St', 'Bakery', '18 min', 'Cafe / Sit-Down', '20-45 mins', '$5-15', '7am-4pm', '7am-4pm', '7am-4pm', '7am-4pm', '7am-4pm', '7am-4pm', '8am-4pm'))
        __db.execute(table_insert, ('Metro 8 Steakhouse', '1116 Broad St', 'Steakhouse', '2 min', 'Sit-Down', '60-120 mins', '$30-70', 'Closed', '5-9pm', '5-9pm', '5-9pm', '5-9pm', '5-9pm', 'Closed'))
        __db.execute(table_insert, ('Mi Calvillo Antojitos Mexicanos', '748 9th St', 'Mexican', '14 min', 'Fast Casual', '10-20 mins', '$10-15', '10am-9:30pm', '10am-9:30pm', '10am-9:30pm', '10am-9:30pm', '10am-10pm', '10:30am-10pm', '11am-9pm'))
        __db.execute(table_insert, ('Mid-Bloom Coffee', '1821 Green St', 'Coffee', '9 min', 'Cafe', '10-20 mins', '$5-10', '7am-3pm', '7am-3pm', '7am-3pm', '7am-3pm', '7am-3pm', '8am-3pm', '8am-3pm'))
        __db.execute(table_insert, ('MOGE TEE', '760 9th St', 'Boba Tea', '13 min', 'To-Go', '5-15 mins', '$5-10', '11:30am-9pm', '11:30am-9pm', '11:30am-9pm', '11:30am-9pm', '11:30am-10pm', '11:30am-10pm', '11:30am-9pm'))
        __db.execute(table_insert, ('Monuts', '1002 9th St', 'Cafe', '7 min', 'Cafe', '15-30 mins', '$5-15', 'Closed', '7am-5pm', '7am-5pm', '7am-5pm', '7am-5pm', '8am-5pm', 'Closed'))
        __db.execute(table_insert, ('Nan Xiang Express', '1605 Erwin Rd #50', 'Chinese', '20 min', 'Fast Casual', '15-30 mins', '$10-20', '11am-10pm', '11am-10pm', '11am-10pm', '11am-10pm', '11am-11pm', '11am-11pm', '11am-10pm'))
        __db.execute(table_insert, ('Nosh', '717 Broad St', 'American', '14 min', 'Cafe / Sit-Down', '20-45 mins', '$10-15', '8am-3pm', '8am-3pm', '8am-3pm', '8am-3pm', '8am-3pm', '8am-3pm', '8am-3pm'))
        __db.execute(table_insert, ('Panera Bread', '737 9th St #200', 'Sandwiches', '14 min', 'Fast Casual', '15-30 mins', '$10-15', '7am-9pm', '7am-9pm', '7am-9pm', '7am-9pm', '7am-9pm', '7am-9pm', '7am-9pm'))
        __db.execute(table_insert, ('Pincho Loco Ice Cream', '1918 Perry St', 'Ice Cream', '16 min', 'To-Go', '5-15 mins', '$5-10', 'Closed', '12pm-10pm', '12pm-10pm', '12pm-10pm', '12pm-10pm', '12pm-10pm', '12pm-10pm'))
        __db.execute(table_insert, ('Playa Bowls', '744B 9th St', 'Acai Bowls', '14 min', 'Fast Casual', '10-20 mins', '$10-15', '8am-9pm', '8am-9pm', '8am-9pm', '8am-9pm', '8am-9pm', '8am-9pm', '8am-9pm'))
        __db.execute(table_insert, ('Quickly Tea House', '2604A Hillsborough Rd', 'Boba Tea', '22 min', 'To-Go', '5-15 mins', '$5-10', 'Closed', '12pm-9pm', '12pm-9pm', '12pm-9pm', '12pm-9pm', '12pm-9pm', '12pm-9pm'))
        __db.execute(table_insert, ('Sho Nuff Seafood', '1104 Broad St', 'Seafood', '3 min', 'Fast Casual', '20-40 mins', '$10-20', 'Closed', '11am-8pm', '11am-8pm', '11am-9pm', '11am-9pm', '11am-9pm', '12pm-6pm'))
        __db.execute(table_insert, ('Starbucks', '706 9th St', 'Coffee', '15 min', 'To-Go (Kiosk)', '5-10 mins', '$5-10', '5am-9pm', '5am-9pm', '5am-9pm', '5am-9pm', '5am-9pm', '5am-9pm', '5am-9pm'))
        __db.execute(table_insert, ('Szechuan Mansion Hotpot', '746 9th St', 'Chinese', '14 min', 'Sit-Down', '60-120 mins', '$20-40', '11:30am-9:30pm', '11:30am-9:30pm', '11:30am-9:30pm', '11:30am-9:30pm', '11:30am-10pm', '11:30am-10pm', '11:30am-9:30pm'))
        __db.execute(table_insert, ('Tsaocha Durham', '1605 Erwin Rd', 'Boba Tea', '20 min', 'Fast Casual', '10-20 mins', '$5-15', '11am-10pm', '11am-10pm', '11am-10pm', '11am-10pm', '11am-11pm', '11am-11pm', '11am-10pm'))
        __db.execute(table_insert, ('Vin Rouge', '2010 Hillsborough Rd', 'French', '12 min', 'Sit-Down', '60-120 mins', '$30-60', 'Closed', '5-9pm', '5-9pm', '5-9pm', '5-9pm', '5-9pm', '10:30am-2pm, 5-9pm'))
        __db.execute(table_insert, ('Wheat', '810 9th St Ste 130', 'Chinese', '10 min', 'Sit-Down', '20-40 mins', '$10-20', '11:30am-9pm', '11:30am-9pm', '11:30am-9pm', '11:30am-9pm', '11:30am-9pm', '11:30am-9pm', '11:30am-9pm'))
        __db.execute(table_insert, ('Whole Foods Market', '621 Broad St', 'Grocery', '17 min', 'Grocery', '10-30 mins', '$10-20', '8am-10pm', '8am-10pm', '8am-10pm', '8am-10pm', '8am-10pm', '8am-10pm', '8am-10pm'))
        __db.execute(table_insert, ('ZenFish Poke Bar', '810 9th St', 'Poke', '10 min', 'Fast Casual', '10-20 mins', '$10-20', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm', '11am-9pm'))
    except:
        #not unique
        __db.close()
        return False
    
    __db.commit()
    __db.close()
    return True

#____________________________________________________________________________________________________________________
#RESTAURANT-RELATED METHODS

'''
    Returns the address of the restaurant with the specified name

    @param name the restaurant name

    @return the address of the restaurant if it's in the database, None otherwise
'''
def get_address(name):
    address_get = "SELECT address FROM restaurants WHERE name = ?"

    __db = sqlite3.connect("restaurants.db")
    address = __db.execute(address_get, (name,)).fetchone()
    __db.close()

    if address:
        return address[0]
    else:
        return None

'''
    Returns the cuisine of the restaurant with the specified name

    @param name the restaurant name

    @return the cuisine of the restaurant if it's in the database, None otherwise
'''
def get_cuisine(name):
    cuisine_get = "SELECT cuisine FROM restaurants WHERE name = ?"

    __db = sqlite3.connect("restaurants.db")
    cuisine = __db.execute(cuisine_get, (name,)).fetchone()
    __db.close()

    if cuisine:
        return cuisine[0]
    else:
        return None

'''
    Returns the walk time to the restaurant with the specified name

    @param name the restaurant name

    @return the walk time of the restaurant if it's in the database, None otherwise
'''
def get_walk_time(name):
    walk_time_get = "SELECT walk_time FROM restaurants WHERE name = ?"

    __db = sqlite3.connect("restaurants.db")
    walk_time = __db.execute(walk_time_get, (name,)).fetchone()
    __db.close()

    if walk_time:
        return walk_time[0]
    else:
        return None

'''
    Returns the type of the restaurant with the specified name

    @param name the restaurant name

    @return the type of the restaurant if it's in the database, None otherwise
'''
def get_type(name):
    type_get = "SELECT type FROM restaurants WHERE name = ?"

    __db = sqlite3.connect("restaurants.db")
    type_ = __db.execute(type_get, (name,)).fetchone()
    __db.close()

    if type_:
        return type_[0]
    else:
        return None

'''
    Returns the time range of the restaurant with the specified name

    @param name the restaurant name

    @return the time range of the restaurant if it's in the database, None otherwise
'''
def get_time_range(name):
    time_range_get = "SELECT time_range FROM restaurants WHERE name = ?"

    __db = sqlite3.connect("restaurants.db")
    time_range = __db.execute(time_range_get, (name,)).fetchone()
    __db.close()

    if time_range:
        return time_range[0]
    else:
        return None

'''
    Returns the price range of the restaurant with the specified name

    @param name the restaurant name

    @return the price range of the restaurant if it's in the database, None otherwise
'''
def get_price_range(name):
    price_range_get = "SELECT price_range FROM restaurants WHERE name = ?"

    __db = sqlite3.connect("restaurants.db")
    price_range = __db.execute(price_range_get, (name,)).fetchone()
    __db.close()

    if price_range:
        return price_range[0]
    else:
        return None

'''
    Returns the Monday hours of the restaurant with the specified name

    @param name the restaurant name

    @return the Monday hours of the restaurant if it's in the database, None otherwise
'''
def get_mon_hrs(name):
    mon_hrs_get = "SELECT mon_hrs FROM restaurants WHERE name = ?"

    __db = sqlite3.connect("restaurants.db")
    mon_hrs = __db.execute(mon_hrs_get, (name,)).fetchone()
    __db.close()

    if mon_hrs:
        return mon_hrs[0]
    else:
        return None

'''
    Returns the Tuesday hours of the restaurant with the specified name

    @param name the restaurant name

    @return the Tuesday hours of the restaurant if it's in the database, None otherwise
'''
def get_tue_hrs(name):
    tue_hrs_get = "SELECT tue_hrs FROM restaurants WHERE name = ?"

    __db = sqlite3.connect("restaurants.db")
    tue_hrs = __db.execute(tue_hrs_get, (name,)).fetchone()
    __db.close()

    if tue_hrs:
        return tue_hrs[0]
    else:
        return None

'''
    Returns the Wednesday hours of the restaurant with the specified name

    @param name the restaurant name

    @return the Wednesday hours of the restaurant if it's in the database, None otherwise
'''
def get_wed_hrs(name):
    wed_hrs_get = "SELECT wed_hrs FROM restaurants WHERE name = ?"

    __db = sqlite3.connect("restaurants.db")
    wed_hrs = __db.execute(wed_hrs_get, (name,)).fetchone()
    __db.close()

    if wed_hrs:
        return wed_hrs[0]
    else:
        return None

'''
    Returns the Thursday hours of the restaurant with the specified name

    @param name the restaurant name

    @return the Thursday hours of the restaurant if it's in the database, None otherwise
'''
def get_thu_hrs(name):
    thu_hrs_get = "SELECT thu_hrs FROM restaurants WHERE name = ?"

    __db = sqlite3.connect("restaurants.db")
    thu_hrs = __db.execute(thu_hrs_get, (name,)).fetchone()
    __db.close()

    if thu_hrs:
        return thu_hrs[0]
    else:
        return None

'''
    Returns the Friday hours of the restaurant with the specified name

    @param name the restaurant name

    @return the Friday hours of the restaurant if it's in the database, None otherwise
'''
def get_fri_hrs(name):
    fri_hrs_get = "SELECT fri_hrs FROM restaurants WHERE name = ?"

    __db = sqlite3.connect("restaurants.db")
    fri_hrs = __db.execute(fri_hrs_get, (name,)).fetchone()
    __db.close()

    if fri_hrs:
        return fri_hrs[0]
    else:
        return None

'''
    Returns the Saturday hours of the restaurant with the specified name

    @param name the restaurant name

    @return the Saturday hours of the restaurant if it's in the database, None otherwise
'''
def get_sat_hrs(name):
    sat_hrs_get = "SELECT sat_hrs FROM restaurants WHERE name = ?"

    __db = sqlite3.connect("restaurants.db")
    sat_hrs = __db.execute(sat_hrs_get, (name,)).fetchone()
    __db.close()

    if sat_hrs:
        return sat_hrs[0]
    else:
        return None

'''
    Returns the Sunday hours of the restaurant with the specified name

    @param name the restaurant name

    @return the Sunday hours of the restaurant if it's in the database, None otherwise
'''
def get_sun_hrs(name):
    sun_hrs_get = "SELECT sun_hrs FROM restaurants WHERE name = ?"

    __db = sqlite3.connect("restaurants.db")
    sun_hrs = __db.execute(sun_hrs_get, (name,)).fetchone()
    __db.close()

    if sun_hrs:
        return sun_hrs[0]
    else:
        return None

#____________________________________________________________________________________________________________________
#REVIEW-RELATED METHODS

'''
    Returns all reviews of the restaurant with the specified name

    @param name the restaurant name

    @return all rows from the database that match the restaurant parameter
'''
def get_reviews(name):
    reviews_get = "SELECT rating, comment FROM reviews WHERE restaurant = ?"

    __db = sqlite3.connect("restaurants.db")
    reviews = __db.execute(reviews_get, (name,)).fetchall()
    __db.close()

    if reviews:
        return reviews
    else:
        return None

'''
    Updates a user's review of the restaurant with the specified name, adding a row to the reviews table if needed

    @param name the restaurant name
    @param user the user giving the rating
    @param rating the user's numerical rating from 1-5
    @param comment the user's optional comment on the restaurant

    @return True if update successful, False otherwise
'''
def update_review(name, user, rating, comment):
    review_find = "SELECT * FROM reviews WHERE restaurant = ? AND user = ?"
    review_add = "INSERT INTO reviews (restaurant, user, rating, comment) VALUES (?, ?, ?, ?)"
    review_update = "UPDATE reviews SET rating = ?, comment = ? WHERE restaurant = ? AND user = ?"
    
    __db = sqlite3.connect("restaurants.db")

    #CHECK FOR REVIEW
    review = __db.execute(review_find, (name, user)).fetchone()

    #add a review or update existing one
    if review:
        try:
            __db.execute(review_update, (rating, comment, name, user))
            __db.commit()
            __db.close()
            return True
        except:
            __db.close()
            return False
    else:
        try:
            __db.execute(review_add, (name, user, rating, comment))
            __db.commit()
            __db.close()
            return True
        except:
            __db.close()
            return False

'''
    Deletes a user's review of the restaurant with the specified name, if they have one

    @param name the restaurant name
    @param user the user giving the rating

    @return True if deletion successful, False otherwise
'''
def delete_review(name, user):
    review_find = "SELECT * FROM reviews WHERE restaurant = ? AND user = ?"
    review_delete = "DELETE FROM reviews WHERE restaurant = ? AND user = ?"
    
    __db = sqlite3.connect("restaurants.db")

    #CHECK FOR REVIEW
    review = __db.execute(review_find, (name, user)).fetchone()

    #delete review if exists
    if review:
        try:
            __db.execute(review_delete, (name, user))
            __db.commit()
            __db.close()
            return True
        except:
            __db.close()
            return False
    __db.close()
    return False

'''
    Calculates/returns the average rating of all the reviews of the restaurant with the specified name

    @param name the restaurant name

    @return the average of the rating values, rounded to the tenth
'''
def avg_rating(name):
    ratings_get = "SELECT rating FROM reviews WHERE restaurant = ?"

    __db = sqlite3.connect("restaurants.db")
    ratings = __db.execute(ratings_get, (name,)).fetchall()
    __db.close()

    #calculate!
    if ratings:
        avg = float(sum(r[0] for r in ratings)) / float(len(ratings))
        return round(avg, 1)
    
#____________________________________________________________________________________________________________________
#EVENT-RELATED METHODS

'''
    Returns all events at the restaurant with the specified name

    @param name the restaurant name

    @return all rows from the events table that match the restaurant parameter
'''
def get_restaurant_events(name):
    events_get = "SELECT * FROM events WHERE restaurant = ?"

    __db = sqlite3.connect("restaurants.db")
    events = __db.execute(events_get, (name,)).fetchall()
    __db.close()
    return events

'''
    Creates a new event at the specified restaurant with an empty guest list

    @param location the restaurant name
    @param host the user hosting the event
    @param date the date of the event
    @param time the time of the event

    @return True if creation successful, False otherwise
'''
def create_event(location, host, date, time):
    make_event = "INSERT INTO events (restaurant, host, guest_list, date, time) VALUES (?, ?, ?, ?, ?)"
    __db = sqlite3.connect("restaurants.db")

    try:
        __db.execute(make_event, (location, host, "[]", date, time))
        __db.commit()
        __db.close()
        return True
    except:
        __db.close()
        return False
    
'''
    Checks whether the specified user is the host of the event with the given id

    @param id the event id
    @param user the user to check

    @return True if the user is the host of the event, False otherwise
'''
def is_host(id, user):
    get_host = "SELECT host FROM events WHERE id = ?"
    __db = sqlite3.connect("restaurants.db")
    host = __db.execute(get_host, (id,)).fetchone()
    __db.close()

    return host[0] == user

'''
    Toggles the specified guest on or off the guest list of the event with the given id,
    adding them if not present or removing them if already on the list

    @param id the event id
    @param guest the guest to add or remove

    @return True if update successful, False otherwise
'''
def toggle_guest(id, guest):
    get_guests = "SELECT guest_list FROM events WHERE id = ?"
    guest_update = "UPDATE events SET guest_list = ? WHERE id = ?"

    __db = sqlite3.connect("restaurants.db")
    guest_list = __db.execute(get_guests, (id,)).fetchone()
    guest_arr = json.loads(guest_list)
    delete_guest = False

    for g in guest_arr:
        if g == guest:
            delete_guest = True
            break
    
    if delete_guest:
        guest_arr.remove(guest)
    else:
        guest_arr.append(guest)
    
    guest_list = json.dumps(guest_arr)

    try:
        __db.execute(guest_update, (guest_list, id))
        __db.commit()
        __db.close()
        return True
    except:
        __db.close()
        return False

'''
    Updates the date and/or time of the event with the given id

    @param id the event id
    @param date the new date of the event, or None to leave unchanged
    @param time the new time of the event, or None to leave unchanged

    @return True if update successful, False otherwise
'''
def update_details(id, date=None, time=None):
    details_update = "UPDATE events SET date = ?, time = ? WHERE id = ?"
    date_update = "UPDATE events SET date = ? WHERE id = ?"
    time_update = "UPDATE events SET time = ? WHERE id = ?"
    __db = sqlite3.connect("restaurants.db")
    
    if (date != None and time != None):
        try:
            __db.execute(details_update, (date, time, id))
            __db.commit()
            __db.close()
            return True
        except:
            __db.close()
            return False
    elif (date == None and time != None):
        try:
            __db.execute(time_update, (time, id))
            __db.commit()
            __db.close()
            return True
        except:
            __db.close()
            return False
    if (date != None and time == None):
        try:
            __db.execute(date_update, (date, id))
            __db.commit()
            __db.close()
            return True
        except:
            __db.close()
            return False
    __db.close()
    return False
    

'''
    Deletes the event with the specified id, if it exists

    @param id the event id

    @return True if deletion successful, False otherwise
'''
def delete_event(id):
    event_find = "SELECT * FROM events WHERE id = ?"
    event_delete = "DELETE FROM events WHERE id = ?"
    __db = sqlite3.connect("restaurants.db")

    #CHECK FOR REVIEW
    review = __db.execute(event_find, (id,)).fetchone()

    #delete review if exists
    if review:
        try:
            __db.execute(event_delete, (id,))
            __db.commit()
            __db.close()
            return True
        except:
            __db.close()
            return False
    __db.close()
    return False

#____________________________________________________________________________________________________________________
if __name__ == "__main__":
    #completes part 2 tasks
    database_init()
    database_fill()