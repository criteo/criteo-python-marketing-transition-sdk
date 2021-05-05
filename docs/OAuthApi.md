# criteo_marketing_transition.OAuthApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](OAuthApi.md#create_token) | **POST** /oauth2/token | 


# **create_token**
> JwtModel create_token(client_id=client_id, client_secret=client_secret, grant_type=grant_type)



Creates a token when the supplied client credentials are valid

### Example

* OAuth Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing_transition
from criteo_marketing_transition.rest import ApiException
from pprint import pprint
configuration = criteo_marketing_transition.Configuration()
# Configure OAuth2 access token for authorization: Authorization
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.criteo.com
configuration.host = "https://api.criteo.com"
# Create an instance of the API class
api_instance = criteo_marketing_transition.OAuthApi(criteo_marketing_transition.ApiClient(configuration))
client_id = 'client_id_example' # str | API Client-Id or Username (optional)
client_secret = 'client_secret_example' # str | API Client secret or password (optional)
grant_type = 'client_credentials' # str | Other grant types are not available (optional) (default to 'client_credentials')

try:
    api_response = api_instance.create_token(client_id=client_id, client_secret=client_secret, grant_type=grant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| API Client-Id or Username | [optional] 
 **client_secret** | **str**| API Client secret or password | [optional] 
 **grant_type** | **str**| Other grant types are not available | [optional] [default to &#39;client_credentials&#39;]

### Return type

[**JwtModel**](JwtModel.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

