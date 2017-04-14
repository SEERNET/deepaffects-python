# deepaffects
OpenAPI Specification of DeepAffects APIs

- API version: v1
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

The python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/SEERNET/deepaffects-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/SEERNET/deepaffects-python.git`)

Then import the package:
```python
import deepaffects 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import deepaffects
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import deepaffects
from deepaffects.rest import ApiException
from pprint import pprint

# Configure API key authorization: UserSecurity
deepaffects.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['apikey'] = 'Bearer'
# create an instance of the API class
api_instance = deepaffects.DenoiseApi()
body = deepaffects.Audio() # Audio | Audio object that needs to be denoised.

try:
    # Denoise an audio file
    api_response = api_instance.denoise_audio(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DenoiseApi->denoise_audio: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DenoiseApi* | [**denoise_audio**](docs/DenoiseApi.md#denoise_audio) | **POST** /api/v1/audio/denoise | Denoise an audio file
*DiarizeApi* | [**diarize_audio**](docs/DiarizeApi.md#diarize_audio) | **POST** /api/v1/audio/diarize | Diarize an audio file
*EllipsisApi* | [**is_depressed**](docs/EllipsisApi.md#is_depressed) | **POST** /api/v1/audio/ellipsis/is_depressed | Find if a person is depressed from audio.
*EmotionApi* | [**recognise_emotion**](docs/EmotionApi.md#recognise_emotion) | **POST** /api/v1/audio/recognise_emotion | Find emotion in an audio file
*FeaturizeApi* | [**featurize_audio**](docs/FeaturizeApi.md#featurize_audio) | **POST** /api/v1/audio/featurize | featurize an audio file


## Documentation For Models

 - [Audio](docs/Audio.md)
 - [DiarizeAudio](docs/DiarizeAudio.md)
 - [EmotionScore](docs/EmotionScore.md)


## Documentation For Authorization


## UserSecurity

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: URL query string


## Author



