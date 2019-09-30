import logging
import requests
import base64

PYAV = False
# try:
#     import av
#     PYAV = True
# except Exception as ex:
#     logging.warn('Install https://github.com/mikeboers/PyAV for ease of use.')

allowed_values = {
    'speaker_id': set('1234567890_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
}

class SpeakerEnroll():
    URL = 'https://proxy.api.deepaffects.com/audio/generic/api/v2/sync/diarization/enroll'
    API_KEY = None
    def __init__(self, api_key):
        if not api_key:
            logging.error('"' + str(api_key) + '" is an invalid API key')
        
        SpeakerEnroll.API_KEY = api_key
    
    def enroll_speaker(
                            self,
                            audio_file_path=None,
                            encoding=None, sampleRate=None,
                            languageCode='en-US',
                            speakerId=None
                        ):
        if not (audio_file_path and speakerId):
            logging.error("audio_file_path must be supplied.")
        
        if [c for c in speakerId if c not in allowed_values['speaker_id']]:
            logging.error("Only english alphabet, numbers and _ are allowed in speakerId")

        params = {'apikey': SpeakerEnroll.API_KEY}
        
        request_json = {}
        if audio_file_path:
            content = open(audio_file_path, 'rb').read()
            content = base64.b64encode(content).decode('utf-8')
            request_json['content'] = content
        
        request_json['encoding'] = encoding
        request_json['sampleRate'] = sampleRate
        request_json['languageCode'] = languageCode
        request_json['speakerId'] = speakerId

        output = requests.post(url=SpeakerEnroll.URL, json=request_json, params=params).json()

        return output