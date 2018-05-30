# deepaffects.DiarizeApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**async_diarize_audio**](DiarizeApiV2.md#async_diarize_audio) | **POST** /api/v1/async/diarize | Diarize an audio file


# **async_diarize_audio**
> AsyncResponse async_diarize_audio(body, webhook, request_id=request_id)

Diarize an audio file.

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
api_instance = deepaffects.DiarizeApiV2()
body = deepaffects.DiarizeAudio.from_file(file_name="/path/to/file") # DiarizeAudio | audio object that needs to be diarized.
webhook = 'https://your_webhook.url' # str | The webhook url where result from async resource is posted
request_id = 'request_id_example' # str | Unique identifier for the request (optional)

try: 
    # Diarize an audio file
    api_response = api_instance.async_diarize_audio(body, webhook, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiarizeApi->async_diarize_audio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DiarizeAudio**](DiarizeAudio.md)| Audio object that needs to be diarized. | 
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
