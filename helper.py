from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route('/get_journey_info', methods=['POST'])
def get_journey_info():
    origin = request.form['origin']
    destination = request.form['destination']
    api_key = request.form['api_key']
    
    directions_url = f"https://api.mapbox.com/datasets/v1/{USER}/{dataset_id}/features/{feature_id}{origin[0]},{origin[1]};{destination[0]},{destination[1]}?geometries=geojson&access_token={API KEY)"
    response = requests.get(directions_url)
    journey_data = response.json()
    journey_time = journey_data['routes'][0]['duration']
    
    return journey_time

@app.route('/create_journey_database', methods=['POST'])
def create_journey_database():
    origin = request.form['origin']
    destination = request.form['destination']
    countries = request.form['countries']
    journey_time = request.form['journey_time']
    
    data = {'Origin': [origin],
            'Destination': [destination],
            'Countries': [countries],
            'Journey Time': [journey_time]}
    df = pd.DataFrame(data)
    
    return df.to_json()

if __name__ == '__main__':
    app.run(debug=True)