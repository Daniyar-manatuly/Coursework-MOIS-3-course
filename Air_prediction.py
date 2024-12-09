import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from tkinter import Tk, Label, Entry, Button, StringVar, Frame, messagebox
import requests

# OpenWeatherMap API Key
OPENWEATHER_API_KEY = "ba1ce234257b1beb413035f614c91575"

# Load dataset
file_path = r"C:/Users/opste/Downloads/astana_air_quality_2000_2024.csv"
data = pd.read_csv(file_path)

# Preprocess data
data = data.dropna()  # Remove rows with missing values
features = ['Temperature', 'Humidity', 'Wind Speed', 'PM2.5', 'PM10']  # Relevant features
target = 'AQI'

X = data[features]
y = data[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model_rf = RandomForestRegressor(random_state=42)
model_rf.fit(X_train, y_train)

# Function to fetch data from OpenWeatherMap API
def get_weather_data():
    try:
        # Get current weather data from OpenWeatherMap
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q=Astana&units=metric&appid={OPENWEATHER_API_KEY}"
        response = requests.get(weather_url)
        data = response.json()

        # Extract necessary values
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        return temp, humidity, wind_speed
    except Exception as e:
        raise ValueError(f"Error fetching weather data: {e}")

# Function to predict AQI with user inputs
def predict_aqi(temp, humidity, wind_speed):
    try:
        # Use historical averages for PM2.5 and PM10
        avg_pm25 = data['PM2.5'].mean()
        avg_pm10 = data['PM10'].mean()


        input_data = pd.DataFrame(
            [[temp, humidity, wind_speed, avg_pm25, avg_pm10]],
            columns=features
        )

        # Make prediction
        prediction = model_rf.predict(input_data)[0]
        return prediction
    except Exception as e:
        raise ValueError(f"Error in prediction: {e}")

def interpret_aqi(aqi_value):
    if aqi_value <= 50:
        return "Good"
    elif aqi_value <= 100:
        return "Moderate"
    elif aqi_value <= 150:
        return "Unhealthy for Sensitive GroupsUnhealthy for Sensitive GroupsModer"
    elif aqi_value <= 200:
        return "Unhealthy"
    elif aqi_value <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

def update_color(aqi_value):
    if aqi_value <= 50:
        return "#00FF00"  # Green
    elif aqi_value <= 100:
        return "#FFFF00"  # Yellow
    elif aqi_value <= 150:
        return "#FFA500"  # Orange
    elif aqi_value <= 200:
        return "#FF0000"  # Red
    elif aqi_value <= 300:
        return "#800080"  # Purple
    else:
        return "#800000"  # Maroon

# Function to predict AQI and update the UI
def predict_and_update_ui(temp, humidity, wind_speed):
    try:
        result = predict_aqi(temp, humidity, wind_speed)
        interpretation = interpret_aqi(result)
        color = update_color(result)

        frame.config(bg=color)

        messagebox.showinfo(
            "Prediction Result",
            f"The predicted AQI is: {result:.2f}\nAir Quality: {interpretation}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Update data function modified to update color
def update_data():
    try:
        # Get data from OpenWeatherMap API
        temp, humidity, wind_speed = get_weather_data()

        # Update the Tkinter entries with fetched data
        temp_var.set(f"{temp:.1f}")
        humidity_var.set(f"{humidity}")
        wind_speed_var.set(f"{wind_speed:.1f}")

        # Predict AQI and update UI
        predict_and_update_ui(temp, humidity, wind_speed)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def handle_predict_button():
    try:
        temp = float(temp_var.get())
        humidity = float(humidity_var.get())
        wind_speed = float(wind_speed_var.get())

        predict_and_update_ui(temp, humidity, wind_speed)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to predict AQI: {e}")

root = Tk()
root.title("Air Quality Prediction - Astana")

root.geometry("450x350")
root.config(bg="#f0f0f0")

# Frame for the main content
frame = Frame(root, bg="#f0f0f0")
frame.pack(padx=20, pady=20)

title_label = Label(frame, text="Air Quality Prediction (Astana)", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

temp_label = Label(frame, text="Temperature (°C):", font=("Helvetica", 12), bg="#f0f0f0")
temp_label.grid(row=1, column=0, pady=5, sticky="w")

temp_var = StringVar()
temp_entry = Entry(frame, textvariable=temp_var, font=("Helvetica", 12), width=20)
temp_entry.grid(row=1, column=1, pady=5)

humidity_label = Label(frame, text="Humidity (%):", font=("Helvetica", 12), bg="#f0f0f0")
humidity_label.grid(row=2, column=0, pady=5, sticky="w")

humidity_var = StringVar()
humidity_entry = Entry(frame, textvariable=humidity_var, font=("Helvetica", 12), width=20)
humidity_entry.grid(row=2, column=1, pady=5)

wind_speed_label = Label(frame, text="Wind Speed (m/s):", font=("Helvetica", 12), bg="#f0f0f0")
wind_speed_label.grid(row=3, column=0, pady=5, sticky="w")

wind_speed_var = StringVar()
wind_speed_entry = Entry(frame, textvariable=wind_speed_var, font=("Helvetica", 12), width=20)
wind_speed_entry.grid(row=3, column=1, pady=5)

predict_button = Button(frame, text="Predict AQI", font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="flat",
                        width=20, command=handle_predict_button)
predict_button.grid(row=4, column=0, columnspan=2, pady=15)

# Update button to fetch today's data and predict AQI
update_button = Button(frame, text="Update Data", command=update_data, font=("Helvetica", 12), bg="#2196F3", fg="white",
                       relief="flat", width=20)
update_button.grid(row=5, column=0, columnspan=2, pady=15)

root.mainloop()

