Readme for Group 1

Final Viewer: http://dsc-iot.ucsd.edu/gid01/FINAL01.html

We observed that of the various markers placed in San Diego and the Bay Area, people living in the Bay Area experience a higher temperature and humidity. On average, the Bay’s humidity and temperature is 1% and 1.5 degrees higher than that of San Diego.

Hypothesis: When there is more wind flowing through an area, the humidity also increases. Specifically, a faster wind speed will lead to more humidity in the air. 

Visualizations:
- Deck.gl Heatmap Layer for Wind Speed
- Deck.gl 3D Hexagon Layer for Humidity
- Highcharts visualizations for humidity, temperature, wind speed, wind direction, and cloudiness

Data Sources:
- ESP32 Humidity and Temperature Data
- OpenWeather API Data on wind speed, direction, and cloudiness - https://openweathermap.org/api/one-call-api
	- Employed an hourly one-call request for each set of coordinates in our devices tables
- Stored data in MCDATA and WEATHER tables


Files:
- FINAL01.html
- final_viewer.html
- API.py
- weather.py
