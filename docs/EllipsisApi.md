# swagger_client.EllipsisApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**is_depressed**](EllipsisApi.md#is_depressed) | **POST** /api/v1/audio/ellipsis/is_depressed | Find if a person is depressed from audio.


# **is_depressed**
> bool is_depressed(body)

Find if a person is depressed from audio.

Find if a person is depressed from audio.

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
api_instance = swagger_client.EllipsisApi()
body = swagger_client.Audio() # Audio | Audio object that needs to be featurized.

try: 
    # Find if a person is depressed from audio.
    api_response = api_instance.is_depressed(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EllipsisApi->is_depressed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Audio**](Audio.md)| Audio object that needs to be featurized. | 

### Return type

**bool**

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

