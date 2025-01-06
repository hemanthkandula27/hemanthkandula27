import requests
import sys

# Function to fetch weather data from OpenWeather API
def get_weather_data(api_key, location, unit):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': unit
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

# Function to display weather information
def display_weather(data, unit):
    if data:
        city = data.get('name')
        country = data['sys'].get('country')
        temperature = data['main'].get('temp')
        humidity = data['main'].get('humidity')
        weather_description = data['weather'][0].get('description')

        temp_unit = '°C' if unit == 'metric' else '°F'

        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temperature}{temp_unit}")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description.capitalize()}")
    else:
        print("Could not retrieve weather data.")

# Function to validate user input for temperature unit
def validate_unit():
    while True:
        unit = input("Enter temperature unit (metric for Celsius, imperial for Fahrenheit): ").strip().lower()
        if unit in ['metric', 'imperial']:
            return unit
        print("Invalid input. Please enter 'metric' or 'imperial'.")

# Function to get a valid location from the user
def validate_location():
    while True:
        location = input("Enter a city or ZIP code: ").strip()
        if location:
            return location
        print("Location cannot be empty. Please try again.")

# Main function to run the weather app
def main():
    print("Welcome to the Basic Weather App")

    # Replace 'your_api_key' with your OpenWeather API key
    api_key = 'your_api_key'

    if not api_key or api_key == 'your_api_key':
        print("Please configure your OpenWeather API key in the code.")
        sys.exit(1)

    # Get user inputs
    location = validate_location()
    unit = validate_unit()

    # Fetch weather data
    weather_data = get_weather_data(api_key, location, unit)

    # Display weather information
    display_weather(weather_data, unit)

if __name__ == "__main__":
    main()