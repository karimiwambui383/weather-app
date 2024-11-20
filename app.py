import tkinter as tk
from tkinter import messagebox
import requests

# Function to get weather data
def get_weather():
    city = city_entry.get()
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            # Display the weather information
            result_text = f"Weather in {city}:\n" \
                          f"Description: {weather_description}\n" \
                          f"Temperature: {temperature}°C\n" \
                          f"Humidity: {humidity}%\n" \
                          f"Wind Speed: {wind_speed} m/s"
            messagebox.showinfo("Weather Info", result_text)
        else:
            messagebox.showerror("Error", "City not found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and place the widgets
city_label = tk.Label(root, text="Enter City Name:")
city_label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=10)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=20)

# Start the main loop
root.mainloop()
