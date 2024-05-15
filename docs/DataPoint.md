# DataPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  | [optional] 
**rigid_path** | **str** |  | [optional] 
**endpoint** | **str** |  | [optional] 
**meta_data** | **List[str]** |  | [optional] 
**value** | **str** |  | [optional] 
**qualifier** | **str** |  | [optional] 
**min_value** | **str** |  | [optional] 
**min_qualifier** | **str** |  | [optional] 
**max_value** | **str** |  | [optional] 
**max_qualifier** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**family** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.data_point import DataPoint

# TODO update the JSON string below
json = "{}"
# create an instance of DataPoint from a JSON string
data_point_instance = DataPoint.from_json(json)
# print the JSON string representation of the object
print(DataPoint.to_json())

# convert the object into a dict
data_point_dict = data_point_instance.to_dict()
# create an instance of DataPoint from a dict
data_point_from_dict = DataPoint.from_dict(data_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


