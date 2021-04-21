# !/bin/python3

import requests
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from datetime import datetime
from pyowm import OWM

latitude  = [lat]
longitude = [long]

owm = OWM('[your API key]')
degrees = u'\N{DEGREE SIGN}'
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=latitude, lon=longitude)
full = mgr.weather_at_coords(latitude, longitude).weather
temp_dict_celsius = full.temperature('celsius')
curr = temp_dict_celsius['temp']
curr = round(curr, 1)
sunset = full.sunset_time(timeformat='date')
sundown = "Sunset: " + sunset.strftime("%H:%M")
today = one_call.forecast_daily[0].temperature('celsius')
current = str(curr) + degrees
today_conditions = one_call.forecast_daily[0]
tomorrow = one_call.forecast_daily[1].temperature('celsius')
tomorrow_conditions = one_call.forecast_daily[1]

currently = "Currently"
feels_like = "feels like"
tonight = "Tonight"
tom = "Tomorrow"

today_temp     = str(round(float(today['day']), 1)) + degrees
today_feels    = feels_like + " " + str(round(float(today['feels_like_day']), 1)) + degrees
tonight_temp   = str(round(float(today['night']), 1)) + degrees
tonight_feels  = str(round(float(today['feels_like_night']), 1)) + degrees
tomorrow_temp  = str(round(float(tomorrow['day']), 1)) + degrees
tomorrow_feels = str(round(float(tomorrow['feels_like_day']), 1)) + degrees
today_conditions    = today_conditions.detailed_status

inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.WHITE)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font_big = ImageFont.truetype(FredokaOne, 112)
font_medium = ImageFont.truetype(FredokaOne, 36)
font_small = ImageFont.truetype(FredokaOne, 20)

draw.rectangle((280, 1), (400,300)), fill = 2, width = 0)
draw.line((280, 150), (400,150)), fill = 0, width = 4)

draw.text((20, 10), currently, inky_display.BLACK, font_medium)
draw.text((20, 35), current, inky_display.BLACK, font_big)
draw.text((20, 165), today_feels, inky_display.BLACK, font_small)
draw.text((20, 195), today_conditions, inky_display.BLACK, font_small)
draw.text((20, 243), sundown, inky_display.BLACK, font_medium)

draw.text((290, 10), tonight, inky_display.WHITE, font_small)
draw.text((290, 34), tonight_temp, inky_display.WHITE, font_medium)
draw.text((290, 81), feels_like, inky_display.WHITE, font_small)
draw.text((290, 108), tonight_feels, inky_display.WHITE, font_small)

draw.text((290, 164), tom, inky_display.WHITE, font_small)
draw.text((290, 187), tomorrow_temp, inky_display.WHITE, font_medium)
draw.text((290, 233), feels_like, inky_display.WHITE, font_small)
draw.text((290, 260), tomorrow_feels, inky_display.WHITE, font_small)

inky_display.set_image(img)
inky_display.show()