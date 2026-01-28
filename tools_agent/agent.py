
import json
import httpx
from google.adk.agents import Agent
from geopy.geocoders import Nominatim

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        raise ValueError(f'Could not find coordinates for {city_name}')

def get_weather(city_name):
    if city_name:
        latitude, longitude = get_coordinates(city_name)
    else:
        raise ValueError(f'City name must be provided to get weather data')

    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()

def get_kbo_rank():
    result = httpx.get("https://sports.daum.net/prx/hermes/api/team/rank.json?leagueCode=kbo&seasonKey=2025")
    return json.loads(result.text)


root_agent = Agent(
    name="tools_agent",
    model="gemini-3-flash-preview",
    description="날씨 정보와 KBO 랭킹을 제공하는 에이전트입니다.",
    instruction="도시이름을 입력하면 해당 도시의 날씨 정보를 제공하고, 'KBO 랭킹'이라고 입력하면 한국 프로야구 구단의 랭킹을 제공합니다",
    tools=[get_weather, get_kbo_rank],
)

if __name__ == "__main__":
    print(get_coordinates('서울'))
    print(get_weather('서울'))
    print(get_kbo_rank())