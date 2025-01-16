// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as enums from "./types/enums";
import * as utilities from "./utilities";

/**
 * A PlanetScale organization.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as planetscale from "@imxeno/pulumi-planetscale";
 *
 * const example = planetscale.getOrganization({
 *     name: "example",
 * });
 * export const org = example;
 * ```
 */
export function getOrganization(
  args: GetOrganizationArgs,
  opts?: pulumi.InvokeOptions
): Promise<GetOrganizationResult> {
  opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
  return pulumi.runtime.invoke(
    "planetscale:index/getOrganization:getOrganization",
    {
      name: args.name,
    },
    opts
  );
}

/**
 * A collection of arguments for invoking getOrganization.
 */
export interface GetOrganizationArgs {
  /**
   * The name of the organization.
   */
  name: string;
}

/**
 * A collection of values returned by getOrganization.
 */
export interface GetOrganizationResult {
  /**
   * The billing email of the organization.
   */
  readonly billingEmail: string;
  /**
   * When the organization was created.
   */
  readonly createdAt: string;
  /**
   * The number of databases in the organization.
   */
  readonly databaseCount: number;
  /**
   * Features that are enabled on the organization.
   */
  readonly features: outputs.GetOrganizationFeatures;
  /**
   * .
   */
  readonly flags: outputs.GetOrganizationFlags;
  /**
   * Whether or not the organization has past due billing invoices.
   */
  readonly hasPastDueInvoices: boolean;
  /**
   * The ID for the organization.
   */
  readonly id: string;
  /**
   * Whether or not the IdP provider is be responsible for managing roles in PlanetScale.
   */
  readonly idpManagedRoles: boolean;
  /**
   * The name of the organization.
   */
  readonly name: string;
  /**
   * The billing plan of the organization.
   */
  readonly plan: string;
  /**
   * Whether or not the organization has single tenancy enabled.
   */
  readonly singleTenancy: boolean;
  /**
   * The number of sleeping databases in the organization.
   */
  readonly sleepingDatabaseCount: number;
  /**
   * Whether or not SSO is enabled on the organization.
   */
  readonly sso: boolean;
  /**
   * Whether or not the organization uses a WorkOS directory.
   */
  readonly ssoDirectory: boolean;
  /**
   * The URL of the organization's SSO portal.
   */
  readonly ssoPortalUrl: string;
  /**
   * When the organization was last updated.
   */
  readonly updatedAt: string;
  /**
   * Whether or not the organization's billing information is valid.
   */
  readonly validBillingInfo: boolean;
}
/**
 * A PlanetScale organization.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as planetscale from "@imxeno/pulumi-planetscale";
 *
 * const example = planetscale.getOrganization({
 *     name: "example",
 * });
 * export const org = example;
 * ```
 */
export function getOrganizationOutput(
  args: GetOrganizationOutputArgs,
  opts?: pulumi.InvokeOutputOptions
): pulumi.Output<GetOrganizationResult> {
  opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
  return pulumi.runtime.invokeOutput(
    "planetscale:index/getOrganization:getOrganization",
    {
      name: args.name,
    },
    opts
  );
}

/**
 * A collection of arguments for invoking getOrganization.
 */
export interface GetOrganizationOutputArgs {
  /**
   * The name of the organization.
   */
  name: pulumi.Input<string>;
}
