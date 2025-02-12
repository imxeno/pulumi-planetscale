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

__all__ = ['BackupArgs', 'Backup']

@pulumi.input_type
class BackupArgs:
    def __init__(__self__, *,
                 branch: pulumi.Input[str],
                 database: pulumi.Input[str],
                 organization: pulumi.Input[str],
                 retention_unit: pulumi.Input[str],
                 retention_value: pulumi.Input[float],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Backup resource.
        :param pulumi.Input[str] branch: The branch being backed up.
        :param pulumi.Input[str] database: The database to which the branch being backed up belongs to.
        :param pulumi.Input[str] organization: The organization in which the database branch being backed up belongs to.
        :param pulumi.Input[str] retention_unit: The unit for the retention period of the backup policy.
        :param pulumi.Input[float] retention_value: A number value for the retention period of the backup policy.
        :param pulumi.Input[str] name: The name of the backup.
        """
        pulumi.set(__self__, "branch", branch)
        pulumi.set(__self__, "database", database)
        pulumi.set(__self__, "organization", organization)
        pulumi.set(__self__, "retention_unit", retention_unit)
        pulumi.set(__self__, "retention_value", retention_value)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def branch(self) -> pulumi.Input[str]:
        """
        The branch being backed up.
        """
        return pulumi.get(self, "branch")

    @branch.setter
    def branch(self, value: pulumi.Input[str]):
        pulumi.set(self, "branch", value)

    @property
    @pulumi.getter
    def database(self) -> pulumi.Input[str]:
        """
        The database to which the branch being backed up belongs to.
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: pulumi.Input[str]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def organization(self) -> pulumi.Input[str]:
        """
        The organization in which the database branch being backed up belongs to.
        """
        return pulumi.get(self, "organization")

    @organization.setter
    def organization(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization", value)

    @property
    @pulumi.getter(name="retentionUnit")
    def retention_unit(self) -> pulumi.Input[str]:
        """
        The unit for the retention period of the backup policy.
        """
        return pulumi.get(self, "retention_unit")

    @retention_unit.setter
    def retention_unit(self, value: pulumi.Input[str]):
        pulumi.set(self, "retention_unit", value)

    @property
    @pulumi.getter(name="retentionValue")
    def retention_value(self) -> pulumi.Input[float]:
        """
        A number value for the retention period of the backup policy.
        """
        return pulumi.get(self, "retention_value")

    @retention_value.setter
    def retention_value(self, value: pulumi.Input[float]):
        pulumi.set(self, "retention_value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the backup.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _BackupState:
    def __init__(__self__, *,
                 actor: Optional[pulumi.Input['BackupActorArgs']] = None,
                 backup_policy: Optional[pulumi.Input['BackupBackupPolicyArgs']] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 estimated_storage_cost: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 required: Optional[pulumi.Input[bool]] = None,
                 restored_branches: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 retention_unit: Optional[pulumi.Input[str]] = None,
                 retention_value: Optional[pulumi.Input[float]] = None,
                 size: Optional[pulumi.Input[float]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Backup resources.
        :param pulumi.Input['BackupActorArgs'] actor: .
        :param pulumi.Input['BackupBackupPolicyArgs'] backup_policy: The policy used by the backup.
        :param pulumi.Input[str] branch: The branch being backed up.
        :param pulumi.Input[str] created_at: When the backup was created.
        :param pulumi.Input[str] database: The database to which the branch being backed up belongs to.
        :param pulumi.Input[float] estimated_storage_cost: The estimated storage cost of the backup.
        :param pulumi.Input[str] name: The name of the backup.
        :param pulumi.Input[str] organization: The organization in which the database branch being backed up belongs to.
        :param pulumi.Input[bool] required: Whether or not the backup policy is required.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] restored_branches: Branches that have been restored with this backup.
        :param pulumi.Input[str] retention_unit: The unit for the retention period of the backup policy.
        :param pulumi.Input[float] retention_value: A number value for the retention period of the backup policy.
        :param pulumi.Input[float] size: The size of the backup.
        :param pulumi.Input[str] state: The current state of the backup.
        :param pulumi.Input[str] updated_at: When the backup was last updated.
        """
        if actor is not None:
            pulumi.set(__self__, "actor", actor)
        if backup_policy is not None:
            pulumi.set(__self__, "backup_policy", backup_policy)
        if branch is not None:
            pulumi.set(__self__, "branch", branch)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if database is not None:
            pulumi.set(__self__, "database", database)
        if estimated_storage_cost is not None:
            pulumi.set(__self__, "estimated_storage_cost", estimated_storage_cost)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if organization is not None:
            pulumi.set(__self__, "organization", organization)
        if required is not None:
            pulumi.set(__self__, "required", required)
        if restored_branches is not None:
            pulumi.set(__self__, "restored_branches", restored_branches)
        if retention_unit is not None:
            pulumi.set(__self__, "retention_unit", retention_unit)
        if retention_value is not None:
            pulumi.set(__self__, "retention_value", retention_value)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter
    def actor(self) -> Optional[pulumi.Input['BackupActorArgs']]:
        """
        .
        """
        return pulumi.get(self, "actor")

    @actor.setter
    def actor(self, value: Optional[pulumi.Input['BackupActorArgs']]):
        pulumi.set(self, "actor", value)

    @property
    @pulumi.getter(name="backupPolicy")
    def backup_policy(self) -> Optional[pulumi.Input['BackupBackupPolicyArgs']]:
        """
        The policy used by the backup.
        """
        return pulumi.get(self, "backup_policy")

    @backup_policy.setter
    def backup_policy(self, value: Optional[pulumi.Input['BackupBackupPolicyArgs']]):
        pulumi.set(self, "backup_policy", value)

    @property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[str]]:
        """
        The branch being backed up.
        """
        return pulumi.get(self, "branch")

    @branch.setter
    def branch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "branch", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        When the backup was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[str]]:
        """
        The database to which the branch being backed up belongs to.
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter(name="estimatedStorageCost")
    def estimated_storage_cost(self) -> Optional[pulumi.Input[float]]:
        """
        The estimated storage cost of the backup.
        """
        return pulumi.get(self, "estimated_storage_cost")

    @estimated_storage_cost.setter
    def estimated_storage_cost(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "estimated_storage_cost", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the backup.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[str]]:
        """
        The organization in which the database branch being backed up belongs to.
        """
        return pulumi.get(self, "organization")

    @organization.setter
    def organization(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization", value)

    @property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not the backup policy is required.
        """
        return pulumi.get(self, "required")

    @required.setter
    def required(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "required", value)

    @property
    @pulumi.getter(name="restoredBranches")
    def restored_branches(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Branches that have been restored with this backup.
        """
        return pulumi.get(self, "restored_branches")

    @restored_branches.setter
    def restored_branches(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "restored_branches", value)

    @property
    @pulumi.getter(name="retentionUnit")
    def retention_unit(self) -> Optional[pulumi.Input[str]]:
        """
        The unit for the retention period of the backup policy.
        """
        return pulumi.get(self, "retention_unit")

    @retention_unit.setter
    def retention_unit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "retention_unit", value)

    @property
    @pulumi.getter(name="retentionValue")
    def retention_value(self) -> Optional[pulumi.Input[float]]:
        """
        A number value for the retention period of the backup policy.
        """
        return pulumi.get(self, "retention_value")

    @retention_value.setter
    def retention_value(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "retention_value", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[float]]:
        """
        The size of the backup.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of the backup.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        When the backup was last updated.
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)


class Backup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 retention_unit: Optional[pulumi.Input[str]] = None,
                 retention_value: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        """
        A PlanetScale backup.

        Known limitations:
        - It is not currently possible to manage backup schedules, only retention periods.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] branch: The branch being backed up.
        :param pulumi.Input[str] database: The database to which the branch being backed up belongs to.
        :param pulumi.Input[str] name: The name of the backup.
        :param pulumi.Input[str] organization: The organization in which the database branch being backed up belongs to.
        :param pulumi.Input[str] retention_unit: The unit for the retention period of the backup policy.
        :param pulumi.Input[float] retention_value: A number value for the retention period of the backup policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BackupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A PlanetScale backup.

        Known limitations:
        - It is not currently possible to manage backup schedules, only retention periods.

        :param str resource_name: The name of the resource.
        :param BackupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BackupArgs, pulumi.ResourceOptions, *args, **kwargs)
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
                 retention_unit: Optional[pulumi.Input[str]] = None,
                 retention_value: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BackupArgs.__new__(BackupArgs)

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
            if retention_unit is None and not opts.urn:
                raise TypeError("Missing required property 'retention_unit'")
            __props__.__dict__["retention_unit"] = retention_unit
            if retention_value is None and not opts.urn:
                raise TypeError("Missing required property 'retention_value'")
            __props__.__dict__["retention_value"] = retention_value
            __props__.__dict__["actor"] = None
            __props__.__dict__["backup_policy"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["estimated_storage_cost"] = None
            __props__.__dict__["required"] = None
            __props__.__dict__["restored_branches"] = None
            __props__.__dict__["size"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["updated_at"] = None
        super(Backup, __self__).__init__(
            'planetscale:index/backup:Backup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            actor: Optional[pulumi.Input[Union['BackupActorArgs', 'BackupActorArgsDict']]] = None,
            backup_policy: Optional[pulumi.Input[Union['BackupBackupPolicyArgs', 'BackupBackupPolicyArgsDict']]] = None,
            branch: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            database: Optional[pulumi.Input[str]] = None,
            estimated_storage_cost: Optional[pulumi.Input[float]] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization: Optional[pulumi.Input[str]] = None,
            required: Optional[pulumi.Input[bool]] = None,
            restored_branches: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            retention_unit: Optional[pulumi.Input[str]] = None,
            retention_value: Optional[pulumi.Input[float]] = None,
            size: Optional[pulumi.Input[float]] = None,
            state: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'Backup':
        """
        Get an existing Backup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['BackupActorArgs', 'BackupActorArgsDict']] actor: .
        :param pulumi.Input[Union['BackupBackupPolicyArgs', 'BackupBackupPolicyArgsDict']] backup_policy: The policy used by the backup.
        :param pulumi.Input[str] branch: The branch being backed up.
        :param pulumi.Input[str] created_at: When the backup was created.
        :param pulumi.Input[str] database: The database to which the branch being backed up belongs to.
        :param pulumi.Input[float] estimated_storage_cost: The estimated storage cost of the backup.
        :param pulumi.Input[str] name: The name of the backup.
        :param pulumi.Input[str] organization: The organization in which the database branch being backed up belongs to.
        :param pulumi.Input[bool] required: Whether or not the backup policy is required.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] restored_branches: Branches that have been restored with this backup.
        :param pulumi.Input[str] retention_unit: The unit for the retention period of the backup policy.
        :param pulumi.Input[float] retention_value: A number value for the retention period of the backup policy.
        :param pulumi.Input[float] size: The size of the backup.
        :param pulumi.Input[str] state: The current state of the backup.
        :param pulumi.Input[str] updated_at: When the backup was last updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BackupState.__new__(_BackupState)

        __props__.__dict__["actor"] = actor
        __props__.__dict__["backup_policy"] = backup_policy
        __props__.__dict__["branch"] = branch
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["database"] = database
        __props__.__dict__["estimated_storage_cost"] = estimated_storage_cost
        __props__.__dict__["name"] = name
        __props__.__dict__["organization"] = organization
        __props__.__dict__["required"] = required
        __props__.__dict__["restored_branches"] = restored_branches
        __props__.__dict__["retention_unit"] = retention_unit
        __props__.__dict__["retention_value"] = retention_value
        __props__.__dict__["size"] = size
        __props__.__dict__["state"] = state
        __props__.__dict__["updated_at"] = updated_at
        return Backup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actor(self) -> pulumi.Output['outputs.BackupActor']:
        """
        .
        """
        return pulumi.get(self, "actor")

    @property
    @pulumi.getter(name="backupPolicy")
    def backup_policy(self) -> pulumi.Output['outputs.BackupBackupPolicy']:
        """
        The policy used by the backup.
        """
        return pulumi.get(self, "backup_policy")

    @property
    @pulumi.getter
    def branch(self) -> pulumi.Output[str]:
        """
        The branch being backed up.
        """
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        When the backup was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def database(self) -> pulumi.Output[str]:
        """
        The database to which the branch being backed up belongs to.
        """
        return pulumi.get(self, "database")

    @property
    @pulumi.getter(name="estimatedStorageCost")
    def estimated_storage_cost(self) -> pulumi.Output[float]:
        """
        The estimated storage cost of the backup.
        """
        return pulumi.get(self, "estimated_storage_cost")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the backup.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def organization(self) -> pulumi.Output[str]:
        """
        The organization in which the database branch being backed up belongs to.
        """
        return pulumi.get(self, "organization")

    @property
    @pulumi.getter
    def required(self) -> pulumi.Output[bool]:
        """
        Whether or not the backup policy is required.
        """
        return pulumi.get(self, "required")

    @property
    @pulumi.getter(name="restoredBranches")
    def restored_branches(self) -> pulumi.Output[Sequence[str]]:
        """
        Branches that have been restored with this backup.
        """
        return pulumi.get(self, "restored_branches")

    @property
    @pulumi.getter(name="retentionUnit")
    def retention_unit(self) -> pulumi.Output[str]:
        """
        The unit for the retention period of the backup policy.
        """
        return pulumi.get(self, "retention_unit")

    @property
    @pulumi.getter(name="retentionValue")
    def retention_value(self) -> pulumi.Output[float]:
        """
        A number value for the retention period of the backup policy.
        """
        return pulumi.get(self, "retention_value")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[float]:
        """
        The size of the backup.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the backup.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        When the backup was last updated.
        """
        return pulumi.get(self, "updated_at")

