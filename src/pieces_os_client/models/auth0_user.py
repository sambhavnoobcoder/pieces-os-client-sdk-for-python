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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from pieces_os_client.models.auth0_identity import Auth0Identity
from pieces_os_client.models.auth0_user_metadata import Auth0UserMetadata

class Auth0User(BaseModel):
    """
      # noqa: E501
    """
    name: Optional[StrictStr] = Field(default=None, description=" User's full name.")
    picture: Optional[StrictStr] = Field(default=None, description="mapped from picture.URL pointing to the user's profile picture. ")
    email: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    email_verified: Optional[StrictBool] = Field(default=None, description="Indicates whether the user has verified their email address. Mapped from email_verified -> emailVerified.")
    family_name: Optional[StrictStr] = Field(default=None, description="User's family name.")
    given_name: Optional[StrictStr] = Field(default=None, description="User's given name. ")
    identities: Optional[conlist(Auth0Identity)] = Field(default=None, description="Contains info retrieved from the identity provider with which the user originally authenticates.")
    nickname: Optional[StrictStr] = Field(default=None, description="User's nickname. ")
    updated_at: Optional[datetime] = None
    username: Optional[StrictStr] = Field(default=None, description=" (unique) User's username.  ")
    user_metadata: Optional[Auth0UserMetadata] = None
    locale: Optional[StrictStr] = None
    user_id: Optional[StrictStr] = None
    last_ip: Optional[StrictStr] = None
    last_login: Optional[datetime] = None
    logins_count: Optional[StrictInt] = None
    blocked_for: Optional[conlist(StrictStr)] = None
    guardian_authenticators: Optional[conlist(StrictStr)] = None
    __properties = ["name", "picture", "email", "created_at", "email_verified", "family_name", "given_name", "identities", "nickname", "updated_at", "username", "user_metadata", "locale", "user_id", "last_ip", "last_login", "logins_count", "blocked_for", "guardian_authenticators"]

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
    def from_json(cls, json_str: str) -> Auth0User:
        """Create an instance of Auth0User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in identities (list)
        _items = []
        if self.identities:
            for _item in self.identities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['identities'] = _items
        # override the default output from pydantic by calling `to_dict()` of user_metadata
        if self.user_metadata:
            _dict['user_metadata'] = self.user_metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Auth0User:
        """Create an instance of Auth0User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Auth0User.parse_obj(obj)

        _obj = Auth0User.parse_obj({
            "name": obj.get("name"),
            "picture": obj.get("picture"),
            "email": obj.get("email"),
            "created_at": obj.get("created_at"),
            "email_verified": obj.get("email_verified"),
            "family_name": obj.get("family_name"),
            "given_name": obj.get("given_name"),
            "identities": [Auth0Identity.from_dict(_item) for _item in obj.get("identities")] if obj.get("identities") is not None else None,
            "nickname": obj.get("nickname"),
            "updated_at": obj.get("updated_at"),
            "username": obj.get("username"),
            "user_metadata": Auth0UserMetadata.from_dict(obj.get("user_metadata")) if obj.get("user_metadata") is not None else None,
            "locale": obj.get("locale"),
            "user_id": obj.get("user_id"),
            "last_ip": obj.get("last_ip"),
            "last_login": obj.get("last_login"),
            "logins_count": obj.get("logins_count"),
            "blocked_for": obj.get("blocked_for"),
            "guardian_authenticators": obj.get("guardian_authenticators")
        })
        return _obj


