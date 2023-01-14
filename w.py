from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/weather/<city>')
def weather(city):
    # Make a request to OpenWeatherMap's API to get the weather for the specified city
    api_key = '<YOUR_API_KEY>'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    r = requests.get(url)
    data = r.json()
    
    # Extract the relevant information from the API response
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']
    
    # Create a dictionary to store the weather data
    weather_data = {
        'temp': temp,
        'humidity': humidity,
        'description': weather_description
    }
    
    # Return the weather data in JSON format
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)