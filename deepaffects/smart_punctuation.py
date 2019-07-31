import logging
import requests

class PunctApi():
    URL = 'https://proxy.api.deepaffects.com/text/generic/api/v1/async/punctuate'
    API_KEY = None
    def __init__(self, api_key):
        if not api_key:
            logging.error('"' + str(api_key) + '" is an invalid API key')
        
        PunctApi.API_KEY = api_key
    
    def async_text_punctuate(self, texts):
        if not isinstance(texts, list):
            logging.warn('Batching multiple texts is much faster than running one by one.')
            texts = [texts]
        
        output = requests.post(url=PunctApi.URL, json={'texts': texts}, params={'apikey': PunctApi.API_KEY}).json()

        return output