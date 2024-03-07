
from OpenWeather import OpenWeather
from LastFM import LastFM

def test_api(message: str, apikey: str, webapi: WebAPI):
    webapi.set_apikey(apikey)
    webapi.load_data()
    result = webapi.transclude(message)
    print(result)


open_weather = OpenWeather() #notice there are no params here...HINT: be sure to use parameter defaults!!!
lastfm = LastFM()

test_api("Testing the weather: @weather", MY_APIKEY, open_weather)
# expected output should include the original message transcluded with the default weather value for the @weather keyword.

test_api("Testing lastFM: @lastfm", MY_APIKEY, lastfm)
# expected output include the original message transcluded with the default music data assigned to the @lastfm keyword

#ISSUE: this should be able to run but WebAPI is not defined in function def