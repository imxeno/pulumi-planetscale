# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs

__all__ = [
    'GetDatabasesResult',
    'AwaitableGetDatabasesResult',
    'get_databases',
    'get_databases_output',
]

@pulumi.output_type
class GetDatabasesResult:
    """
    A collection of values returned by getDatabases.
    """
    def __init__(__self__, databases=None, id=None, organization=None):
        if databases and not isinstance(databases, list):
            raise TypeError("Expected argument 'databases' to be a list")
        pulumi.set(__self__, "databases", databases)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if organization and not isinstance(organization, str):
            raise TypeError("Expected argument 'organization' to be a str")
        pulumi.set(__self__, "organization", organization)

    @property
    @pulumi.getter
    def databases(self) -> Sequence['outputs.GetDatabasesDatabaseResult']:
        return pulumi.get(self, "databases")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def organization(self) -> str:
        return pulumi.get(self, "organization")


class AwaitableGetDatabasesResult(GetDatabasesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabasesResult(
            databases=self.databases,
            id=self.id,
            organization=self.organization)


def get_databases(organization: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabasesResult:
    """
    A list of PlanetScale databases.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_planetscale as planetscale

    example = planetscale.get_databases(organization="example")
    pulumi.export("dbs", example)
    ```
    """
    __args__ = dict()
    __args__['organization'] = organization
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('planetscale:index/getDatabases:getDatabases', __args__, opts=opts, typ=GetDatabasesResult).value

    return AwaitableGetDatabasesResult(
        databases=pulumi.get(__ret__, 'databases'),
        id=pulumi.get(__ret__, 'id'),
        organization=pulumi.get(__ret__, 'organization'))
def get_databases_output(organization: Optional[pulumi.Input[str]] = None,
                         opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDatabasesResult]:
    """
    A list of PlanetScale databases.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_planetscale as planetscale

    example = planetscale.get_databases(organization="example")
    pulumi.export("dbs", example)
    ```
    """
    __args__ = dict()
    __args__['organization'] = organization
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('planetscale:index/getDatabases:getDatabases', __args__, opts=opts, typ=GetDatabasesResult)
    return __ret__.apply(lambda __response__: GetDatabasesResult(
        databases=pulumi.get(__response__, 'databases'),
        id=pulumi.get(__response__, 'id'),
        organization=pulumi.get(__response__, 'organization')))
