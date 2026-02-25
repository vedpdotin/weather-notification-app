# Weather Notification App

A Python application that sends daily weather notifications using **Twilio**, deployed on **PythonAnywhere (Free Plan)**.

## Features

* Sends daily weather updates at a specified time
* Uses OpenWeatherMap API for weather data
* Sends SMS notifications via Twilio
* Deployable on PythonAnywhere free version
* Only requires uploading the `main.py` file

---

## Deployment on PythonAnywhere

1. Upload your `main.py` file to PythonAnywhere.
2. Go to the **Tasks** tab.
3. Create a new scheduled task.

 **Important:** PythonAnywhere uses **UTC time**, so adjust the scheduled time according to your local timezone.

---

## Scheduled Task Command

In the command box, paste the following:

```bash
export OPENWEATHERMAP_API_KEY="YOUR_OPENWEATHERMAP_API_KEY"; \
export LATITUDE="YOUR_LATITUDE"; \
export LONGITUDE="YOUR_LONGITUDE"; \
export TWILIO_ACCOUNT_SID="YOUR_TWILIO_ACCOUNT_SID"; \
export TWILIO_AUTH_TOKEN="YOUR_TWILIO_AUTH_TOKEN"; \
export MY_PHONE="+YOUR_PHONE_NUMBER"; \
export SENDER_PHONE="+YOUR_TWILIO_PHONE_NUMBER"; \
python3 main.py
```

---

## Configuration

Replace all placeholder values with your actual credentials:

* `OPENWEATHERMAP_API_KEY` → Your OpenWeatherMap API key
* `LATITUDE` → Your location latitude
* `LONGITUDE` → Your location longitude
* `TWILIO_ACCOUNT_SID` → From Twilio dashboard
* `TWILIO_AUTH_TOKEN` → From Twilio dashboard
* `MY_PHONE` → Your personal phone number
* `SENDER_PHONE` → Your Twilio phone number

---

## Requirements

Make sure you install required packages (if needed):

```bash
pip install requests twilio
```
