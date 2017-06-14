# deepaffects.FeaturizeApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**async_featurize_audio**](FeaturizeApi.md#async_featurize_audio) | **POST** /api/v1/async/featurize | featurize an audio file
[**sync_featurize_audio**](FeaturizeApi.md#sync_featurize_audio) | **POST** /api/v1/sync/featurize | featurize an audio file


# **async_featurize_audio**
> AsyncResponse async_featurize_audio(body, webhook, request_id=request_id)

featurize an audio file

Extract paralinguistic feature from an audio file.

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
api_instance = deepaffects.FeaturizeApi()
body = deepaffects.Audio.from_file('/path/to/file') # Audio | Audio object that needs to be featurized.
webhook = 'webhook_example' # str | The webhook url where result from async resource is posted
request_id = 'request_id_example' # str | Unique identifier for the request (optional)

try: 
    # featurize an audio file
    api_response = api_instance.async_featurize_audio(body, webhook, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturizeApi->async_featurize_audio: %s\n" % e)
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

# **sync_featurize_audio**
> list[list[float]] sync_featurize_audio(body)

featurize an audio file

Extract paralinguistic feature from an audio file.

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
api_instance = deepaffects.FeaturizeApi()
body = deepaffects.Audio.from_file('/path/to/file') # Audio | Audio object that needs to be featurized.

try: 
    # featurize an audio file
    api_response = api_instance.sync_featurize_audio(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturizeApi->sync_featurize_audio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Audio**](Audio.md)| Audio object that needs to be featurized. | 

### Return type

**list[list[float]]**

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

