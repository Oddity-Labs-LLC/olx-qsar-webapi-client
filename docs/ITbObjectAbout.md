# ITbObjectAbout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**description** | **str** |  | [optional] [readonly] 
**donator** | **str** |  | [optional] [readonly] 
**disclaimer** | **str** |  | [optional] [readonly] 
**authors** | **str** |  | [optional] [readonly] 
**url** | **str** |  | [optional] [readonly] 
**additional_info** | [**List[AboutTextPair]**](AboutTextPair.md) |  | [optional] [readonly] 
**help_file** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.itb_object_about import ITbObjectAbout

# TODO update the JSON string below
json = "{}"
# create an instance of ITbObjectAbout from a JSON string
itb_object_about_instance = ITbObjectAbout.from_json(json)
# print the JSON string representation of the object
print(ITbObjectAbout.to_json())

# convert the object into a dict
itb_object_about_dict = itb_object_about_instance.to_dict()
# create an instance of ITbObjectAbout from a dict
itb_object_about_from_dict = ITbObjectAbout.from_dict(itb_object_about_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


