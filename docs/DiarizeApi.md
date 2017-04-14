# swagger_client.DiarizeApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diarize_audio**](DiarizeApi.md#diarize_audio) | **POST** /api/v1/audio/diarize | Diarize an audio file


# **diarize_audio**
> list[Audio] diarize_audio(body)

Diarize an audio file

Diarize an audio file.

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
api_instance = swagger_client.DiarizeApi()
body = swagger_client.DiarizeAudio() # DiarizeAudio | Audio object that needs to be diarized.

try: 
    # Diarize an audio file
    api_response = api_instance.diarize_audio(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiarizeApi->diarize_audio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DiarizeAudio**](DiarizeAudio.md)| Audio object that needs to be diarized. | 

### Return type

[**list[Audio]**](Audio.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

