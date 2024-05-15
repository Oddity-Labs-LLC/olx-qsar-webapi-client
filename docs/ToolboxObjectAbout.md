# ToolboxObjectAbout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**description** | **str** |  | [optional] [readonly] 
**donator** | **str** |  | [optional] [readonly] 
**disclaimer** | **str** |  | [optional] [readonly] 
**authors** | **str** |  | [optional] [readonly] 
**url** | **str** |  | [optional] [readonly] 
**additional_info** | **Dict[str, str]** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.toolbox_object_about import ToolboxObjectAbout

# TODO update the JSON string below
json = "{}"
# create an instance of ToolboxObjectAbout from a JSON string
toolbox_object_about_instance = ToolboxObjectAbout.from_json(json)
# print the JSON string representation of the object
print(ToolboxObjectAbout.to_json())

# convert the object into a dict
toolbox_object_about_dict = toolbox_object_about_instance.to_dict()
# create an instance of ToolboxObjectAbout from a dict
toolbox_object_about_from_dict = ToolboxObjectAbout.from_dict(toolbox_object_about_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


