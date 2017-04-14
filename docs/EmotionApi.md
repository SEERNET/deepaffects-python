# swagger_client.EmotionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recognise_emotion**](EmotionApi.md#recognise_emotion) | **POST** /api/v1/audio/recognise_emotion | Find emotion in an audio file


# **recognise_emotion**
> list[EmotionScore] recognise_emotion(body)

Find emotion in an audio file

Extract emotion from an audio file.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: UserSecurity
swagger_client.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EmotionApi()
body = swagger_client.Audio() # Audio | Audio object that needs to be featurized.

try: 
    # Find emotion in an audio file
    api_response = api_instance.recognise_emotion(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmotionApi->recognise_emotion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Audio**](Audio.md)| Audio object that needs to be featurized. | 

### Return type

[**list[EmotionScore]**](EmotionScore.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

