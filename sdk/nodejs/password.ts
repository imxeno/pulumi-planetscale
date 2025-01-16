// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as enums from "./types/enums";
import * as utilities from "./utilities";

/**
 * A PlanetScale database password.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as planetscale from "@pulumi/planetscale";
 *
 * const example = new planetscale.Password("example", {
 *     organization: "example",
 *     database: "example_db",
 *     branch: "main",
 *     name: "a-password-for-antoine",
 * });
 * export const password = example;
 * ```
 */
export class Password extends pulumi.CustomResource {
    /**
     * Get an existing Password resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PasswordState, opts?: pulumi.CustomResourceOptions): Password {
        return new Password(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'planetscale:index/password:Password';

    /**
     * Returns true if the given object is an instance of Password.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Password {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Password.__pulumiType;
    }

    /**
     * The host URL for the password.
     */
    public /*out*/ readonly accessHostUrl!: pulumi.Output<string>;
    /**
     * The actor that created this branch.
     */
    public /*out*/ readonly actor!: pulumi.Output<outputs.PasswordActor>;
    /**
     * The branch this password belongs to.
     */
    public readonly branch!: pulumi.Output<string>;
    /**
     * When the password was created.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The database this branch password belongs to.
     */
    public readonly database!: pulumi.Output<string>;
    /**
     * The branch this password is allowed to access.
     */
    public /*out*/ readonly databaseBranch!: pulumi.Output<outputs.PasswordDatabaseBranch>;
    /**
     * When the password was deleted.
     */
    public /*out*/ readonly deletedAt!: pulumi.Output<string>;
    /**
     * When the password will expire.
     */
    public /*out*/ readonly expiresAt!: pulumi.Output<string>;
    /**
     * The display name for the password.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The organization this database branch password belongs to.
     */
    public readonly organization!: pulumi.Output<string>;
    /**
     * The plaintext password, only available if the password was created by this provider.
     */
    public /*out*/ readonly plaintext!: pulumi.Output<string>;
    /**
     * The region in which this password can be used.
     */
    public /*out*/ readonly region!: pulumi.Output<outputs.PasswordRegion>;
    /**
     * Whether or not the password can be renewed.
     */
    public /*out*/ readonly renewable!: pulumi.Output<boolean>;
    /**
     * The role for the password.
     */
    public readonly role!: pulumi.Output<string>;
    /**
     * Time to live (in seconds) for the password. The password will be invalid and unrenewable when TTL has passed.
     */
    public readonly ttlSeconds!: pulumi.Output<number>;
    /**
     * The username for the password.
     */
    public /*out*/ readonly username!: pulumi.Output<string>;

    /**
     * Create a Password resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PasswordArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PasswordArgs | PasswordState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PasswordState | undefined;
            resourceInputs["accessHostUrl"] = state ? state.accessHostUrl : undefined;
            resourceInputs["actor"] = state ? state.actor : undefined;
            resourceInputs["branch"] = state ? state.branch : undefined;
            resourceInputs["createdAt"] = state ? state.createdAt : undefined;
            resourceInputs["database"] = state ? state.database : undefined;
            resourceInputs["databaseBranch"] = state ? state.databaseBranch : undefined;
            resourceInputs["deletedAt"] = state ? state.deletedAt : undefined;
            resourceInputs["expiresAt"] = state ? state.expiresAt : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["organization"] = state ? state.organization : undefined;
            resourceInputs["plaintext"] = state ? state.plaintext : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["renewable"] = state ? state.renewable : undefined;
            resourceInputs["role"] = state ? state.role : undefined;
            resourceInputs["ttlSeconds"] = state ? state.ttlSeconds : undefined;
            resourceInputs["username"] = state ? state.username : undefined;
        } else {
            const args = argsOrState as PasswordArgs | undefined;
            if ((!args || args.branch === undefined) && !opts.urn) {
                throw new Error("Missing required property 'branch'");
            }
            if ((!args || args.database === undefined) && !opts.urn) {
                throw new Error("Missing required property 'database'");
            }
            if ((!args || args.organization === undefined) && !opts.urn) {
                throw new Error("Missing required property 'organization'");
            }
            resourceInputs["branch"] = args ? args.branch : undefined;
            resourceInputs["database"] = args ? args.database : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["organization"] = args ? args.organization : undefined;
            resourceInputs["role"] = args ? args.role : undefined;
            resourceInputs["ttlSeconds"] = args ? args.ttlSeconds : undefined;
            resourceInputs["accessHostUrl"] = undefined /*out*/;
            resourceInputs["actor"] = undefined /*out*/;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["databaseBranch"] = undefined /*out*/;
            resourceInputs["deletedAt"] = undefined /*out*/;
            resourceInputs["expiresAt"] = undefined /*out*/;
            resourceInputs["plaintext"] = undefined /*out*/;
            resourceInputs["region"] = undefined /*out*/;
            resourceInputs["renewable"] = undefined /*out*/;
            resourceInputs["username"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["plaintext"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(Password.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Password resources.
 */
export interface PasswordState {
    /**
     * The host URL for the password.
     */
    accessHostUrl?: pulumi.Input<string>;
    /**
     * The actor that created this branch.
     */
    actor?: pulumi.Input<inputs.PasswordActor>;
    /**
     * The branch this password belongs to.
     */
    branch?: pulumi.Input<string>;
    /**
     * When the password was created.
     */
    createdAt?: pulumi.Input<string>;
    /**
     * The database this branch password belongs to.
     */
    database?: pulumi.Input<string>;
    /**
     * The branch this password is allowed to access.
     */
    databaseBranch?: pulumi.Input<inputs.PasswordDatabaseBranch>;
    /**
     * When the password was deleted.
     */
    deletedAt?: pulumi.Input<string>;
    /**
     * When the password will expire.
     */
    expiresAt?: pulumi.Input<string>;
    /**
     * The display name for the password.
     */
    name?: pulumi.Input<string>;
    /**
     * The organization this database branch password belongs to.
     */
    organization?: pulumi.Input<string>;
    /**
     * The plaintext password, only available if the password was created by this provider.
     */
    plaintext?: pulumi.Input<string>;
    /**
     * The region in which this password can be used.
     */
    region?: pulumi.Input<inputs.PasswordRegion>;
    /**
     * Whether or not the password can be renewed.
     */
    renewable?: pulumi.Input<boolean>;
    /**
     * The role for the password.
     */
    role?: pulumi.Input<string>;
    /**
     * Time to live (in seconds) for the password. The password will be invalid and unrenewable when TTL has passed.
     */
    ttlSeconds?: pulumi.Input<number>;
    /**
     * The username for the password.
     */
    username?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Password resource.
 */
export interface PasswordArgs {
    /**
     * The branch this password belongs to.
     */
    branch: pulumi.Input<string>;
    /**
     * The database this branch password belongs to.
     */
    database: pulumi.Input<string>;
    /**
     * The display name for the password.
     */
    name?: pulumi.Input<string>;
    /**
     * The organization this database branch password belongs to.
     */
    organization: pulumi.Input<string>;
    /**
     * The role for the password.
     */
    role?: pulumi.Input<string>;
    /**
     * Time to live (in seconds) for the password. The password will be invalid and unrenewable when TTL has passed.
     */
    ttlSeconds?: pulumi.Input<number>;
}
