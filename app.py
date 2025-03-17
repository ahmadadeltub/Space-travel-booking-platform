from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# In-memory storage for bookings
bookings = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        departure_date = request.form['departure_date']
        destination = request.form['destination']
        seat_class = request.form['seat_class']
        booking = {
            'departure_date': departure_date,
            'destination': destination,
            'seat_class': seat_class
        }
        bookings.append(booking)
        return redirect(url_for('dashboard'))
    return render_template('book.html')

@app.route('/pricing')
def pricing():
    packages = [
        {'name': 'Luxury Cabin', 'price': '$100,000', 'description': 'Experience the pinnacle of comfort and style in space.'},
        {'name': 'Economy Shuttle', 'price': '$50,000', 'description': 'Affordable travel without compromising the thrill.'},
        {'name': 'VIP Zero-Gravity', 'price': '$150,000', 'description': 'Enjoy exclusive zero-gravity experiences with premium service.'}
    ]
    return render_template('pricing.html', packages=packages)

@app.route('/accommodations')
def accommodations():
    accommodations_list = [
        {'name': 'Orbital Station Alpha', 'type': 'Space Hotel', 'description': 'Luxury accommodations with breathtaking views of Earth.'},
        {'name': 'Lunar Lodge', 'type': 'Lunar Hotel', 'description': 'Experience serenity on the moon’s surface.'},
        {'name': 'Mars Resort', 'type': 'Space Resort', 'description': 'A unique getaway on the red planet.'}
    ]
    return render_template('accommodations.html', accommodations=accommodations_list)

@app.route('/dashboard')
def dashboard():
    now = datetime.datetime.now()
    next_departure = None
    countdown = None
    if bookings:
        sorted_bookings = sorted(bookings, key=lambda x: x['departure_date'])
        for booking in sorted_bookings:
            departure = datetime.datetime.strptime(booking['departure_date'], '%Y-%m-%d')
            if departure > now:
                next_departure = departure
                countdown = departure - now
                break
    travel_tips = "Tip: Pack light, stay curious, and always enjoy the view of Earth from above!"
    return render_template('dashboard.html', bookings=bookings, countdown=countdown, travel_tips=travel_tips)

if __name__ == '__main__':
    app.run(debug=True)
