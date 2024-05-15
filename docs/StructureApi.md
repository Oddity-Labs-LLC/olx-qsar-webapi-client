# openapi_client.StructureApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v6_structure_canonize_get**](StructureApi.md#api_v6_structure_canonize_get) | **GET** /api/v6/structure/canonize | Returns the canonized version of the provided smiles
[**api_v6_structure_connectivity_get**](StructureApi.md#api_v6_structure_connectivity_get) | **GET** /api/v6/structure/connectivity | Returns connectivity string for the supplied smiles


# **api_v6_structure_canonize_get**
> str api_v6_structure_canonize_get(smiles=smiles)

Returns the canonized version of the provided smiles

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
    api_instance = openapi_client.StructureApi(api_client)
    smiles = 'smiles_example' # str | The SMILES to canonize (optional)

    try:
        # Returns the canonized version of the provided smiles
        api_response = api_instance.api_v6_structure_canonize_get(smiles=smiles)
        print("The response of StructureApi->api_v6_structure_canonize_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StructureApi->api_v6_structure_canonize_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smiles** | **str**| The SMILES to canonize | [optional] 

### Return type

**str**

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

# **api_v6_structure_connectivity_get**
> str api_v6_structure_connectivity_get(smiles=smiles)

Returns connectivity string for the supplied smiles

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
    api_instance = openapi_client.StructureApi(api_client)
    smiles = 'smiles_example' # str | The SMILES of the structure (optional)

    try:
        # Returns connectivity string for the supplied smiles
        api_response = api_instance.api_v6_structure_connectivity_get(smiles=smiles)
        print("The response of StructureApi->api_v6_structure_connectivity_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StructureApi->api_v6_structure_connectivity_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smiles** | **str**| The SMILES of the structure | [optional] 

### Return type

**str**

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

