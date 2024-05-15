# DataEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from openapi_client.models.data_entry import DataEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DataEntry from a JSON string
data_entry_instance = DataEntry.from_json(json)
# print the JSON string representation of the object
print(DataEntry.to_json())

# convert the object into a dict
data_entry_dict = data_entry_instance.to_dict()
# create an instance of DataEntry from a dict
data_entry_from_dict = DataEntry.from_dict(data_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


