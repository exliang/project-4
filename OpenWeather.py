
"""
OpenWeather.py

Module that includes OpenWeather class to deal with OpenWeather api
"""

# Emily Liang
# exliang@uci.edu
# 79453973

from WebAPI import WebAPI


class OpenWeather(WebAPI):
    """
    Class to load data from OpenWeather web api and
    transclude messages including @weather keyword
    """

    def __init__(self, zipcode="92697", ccode="US", apikey="2e3c48c013d9e78fe6363ee699b838db"):
        self.zipcode = zipcode
        self.code = ccode
        self.apikey = apikey
        self.temperature = 0
        self.high_temperature = 0
        self.low_temperature = 0
        self.longitude = 0
        self.latitude = 0
        self.description = ""
        self.humidity = 0
        self.city = ""
        self.sunset = 0

    def load_data(self) -> None:
        '''
        Calls the web api using the required values
        and stores the response in class data attributes.

        '''
        # TODO: use the apikey data attribute and the urllib
        # module to request data from the web api. See sample
        # code at the begining of Part 1 for a hint.

        self.set_apikey(self.apikey)
        url = f"http://api.openweathermap.org/data/2.5/weather?zip"\
            f"={self.zipcode},{self.code}&appid={self.apikey}"
        # url = "http://www.python.org/fish.html"  # gives 404 error
        # url = 'https://api.openweathermap.org/data/2.5/weathe?zip=92697\
        #     ',US&appid=2e3c48c013d9e78fe6363ee699b838db'  # HTTP error
        # url = f"http://api.openweathemap.org/data/2.5/weather?zip="\
        #     "{self.zipcode},{self.code}&appid={self.data_key}"  # URL error

        # TODO: assign response data to required class data attributes
        data_dict = self._download_url(url)

        self.temperature = data_dict["main"]["temp"]
        self.high_temperature = data_dict["main"]["temp_max"]
        self.low_temperature = data_dict["main"]["temp_min"]
        self.longitude = data_dict["coord"]["lon"]
        self.latitude = data_dict["coord"]["lat"]
        self.description = data_dict["weather"][0]["description"]
        self.humidity = data_dict["main"]["humidity"]
        self.city = data_dict["name"]
        self.sunset = data_dict["sys"]["sunset"]

    def transclude(self, message: str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
        :returns: The transcluded message
        '''
        # TODO: write code necessary to transclude keywords in
        # the message parameter with appropriate data from API
        if "@weather" in message:
            # bind some data from the OpenWeather API to the @weather keyword
            message = message.replace("@weather", str(self.temperature))
        return message

# zipcode = "92697"
# ccode = "US"
# apikey = "2e3c48c013d9e78fe6363ee699b838db"

# w = OpenWeather(zipcode, ccode)
# w.set_apikey(apikey)
# w.load_data()
# print(w.transclude("Hello World! Today is the first day of the
# rest of my life. It is @weather outside and I am thrilled!"))
