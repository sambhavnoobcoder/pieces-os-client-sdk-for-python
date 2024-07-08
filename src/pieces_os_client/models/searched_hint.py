# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.hint import Hint

class SearchedHint(BaseModel):
    """
    This is used for the Hint searching endpoint  hint here is only provided if transferables are set to true.  temporal: if this is provided this means that their material matched the input via a timestamp.  TODO will want to consider returning related materials to this material potentially both associated/ and not associated materials ie suggestion: WorkstreamSuggestions  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    hint: Optional[Hint] = None
    exact: StrictBool = Field(...)
    similarity: Union[StrictFloat, StrictInt] = Field(...)
    temporal: Optional[StrictBool] = None
    identifier: StrictStr = Field(default=..., description="This is the uuid of the hint.")
    __properties = ["schema", "hint", "exact", "similarity", "temporal", "identifier"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SearchedHint:
        """Create an instance of SearchedHint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hint
        if self.hint:
            _dict['hint'] = self.hint.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SearchedHint:
        """Create an instance of SearchedHint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SearchedHint.parse_obj(obj)

        _obj = SearchedHint.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "hint": Hint.from_dict(obj.get("hint")) if obj.get("hint") is not None else None,
            "exact": obj.get("exact"),
            "similarity": obj.get("similarity"),
            "temporal": obj.get("temporal"),
            "identifier": obj.get("identifier")
        })
        return _obj


