# (C) Copyright 2024- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

"""API types"""

from dataclasses import dataclass
from typing import Optional, Any

from forecastbox.products.product import USER_DEFINED
from pydantic import BaseModel, Field, field_validator, model_validator, PositiveInt

CONFIG_ORDER = ["param", "levtype", "levelist"]

ModelName = str


class FIABBaseModel(BaseModel):
    pass


class ModelSpecification(FIABBaseModel):
    """Model Configuration"""

    model: ModelName
    """Model name"""
    date: str
    """Date"""
    lead_time: int
    """Lead time"""
    ensemble_members: int
    """Number of ensemble members"""
    entries: dict[str, str] = Field(default_factory=dict)
    """Configuration entries"""

    @field_validator("model")
    def model_cleanup(cls, m):
        return m.lower().replace("_", "/")


class ConfigEntry(FIABBaseModel):
    """Configuration Entry"""

    label: str
    """Label of the configuration entry"""
    description: str | None
    """Description of the configuration entry"""
    values: Optional[list[Any]] = None
    """Available values for the configuration entry"""
    example: Optional[str] = None
    """Example value for the configuration entry"""
    multiple: bool = False
    """Whether the configuration entry is a multiple select"""
    constrained_by: list[str] = Field(default_factory=list)
    """List of configuration entries that this entry is constrained by"""
    default: Optional[str] = None

    @model_validator(mode="after")
    def __post_init__(self):
        if self.values and USER_DEFINED in self.values:
            self.values = None

        if self.values is None:
            self.multiple = False
        else:
            self._sort_values()
        return self

    def _sort_values(self):
        """Sort values."""
        if all(str(x).isdigit() for x in self.values):
            self.values = list(map(str, sorted(self.values, key=float)))
            return
        self.values = list(map(str, sorted(self.values, key=lambda x: str(x).lower())))


class ProductConfiguration(FIABBaseModel):
    """
    Product Configuration

    Provides the available configuration entries for a product.
    """

    product: str
    """Product name"""
    options: dict[str, ConfigEntry]
    """Configuration spec"""

    @model_validator(mode="after")
    def sort_values(self):
        new_options = {}
        for key in CONFIG_ORDER:
            if key in self.options:
                new_options[key] = self.options[key]

        for key in self.options:
            if key not in new_options:
                new_options[key] = self.options[key]

        self.options = new_options
        return self


@dataclass
class ProductSpecification:
    """Product Specification

    A user has chosen a product and specified the configuration.
    """

    product: str
    """Product name"""
    specification: dict[str, Any]
    """Specification"""


class EnvironmentSpecification(FIABBaseModel):
    """Environment Configuration"""

    hosts: PositiveInt | None = Field(default=None)
    """Number of hosts"""
    workers_per_host: PositiveInt | None = Field(default=None)
    """Number of workers per host"""
    environment_variables: dict[str, str] = Field(default_factory=dict)
    """Environment variables"""


class ExecutionSpecification(FIABBaseModel):
    model: ModelSpecification
    """Model Configuration"""
    products: list[ProductSpecification]
    """Product Configuration"""
    environment: EnvironmentSpecification
    """Environment Configuration"""
    shared: bool = Field(default=False)


class VisualisationOptions(FIABBaseModel):
    """Options for the visualisation."""

    preset: str = "blob"
    # width: str | int = '100%'
    # height: str | int = 600
