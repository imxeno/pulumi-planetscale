// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as enums from "./types/enums";
import * as utilities from "./utilities";

/**
 * A list of PlanetScale databases.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as planetscale from "@imxeno/pulumi-planetscale";
 *
 * const example = planetscale.getDatabases({
 *     organization: "example",
 * });
 * export const dbs = example;
 * ```
 */
export function getDatabases(
  args: GetDatabasesArgs,
  opts?: pulumi.InvokeOptions
): Promise<GetDatabasesResult> {
  opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
  return pulumi.runtime.invoke(
    "planetscale:index/getDatabases:getDatabases",
    {
      organization: args.organization,
    },
    opts
  );
}

/**
 * A collection of arguments for invoking getDatabases.
 */
export interface GetDatabasesArgs {
  organization: string;
}

/**
 * A collection of values returned by getDatabases.
 */
export interface GetDatabasesResult {
  readonly databases: outputs.GetDatabasesDatabase[];
  /**
   * The provider-assigned unique ID for this managed resource.
   */
  readonly id: string;
  readonly organization: string;
}
/**
 * A list of PlanetScale databases.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as planetscale from "@imxeno/pulumi-planetscale";
 *
 * const example = planetscale.getDatabases({
 *     organization: "example",
 * });
 * export const dbs = example;
 * ```
 */
export function getDatabasesOutput(
  args: GetDatabasesOutputArgs,
  opts?: pulumi.InvokeOutputOptions
): pulumi.Output<GetDatabasesResult> {
  opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
  return pulumi.runtime.invokeOutput(
    "planetscale:index/getDatabases:getDatabases",
    {
      organization: args.organization,
    },
    opts
  );
}

/**
 * A collection of arguments for invoking getDatabases.
 */
export interface GetDatabasesOutputArgs {
  organization: pulumi.Input<string>;
}
