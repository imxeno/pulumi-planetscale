// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as enums from "./types/enums";
import * as utilities from "./utilities";

/**
 * A PlanetScale user.
 *
 * Known limitations:
 * - Does not work when the provider is configured with a service token.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as planetscale from "@imxeno/pulumi-planetscale";
 *
 * // doesn't work right now for some reason
 * const example = planetscale.getUser({});
 * export const currentUser = example;
 * ```
 */
export function getUser(opts?: pulumi.InvokeOptions): Promise<GetUserResult> {
  opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
  return pulumi.runtime.invoke("planetscale:index/getUser:getUser", {}, opts);
}

/**
 * A collection of values returned by getUser.
 */
export interface GetUserResult {
  /**
   * The URL source of the user's avatar.
   */
  readonly avatarUrl: string;
  /**
   * When the user was created.
   */
  readonly createdAt: string;
  /**
   * The default organization for the user.
   */
  readonly defaultOrganization: outputs.GetUserDefaultOrganization;
  /**
   * Whether or not the user is managed by a WorkOS directory.
   */
  readonly directoryManaged: boolean;
  /**
   * The display name of the user.
   */
  readonly displayName: string;
  /**
   * The email of the user.
   */
  readonly email: string;
  /**
   * Whether or not the user is verified by email.
   */
  readonly emailVerified: boolean;
  /**
   * The ID of the user.
   */
  readonly id: string;
  /**
   * Whether or not the user is managed by an authentication provider.
   */
  readonly managed: boolean;
  /**
   * The name of the user.
   */
  readonly name: string;
  /**
   * Whether or not the user is managed by WorkOS.
   */
  readonly sso: boolean;
  /**
   * Whether or not the user has configured two factor authentication.
   */
  readonly twoFactorAuthConfigured: boolean;
  /**
   * When the user was last updated.
   */
  readonly updatedAt: string;
}
/**
 * A PlanetScale user.
 *
 * Known limitations:
 * - Does not work when the provider is configured with a service token.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as planetscale from "@imxeno/pulumi-planetscale";
 *
 * // doesn't work right now for some reason
 * const example = planetscale.getUser({});
 * export const currentUser = example;
 * ```
 */
export function getUserOutput(
  opts?: pulumi.InvokeOutputOptions
): pulumi.Output<GetUserResult> {
  opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
  return pulumi.runtime.invokeOutput(
    "planetscale:index/getUser:getUser",
    {},
    opts
  );
}
