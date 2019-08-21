import logging
import requests
import base64

PYAV = False
# try:
#     import av
#     PYAV = True
# except Exception as ex:
#     logging.warn('Install https://github.com/mikeboers/PyAV for ease of use.')

class VADApi():
    URL = 'https://proxy.api.deepaffects.com/audio/generic/api/v1/async/vad'
    API_KEY = None
    def __init__(self, api_key):
        if not api_key:
            logging.error('"' + str(api_key) + '" is an invalid API key')
        
        VADApi.API_KEY = api_key
    
    def async_voice_activity_detect(
                            self,
                            audio_file_path=None, url=None,
                            encoding=None, sampleRate=None,
                            languageCode='en-US', minNonSpeechDuration=0,
                            webhook=None, request_id=None
                        ):
        if not (audio_file_path or url):
            logging.error("One of audio_file_path or url must be supplied.")
        
        if audio_file_path and url:
            logging.error("Only one of audio_file_path and url must be supplied. Both cannot be true at the same time.")
        
        if not webhook:
            logging.warn('Consider using webhooks for async requests.')

        params = {'apikey': VADApi.API_KEY}
        if webhook:
            params['webhook'] = webhook
        if request_id:
            params['request_id'] = request_id
        
        if not PYAV:
            if not encoding:
                logging.error("Encoding is not valid")
            if not sampleRate:
                logging.error("sampleRate is not valid")
            
        else:
            pass

        request_json = {}
        if audio_file_path:
            content = open(audio_file_path, 'rb').read()
            content = base64.b64encode(content).decode('utf-8')
            request_json['content'] = content
        
        elif url:
            request_json['url'] = url
        
        request_json['encoding'] = encoding
        request_json['sampleRate'] = sampleRate
        request_json['languageCode'] = languageCode
        request_json['minNonSpeechDuration'] = minNonSpeechDuration

        output = requests.post(url=VADApi.URL, json=request_json, params=params).json()

        return output