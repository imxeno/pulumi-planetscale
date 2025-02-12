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
from ._inputs import *

__all__ = ['PasswordArgs', 'Password']

@pulumi.input_type
class PasswordArgs:
    def __init__(__self__, *,
                 branch: pulumi.Input[str],
                 database: pulumi.Input[str],
                 organization: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 ttl_seconds: Optional[pulumi.Input[float]] = None):
        """
        The set of arguments for constructing a Password resource.
        :param pulumi.Input[str] branch: The branch this password belongs to.
        :param pulumi.Input[str] database: The database this branch password belongs to.
        :param pulumi.Input[str] organization: The organization this database branch password belongs to.
        :param pulumi.Input[str] name: The display name for the password.
        :param pulumi.Input[str] role: The role for the password.
        :param pulumi.Input[float] ttl_seconds: Time to live (in seconds) for the password. The password will be invalid and unrenewable when TTL has passed.
        """
        pulumi.set(__self__, "branch", branch)
        pulumi.set(__self__, "database", database)
        pulumi.set(__self__, "organization", organization)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if ttl_seconds is not None:
            pulumi.set(__self__, "ttl_seconds", ttl_seconds)

    @property
    @pulumi.getter
    def branch(self) -> pulumi.Input[str]:
        """
        The branch this password belongs to.
        """
        return pulumi.get(self, "branch")

    @branch.setter
    def branch(self, value: pulumi.Input[str]):
        pulumi.set(self, "branch", value)

    @property
    @pulumi.getter
    def database(self) -> pulumi.Input[str]:
        """
        The database this branch password belongs to.
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: pulumi.Input[str]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def organization(self) -> pulumi.Input[str]:
        """
        The organization this database branch password belongs to.
        """
        return pulumi.get(self, "organization")

    @organization.setter
    def organization(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name for the password.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The role for the password.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="ttlSeconds")
    def ttl_seconds(self) -> Optional[pulumi.Input[float]]:
        """
        Time to live (in seconds) for the password. The password will be invalid and unrenewable when TTL has passed.
        """
        return pulumi.get(self, "ttl_seconds")

    @ttl_seconds.setter
    def ttl_seconds(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "ttl_seconds", value)


@pulumi.input_type
class _PasswordState:
    def __init__(__self__, *,
                 access_host_url: Optional[pulumi.Input[str]] = None,
                 actor: Optional[pulumi.Input['PasswordActorArgs']] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 database_branch: Optional[pulumi.Input['PasswordDatabaseBranchArgs']] = None,
                 deleted_at: Optional[pulumi.Input[str]] = None,
                 expires_at: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 plaintext: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input['PasswordRegionArgs']] = None,
                 renewable: Optional[pulumi.Input[bool]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 ttl_seconds: Optional[pulumi.Input[float]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Password resources.
        :param pulumi.Input[str] access_host_url: The host URL for the password.
        :param pulumi.Input['PasswordActorArgs'] actor: The actor that created this branch.
        :param pulumi.Input[str] branch: The branch this password belongs to.
        :param pulumi.Input[str] created_at: When the password was created.
        :param pulumi.Input[str] database: The database this branch password belongs to.
        :param pulumi.Input['PasswordDatabaseBranchArgs'] database_branch: The branch this password is allowed to access.
        :param pulumi.Input[str] deleted_at: When the password was deleted.
        :param pulumi.Input[str] expires_at: When the password will expire.
        :param pulumi.Input[str] name: The display name for the password.
        :param pulumi.Input[str] organization: The organization this database branch password belongs to.
        :param pulumi.Input[str] plaintext: The plaintext password, only available if the password was created by this provider.
        :param pulumi.Input['PasswordRegionArgs'] region: The region in which this password can be used.
        :param pulumi.Input[bool] renewable: Whether or not the password can be renewed.
        :param pulumi.Input[str] role: The role for the password.
        :param pulumi.Input[float] ttl_seconds: Time to live (in seconds) for the password. The password will be invalid and unrenewable when TTL has passed.
        :param pulumi.Input[str] username: The username for the password.
        """
        if access_host_url is not None:
            pulumi.set(__self__, "access_host_url", access_host_url)
        if actor is not None:
            pulumi.set(__self__, "actor", actor)
        if branch is not None:
            pulumi.set(__self__, "branch", branch)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if database is not None:
            pulumi.set(__self__, "database", database)
        if database_branch is not None:
            pulumi.set(__self__, "database_branch", database_branch)
        if deleted_at is not None:
            pulumi.set(__self__, "deleted_at", deleted_at)
        if expires_at is not None:
            pulumi.set(__self__, "expires_at", expires_at)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if organization is not None:
            pulumi.set(__self__, "organization", organization)
        if plaintext is not None:
            pulumi.set(__self__, "plaintext", plaintext)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if renewable is not None:
            pulumi.set(__self__, "renewable", renewable)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if ttl_seconds is not None:
            pulumi.set(__self__, "ttl_seconds", ttl_seconds)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="accessHostUrl")
    def access_host_url(self) -> Optional[pulumi.Input[str]]:
        """
        The host URL for the password.
        """
        return pulumi.get(self, "access_host_url")

    @access_host_url.setter
    def access_host_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_host_url", value)

    @property
    @pulumi.getter
    def actor(self) -> Optional[pulumi.Input['PasswordActorArgs']]:
        """
        The actor that created this branch.
        """
        return pulumi.get(self, "actor")

    @actor.setter
    def actor(self, value: Optional[pulumi.Input['PasswordActorArgs']]):
        pulumi.set(self, "actor", value)

    @property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[str]]:
        """
        The branch this password belongs to.
        """
        return pulumi.get(self, "branch")

    @branch.setter
    def branch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "branch", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        When the password was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[str]]:
        """
        The database this branch password belongs to.
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter(name="databaseBranch")
    def database_branch(self) -> Optional[pulumi.Input['PasswordDatabaseBranchArgs']]:
        """
        The branch this password is allowed to access.
        """
        return pulumi.get(self, "database_branch")

    @database_branch.setter
    def database_branch(self, value: Optional[pulumi.Input['PasswordDatabaseBranchArgs']]):
        pulumi.set(self, "database_branch", value)

    @property
    @pulumi.getter(name="deletedAt")
    def deleted_at(self) -> Optional[pulumi.Input[str]]:
        """
        When the password was deleted.
        """
        return pulumi.get(self, "deleted_at")

    @deleted_at.setter
    def deleted_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deleted_at", value)

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[pulumi.Input[str]]:
        """
        When the password will expire.
        """
        return pulumi.get(self, "expires_at")

    @expires_at.setter
    def expires_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires_at", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name for the password.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[str]]:
        """
        The organization this database branch password belongs to.
        """
        return pulumi.get(self, "organization")

    @organization.setter
    def organization(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization", value)

    @property
    @pulumi.getter
    def plaintext(self) -> Optional[pulumi.Input[str]]:
        """
        The plaintext password, only available if the password was created by this provider.
        """
        return pulumi.get(self, "plaintext")

    @plaintext.setter
    def plaintext(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plaintext", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input['PasswordRegionArgs']]:
        """
        The region in which this password can be used.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input['PasswordRegionArgs']]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def renewable(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not the password can be renewed.
        """
        return pulumi.get(self, "renewable")

    @renewable.setter
    def renewable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "renewable", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The role for the password.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="ttlSeconds")
    def ttl_seconds(self) -> Optional[pulumi.Input[float]]:
        """
        Time to live (in seconds) for the password. The password will be invalid and unrenewable when TTL has passed.
        """
        return pulumi.get(self, "ttl_seconds")

    @ttl_seconds.setter
    def ttl_seconds(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "ttl_seconds", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        The username for the password.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class Password(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 ttl_seconds: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        """
        A PlanetScale database password.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_planetscale as planetscale

        example = planetscale.Password("example",
            organization="example",
            database="example_db",
            branch="main",
            name="a-password-for-antoine")
        pulumi.export("password", example)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] branch: The branch this password belongs to.
        :param pulumi.Input[str] database: The database this branch password belongs to.
        :param pulumi.Input[str] name: The display name for the password.
        :param pulumi.Input[str] organization: The organization this database branch password belongs to.
        :param pulumi.Input[str] role: The role for the password.
        :param pulumi.Input[float] ttl_seconds: Time to live (in seconds) for the password. The password will be invalid and unrenewable when TTL has passed.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PasswordArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A PlanetScale database password.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_planetscale as planetscale

        example = planetscale.Password("example",
            organization="example",
            database="example_db",
            branch="main",
            name="a-password-for-antoine")
        pulumi.export("password", example)
        ```

        :param str resource_name: The name of the resource.
        :param PasswordArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PasswordArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 ttl_seconds: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PasswordArgs.__new__(PasswordArgs)

            if branch is None and not opts.urn:
                raise TypeError("Missing required property 'branch'")
            __props__.__dict__["branch"] = branch
            if database is None and not opts.urn:
                raise TypeError("Missing required property 'database'")
            __props__.__dict__["database"] = database
            __props__.__dict__["name"] = name
            if organization is None and not opts.urn:
                raise TypeError("Missing required property 'organization'")
            __props__.__dict__["organization"] = organization
            __props__.__dict__["role"] = role
            __props__.__dict__["ttl_seconds"] = ttl_seconds
            __props__.__dict__["access_host_url"] = None
            __props__.__dict__["actor"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["database_branch"] = None
            __props__.__dict__["deleted_at"] = None
            __props__.__dict__["expires_at"] = None
            __props__.__dict__["plaintext"] = None
            __props__.__dict__["region"] = None
            __props__.__dict__["renewable"] = None
            __props__.__dict__["username"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["plaintext"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Password, __self__).__init__(
            'planetscale:index/password:Password',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_host_url: Optional[pulumi.Input[str]] = None,
            actor: Optional[pulumi.Input[Union['PasswordActorArgs', 'PasswordActorArgsDict']]] = None,
            branch: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            database: Optional[pulumi.Input[str]] = None,
            database_branch: Optional[pulumi.Input[Union['PasswordDatabaseBranchArgs', 'PasswordDatabaseBranchArgsDict']]] = None,
            deleted_at: Optional[pulumi.Input[str]] = None,
            expires_at: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization: Optional[pulumi.Input[str]] = None,
            plaintext: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[Union['PasswordRegionArgs', 'PasswordRegionArgsDict']]] = None,
            renewable: Optional[pulumi.Input[bool]] = None,
            role: Optional[pulumi.Input[str]] = None,
            ttl_seconds: Optional[pulumi.Input[float]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'Password':
        """
        Get an existing Password resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_host_url: The host URL for the password.
        :param pulumi.Input[Union['PasswordActorArgs', 'PasswordActorArgsDict']] actor: The actor that created this branch.
        :param pulumi.Input[str] branch: The branch this password belongs to.
        :param pulumi.Input[str] created_at: When the password was created.
        :param pulumi.Input[str] database: The database this branch password belongs to.
        :param pulumi.Input[Union['PasswordDatabaseBranchArgs', 'PasswordDatabaseBranchArgsDict']] database_branch: The branch this password is allowed to access.
        :param pulumi.Input[str] deleted_at: When the password was deleted.
        :param pulumi.Input[str] expires_at: When the password will expire.
        :param pulumi.Input[str] name: The display name for the password.
        :param pulumi.Input[str] organization: The organization this database branch password belongs to.
        :param pulumi.Input[str] plaintext: The plaintext password, only available if the password was created by this provider.
        :param pulumi.Input[Union['PasswordRegionArgs', 'PasswordRegionArgsDict']] region: The region in which this password can be used.
        :param pulumi.Input[bool] renewable: Whether or not the password can be renewed.
        :param pulumi.Input[str] role: The role for the password.
        :param pulumi.Input[float] ttl_seconds: Time to live (in seconds) for the password. The password will be invalid and unrenewable when TTL has passed.
        :param pulumi.Input[str] username: The username for the password.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PasswordState.__new__(_PasswordState)

        __props__.__dict__["access_host_url"] = access_host_url
        __props__.__dict__["actor"] = actor
        __props__.__dict__["branch"] = branch
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["database"] = database
        __props__.__dict__["database_branch"] = database_branch
        __props__.__dict__["deleted_at"] = deleted_at
        __props__.__dict__["expires_at"] = expires_at
        __props__.__dict__["name"] = name
        __props__.__dict__["organization"] = organization
        __props__.__dict__["plaintext"] = plaintext
        __props__.__dict__["region"] = region
        __props__.__dict__["renewable"] = renewable
        __props__.__dict__["role"] = role
        __props__.__dict__["ttl_seconds"] = ttl_seconds
        __props__.__dict__["username"] = username
        return Password(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessHostUrl")
    def access_host_url(self) -> pulumi.Output[str]:
        """
        The host URL for the password.
        """
        return pulumi.get(self, "access_host_url")

    @property
    @pulumi.getter
    def actor(self) -> pulumi.Output['outputs.PasswordActor']:
        """
        The actor that created this branch.
        """
        return pulumi.get(self, "actor")

    @property
    @pulumi.getter
    def branch(self) -> pulumi.Output[str]:
        """
        The branch this password belongs to.
        """
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        When the password was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def database(self) -> pulumi.Output[str]:
        """
        The database this branch password belongs to.
        """
        return pulumi.get(self, "database")

    @property
    @pulumi.getter(name="databaseBranch")
    def database_branch(self) -> pulumi.Output['outputs.PasswordDatabaseBranch']:
        """
        The branch this password is allowed to access.
        """
        return pulumi.get(self, "database_branch")

    @property
    @pulumi.getter(name="deletedAt")
    def deleted_at(self) -> pulumi.Output[str]:
        """
        When the password was deleted.
        """
        return pulumi.get(self, "deleted_at")

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> pulumi.Output[str]:
        """
        When the password will expire.
        """
        return pulumi.get(self, "expires_at")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The display name for the password.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def organization(self) -> pulumi.Output[str]:
        """
        The organization this database branch password belongs to.
        """
        return pulumi.get(self, "organization")

    @property
    @pulumi.getter
    def plaintext(self) -> pulumi.Output[str]:
        """
        The plaintext password, only available if the password was created by this provider.
        """
        return pulumi.get(self, "plaintext")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output['outputs.PasswordRegion']:
        """
        The region in which this password can be used.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def renewable(self) -> pulumi.Output[bool]:
        """
        Whether or not the password can be renewed.
        """
        return pulumi.get(self, "renewable")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The role for the password.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="ttlSeconds")
    def ttl_seconds(self) -> pulumi.Output[float]:
        """
        Time to live (in seconds) for the password. The password will be invalid and unrenewable when TTL has passed.
        """
        return pulumi.get(self, "ttl_seconds")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        The username for the password.
        """
        return pulumi.get(self, "username")

