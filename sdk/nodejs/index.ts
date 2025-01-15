// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { BackupArgs, BackupState } from "./backup";
export type Backup = import("./backup").Backup;
export const Backup: typeof import("./backup").Backup = null as any;
utilities.lazyLoad(exports, ["Backup"], () => require("./backup"));

export { BranchArgs, BranchState } from "./branch";
export type Branch = import("./branch").Branch;
export const Branch: typeof import("./branch").Branch = null as any;
utilities.lazyLoad(exports, ["Branch"], () => require("./branch"));

export { DatabaseArgs, DatabaseState } from "./database";
export type Database = import("./database").Database;
export const Database: typeof import("./database").Database = null as any;
utilities.lazyLoad(exports, ["Database"], () => require("./database"));

export { GetBackupArgs, GetBackupResult, GetBackupOutputArgs } from "./getBackup";
export const getBackup: typeof import("./getBackup").getBackup = null as any;
export const getBackupOutput: typeof import("./getBackup").getBackupOutput = null as any;
utilities.lazyLoad(exports, ["getBackup","getBackupOutput"], () => require("./getBackup"));

export { GetBackupsArgs, GetBackupsResult, GetBackupsOutputArgs } from "./getBackups";
export const getBackups: typeof import("./getBackups").getBackups = null as any;
export const getBackupsOutput: typeof import("./getBackups").getBackupsOutput = null as any;
utilities.lazyLoad(exports, ["getBackups","getBackupsOutput"], () => require("./getBackups"));

export { GetBranchArgs, GetBranchResult, GetBranchOutputArgs } from "./getBranch";
export const getBranch: typeof import("./getBranch").getBranch = null as any;
export const getBranchOutput: typeof import("./getBranch").getBranchOutput = null as any;
utilities.lazyLoad(exports, ["getBranch","getBranchOutput"], () => require("./getBranch"));

export { GetBranchSchemaArgs, GetBranchSchemaResult, GetBranchSchemaOutputArgs } from "./getBranchSchema";
export const getBranchSchema: typeof import("./getBranchSchema").getBranchSchema = null as any;
export const getBranchSchemaOutput: typeof import("./getBranchSchema").getBranchSchemaOutput = null as any;
utilities.lazyLoad(exports, ["getBranchSchema","getBranchSchemaOutput"], () => require("./getBranchSchema"));

export { GetBranchSchemaLintArgs, GetBranchSchemaLintResult, GetBranchSchemaLintOutputArgs } from "./getBranchSchemaLint";
export const getBranchSchemaLint: typeof import("./getBranchSchemaLint").getBranchSchemaLint = null as any;
export const getBranchSchemaLintOutput: typeof import("./getBranchSchemaLint").getBranchSchemaLintOutput = null as any;
utilities.lazyLoad(exports, ["getBranchSchemaLint","getBranchSchemaLintOutput"], () => require("./getBranchSchemaLint"));

export { GetBranchesArgs, GetBranchesResult, GetBranchesOutputArgs } from "./getBranches";
export const getBranches: typeof import("./getBranches").getBranches = null as any;
export const getBranchesOutput: typeof import("./getBranches").getBranchesOutput = null as any;
utilities.lazyLoad(exports, ["getBranches","getBranchesOutput"], () => require("./getBranches"));

export { GetDatabaseArgs, GetDatabaseResult, GetDatabaseOutputArgs } from "./getDatabase";
export const getDatabase: typeof import("./getDatabase").getDatabase = null as any;
export const getDatabaseOutput: typeof import("./getDatabase").getDatabaseOutput = null as any;
utilities.lazyLoad(exports, ["getDatabase","getDatabaseOutput"], () => require("./getDatabase"));

export { GetDatabaseReadOnlyRegionsArgs, GetDatabaseReadOnlyRegionsResult, GetDatabaseReadOnlyRegionsOutputArgs } from "./getDatabaseReadOnlyRegions";
export const getDatabaseReadOnlyRegions: typeof import("./getDatabaseReadOnlyRegions").getDatabaseReadOnlyRegions = null as any;
export const getDatabaseReadOnlyRegionsOutput: typeof import("./getDatabaseReadOnlyRegions").getDatabaseReadOnlyRegionsOutput = null as any;
utilities.lazyLoad(exports, ["getDatabaseReadOnlyRegions","getDatabaseReadOnlyRegionsOutput"], () => require("./getDatabaseReadOnlyRegions"));

export { GetDatabaseRegionsArgs, GetDatabaseRegionsResult, GetDatabaseRegionsOutputArgs } from "./getDatabaseRegions";
export const getDatabaseRegions: typeof import("./getDatabaseRegions").getDatabaseRegions = null as any;
export const getDatabaseRegionsOutput: typeof import("./getDatabaseRegions").getDatabaseRegionsOutput = null as any;
utilities.lazyLoad(exports, ["getDatabaseRegions","getDatabaseRegionsOutput"], () => require("./getDatabaseRegions"));

export { GetDatabasesArgs, GetDatabasesResult, GetDatabasesOutputArgs } from "./getDatabases";
export const getDatabases: typeof import("./getDatabases").getDatabases = null as any;
export const getDatabasesOutput: typeof import("./getDatabases").getDatabasesOutput = null as any;
utilities.lazyLoad(exports, ["getDatabases","getDatabasesOutput"], () => require("./getDatabases"));

export { GetOauthApplicationsArgs, GetOauthApplicationsResult, GetOauthApplicationsOutputArgs } from "./getOauthApplications";
export const getOauthApplications: typeof import("./getOauthApplications").getOauthApplications = null as any;
export const getOauthApplicationsOutput: typeof import("./getOauthApplications").getOauthApplicationsOutput = null as any;
utilities.lazyLoad(exports, ["getOauthApplications","getOauthApplicationsOutput"], () => require("./getOauthApplications"));

export { GetOrganizationArgs, GetOrganizationResult, GetOrganizationOutputArgs } from "./getOrganization";
export const getOrganization: typeof import("./getOrganization").getOrganization = null as any;
export const getOrganizationOutput: typeof import("./getOrganization").getOrganizationOutput = null as any;
utilities.lazyLoad(exports, ["getOrganization","getOrganizationOutput"], () => require("./getOrganization"));

export { GetOrganizationRegionsArgs, GetOrganizationRegionsResult, GetOrganizationRegionsOutputArgs } from "./getOrganizationRegions";
export const getOrganizationRegions: typeof import("./getOrganizationRegions").getOrganizationRegions = null as any;
export const getOrganizationRegionsOutput: typeof import("./getOrganizationRegions").getOrganizationRegionsOutput = null as any;
utilities.lazyLoad(exports, ["getOrganizationRegions","getOrganizationRegionsOutput"], () => require("./getOrganizationRegions"));

export { GetOrganizationsResult } from "./getOrganizations";
export const getOrganizations: typeof import("./getOrganizations").getOrganizations = null as any;
export const getOrganizationsOutput: typeof import("./getOrganizations").getOrganizationsOutput = null as any;
utilities.lazyLoad(exports, ["getOrganizations","getOrganizationsOutput"], () => require("./getOrganizations"));

export { GetPasswordArgs, GetPasswordResult, GetPasswordOutputArgs } from "./getPassword";
export const getPassword: typeof import("./getPassword").getPassword = null as any;
export const getPasswordOutput: typeof import("./getPassword").getPasswordOutput = null as any;
utilities.lazyLoad(exports, ["getPassword","getPasswordOutput"], () => require("./getPassword"));

export { GetPasswordsArgs, GetPasswordsResult, GetPasswordsOutputArgs } from "./getPasswords";
export const getPasswords: typeof import("./getPasswords").getPasswords = null as any;
export const getPasswordsOutput: typeof import("./getPasswords").getPasswordsOutput = null as any;
utilities.lazyLoad(exports, ["getPasswords","getPasswordsOutput"], () => require("./getPasswords"));

export { GetUserResult } from "./getUser";
export const getUser: typeof import("./getUser").getUser = null as any;
export const getUserOutput: typeof import("./getUser").getUserOutput = null as any;
utilities.lazyLoad(exports, ["getUser","getUserOutput"], () => require("./getUser"));

export { PasswordArgs, PasswordState } from "./password";
export type Password = import("./password").Password;
export const Password: typeof import("./password").Password = null as any;
utilities.lazyLoad(exports, ["Password"], () => require("./password"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));


// Export sub-modules:
import * as config from "./config";
import * as region from "./region";
import * as types from "./types";

export {
    config,
    region,
    types,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "planetscale:index/backup:Backup":
                return new Backup(name, <any>undefined, { urn })
            case "planetscale:index/branch:Branch":
                return new Branch(name, <any>undefined, { urn })
            case "planetscale:index/database:Database":
                return new Database(name, <any>undefined, { urn })
            case "planetscale:index/password:Password":
                return new Password(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("planetscale", "index/backup", _module)
pulumi.runtime.registerResourceModule("planetscale", "index/branch", _module)
pulumi.runtime.registerResourceModule("planetscale", "index/database", _module)
pulumi.runtime.registerResourceModule("planetscale", "index/password", _module)
pulumi.runtime.registerResourcePackage("planetscale", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:planetscale") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
