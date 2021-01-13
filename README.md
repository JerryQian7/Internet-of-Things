{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf500
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue233;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c93333;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Readme for Group 1\
\
Final Viewer: {\field{\*\fldinst{HYPERLINK "http://dsc-iot.ucsd.edu/gid01/FINAL01.html"}}{\fldrslt 
\f1 \cf2 \expnd0\expndtw0\kerning0
\ul \ulc2 \outl0\strokewidth0 \strokec2 http://dsc-iot.ucsd.edu/gid01/FINAL01.html}}
\f1 \cf2 \expnd0\expndtw0\kerning0
\ul \ulc2 \outl0\strokewidth0 \strokec2 \
\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0 \cf0 \kerning1\expnd0\expndtw0 \ulnone \outl0\strokewidth0 We observed that of the various markers placed in San Diego and the Bay Area, people living in the Bay Area experience a higher temperature and humidity. On average, the Bay\'92s humidity and temperature is 1% and 1.5 degrees higher than that of San Diego.\
\
Hypothesis: When there is more wind flowing through an area, the humidity also increases. Specifically, a faster wind speed will lead to more humidity in the air. \
\
Visualizations:\
- Deck.gl Heatmap Layer for Wind Speed\
- Deck.gl 3D Hexagon Layer for Humidity\
- Highcharts visualizations for humidity, temperature, wind speed, wind direction, and cloudiness\
\
Data Sources:\
- ESP32 Humidity and Temperature Data\
- OpenWeather API Data on wind speed, direction, and cloudiness - {\field{\*\fldinst{HYPERLINK "https://openweathermap.org/api/one-call-api"}}{\fldrslt 
\f1 \cf2 \expnd0\expndtw0\kerning0
\ul \ulc2 \outl0\strokewidth0 \strokec2 https://openweathermap.org/api/one-call-api}}\
	- Employed an hourly one-call request for each set of coordinates in our devices tables\
- Stored data in MCDATA and WEATHER tables\
\
\
Files:\
- FINAL01.html\
- final_viewer.html\
- API.py\
- weather.py\
\
\
}
