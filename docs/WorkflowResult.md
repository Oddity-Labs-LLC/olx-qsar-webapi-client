# WorkflowResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**prediction** | [**DataPoint**](DataPoint.md) |  | [optional] 
**domain_result** | **str** |  | [optional] 
**domain_explain** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.workflow_result import WorkflowResult

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowResult from a JSON string
workflow_result_instance = WorkflowResult.from_json(json)
# print the JSON string representation of the object
print(WorkflowResult.to_json())

# convert the object into a dict
workflow_result_dict = workflow_result_instance.to_dict()
# create an instance of WorkflowResult from a dict
workflow_result_from_dict = WorkflowResult.from_dict(workflow_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


