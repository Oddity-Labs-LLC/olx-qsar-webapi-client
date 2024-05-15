# Workflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** | Caption of the Toolbox Object | [optional] 
**guid** | **str** | Unique identifier of the Toolbox Object | [optional] 
**endpoint** | **str** | The endpoint for which the workflow was built for | [optional] 
**rigid_path** | **str** | Fixed position in the endpoint tree | [optional] 

## Example

```python
from openapi_client.models.workflow import Workflow

# TODO update the JSON string below
json = "{}"
# create an instance of Workflow from a JSON string
workflow_instance = Workflow.from_json(json)
# print the JSON string representation of the object
print(Workflow.to_json())

# convert the object into a dict
workflow_dict = workflow_instance.to_dict()
# create an instance of Workflow from a dict
workflow_from_dict = Workflow.from_dict(workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


