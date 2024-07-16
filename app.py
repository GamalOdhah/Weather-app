from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('weather.html')


@app.route('/note')
def show_note():
    return render_template('note.html')

@app.route('/map')
def show_map():
    return render_template('map.html')


@app.route('/weather', methods=['POST'])
def get_weather():
    APIKey = '78c82cea441ad0ce523d711c2a90d106'
    data = request.get_json()
    city = data.get('city', '').strip()

    if city == '':
        return jsonify({'cod': '400', 'message': 'Invalid city'})

    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={APIKey}')
    weather_data = response.json()

    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
