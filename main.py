# надо установить модуль с командой `pip install python-weather`

import python_weather # https://pypi.org/project/python-weather/

import asyncio
import os

async def getweather():
  async with python_weather.Client(unit=python_weather.METRIC) as client:
    place = 'Ashgabat'
    weather = await client.get(place)
    print('Weather in ' + place + ': ' + str(weather.current.temperature) + "C, " + weather.current.description + ' and ' + str(weather.current.kind))
    
if __name__ == '__main__':
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  
  asyncio.run(getweather())