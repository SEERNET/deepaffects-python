# deepaffects.DenoiseApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**async_denoise_audio**](DenoiseApi.md#async_denoise_audio) | **POST** /api/v1/async/denoise | Denoise an audio file
[**sync_denoise_audio**](DenoiseApi.md#sync_denoise_audio) | **POST** /api/v1/sync/denoise | Denoise an audio file


# **async_denoise_audio**
> AsyncResponse async_denoise_audio(body, webhook, request_id=request_id)

Denoise an audio file.

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
api_instance = deepaffects.DenoiseApi()
body = deepaffects.Audio.from_file(file_name="/path/to/file") # Audio | Audio object that needs to be denoised.
webhook = 'webhook_example' # str | The webhook url where result from async resource is posted
request_id = 'request_id_example' # str | Unique identifier for the request (optional)

try: 
    # Denoise an audio file
    api_response = api_instance.async_denoise_audio(body, webhook, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DenoiseApi->async_denoise_audio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Audio**](Audio.md)| Audio object that needs to be denoised. | 
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

# **sync_denoise_audio**
> Audio sync_denoise_audio(body)

Denoise an audio file


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
api_instance = deepaffects.DenoiseApi()
body = deepaffects.Audio.from_file(file_name="/path/to/file") # Audio | Audio object that needs to be denoised.

try: 
    # Denoise an audio file
    api_response = api_instance.sync_denoise_audio(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DenoiseApi->sync_denoise_audio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Audio**](Audio.md)| Audio object that needs to be denoised. | 

### Return type

[**Audio**](Audio.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

