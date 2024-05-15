# MetadataLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | \&quot;Endpoint\&quot;, \&quot;Effect\&quot;, etc. | [optional] 
**is_numeric** | **bool** | Most metadata labels are textual, but some are numeric like \&quot;Duration\&quot; | [optional] 
**is_automatic** | **bool** | Automatic nodes are filled in by the server once the TE is applied.  They should colored in orange and not allow further user interaction. | [optional] 

## Example

```python
from openapi_client.models.metadata_label import MetadataLabel

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataLabel from a JSON string
metadata_label_instance = MetadataLabel.from_json(json)
# print the JSON string representation of the object
print(MetadataLabel.to_json())

# convert the object into a dict
metadata_label_dict = metadata_label_instance.to_dict()
# create an instance of MetadataLabel from a dict
metadata_label_from_dict = MetadataLabel.from_dict(metadata_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


