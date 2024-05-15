# MetadataHierarchy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rigid_path** | **str** | Rigid path associated with the list of metadata labels | [optional] 
**labels** | [**List[MetadataLabel]**](MetadataLabel.md) | Metadatadata labels | [optional] 

## Example

```python
from openapi_client.models.metadata_hierarchy import MetadataHierarchy

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataHierarchy from a JSON string
metadata_hierarchy_instance = MetadataHierarchy.from_json(json)
# print the JSON string representation of the object
print(MetadataHierarchy.to_json())

# convert the object into a dict
metadata_hierarchy_dict = metadata_hierarchy_instance.to_dict()
# create an instance of MetadataHierarchy from a dict
metadata_hierarchy_from_dict = MetadataHierarchy.from_dict(metadata_hierarchy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


