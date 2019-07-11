import pyowm
 
owm = pyowm.OWM('a54f219496fade154648010765635f28')
observation = owm.weather_at_place('Ghana,cape coast')
w = observation.get_weather()
 
print (w.get_wind()['deg'])
print( w.get_humidity())


