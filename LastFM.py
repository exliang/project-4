
"""
LastFM.py

Module that includes LastFM class to deal with LastFM api
"""

# Emily Liang
# exliang@uci.edu
# 79453973

from WebAPI import WebAPI


class LastFM(WebAPI):  # method: artist.getTopTracks
    """
    Class to load data from LastFM web api and
    transclude messages including @lastfm keyword
    """

    def __init__(self, track="1", apikey="8a89f4b3dde9fabe1782f291b0d7a2c1"):
        self.track = track
        self.apikey = apikey
        self.artist = ""
        self.name = ""
        self.playcount = 0
        self.listeners = 0
        self.url = ""
        self.rank = 0

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and
        stores the response in class data attributes.

        '''
        self.set_apikey(self.apikey)
        url = f'https://ws.audioscrobbler.com/2.0/?method=artist'\
            f'.gettoptracks&artist=illenium&api_key={self.apikey}&format=json'

        data_dict = self._download_url(url)

        # assign necessary response data (tracks) to class data attributes
        index = int(self.track) - 1
        self.artist = data_dict["toptracks"]["track"][index]["artist"]["name"]
        self.name = data_dict["toptracks"]["track"][index]["name"]
        self.playcount = data_dict["toptracks"]["track"][index]["playcount"]
        self.listeners = data_dict["toptracks"]["track"][index]["listeners"]
        self.url = data_dict["toptracks"]["track"][index]["url"]
        self.rank = data_dict["toptracks"]["track"][index]["@attr"]["rank"]
        # print(self.artist)
        # print(self.name)
        # print(self.playcount)
        # print(self.listeners)
        # print(self.url)
        # print(self.rank)

    def transclude(self, message: str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
        :returns: The transcluded message
        '''
        # TODO: write code necessary to transclude keywords in
        # the message parameter with appropriate data from API
        if "@lastfm" in message:
            # bind data from OpenWeather API to @lastfm keyword
            message = message.replace("@lastfm", self.name)
        return message


# apikey = "8a89f4b3dde9fabe1782f291b0d7a2c1"
# track_num = input("Enter a track number between 1-50: ")

# l = LastFM(track_num)
# l.set_apikey(apikey)
# l.load_data()
# print(l.transclude("Hello World! Today is the first day of the rest
# of my life. It is @lastfm outside and I am thrilled!"))
