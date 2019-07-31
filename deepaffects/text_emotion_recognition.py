import logging
import requests

class EmotionApi():
    URL = 'https://proxy.api.deepaffects.com/text/generic/api/latest/sync/text_recognise_emotion?apikey='
    def __init__(self, api_key):
        if not api_key:
            logging.error('"' + str(api_key) + '" is an invalid API key')
        
        EmotionApi.URL = EmotionApi.URL + api_key
    
    def sync_text_recognise_emotion(self, texts):
        if not isinstance(texts, list):
            logging.warn('Batching multiple texts is much faster than running one by one.')
        
        output = requests.post(url=EmotionApi.URL, json={'content': texts}).json()

        return output

