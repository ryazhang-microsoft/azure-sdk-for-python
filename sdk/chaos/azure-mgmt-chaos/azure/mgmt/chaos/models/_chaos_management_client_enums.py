# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs."""

    INTERNAL = "Internal"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class FilterType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum that discriminates between filter types. Currently only ``Simple`` type is supported."""

    SIMPLE = "Simple"


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"


class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """String of the resource identity type."""

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"


class SelectorType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum of the selector type."""

    LIST = "List"
    QUERY = "Query"


class TargetReferenceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum of the Target reference type."""

    CHAOS_TARGET = "ChaosTarget"
