import logging
import requests

class EmotionApi():
    URL = 'https://proxy.api.deepaffects.com/text/generic/api/latest/sync/text_recognise_emotion'
    API_KEY = None
    def __init__(self, api_key):
        if not api_key:
            logging.error('"' + str(api_key) + '" is an invalid API key')
        
        EmotionApi.API_KEY = api_key
    
    def sync_text_recognise_emotion(self, texts):
        if not isinstance(texts, list):
            logging.warn('Batching multiple texts is much faster than running one by one.')
        
        output = requests.post(
                                url=EmotionApi.URL,
                                json={'content': texts},
                                params={'apikey': EmotionApi.API_KEY}
                            ).json()

        return output

