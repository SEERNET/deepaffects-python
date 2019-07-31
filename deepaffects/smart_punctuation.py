import logging
import requests

class PunctApi():
    URL = 'https://proxy.api.deepaffects.com/text/generic/api/v1/async/punctuate'
    API_KEY = None
    def __init__(self, api_key):
        if not api_key:
            logging.error('"' + str(api_key) + '" is an invalid API key')
        
        PunctApi.API_KEY = api_key
    
    def async_text_punctuate(self, texts, webhook=None, request_id=None):
        if not isinstance(texts, list):
            logging.warn('Batching multiple texts is much faster than running one by one.')
            texts = [texts]
        
        if not webhook:
            logging.warn('Consider using webhooks for async requests.')

        params = {'apikey': PunctApi.API_KEY}
        if webhook:
            params['webhook'] = webhook
        if request_id:
            params['request_id'] = request_id

        output = requests.post(url=PunctApi.URL, json={'texts': texts}, params=params).json()

        return output