# deepaffects.EmotionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**async_recognise_emotion**](EmotionApi.md#async_recognise_emotion) | **POST** /api/v1/async/recognise_emotion | Find emotion in an audio file
[**sync_recognise_emotion**](EmotionApi.md#sync_recognise_emotion) | **POST** /api/v1/sync/recognise_emotion | Find emotion in an audio file


# **async_recognise_emotion**
> AsyncResponse async_recognise_emotion(body, webhook, request_id=request_id)

Find emotion in an audio file

Extract emotion from an audio file.

### Example 
```python
from __future__ import print_function
import time
import deepaffects
from deepaffects.rest import ApiException
from pprint import pprint

# Configure API key authorization: UserSecurity
deepaffects.configuration.api_key['apikey'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = deepaffects.EmotionApi()
body = deepaffects.Audio.from_file(file_name="/path/to/file") # Audio | Audio object to extract emotions from.
webhook = 'https://your_webhook.url' # str | The webhook url where result from async resource is posted
request_id = 'request_id_example' # str | Unique identifier for the request (optional)

try: 
    # Find emotion in an audio file
    api_response = api_instance.async_recognise_emotion(body, webhook, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmotionApi->async_recognise_emotion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Audio**](Audio.md)| Audio object that needs to be featurized. | 
 **webhook** | **str**| The webhook url where result from async resource is posted | 
 **request_id** | **str**| Unique identifier for the request | [optional] 

### Return type

[**AsyncResponse**](AsyncResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_recognise_emotion**
> list[EmotionScore] sync_recognise_emotion(body)

Find emotion in an audio file

Extract emotion from an audio file.

### Example 
```python
from __future__ import print_function
import time
import deepaffects
from deepaffects.rest import ApiException
from pprint import pprint

# Configure API key authorization: UserSecurity
deepaffects.configuration.api_key['apikey'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = deepaffects.EmotionApi()
body = deepaffects.Audio.from_file(file_name="/path/to/file") # Audio | Audio object to extract emotions from.

try: 
    # Find emotion in an audio file
    api_response = api_instance.sync_recognise_emotion(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmotionApi->sync_recognise_emotion: %s\n" % e)
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

