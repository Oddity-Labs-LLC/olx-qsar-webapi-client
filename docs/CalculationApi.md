# openapi_client.CalculationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v6_calculation_all_chem_id_get**](CalculationApi.md#api_v6_calculation_all_chem_id_get) | **GET** /api/v6/calculation/all/{chemId} | Applies all available calculators to the given chemical
[**api_v6_calculation_calculator_guid_chem_id_get**](CalculationApi.md#api_v6_calculation_calculator_guid_chem_id_get) | **GET** /api/v6/calculation/{calculatorGuid}/{chemId} | Applies the given calculator to the given chemical
[**api_v6_calculation_calculator_guid_info_get**](CalculationApi.md#api_v6_calculation_calculator_guid_info_get) | **GET** /api/v6/calculation/{calculatorGuid}/info | 
[**api_v6_calculation_get**](CalculationApi.md#api_v6_calculation_get) | **GET** /api/v6/calculation | Returns all available calculators


# **api_v6_calculation_all_chem_id_get**
> List[CalculationResult] api_v6_calculation_all_chem_id_get(chem_id)

Applies all available calculators to the given chemical

### Example


```python
import openapi_client
from openapi_client.models.calculation_result import CalculationResult
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
    api_instance = openapi_client.CalculationApi(api_client)
    chem_id = 'chem_id_example' # str | The chemId of the target chemical

    try:
        # Applies all available calculators to the given chemical
        api_response = api_instance.api_v6_calculation_all_chem_id_get(chem_id)
        print("The response of CalculationApi->api_v6_calculation_all_chem_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationApi->api_v6_calculation_all_chem_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chem_id** | **str**| The chemId of the target chemical | 

### Return type

[**List[CalculationResult]**](CalculationResult.md)

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

# **api_v6_calculation_calculator_guid_chem_id_get**
> DataEntry api_v6_calculation_calculator_guid_chem_id_get(calculator_guid, chem_id)

Applies the given calculator to the given chemical

### Example


```python
import openapi_client
from openapi_client.models.data_entry import DataEntry
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
    api_instance = openapi_client.CalculationApi(api_client)
    calculator_guid = 'calculator_guid_example' # str | The GUID of the calculator
    chem_id = 'chem_id_example' # str | The chemId of the target chemical

    try:
        # Applies the given calculator to the given chemical
        api_response = api_instance.api_v6_calculation_calculator_guid_chem_id_get(calculator_guid, chem_id)
        print("The response of CalculationApi->api_v6_calculation_calculator_guid_chem_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationApi->api_v6_calculation_calculator_guid_chem_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calculator_guid** | **str**| The GUID of the calculator | 
 **chem_id** | **str**| The chemId of the target chemical | 

### Return type

[**DataEntry**](DataEntry.md)

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

# **api_v6_calculation_calculator_guid_info_get**
> ITbObjectAbout api_v6_calculation_calculator_guid_info_get(calculator_guid)



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
    api_instance = openapi_client.CalculationApi(api_client)
    calculator_guid = 'calculator_guid_example' # str | 

    try:
        api_response = api_instance.api_v6_calculation_calculator_guid_info_get(calculator_guid)
        print("The response of CalculationApi->api_v6_calculation_calculator_guid_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationApi->api_v6_calculation_calculator_guid_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calculator_guid** | **str**|  | 

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

# **api_v6_calculation_get**
> List[Calculator] api_v6_calculation_get()

Returns all available calculators

### Example


```python
import openapi_client
from openapi_client.models.calculator import Calculator
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
    api_instance = openapi_client.CalculationApi(api_client)

    try:
        # Returns all available calculators
        api_response = api_instance.api_v6_calculation_get()
        print("The response of CalculationApi->api_v6_calculation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationApi->api_v6_calculation_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Calculator]**](Calculator.md)

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

