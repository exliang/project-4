
"""
WebAPI.py

Module that includes a WebAPI class to deal with abstract
and non-abstract methods for all API classes
"""

# Emily Liang
# exliang@uci.edu
# 79453973

from abc import ABC, abstractmethod
import urllib
from urllib import request, error
import json
import exception


class WebAPI(ABC):  # for part 3 (includes commaon features for API modules)
    """
    Abstract class containing methods to handle web apis
    """
    def _download_url(self, url: str) -> dict:
        """
        Function summary: downloads data from web api url
        Parameters: self (keyword)
                    url of web api (string)
        Return value: web api data (dictionary)
        """
        # retrieve data
        try:
            with urllib.request.urlopen(url) as response:
                response_data = response.read()
                response.close()
        except urllib.error.HTTPError as e:
            raise exception.HTTPException(f'{e.code}'
                                          'Error - Remote API is unavailable')
        except urllib.request.URLError as e:
            raise exception.URLException('Error - '
                                         'Client has no connection to the '
                                         'Internet OR invalid URL'
                                         f' ~ {e.reason}')

        # parse the json data that was received
        try:
            dict_data = json.loads(response_data)  # convert data to a dict
        except json.JSONDecodeError as e:
            raise exception.JSONException("Error: "
                                          "Invalid data formatting"
                                          " from remote API")
        return dict_data

    def set_apikey(self, apikey: str) -> None:
        """
        Function summary: sets the api key
        Parameters: self (keyword)
                    api key (string)
        Return value: None
        """
        data_key = apikey

    @abstractmethod
    def load_data(self):
        """
        Function summary: abstract method to load data from web api
        Parameters: self (keyword)
        Return value: None
        """

    @abstractmethod
    def transclude(self, message: str) -> str:
        """
        Function summary: abstract method to transclude the message to post
        Parameters: self (keyword)
        Return value: message after transclusion (string)
        """
