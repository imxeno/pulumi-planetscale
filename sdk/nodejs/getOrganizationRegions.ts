// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as enums from "./types/enums";
import * as utilities from "./utilities";

/**
 * A list of PlanetScale regions for the organization.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as planetscale from "@imxeno/pulumi-planetscale";
 *
 * const example = planetscale.getOrganizationRegions({
 *     organization: "example",
 * });
 * export const orgRegions = example;
 * ```
 */
export function getOrganizationRegions(
  args: GetOrganizationRegionsArgs,
  opts?: pulumi.InvokeOptions
): Promise<GetOrganizationRegionsResult> {
  opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
  return pulumi.runtime.invoke(
    "planetscale:index/getOrganizationRegions:getOrganizationRegions",
    {
      organization: args.organization,
    },
    opts
  );
}

/**
 * A collection of arguments for invoking getOrganizationRegions.
 */
export interface GetOrganizationRegionsArgs {
  organization: string;
}

/**
 * A collection of values returned by getOrganizationRegions.
 */
export interface GetOrganizationRegionsResult {
  /**
   * The provider-assigned unique ID for this managed resource.
   */
  readonly id: string;
  readonly organization: string;
  readonly regions: outputs.GetOrganizationRegionsRegion[];
}
/**
 * A list of PlanetScale regions for the organization.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as planetscale from "@imxeno/pulumi-planetscale";
 *
 * const example = planetscale.getOrganizationRegions({
 *     organization: "example",
 * });
 * export const orgRegions = example;
 * ```
 */
export function getOrganizationRegionsOutput(
  args: GetOrganizationRegionsOutputArgs,
  opts?: pulumi.InvokeOutputOptions
): pulumi.Output<GetOrganizationRegionsResult> {
  opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
  return pulumi.runtime.invokeOutput(
    "planetscale:index/getOrganizationRegions:getOrganizationRegions",
    {
      organization: args.organization,
    },
    opts
  );
}

/**
 * A collection of arguments for invoking getOrganizationRegions.
 */
export interface GetOrganizationRegionsOutputArgs {
  organization: pulumi.Input<string>;
}
