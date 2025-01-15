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

__all__ = [
    'GetDatabaseResult',
    'AwaitableGetDatabaseResult',
    'get_database',
    'get_database_output',
]

@pulumi.output_type
class GetDatabaseResult:
    """
    A collection of values returned by getDatabase.
    """
    def __init__(__self__, allow_data_branching=None, at_backup_restore_branches_limit=None, at_development_branch_limit=None, automatic_migrations=None, branches_count=None, branches_url=None, created_at=None, data_import=None, default_branch=None, default_branch_read_only_regions_count=None, default_branch_shard_count=None, default_branch_table_count=None, development_branches_count=None, html_url=None, id=None, insights_raw_queries=None, issues_count=None, migration_framework=None, migration_table_name=None, multiple_admins_required_for_deletion=None, name=None, organization=None, plan=None, production_branch_web_console=None, production_branches_count=None, ready=None, region=None, require_approval_for_deploy=None, restrict_branch_region=None, schema_last_updated_at=None, sharded=None, state=None, updated_at=None, url=None):
        if allow_data_branching and not isinstance(allow_data_branching, bool):
            raise TypeError("Expected argument 'allow_data_branching' to be a bool")
        pulumi.set(__self__, "allow_data_branching", allow_data_branching)
        if at_backup_restore_branches_limit and not isinstance(at_backup_restore_branches_limit, bool):
            raise TypeError("Expected argument 'at_backup_restore_branches_limit' to be a bool")
        pulumi.set(__self__, "at_backup_restore_branches_limit", at_backup_restore_branches_limit)
        if at_development_branch_limit and not isinstance(at_development_branch_limit, bool):
            raise TypeError("Expected argument 'at_development_branch_limit' to be a bool")
        pulumi.set(__self__, "at_development_branch_limit", at_development_branch_limit)
        if automatic_migrations and not isinstance(automatic_migrations, bool):
            raise TypeError("Expected argument 'automatic_migrations' to be a bool")
        pulumi.set(__self__, "automatic_migrations", automatic_migrations)
        if branches_count and not isinstance(branches_count, float):
            raise TypeError("Expected argument 'branches_count' to be a float")
        pulumi.set(__self__, "branches_count", branches_count)
        if branches_url and not isinstance(branches_url, str):
            raise TypeError("Expected argument 'branches_url' to be a str")
        pulumi.set(__self__, "branches_url", branches_url)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if data_import and not isinstance(data_import, dict):
            raise TypeError("Expected argument 'data_import' to be a dict")
        pulumi.set(__self__, "data_import", data_import)
        if default_branch and not isinstance(default_branch, str):
            raise TypeError("Expected argument 'default_branch' to be a str")
        pulumi.set(__self__, "default_branch", default_branch)
        if default_branch_read_only_regions_count and not isinstance(default_branch_read_only_regions_count, float):
            raise TypeError("Expected argument 'default_branch_read_only_regions_count' to be a float")
        pulumi.set(__self__, "default_branch_read_only_regions_count", default_branch_read_only_regions_count)
        if default_branch_shard_count and not isinstance(default_branch_shard_count, float):
            raise TypeError("Expected argument 'default_branch_shard_count' to be a float")
        pulumi.set(__self__, "default_branch_shard_count", default_branch_shard_count)
        if default_branch_table_count and not isinstance(default_branch_table_count, float):
            raise TypeError("Expected argument 'default_branch_table_count' to be a float")
        pulumi.set(__self__, "default_branch_table_count", default_branch_table_count)
        if development_branches_count and not isinstance(development_branches_count, float):
            raise TypeError("Expected argument 'development_branches_count' to be a float")
        pulumi.set(__self__, "development_branches_count", development_branches_count)
        if html_url and not isinstance(html_url, str):
            raise TypeError("Expected argument 'html_url' to be a str")
        pulumi.set(__self__, "html_url", html_url)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if insights_raw_queries and not isinstance(insights_raw_queries, bool):
            raise TypeError("Expected argument 'insights_raw_queries' to be a bool")
        pulumi.set(__self__, "insights_raw_queries", insights_raw_queries)
        if issues_count and not isinstance(issues_count, float):
            raise TypeError("Expected argument 'issues_count' to be a float")
        pulumi.set(__self__, "issues_count", issues_count)
        if migration_framework and not isinstance(migration_framework, str):
            raise TypeError("Expected argument 'migration_framework' to be a str")
        pulumi.set(__self__, "migration_framework", migration_framework)
        if migration_table_name and not isinstance(migration_table_name, str):
            raise TypeError("Expected argument 'migration_table_name' to be a str")
        pulumi.set(__self__, "migration_table_name", migration_table_name)
        if multiple_admins_required_for_deletion and not isinstance(multiple_admins_required_for_deletion, bool):
            raise TypeError("Expected argument 'multiple_admins_required_for_deletion' to be a bool")
        pulumi.set(__self__, "multiple_admins_required_for_deletion", multiple_admins_required_for_deletion)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if organization and not isinstance(organization, str):
            raise TypeError("Expected argument 'organization' to be a str")
        pulumi.set(__self__, "organization", organization)
        if plan and not isinstance(plan, str):
            raise TypeError("Expected argument 'plan' to be a str")
        pulumi.set(__self__, "plan", plan)
        if production_branch_web_console and not isinstance(production_branch_web_console, bool):
            raise TypeError("Expected argument 'production_branch_web_console' to be a bool")
        pulumi.set(__self__, "production_branch_web_console", production_branch_web_console)
        if production_branches_count and not isinstance(production_branches_count, float):
            raise TypeError("Expected argument 'production_branches_count' to be a float")
        pulumi.set(__self__, "production_branches_count", production_branches_count)
        if ready and not isinstance(ready, bool):
            raise TypeError("Expected argument 'ready' to be a bool")
        pulumi.set(__self__, "ready", ready)
        if region and not isinstance(region, dict):
            raise TypeError("Expected argument 'region' to be a dict")
        pulumi.set(__self__, "region", region)
        if require_approval_for_deploy and not isinstance(require_approval_for_deploy, bool):
            raise TypeError("Expected argument 'require_approval_for_deploy' to be a bool")
        pulumi.set(__self__, "require_approval_for_deploy", require_approval_for_deploy)
        if restrict_branch_region and not isinstance(restrict_branch_region, bool):
            raise TypeError("Expected argument 'restrict_branch_region' to be a bool")
        pulumi.set(__self__, "restrict_branch_region", restrict_branch_region)
        if schema_last_updated_at and not isinstance(schema_last_updated_at, str):
            raise TypeError("Expected argument 'schema_last_updated_at' to be a str")
        pulumi.set(__self__, "schema_last_updated_at", schema_last_updated_at)
        if sharded and not isinstance(sharded, bool):
            raise TypeError("Expected argument 'sharded' to be a bool")
        pulumi.set(__self__, "sharded", sharded)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="allowDataBranching")
    def allow_data_branching(self) -> bool:
        """
        Whether seeding branches with data is enabled for all branches.
        """
        return pulumi.get(self, "allow_data_branching")

    @property
    @pulumi.getter(name="atBackupRestoreBranchesLimit")
    def at_backup_restore_branches_limit(self) -> bool:
        """
        If the database has reached its backup restored branch limit.
        """
        return pulumi.get(self, "at_backup_restore_branches_limit")

    @property
    @pulumi.getter(name="atDevelopmentBranchLimit")
    def at_development_branch_limit(self) -> bool:
        """
        If the database has reached its development branch limit.
        """
        return pulumi.get(self, "at_development_branch_limit")

    @property
    @pulumi.getter(name="automaticMigrations")
    def automatic_migrations(self) -> bool:
        """
        Whether to automatically manage Rails migrations during deploy requests.
        """
        return pulumi.get(self, "automatic_migrations")

    @property
    @pulumi.getter(name="branchesCount")
    def branches_count(self) -> float:
        """
        The total number of database branches.
        """
        return pulumi.get(self, "branches_count")

    @property
    @pulumi.getter(name="branchesUrl")
    def branches_url(self) -> str:
        """
        The URL to retrieve this database's branches via the API.
        """
        return pulumi.get(self, "branches_url")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        When the database was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="dataImport")
    def data_import(self) -> Optional['outputs.GetDatabaseDataImportResult']:
        """
        If the database was created from an import, describes the import process.
        """
        return pulumi.get(self, "data_import")

    @property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> str:
        """
        The default branch for the database.
        """
        return pulumi.get(self, "default_branch")

    @property
    @pulumi.getter(name="defaultBranchReadOnlyRegionsCount")
    def default_branch_read_only_regions_count(self) -> float:
        """
        Number of read only regions in the default branch.
        """
        return pulumi.get(self, "default_branch_read_only_regions_count")

    @property
    @pulumi.getter(name="defaultBranchShardCount")
    def default_branch_shard_count(self) -> float:
        """
        Number of shards in the default branch.
        """
        return pulumi.get(self, "default_branch_shard_count")

    @property
    @pulumi.getter(name="defaultBranchTableCount")
    def default_branch_table_count(self) -> float:
        """
        Number of tables in the default branch schema.
        """
        return pulumi.get(self, "default_branch_table_count")

    @property
    @pulumi.getter(name="developmentBranchesCount")
    def development_branches_count(self) -> float:
        """
        The total number of database development branches.
        """
        return pulumi.get(self, "development_branches_count")

    @property
    @pulumi.getter(name="htmlUrl")
    def html_url(self) -> str:
        """
        The total number of database development branches.
        """
        return pulumi.get(self, "html_url")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the database.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="insightsRawQueries")
    def insights_raw_queries(self) -> bool:
        """
        The URL to see this database's branches in the web UI.
        """
        return pulumi.get(self, "insights_raw_queries")

    @property
    @pulumi.getter(name="issuesCount")
    def issues_count(self) -> float:
        """
        The total number of ongoing issues within a database.
        """
        return pulumi.get(self, "issues_count")

    @property
    @pulumi.getter(name="migrationFramework")
    def migration_framework(self) -> str:
        """
        Framework used for applying migrations.
        """
        return pulumi.get(self, "migration_framework")

    @property
    @pulumi.getter(name="migrationTableName")
    def migration_table_name(self) -> str:
        """
        Table name to use for copying schema migration data.
        """
        return pulumi.get(self, "migration_table_name")

    @property
    @pulumi.getter(name="multipleAdminsRequiredForDeletion")
    def multiple_admins_required_for_deletion(self) -> bool:
        """
        If the database requires multiple admins for deletion.
        """
        return pulumi.get(self, "multiple_admins_required_for_deletion")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of this database.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def organization(self) -> str:
        """
        The organization this database belongs to.
        """
        return pulumi.get(self, "organization")

    @property
    @pulumi.getter
    def plan(self) -> str:
        """
        The database plan.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="productionBranchWebConsole")
    def production_branch_web_console(self) -> bool:
        """
        Whether web console is enabled for production branches.
        """
        return pulumi.get(self, "production_branch_web_console")

    @property
    @pulumi.getter(name="productionBranchesCount")
    def production_branches_count(self) -> float:
        """
        The total number of database production branches.
        """
        return pulumi.get(self, "production_branches_count")

    @property
    @pulumi.getter
    def ready(self) -> bool:
        """
        If the database is ready to be used.
        """
        return pulumi.get(self, "ready")

    @property
    @pulumi.getter
    def region(self) -> 'outputs.GetDatabaseRegionResult':
        """
        The region the database lives in.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="requireApprovalForDeploy")
    def require_approval_for_deploy(self) -> bool:
        """
        Whether an approval is required to deploy schema changes to this database.
        """
        return pulumi.get(self, "require_approval_for_deploy")

    @property
    @pulumi.getter(name="restrictBranchRegion")
    def restrict_branch_region(self) -> bool:
        """
        Whether to restrict branch creation to one region.
        """
        return pulumi.get(self, "restrict_branch_region")

    @property
    @pulumi.getter(name="schemaLastUpdatedAt")
    def schema_last_updated_at(self) -> str:
        """
        When the default branch schema was last changed.
        """
        return pulumi.get(self, "schema_last_updated_at")

    @property
    @pulumi.getter
    def sharded(self) -> bool:
        """
        If the database is sharded.
        """
        return pulumi.get(self, "sharded")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        State of the database.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        When the database was last updated.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def url(self) -> str:
        """
        The URL to the database API endpoint.
        """
        return pulumi.get(self, "url")


class AwaitableGetDatabaseResult(GetDatabaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseResult(
            allow_data_branching=self.allow_data_branching,
            at_backup_restore_branches_limit=self.at_backup_restore_branches_limit,
            at_development_branch_limit=self.at_development_branch_limit,
            automatic_migrations=self.automatic_migrations,
            branches_count=self.branches_count,
            branches_url=self.branches_url,
            created_at=self.created_at,
            data_import=self.data_import,
            default_branch=self.default_branch,
            default_branch_read_only_regions_count=self.default_branch_read_only_regions_count,
            default_branch_shard_count=self.default_branch_shard_count,
            default_branch_table_count=self.default_branch_table_count,
            development_branches_count=self.development_branches_count,
            html_url=self.html_url,
            id=self.id,
            insights_raw_queries=self.insights_raw_queries,
            issues_count=self.issues_count,
            migration_framework=self.migration_framework,
            migration_table_name=self.migration_table_name,
            multiple_admins_required_for_deletion=self.multiple_admins_required_for_deletion,
            name=self.name,
            organization=self.organization,
            plan=self.plan,
            production_branch_web_console=self.production_branch_web_console,
            production_branches_count=self.production_branches_count,
            ready=self.ready,
            region=self.region,
            require_approval_for_deploy=self.require_approval_for_deploy,
            restrict_branch_region=self.restrict_branch_region,
            schema_last_updated_at=self.schema_last_updated_at,
            sharded=self.sharded,
            state=self.state,
            updated_at=self.updated_at,
            url=self.url)


def get_database(allow_data_branching: Optional[bool] = None,
                 automatic_migrations: Optional[bool] = None,
                 data_import: Optional[Union['GetDatabaseDataImportArgs', 'GetDatabaseDataImportArgsDict']] = None,
                 default_branch: Optional[str] = None,
                 insights_raw_queries: Optional[bool] = None,
                 issues_count: Optional[float] = None,
                 migration_framework: Optional[str] = None,
                 migration_table_name: Optional[str] = None,
                 multiple_admins_required_for_deletion: Optional[bool] = None,
                 name: Optional[str] = None,
                 organization: Optional[str] = None,
                 plan: Optional[str] = None,
                 production_branch_web_console: Optional[bool] = None,
                 region: Optional[Union['GetDatabaseRegionArgs', 'GetDatabaseRegionArgsDict']] = None,
                 require_approval_for_deploy: Optional[bool] = None,
                 restrict_branch_region: Optional[bool] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseResult:
    """
    A PlanetScale database.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_planetscale as planetscale

    example = planetscale.get_database(organization="example",
        name="again")
    pulumi.export("db", example)
    ```


    :param bool allow_data_branching: Whether seeding branches with data is enabled for all branches.
    :param bool automatic_migrations: Whether to automatically manage Rails migrations during deploy requests.
    :param Union['GetDatabaseDataImportArgs', 'GetDatabaseDataImportArgsDict'] data_import: If the database was created from an import, describes the import process.
    :param str default_branch: The default branch for the database.
    :param bool insights_raw_queries: The URL to see this database's branches in the web UI.
    :param float issues_count: The total number of ongoing issues within a database.
    :param str migration_framework: Framework used for applying migrations.
    :param str migration_table_name: Table name to use for copying schema migration data.
    :param bool multiple_admins_required_for_deletion: If the database requires multiple admins for deletion.
    :param str name: The name of this database.
    :param str organization: The organization this database belongs to.
    :param str plan: The database plan.
    :param bool production_branch_web_console: Whether web console is enabled for production branches.
    :param Union['GetDatabaseRegionArgs', 'GetDatabaseRegionArgsDict'] region: The region the database lives in.
    :param bool require_approval_for_deploy: Whether an approval is required to deploy schema changes to this database.
    :param bool restrict_branch_region: Whether to restrict branch creation to one region.
    """
    __args__ = dict()
    __args__['allowDataBranching'] = allow_data_branching
    __args__['automaticMigrations'] = automatic_migrations
    __args__['dataImport'] = data_import
    __args__['defaultBranch'] = default_branch
    __args__['insightsRawQueries'] = insights_raw_queries
    __args__['issuesCount'] = issues_count
    __args__['migrationFramework'] = migration_framework
    __args__['migrationTableName'] = migration_table_name
    __args__['multipleAdminsRequiredForDeletion'] = multiple_admins_required_for_deletion
    __args__['name'] = name
    __args__['organization'] = organization
    __args__['plan'] = plan
    __args__['productionBranchWebConsole'] = production_branch_web_console
    __args__['region'] = region
    __args__['requireApprovalForDeploy'] = require_approval_for_deploy
    __args__['restrictBranchRegion'] = restrict_branch_region
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('planetscale:index/getDatabase:getDatabase', __args__, opts=opts, typ=GetDatabaseResult).value

    return AwaitableGetDatabaseResult(
        allow_data_branching=pulumi.get(__ret__, 'allow_data_branching'),
        at_backup_restore_branches_limit=pulumi.get(__ret__, 'at_backup_restore_branches_limit'),
        at_development_branch_limit=pulumi.get(__ret__, 'at_development_branch_limit'),
        automatic_migrations=pulumi.get(__ret__, 'automatic_migrations'),
        branches_count=pulumi.get(__ret__, 'branches_count'),
        branches_url=pulumi.get(__ret__, 'branches_url'),
        created_at=pulumi.get(__ret__, 'created_at'),
        data_import=pulumi.get(__ret__, 'data_import'),
        default_branch=pulumi.get(__ret__, 'default_branch'),
        default_branch_read_only_regions_count=pulumi.get(__ret__, 'default_branch_read_only_regions_count'),
        default_branch_shard_count=pulumi.get(__ret__, 'default_branch_shard_count'),
        default_branch_table_count=pulumi.get(__ret__, 'default_branch_table_count'),
        development_branches_count=pulumi.get(__ret__, 'development_branches_count'),
        html_url=pulumi.get(__ret__, 'html_url'),
        id=pulumi.get(__ret__, 'id'),
        insights_raw_queries=pulumi.get(__ret__, 'insights_raw_queries'),
        issues_count=pulumi.get(__ret__, 'issues_count'),
        migration_framework=pulumi.get(__ret__, 'migration_framework'),
        migration_table_name=pulumi.get(__ret__, 'migration_table_name'),
        multiple_admins_required_for_deletion=pulumi.get(__ret__, 'multiple_admins_required_for_deletion'),
        name=pulumi.get(__ret__, 'name'),
        organization=pulumi.get(__ret__, 'organization'),
        plan=pulumi.get(__ret__, 'plan'),
        production_branch_web_console=pulumi.get(__ret__, 'production_branch_web_console'),
        production_branches_count=pulumi.get(__ret__, 'production_branches_count'),
        ready=pulumi.get(__ret__, 'ready'),
        region=pulumi.get(__ret__, 'region'),
        require_approval_for_deploy=pulumi.get(__ret__, 'require_approval_for_deploy'),
        restrict_branch_region=pulumi.get(__ret__, 'restrict_branch_region'),
        schema_last_updated_at=pulumi.get(__ret__, 'schema_last_updated_at'),
        sharded=pulumi.get(__ret__, 'sharded'),
        state=pulumi.get(__ret__, 'state'),
        updated_at=pulumi.get(__ret__, 'updated_at'),
        url=pulumi.get(__ret__, 'url'))
def get_database_output(allow_data_branching: Optional[pulumi.Input[Optional[bool]]] = None,
                        automatic_migrations: Optional[pulumi.Input[Optional[bool]]] = None,
                        data_import: Optional[pulumi.Input[Optional[Union['GetDatabaseDataImportArgs', 'GetDatabaseDataImportArgsDict']]]] = None,
                        default_branch: Optional[pulumi.Input[Optional[str]]] = None,
                        insights_raw_queries: Optional[pulumi.Input[Optional[bool]]] = None,
                        issues_count: Optional[pulumi.Input[Optional[float]]] = None,
                        migration_framework: Optional[pulumi.Input[Optional[str]]] = None,
                        migration_table_name: Optional[pulumi.Input[Optional[str]]] = None,
                        multiple_admins_required_for_deletion: Optional[pulumi.Input[Optional[bool]]] = None,
                        name: Optional[pulumi.Input[str]] = None,
                        organization: Optional[pulumi.Input[str]] = None,
                        plan: Optional[pulumi.Input[Optional[str]]] = None,
                        production_branch_web_console: Optional[pulumi.Input[Optional[bool]]] = None,
                        region: Optional[pulumi.Input[Optional[Union['GetDatabaseRegionArgs', 'GetDatabaseRegionArgsDict']]]] = None,
                        require_approval_for_deploy: Optional[pulumi.Input[Optional[bool]]] = None,
                        restrict_branch_region: Optional[pulumi.Input[Optional[bool]]] = None,
                        opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDatabaseResult]:
    """
    A PlanetScale database.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_planetscale as planetscale

    example = planetscale.get_database(organization="example",
        name="again")
    pulumi.export("db", example)
    ```


    :param bool allow_data_branching: Whether seeding branches with data is enabled for all branches.
    :param bool automatic_migrations: Whether to automatically manage Rails migrations during deploy requests.
    :param Union['GetDatabaseDataImportArgs', 'GetDatabaseDataImportArgsDict'] data_import: If the database was created from an import, describes the import process.
    :param str default_branch: The default branch for the database.
    :param bool insights_raw_queries: The URL to see this database's branches in the web UI.
    :param float issues_count: The total number of ongoing issues within a database.
    :param str migration_framework: Framework used for applying migrations.
    :param str migration_table_name: Table name to use for copying schema migration data.
    :param bool multiple_admins_required_for_deletion: If the database requires multiple admins for deletion.
    :param str name: The name of this database.
    :param str organization: The organization this database belongs to.
    :param str plan: The database plan.
    :param bool production_branch_web_console: Whether web console is enabled for production branches.
    :param Union['GetDatabaseRegionArgs', 'GetDatabaseRegionArgsDict'] region: The region the database lives in.
    :param bool require_approval_for_deploy: Whether an approval is required to deploy schema changes to this database.
    :param bool restrict_branch_region: Whether to restrict branch creation to one region.
    """
    __args__ = dict()
    __args__['allowDataBranching'] = allow_data_branching
    __args__['automaticMigrations'] = automatic_migrations
    __args__['dataImport'] = data_import
    __args__['defaultBranch'] = default_branch
    __args__['insightsRawQueries'] = insights_raw_queries
    __args__['issuesCount'] = issues_count
    __args__['migrationFramework'] = migration_framework
    __args__['migrationTableName'] = migration_table_name
    __args__['multipleAdminsRequiredForDeletion'] = multiple_admins_required_for_deletion
    __args__['name'] = name
    __args__['organization'] = organization
    __args__['plan'] = plan
    __args__['productionBranchWebConsole'] = production_branch_web_console
    __args__['region'] = region
    __args__['requireApprovalForDeploy'] = require_approval_for_deploy
    __args__['restrictBranchRegion'] = restrict_branch_region
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('planetscale:index/getDatabase:getDatabase', __args__, opts=opts, typ=GetDatabaseResult)
    return __ret__.apply(lambda __response__: GetDatabaseResult(
        allow_data_branching=pulumi.get(__response__, 'allow_data_branching'),
        at_backup_restore_branches_limit=pulumi.get(__response__, 'at_backup_restore_branches_limit'),
        at_development_branch_limit=pulumi.get(__response__, 'at_development_branch_limit'),
        automatic_migrations=pulumi.get(__response__, 'automatic_migrations'),
        branches_count=pulumi.get(__response__, 'branches_count'),
        branches_url=pulumi.get(__response__, 'branches_url'),
        created_at=pulumi.get(__response__, 'created_at'),
        data_import=pulumi.get(__response__, 'data_import'),
        default_branch=pulumi.get(__response__, 'default_branch'),
        default_branch_read_only_regions_count=pulumi.get(__response__, 'default_branch_read_only_regions_count'),
        default_branch_shard_count=pulumi.get(__response__, 'default_branch_shard_count'),
        default_branch_table_count=pulumi.get(__response__, 'default_branch_table_count'),
        development_branches_count=pulumi.get(__response__, 'development_branches_count'),
        html_url=pulumi.get(__response__, 'html_url'),
        id=pulumi.get(__response__, 'id'),
        insights_raw_queries=pulumi.get(__response__, 'insights_raw_queries'),
        issues_count=pulumi.get(__response__, 'issues_count'),
        migration_framework=pulumi.get(__response__, 'migration_framework'),
        migration_table_name=pulumi.get(__response__, 'migration_table_name'),
        multiple_admins_required_for_deletion=pulumi.get(__response__, 'multiple_admins_required_for_deletion'),
        name=pulumi.get(__response__, 'name'),
        organization=pulumi.get(__response__, 'organization'),
        plan=pulumi.get(__response__, 'plan'),
        production_branch_web_console=pulumi.get(__response__, 'production_branch_web_console'),
        production_branches_count=pulumi.get(__response__, 'production_branches_count'),
        ready=pulumi.get(__response__, 'ready'),
        region=pulumi.get(__response__, 'region'),
        require_approval_for_deploy=pulumi.get(__response__, 'require_approval_for_deploy'),
        restrict_branch_region=pulumi.get(__response__, 'restrict_branch_region'),
        schema_last_updated_at=pulumi.get(__response__, 'schema_last_updated_at'),
        sharded=pulumi.get(__response__, 'sharded'),
        state=pulumi.get(__response__, 'state'),
        updated_at=pulumi.get(__response__, 'updated_at'),
        url=pulumi.get(__response__, 'url')))
