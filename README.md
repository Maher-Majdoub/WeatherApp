# WeatherApp
This is a basic Weather desktop application that detect local weather using the external IP adress.

# ScreenShots
![Untitled2](https://user-images.githubusercontent.com/117224723/233740909-5b05de35-7573-4eea-9952-e359ef2efcd4.png)
![Untitled3](https://user-images.githubusercontent.com/117224723/233740936-fdf49b40-6ce7-4e2f-ab06-04b40db61f00.png)
![Untitled4](https://user-images.githubusercontent.com/117224723/233740942-31a87345-6b66-498e-b303-6faccfc7b114.png)

# Setup
- Install dependencies
  - `pip install pyside6`
  - `pip install yaml`
  - `pip install pydantic`
- Add environment variables
  - `apiip_APIKEY= "**********"`.
  You can get an apiip APIKEY for free from https://apiip.net/
  - `openweathermap_APIKEY= "***********"`.
  You can get an openweathermap APIKEY for free from https://openweathermap.org/ 
 - Run
   - `cd weatherapp`
   - `python main.py` 
 
 # Functionality
This application gets the external IP adress of the machine then it used an API from https://apiip.net/ to get the location using the IP adress then it gets the weather and the forecast from https://openweathermap.org/

# Contributing
Feel free to fork this repository and contribute back. It is a basic project so any contribution (large or small) is welcomed and appreciated .
 


