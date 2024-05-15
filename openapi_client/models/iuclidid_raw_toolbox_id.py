# coding: utf-8

"""
    Toolbox WebAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.iuclidid_type import IUCLIDIdType
from typing import Optional, Set
from typing_extensions import Self

class IUCLIDIdRawToolboxId(BaseModel):
    """
    IUCLIDIdRawToolboxId
    """ # noqa: E501
    json_search_details: Optional[StrictStr] = Field(default=None, alias="JSONSearchDetails")
    raw_toolbox_id: Optional[StrictInt] = Field(default=None, alias="RawToolboxId")
    iuclid_name: Optional[StrictStr] = Field(default=None, alias="IUCLIDName")
    source_id: Optional[StrictInt] = Field(default=None, alias="SourceId")
    iuclid_entity_id: Optional[StrictStr] = Field(default=None, alias="IUCLIDEntityId")
    type: Optional[IUCLIDIdType] = Field(default=None, alias="Type")
    __properties: ClassVar[List[str]] = ["JSONSearchDetails", "RawToolboxId", "IUCLIDName", "SourceId", "IUCLIDEntityId", "Type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IUCLIDIdRawToolboxId from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "raw_toolbox_id",
            "iuclid_entity_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if json_search_details (nullable) is None
        # and model_fields_set contains the field
        if self.json_search_details is None and "json_search_details" in self.model_fields_set:
            _dict['JSONSearchDetails'] = None

        # set to None if iuclid_name (nullable) is None
        # and model_fields_set contains the field
        if self.iuclid_name is None and "iuclid_name" in self.model_fields_set:
            _dict['IUCLIDName'] = None

        # set to None if iuclid_entity_id (nullable) is None
        # and model_fields_set contains the field
        if self.iuclid_entity_id is None and "iuclid_entity_id" in self.model_fields_set:
            _dict['IUCLIDEntityId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IUCLIDIdRawToolboxId from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "JSONSearchDetails": obj.get("JSONSearchDetails"),
            "RawToolboxId": obj.get("RawToolboxId"),
            "IUCLIDName": obj.get("IUCLIDName"),
            "SourceId": obj.get("SourceId"),
            "IUCLIDEntityId": obj.get("IUCLIDEntityId"),
            "Type": obj.get("Type")
        })
        return _obj


