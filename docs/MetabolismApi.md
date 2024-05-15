# openapi_client.MetabolismApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v6_metabolism_get**](MetabolismApi.md#api_v6_metabolism_get) | **GET** /api/v6/metabolism | Requests all available simulators
[**api_v6_metabolism_simulator_guid_chem_id_get**](MetabolismApi.md#api_v6_metabolism_simulator_guid_chem_id_get) | **GET** /api/v6/metabolism/{simulatorGuid}/{chemId} | Applies the given simulator to the given chemical returning the produced metabolites
[**api_v6_metabolism_simulator_guid_get**](MetabolismApi.md#api_v6_metabolism_simulator_guid_get) | **GET** /api/v6/metabolism/{simulatorGuid} | Applies the given simulator to the given SMILES returning the produced metabolites
[**api_v6_metabolism_simulator_guid_info_get**](MetabolismApi.md#api_v6_metabolism_simulator_guid_info_get) | **GET** /api/v6/metabolism/{simulatorGuid}/info | Provides general information for the specified simulator


# **api_v6_metabolism_get**
> List[Simulator] api_v6_metabolism_get()

Requests all available simulators

### Example


```python
import openapi_client
from openapi_client.models.simulator import Simulator
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
    api_instance = openapi_client.MetabolismApi(api_client)

    try:
        # Requests all available simulators
        api_response = api_instance.api_v6_metabolism_get()
        print("The response of MetabolismApi->api_v6_metabolism_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetabolismApi->api_v6_metabolism_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Simulator]**](Simulator.md)

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

# **api_v6_metabolism_simulator_guid_chem_id_get**
> List[str] api_v6_metabolism_simulator_guid_chem_id_get(chem_id, simulator_guid)

Applies the given simulator to the given chemical returning the produced metabolites

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
    api_instance = openapi_client.MetabolismApi(api_client)
    chem_id = 'chem_id_example' # str | The ChemId of the chemical to metabolize
    simulator_guid = 'simulator_guid_example' # str | The GUID of the simulator to apply

    try:
        # Applies the given simulator to the given chemical returning the produced metabolites
        api_response = api_instance.api_v6_metabolism_simulator_guid_chem_id_get(chem_id, simulator_guid)
        print("The response of MetabolismApi->api_v6_metabolism_simulator_guid_chem_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetabolismApi->api_v6_metabolism_simulator_guid_chem_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chem_id** | **str**| The ChemId of the chemical to metabolize | 
 **simulator_guid** | **str**| The GUID of the simulator to apply | 

### Return type

**List[str]**

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

# **api_v6_metabolism_simulator_guid_get**
> List[str] api_v6_metabolism_simulator_guid_get(simulator_guid, smiles=smiles)

Applies the given simulator to the given SMILES returning the produced metabolites

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
    api_instance = openapi_client.MetabolismApi(api_client)
    simulator_guid = 'simulator_guid_example' # str | The GUID of the simmulator to apply
    smiles = 'smiles_example' # str | The SMILES of the chemical to metabolize (optional)

    try:
        # Applies the given simulator to the given SMILES returning the produced metabolites
        api_response = api_instance.api_v6_metabolism_simulator_guid_get(simulator_guid, smiles=smiles)
        print("The response of MetabolismApi->api_v6_metabolism_simulator_guid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetabolismApi->api_v6_metabolism_simulator_guid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulator_guid** | **str**| The GUID of the simmulator to apply | 
 **smiles** | **str**| The SMILES of the chemical to metabolize | [optional] 

### Return type

**List[str]**

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

# **api_v6_metabolism_simulator_guid_info_get**
> ITbObjectAbout api_v6_metabolism_simulator_guid_info_get(simulator_guid)

Provides general information for the specified simulator

### Example


```python
import openapi_client
from openapi_client.models.itb_object_about import ITbObjectAbout
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
    api_instance = openapi_client.MetabolismApi(api_client)
    simulator_guid = 'simulator_guid_example' # str | GUID of the Simulator

    try:
        # Provides general information for the specified simulator
        api_response = api_instance.api_v6_metabolism_simulator_guid_info_get(simulator_guid)
        print("The response of MetabolismApi->api_v6_metabolism_simulator_guid_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetabolismApi->api_v6_metabolism_simulator_guid_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulator_guid** | **str**| GUID of the Simulator | 

### Return type

[**ITbObjectAbout**](ITbObjectAbout.md)

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

