# deepaffects-python

[![Build Status](https://travis-ci.org/SEERNET/deepaffects-python.svg)](https://travis-ci.org/SEERNET/deepaffects-python)

Python client library for DeepAffects APIs

- API version: v1
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.3+

## Installation
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

## Documentation for Authorization

DeepAffects API authenticates all the api requests via API Key.

For API key registration and setup, checkout our [quickstart guide](https://developers.deepaffects.com/docs/#quickstart-guide)

### UserSecurity

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: URL query string


## Getting Started

Please follow the [installation](#installation) instruction and execute the following python code:


```python
from __future__ import print_function
import time
import deepaffects
from deepaffects.rest import ApiException
from pprint import pprint

# Configure API key authorization: UserSecurity
deepaffects.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# create an instance of the API class
api_instance = deepaffects.DenoiseApi()
body = deepaffects.Audio.from_file('/path/to/file') # Audio | Audio object that needs to be denoised.
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
*DiarizeApiV2* | [**async_diarize_audio**](docs/DiarizeApiV2.md#async_diarize_audio) | **POST** /api/v2/async/diarize | Diarize an audio file
*DiarizeApi* | [**async_diarize_audio**](docs/DiarizeApi.md#async_diarize_audio) | **POST** /api/v1/async/diarize | Diarize an audio file (Legacy)
*DiarizeApi* | [**sync_diarize_audio**](docs/DiarizeApi.md#sync_diarize_audio) | **POST** /api/v1/sync/diarize | Diarize an audio file (Legacy)
*EmotionApi* | [**async_recognise_emotion**](docs/EmotionApi.md#async_recognise_emotion) | **POST** /api/v1/async/recognise_emotion | Find emotion in an audio file
*EmotionApi* | [**sync_recognise_emotion**](docs/EmotionApi.md#sync_recognise_emotion) | **POST** /api/v1/sync/recognise_emotion | Find emotion in an audio file
*FeaturizeApi* | [**async_featurize_audio**](docs/FeaturizeApi.md#async_featurize_audio) | **POST** /api/v1/async/featurize | featurize an audio file
*FeaturizeApi* | [**sync_featurize_audio**](docs/FeaturizeApi.md#sync_featurize_audio) | **POST** /api/v1/sync/featurize | featurize an audio file


## Documentation For Models

 - [AsyncResponse](docs/AsyncResponse.md)
 - [Audio](docs/Audio.md)
 - [DiarizeAudio](docs/DiarizeAudio.md)
 - [EmotionScore](docs/EmotionScore.md)




## UserSecurity

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: URL query string


## About
[DeepAffects](https://www.deepaffects.com/dashboard) is an emotional intelligence analysis engine that measures the effect emotional intelligence
has on team dynamics, and provides emotional analytics that serve as the basis of insights to improve
project management, performance and satisfaction across organizations, projects, and teams. To watch DeepAffects in action: check out DeepAffects [Atlassian JIRA addon](https://marketplace.atlassian.com/plugins/com.deepaffects.teams.jira/cloud/overview) and our [Github addon](https://teams.deepaffects.com/).



