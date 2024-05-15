# openapi_client.ExportApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v6_export_list_smi_get**](ExportApi.md#api_v6_export_list_smi_get) | **GET** /api/v6/export/list/smi | Exports the given chemicals as a .smi text file


# **api_v6_export_list_smi_get**
> api_v6_export_list_smi_get(chem_ids=chem_ids)

Exports the given chemicals as a .smi text file

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ExportApi(api_client)
    chem_ids = ['chem_ids_example'] # List[str] | List of chemical ids (optional)

    try:
        # Exports the given chemicals as a .smi text file
        api_instance.api_v6_export_list_smi_get(chem_ids=chem_ids)
    except Exception as e:
        print("Exception when calling ExportApi->api_v6_export_list_smi_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chem_ids** | [**List[str]**](str.md)| List of chemical ids | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

