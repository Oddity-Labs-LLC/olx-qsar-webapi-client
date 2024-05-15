# openapi_client.AboutApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v6_about_object_object_guid_get**](AboutApi.md#api_v6_about_object_object_guid_get) | **GET** /api/v6/about/object/{objectGuid} | Provides general information for the specified Toolbox object


# **api_v6_about_object_object_guid_get**
> ToolboxObjectAbout api_v6_about_object_object_guid_get(object_guid)

Provides general information for the specified Toolbox object

### Example


```python
import openapi_client
from openapi_client.models.toolbox_object_about import ToolboxObjectAbout
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AboutApi(api_client)
    object_guid = 'object_guid_example' # str | GUID of the Toolbox object

    try:
        # Provides general information for the specified Toolbox object
        api_response = api_instance.api_v6_about_object_object_guid_get(object_guid)
        print("The response of AboutApi->api_v6_about_object_object_guid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AboutApi->api_v6_about_object_object_guid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_guid** | **str**| GUID of the Toolbox object | 

### Return type

[**ToolboxObjectAbout**](ToolboxObjectAbout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

