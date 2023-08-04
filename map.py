from flask import Flask, request
import pandas as pd
import requests

app = Flask(__name__)

@app.route('/journey', methods=['POST'])
def journey():
    origin = request.json['origin']
    destination = request.json['destination']
    api_key = "API KEY"
    
    def get_journey_info(origin, destination, api_key):
        directions_url = f"https://api.mapbox.com/directions/v5/mapbox/driving/{origin[0]},{origin[1]};{destination[0]},{destination[1]}?access_token={api_key}"
        response = requests.get(directions_url)
        journey_data = response.json()
        journey_time = journey_data['routes'][0]['duration']
        return journey_time

    def create_journey_database(origin, destination, countries, journey_time):
        data = {'Origin': [origin],
                'Destination': [destination],
                'Countries': [countries],
                'Journey Time': [journey_time]}
        df = pd.DataFrame(data)
        return df

    def main(origin, destination, api_key):
        journey_time = get_journey_info(origin, destination, api_key)
        journey_df = create_journey_database(origin, destination, countries, journey_time)
        return journey_df.to_json(orient='records')

    journey_data = main(origin, destination, api_key)
    return journey_data

if __name__ == '__main__':
    app.run()