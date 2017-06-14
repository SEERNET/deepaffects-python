# deepaffects-python
Python client library for DeepAffects APIs

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
webhook = 'webhook_example' # str | The webhook url where result from async resource is posted
request_id = 'request_id_example' # str | Unique identifier for the request (optional)

try:
    # Denoise an audio file
    api_response = api_instance.async_denoise_audio(body, webhook, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DenoiseApi->async_denoise_audio: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DenoiseApi* | [**async_denoise_audio**](docs/DenoiseApi.md#async_denoise_audio) | **POST** /api/v1/async/denoise | Denoise an audio file
*DenoiseApi* | [**sync_denoise_audio**](docs/DenoiseApi.md#sync_denoise_audio) | **POST** /api/v1/sync/denoise | Denoise an audio file
*DiarizeApi* | [**async_diarize_audio**](docs/DiarizeApi.md#async_diarize_audio) | **POST** /api/v1/async/diarize | Diarize an audio file
*DiarizeApi* | [**sync_diarize_audio**](docs/DiarizeApi.md#sync_diarize_audio) | **POST** /api/v1/sync/diarize | Diarize an audio file
*EmotionApi* | [**async_recognise_emotion**](docs/EmotionApi.md#async_recognise_emotion) | **POST** /api/v1/async/recognise_emotion | Find emotion in an audio file
*EmotionApi* | [**sync_recognise_emotion**](docs/EmotionApi.md#sync_recognise_emotion) | **POST** /api/v1/sync/recognise_emotion | Find emotion in an audio file
*FeaturizeApi* | [**async_featurize_audio**](docs/FeaturizeApi.md#async_featurize_audio) | **POST** /api/v1/async/featurize | featurize an audio file
*FeaturizeApi* | [**sync_featurize_audio**](docs/FeaturizeApi.md#sync_featurize_audio) | **POST** /api/v1/sync/featurize | featurize an audio file


## Documentation For Models

 - [AsyncResponse](docs/AsyncResponse.md)
 - [Audio](docs/Audio.md)
 - [DiarizeAudio](docs/DiarizeAudio.md)
 - [EmotionScore](docs/EmotionScore.md)


## Documentation For Authorization


## UserSecurity

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: URL query string


## Author



