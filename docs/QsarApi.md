# openapi_client.QsarApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v6_qsar_apply_qsar_guid_chem_id_get**](QsarApi.md#api_v6_qsar_apply_qsar_guid_chem_id_get) | **GET** /api/v6/qsar/apply/{qsarGuid}/{chemId} | Applies the specified QSAR model onto the provided chemical
[**api_v6_qsar_domain_qsar_guid_chem_id_get**](QsarApi.md#api_v6_qsar_domain_qsar_guid_chem_id_get) | **GET** /api/v6/qsar/domain/{qsarGuid}/{chemId} | Checks whether the chemicals falls within the domain of the specified QSAR model
[**api_v6_qsar_list_position_get**](QsarApi.md#api_v6_qsar_list_position_get) | **GET** /api/v6/qsar/list/{position} | Retrieves all QSAR models that are associated to the provided position of the endpoint tree


# **api_v6_qsar_apply_qsar_guid_chem_id_get**
> DataPoint api_v6_qsar_apply_qsar_guid_chem_id_get(qsar_guid, chem_id)

Applies the specified QSAR model onto the provided chemical

### Example


```python
import openapi_client
from openapi_client.models.data_point import DataPoint
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
    api_instance = openapi_client.QsarApi(api_client)
    qsar_guid = 'qsar_guid_example' # str | 
    chem_id = 'chem_id_example' # str | 

    try:
        # Applies the specified QSAR model onto the provided chemical
        api_response = api_instance.api_v6_qsar_apply_qsar_guid_chem_id_get(qsar_guid, chem_id)
        print("The response of QsarApi->api_v6_qsar_apply_qsar_guid_chem_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QsarApi->api_v6_qsar_apply_qsar_guid_chem_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qsar_guid** | **str**|  | 
 **chem_id** | **str**|  | 

### Return type

[**DataPoint**](DataPoint.md)

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

# **api_v6_qsar_domain_qsar_guid_chem_id_get**
> str api_v6_qsar_domain_qsar_guid_chem_id_get(qsar_guid, chem_id)

Checks whether the chemicals falls within the domain of the specified QSAR model

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
    api_instance = openapi_client.QsarApi(api_client)
    qsar_guid = 'qsar_guid_example' # str | 
    chem_id = 'chem_id_example' # str | 

    try:
        # Checks whether the chemicals falls within the domain of the specified QSAR model
        api_response = api_instance.api_v6_qsar_domain_qsar_guid_chem_id_get(qsar_guid, chem_id)
        print("The response of QsarApi->api_v6_qsar_domain_qsar_guid_chem_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QsarApi->api_v6_qsar_domain_qsar_guid_chem_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qsar_guid** | **str**|  | 
 **chem_id** | **str**|  | 

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

# **api_v6_qsar_list_position_get**
> List[Qsar] api_v6_qsar_list_position_get(position)

Retrieves all QSAR models that are associated to the provided position of the endpoint tree

### Example


```python
import openapi_client
from openapi_client.models.qsar import Qsar
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
    api_instance = openapi_client.QsarApi(api_client)
    position = 'position_example' # str | 

    try:
        # Retrieves all QSAR models that are associated to the provided position of the endpoint tree
        api_response = api_instance.api_v6_qsar_list_position_get(position)
        print("The response of QsarApi->api_v6_qsar_list_position_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QsarApi->api_v6_qsar_list_position_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**|  | 

### Return type

[**List[Qsar]**](Qsar.md)

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

