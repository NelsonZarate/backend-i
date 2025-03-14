import requests


def retrieve_forecast_values(latitude, longitude):
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(url)
    if (response.status_code != 200):
        return None, None
    forecast_url = response.json()['properties']['forecast']
    city = response.json()[
        'properties']['relativeLocation']['properties']['city']
    state = response.json()[
        'properties']['relativeLocation']['properties']['state']
    location = f"{city}, {state}"

    return forecast_url, location

if __name__ == '__main__':
    location_url, location = retrieve_forecast_values(
        '39.0997', '-94.5786')
    print(location_url)
    print(location)
