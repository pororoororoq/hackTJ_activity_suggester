from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/home', methods = ['POST'])
def weather_info():
    zipcode = request.form['zip']
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=ac7c75b9937a495021393024d0a90c44')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_f = round((temp_k - 273.15) * 1.8 + 32, 3)
    max_f = round(float((json_object['main']['temp_max'])-273.15) * 1.8 + 32, 3)
    min_f = round(float((json_object['main']['temp_min'])-273.15) * 1.8 + 32, 3)
    humidity = round(float((json_object['main']['humidity'])), 3)
    w_speed = round(float((json_object['wind']['speed'])), 3)
    m_weather = json_object['weather'][0]['main']
    d_weather = json_object['weather'][0]['description']

    activities = ['skiing or snowboarding', 'ice skating', 'sledding', 'hiking', 'birdwatching', 'brisk walks', 'cycling', 'outdoor sports(soccer, baseball, frisbee)', 'gardening', 'picnics', 'outdoor yoga', 'swimming', 'kayaking', 'paddleboarding', 'outdoor workout', 'water parks', 'rafting', 'tubing', 'sunbathing', 'beach volleyball', 'boating', 'floating in a pool or lake', 'jogging', 'fishing', 'barbecue party', 'camping', 'indoor rock climbing', 'low-intensity exercise', 'visiting an outdoor attraction', 'stargazing', 'water aerobics', 'snorkeling', 'scuba diving', 'surfing', 'water skiing and wakeboarding']
    activities = set(activities)
    #Temperature
    if temp_f <= 50:
        remove = {'water parks', 'swimming', 'kayaking', 'paddleboarding', 'boating', 'floating in a pool or lake', 'water aerobics', 'snorkeling', 'scuba diving', 'surfing', 'water skiing and wakeboarding', 'picnics', 'outdoor yoga', 'camping', 'outdoor workout', 'outdoor sports(soccer, baseball, frisbee)', 'hiking', 'cycling', 'rafting', 'tubing', 'sunbathing', 'beach volleyball', 'jogging',  'fishing', 'gardening', 'visiting an outdoor attraction'}
        activities -= remove
        #Notes: Wear appropriate gears such as warm layers, hats, gloves, and scarves.
    elif temp_f <= 60:
        remove = {'skiing or snowboarding', 'ice skating', 'sledding', 'water parks', 'swimming', 'kayaking', 'paddleboarding', 'boating', 'floating in a pool or lake', 'water aerobics', 'snorkeling', 'scuba diving', 'surfing', 'water skiing and wakeboarding', 'picnics', 'outdoor yoga', 'camping', 'rafting', 'tubing', 'sunbathing', 'beach volleyball', 'fishing', 'gardening', 'visiting an outdoor attraction'}
        activities -= remove
        #Notes: Protect your skins from being exposed to windburn.
    elif temp_f <= 70:
        
        remove = ['skiing or snowboarding', 'ice skating', 'sledding', 'water parks', 'swimming', 'kayaking', 'paddleboarding', 'boating', 'floating in a pool or lake', 'water aerobics', 'snorkeling', 'scuba diving', 'surfing', 'water skiing and wakeboarding', 'rafting', 'tubing', 'sunbathing', 'beach volleyball']
        remove = set(remove)
        activities -= remove
        #Notes: Watch out weather conditions such as rain or thunderstorms.
    elif temp_f <= 80:
        remove = ['skiing or snowboarding', 'ice skating', 'sledding', 'water parks', 'rafting', 'tubing', 'sunbathing', 'beach volleyball', 'boating', 'floating in a pool or lake', 'water aerobics', 'snorkeling', 'scuba diving', 'surfing', 'water skiing and wakeboarding']
        remove = set(remove)
        activities -= remove
        #Notes: Stay hydrated and cool down when necessary.
    elif temp_f <= 90:
        remove = ['skiing or snowboarding', 'ice skating', 'sledding']
        remove = set(remove)
        activities -= remove
        #Notes: Wear sunscreens to minimize sun exposure, stay hydrated, and take breaks to avoid exhaustion or heat stroke.
    else:
        remove = ['skiing or snowboarding', 'ice skating', 'sledding', 'hiking', 'birdwatching', 'brisk walks', 'cycling', 'outdoor sports(soccer, baseball, frisbee)', 'gardening', 'picnics', 'outdoor yoga', 'kayaking', 'paddleboarding', 'outdoor workout', 'rafting', 'tubing', 'sunbathing', 'beach volleyball', 'boating', 'jogging', 'fishing', 'barbecue party', 'camping', 'indoor rock climbing', 'low-intensity exercise', 'visiting an outdoor attraction', 'stargazing', 'water aerobics', 'snorkeling', 'scuba diving', 'surfing', 'water skiing and wakeboarding']
        remove = set(remove)
        activities -= remove
        #Notes: Seriously take precautions such as staying hydrated and avoiding direct sun exposure, and choose indoor or water-related activites. The best is to STAY at home. 

    #Wind Speed
    if w_speed >= 20 and w_speed <= 40:
        remove = ['skiing or snowboarding', 'ice skating', 'sledding', 'cycling', 'outdoor sports(soccer, baseball, frisbee)', 'water parks', 'rafting', 'tubing', 'beach volleyball', 'boating', 'floating in a pool or lake', 'surfing', 'water skiing and wakeboarding']
        remove = set(remove)
        activities -= remove
    elif w_speed <= 60:
        remove = activities_not_possible = ['skiing or snowboarding', 'ice skating', 'sledding', 'cycling', 'outdoor sports(soccer, baseball, frisbee)', 'water parks', 'rafting', 'tubing', 'beach volleyball', 'boating', 'floating in a pool or lake', 'jogging', 'fishing', 'barbecue party', 'camping', 'indoor rock climbing', 'low-intensity exercise', 'visiting an outdoor attraction', 'stargazing', 'water aerobics', 'snorkeling', 'scuba diving', 'surfing', 'water skiing and wakeboarding']
        remove = set(remove)
        activities -= remove
    elif w_speed <= 80:
        remove = activities_not_possible = ['skiing or snowboarding', 'ice skating', 'sledding', 'hiking', 'birdwatching', 'brisk walks', 'cycling', 'outdoor sports(soccer, baseball, frisbee)', 'gardening', 'picnics', 'outdoor yoga', 'swimming', 'kayaking', 'paddleboarding', 'outdoor workout', 'water parks', 'rafting', 'tubing', 'sunbathing', 'beach volleyball', 'boating', 'floating in a pool or lake', 'jogging', 'fishing', 'barbecue party', 'camping', 'visiting an outdoor attraction', 'stargazing', 'water aerobics', 'snorkeling', 'scuba diving', 'surfing', 'water skiing and wakeboarding']
        remove = set(remove)
        activities -= remove
    elif w_speed > 80:
        activities = []
        #stay at home if the wind speed is over 80 mph! Perhaps, evacuate if necessary!
 
    
    #Humidity
    if humidity >= 70:
        remove = ['skiing or snowboarding', 'ice skating', 'cycling', 'outdoor sports(soccer, baseball, frisbee)', 'outdoor workout', 'sunbathing', 'beach volleyball', 'barbecue party', 'camping', 'snorkeling', 'scuba diving', 'surfing', 'water skiing and wakeboarding']
        remove = set(remove)
        activities -= remove
    elif humidity <= 30:
        remove = ['skiing or snowboarding', 'ice skating', 'sledding', 'hiking', 'cycling', 'outdoor sports(soccer, baseball, frisbee)', 'gardening', 'picnics', 'swimming', 'kayaking', 'paddleboarding', 'outdoor workout', 'water parks', 'rafting', 'tubing', 'sunbathing', 'beach volleyball', 'boating', 'floating in a pool or lake', 'jogging', 'fishing', 'barbecue party', 'camping', 'water aerobics', 'snorkeling', 'scuba diving', 'surfing', 'water skiing and wakeboarding']
        remove = set(remove)
        activities -= remove

    activities = sorted(activities)
    return render_template('home.html', temp = temp_f, max_temp = max_f, min_temp = min_f, humidity = humidity, wind_speed = w_speed, main_weather = m_weather, description = d_weather, activities = activities)


@app.route('/')
def input_zip():
    return render_template('input_zip.html')



@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run(debug = True)