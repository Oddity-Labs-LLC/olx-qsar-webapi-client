# IUCLIDIdRawToolboxId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_search_details** | **str** |  | [optional] 
**raw_toolbox_id** | **int** |  | [optional] [readonly] 
**iuclid_name** | **str** |  | [optional] 
**source_id** | **int** |  | [optional] 
**iuclid_entity_id** | **str** |  | [optional] [readonly] 
**type** | [**IUCLIDIdType**](IUCLIDIdType.md) |  | [optional] 

## Example

```python
from openapi_client.models.iuclidid_raw_toolbox_id import IUCLIDIdRawToolboxId

# TODO update the JSON string below
json = "{}"
# create an instance of IUCLIDIdRawToolboxId from a JSON string
iuclidid_raw_toolbox_id_instance = IUCLIDIdRawToolboxId.from_json(json)
# print the JSON string representation of the object
print(IUCLIDIdRawToolboxId.to_json())

# convert the object into a dict
iuclidid_raw_toolbox_id_dict = iuclidid_raw_toolbox_id_instance.to_dict()
# create an instance of IUCLIDIdRawToolboxId from a dict
iuclidid_raw_toolbox_id_from_dict = IUCLIDIdRawToolboxId.from_dict(iuclidid_raw_toolbox_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


