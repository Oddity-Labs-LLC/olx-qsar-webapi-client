# openapi_client.WorkflowsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v6_workflows_get**](WorkflowsApi.md#api_v6_workflows_get) | **GET** /api/v6/workflows | Requests all available workflows
[**api_v6_workflows_workflow_guid_chem_id_get**](WorkflowsApi.md#api_v6_workflows_workflow_guid_chem_id_get) | **GET** /api/v6/workflows/{workflowGuid}/{chemId} | Executes a workflow with a given chemical


# **api_v6_workflows_get**
> List[Workflow] api_v6_workflows_get()

Requests all available workflows

### Example


```python
import openapi_client
from openapi_client.models.workflow import Workflow
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
    api_instance = openapi_client.WorkflowsApi(api_client)

    try:
        # Requests all available workflows
        api_response = api_instance.api_v6_workflows_get()
        print("The response of WorkflowsApi->api_v6_workflows_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->api_v6_workflows_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Workflow]**](Workflow.md)

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

# **api_v6_workflows_workflow_guid_chem_id_get**
> WorkflowResult api_v6_workflows_workflow_guid_chem_id_get(workflow_guid, chem_id)

Executes a workflow with a given chemical

### Example


```python
import openapi_client
from openapi_client.models.workflow_result import WorkflowResult
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    workflow_guid = 'workflow_guid_example' # str | GUID of the workflow to be used
    chem_id = 'chem_id_example' # str | The ChemID of the chemical to be profiled

    try:
        # Executes a workflow with a given chemical
        api_response = api_instance.api_v6_workflows_workflow_guid_chem_id_get(workflow_guid, chem_id)
        print("The response of WorkflowsApi->api_v6_workflows_workflow_guid_chem_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->api_v6_workflows_workflow_guid_chem_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_guid** | **str**| GUID of the workflow to be used | 
 **chem_id** | **str**| The ChemID of the chemical to be profiled | 

### Return type

[**WorkflowResult**](WorkflowResult.md)

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

