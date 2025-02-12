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
    'GetOrganizationResult',
    'AwaitableGetOrganizationResult',
    'get_organization',
    'get_organization_output',
]

@pulumi.output_type
class GetOrganizationResult:
    """
    A collection of values returned by getOrganization.
    """
    def __init__(__self__, billing_email=None, created_at=None, database_count=None, features=None, flags=None, has_past_due_invoices=None, id=None, idp_managed_roles=None, name=None, plan=None, single_tenancy=None, sleeping_database_count=None, sso=None, sso_directory=None, sso_portal_url=None, updated_at=None, valid_billing_info=None):
        if billing_email and not isinstance(billing_email, str):
            raise TypeError("Expected argument 'billing_email' to be a str")
        pulumi.set(__self__, "billing_email", billing_email)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if database_count and not isinstance(database_count, float):
            raise TypeError("Expected argument 'database_count' to be a float")
        pulumi.set(__self__, "database_count", database_count)
        if features and not isinstance(features, dict):
            raise TypeError("Expected argument 'features' to be a dict")
        pulumi.set(__self__, "features", features)
        if flags and not isinstance(flags, dict):
            raise TypeError("Expected argument 'flags' to be a dict")
        pulumi.set(__self__, "flags", flags)
        if has_past_due_invoices and not isinstance(has_past_due_invoices, bool):
            raise TypeError("Expected argument 'has_past_due_invoices' to be a bool")
        pulumi.set(__self__, "has_past_due_invoices", has_past_due_invoices)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if idp_managed_roles and not isinstance(idp_managed_roles, bool):
            raise TypeError("Expected argument 'idp_managed_roles' to be a bool")
        pulumi.set(__self__, "idp_managed_roles", idp_managed_roles)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if plan and not isinstance(plan, str):
            raise TypeError("Expected argument 'plan' to be a str")
        pulumi.set(__self__, "plan", plan)
        if single_tenancy and not isinstance(single_tenancy, bool):
            raise TypeError("Expected argument 'single_tenancy' to be a bool")
        pulumi.set(__self__, "single_tenancy", single_tenancy)
        if sleeping_database_count and not isinstance(sleeping_database_count, float):
            raise TypeError("Expected argument 'sleeping_database_count' to be a float")
        pulumi.set(__self__, "sleeping_database_count", sleeping_database_count)
        if sso and not isinstance(sso, bool):
            raise TypeError("Expected argument 'sso' to be a bool")
        pulumi.set(__self__, "sso", sso)
        if sso_directory and not isinstance(sso_directory, bool):
            raise TypeError("Expected argument 'sso_directory' to be a bool")
        pulumi.set(__self__, "sso_directory", sso_directory)
        if sso_portal_url and not isinstance(sso_portal_url, str):
            raise TypeError("Expected argument 'sso_portal_url' to be a str")
        pulumi.set(__self__, "sso_portal_url", sso_portal_url)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if valid_billing_info and not isinstance(valid_billing_info, bool):
            raise TypeError("Expected argument 'valid_billing_info' to be a bool")
        pulumi.set(__self__, "valid_billing_info", valid_billing_info)

    @property
    @pulumi.getter(name="billingEmail")
    def billing_email(self) -> str:
        """
        The billing email of the organization.
        """
        return pulumi.get(self, "billing_email")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        When the organization was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="databaseCount")
    def database_count(self) -> float:
        """
        The number of databases in the organization.
        """
        return pulumi.get(self, "database_count")

    @property
    @pulumi.getter
    def features(self) -> 'outputs.GetOrganizationFeaturesResult':
        """
        Features that are enabled on the organization.
        """
        return pulumi.get(self, "features")

    @property
    @pulumi.getter
    def flags(self) -> 'outputs.GetOrganizationFlagsResult':
        """
        .
        """
        return pulumi.get(self, "flags")

    @property
    @pulumi.getter(name="hasPastDueInvoices")
    def has_past_due_invoices(self) -> bool:
        """
        Whether or not the organization has past due billing invoices.
        """
        return pulumi.get(self, "has_past_due_invoices")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID for the organization.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idpManagedRoles")
    def idp_managed_roles(self) -> bool:
        """
        Whether or not the IdP provider is be responsible for managing roles in PlanetScale.
        """
        return pulumi.get(self, "idp_managed_roles")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the organization.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def plan(self) -> str:
        """
        The billing plan of the organization.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="singleTenancy")
    def single_tenancy(self) -> bool:
        """
        Whether or not the organization has single tenancy enabled.
        """
        return pulumi.get(self, "single_tenancy")

    @property
    @pulumi.getter(name="sleepingDatabaseCount")
    def sleeping_database_count(self) -> float:
        """
        The number of sleeping databases in the organization.
        """
        return pulumi.get(self, "sleeping_database_count")

    @property
    @pulumi.getter
    def sso(self) -> bool:
        """
        Whether or not SSO is enabled on the organization.
        """
        return pulumi.get(self, "sso")

    @property
    @pulumi.getter(name="ssoDirectory")
    def sso_directory(self) -> bool:
        """
        Whether or not the organization uses a WorkOS directory.
        """
        return pulumi.get(self, "sso_directory")

    @property
    @pulumi.getter(name="ssoPortalUrl")
    def sso_portal_url(self) -> str:
        """
        The URL of the organization's SSO portal.
        """
        return pulumi.get(self, "sso_portal_url")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        When the organization was last updated.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="validBillingInfo")
    def valid_billing_info(self) -> bool:
        """
        Whether or not the organization's billing information is valid.
        """
        return pulumi.get(self, "valid_billing_info")


class AwaitableGetOrganizationResult(GetOrganizationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOrganizationResult(
            billing_email=self.billing_email,
            created_at=self.created_at,
            database_count=self.database_count,
            features=self.features,
            flags=self.flags,
            has_past_due_invoices=self.has_past_due_invoices,
            id=self.id,
            idp_managed_roles=self.idp_managed_roles,
            name=self.name,
            plan=self.plan,
            single_tenancy=self.single_tenancy,
            sleeping_database_count=self.sleeping_database_count,
            sso=self.sso,
            sso_directory=self.sso_directory,
            sso_portal_url=self.sso_portal_url,
            updated_at=self.updated_at,
            valid_billing_info=self.valid_billing_info)


def get_organization(name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOrganizationResult:
    """
    A PlanetScale organization.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_planetscale as planetscale

    example = planetscale.get_organization(name="example")
    pulumi.export("org", example)
    ```


    :param str name: The name of the organization.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('planetscale:index/getOrganization:getOrganization', __args__, opts=opts, typ=GetOrganizationResult).value

    return AwaitableGetOrganizationResult(
        billing_email=pulumi.get(__ret__, 'billing_email'),
        created_at=pulumi.get(__ret__, 'created_at'),
        database_count=pulumi.get(__ret__, 'database_count'),
        features=pulumi.get(__ret__, 'features'),
        flags=pulumi.get(__ret__, 'flags'),
        has_past_due_invoices=pulumi.get(__ret__, 'has_past_due_invoices'),
        id=pulumi.get(__ret__, 'id'),
        idp_managed_roles=pulumi.get(__ret__, 'idp_managed_roles'),
        name=pulumi.get(__ret__, 'name'),
        plan=pulumi.get(__ret__, 'plan'),
        single_tenancy=pulumi.get(__ret__, 'single_tenancy'),
        sleeping_database_count=pulumi.get(__ret__, 'sleeping_database_count'),
        sso=pulumi.get(__ret__, 'sso'),
        sso_directory=pulumi.get(__ret__, 'sso_directory'),
        sso_portal_url=pulumi.get(__ret__, 'sso_portal_url'),
        updated_at=pulumi.get(__ret__, 'updated_at'),
        valid_billing_info=pulumi.get(__ret__, 'valid_billing_info'))
def get_organization_output(name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetOrganizationResult]:
    """
    A PlanetScale organization.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_planetscale as planetscale

    example = planetscale.get_organization(name="example")
    pulumi.export("org", example)
    ```


    :param str name: The name of the organization.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('planetscale:index/getOrganization:getOrganization', __args__, opts=opts, typ=GetOrganizationResult)
    return __ret__.apply(lambda __response__: GetOrganizationResult(
        billing_email=pulumi.get(__response__, 'billing_email'),
        created_at=pulumi.get(__response__, 'created_at'),
        database_count=pulumi.get(__response__, 'database_count'),
        features=pulumi.get(__response__, 'features'),
        flags=pulumi.get(__response__, 'flags'),
        has_past_due_invoices=pulumi.get(__response__, 'has_past_due_invoices'),
        id=pulumi.get(__response__, 'id'),
        idp_managed_roles=pulumi.get(__response__, 'idp_managed_roles'),
        name=pulumi.get(__response__, 'name'),
        plan=pulumi.get(__response__, 'plan'),
        single_tenancy=pulumi.get(__response__, 'single_tenancy'),
        sleeping_database_count=pulumi.get(__response__, 'sleeping_database_count'),
        sso=pulumi.get(__response__, 'sso'),
        sso_directory=pulumi.get(__response__, 'sso_directory'),
        sso_portal_url=pulumi.get(__response__, 'sso_portal_url'),
        updated_at=pulumi.get(__response__, 'updated_at'),
        valid_billing_info=pulumi.get(__response__, 'valid_billing_info')))
