// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Planetscale
{
    /// <summary>
    /// A PlanetScale backup.
    /// 
    /// Known limitations:
    /// - It is not currently possible to manage backup schedules, only retention periods.
    /// </summary>
    [PlanetscaleResourceType("planetscale:index/backup:Backup")]
    public partial class Backup : global::Pulumi.CustomResource
    {
        /// <summary>
        /// .
        /// </summary>
        [Output("actor")]
        public Output<Outputs.BackupActor> Actor { get; private set; } = null!;

        /// <summary>
        /// The policy used by the backup.
        /// </summary>
        [Output("backupPolicy")]
        public Output<Outputs.BackupBackupPolicy> BackupPolicy { get; private set; } = null!;

        /// <summary>
        /// The branch being backed up.
        /// </summary>
        [Output("branch")]
        public Output<string> Branch { get; private set; } = null!;

        /// <summary>
        /// When the backup was created.
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The database to which the branch being backed up belongs to.
        /// </summary>
        [Output("database")]
        public Output<string> Database { get; private set; } = null!;

        /// <summary>
        /// The estimated storage cost of the backup.
        /// </summary>
        [Output("estimatedStorageCost")]
        public Output<double> EstimatedStorageCost { get; private set; } = null!;

        /// <summary>
        /// The name of the backup.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The organization in which the database branch being backed up belongs to.
        /// </summary>
        [Output("organization")]
        public Output<string> Organization { get; private set; } = null!;

        /// <summary>
        /// Whether or not the backup policy is required.
        /// </summary>
        [Output("required")]
        public Output<bool> Required { get; private set; } = null!;

        /// <summary>
        /// Branches that have been restored with this backup.
        /// </summary>
        [Output("restoredBranches")]
        public Output<ImmutableArray<string>> RestoredBranches { get; private set; } = null!;

        /// <summary>
        /// The unit for the retention period of the backup policy.
        /// </summary>
        [Output("retentionUnit")]
        public Output<string> RetentionUnit { get; private set; } = null!;

        /// <summary>
        /// A number value for the retention period of the backup policy.
        /// </summary>
        [Output("retentionValue")]
        public Output<double> RetentionValue { get; private set; } = null!;

        /// <summary>
        /// The size of the backup.
        /// </summary>
        [Output("size")]
        public Output<double> Size { get; private set; } = null!;

        /// <summary>
        /// The current state of the backup.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// When the backup was last updated.
        /// </summary>
        [Output("updatedAt")]
        public Output<string> UpdatedAt { get; private set; } = null!;


        /// <summary>
        /// Create a Backup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Backup(string name, BackupArgs args, CustomResourceOptions? options = null)
            : base("planetscale:index/backup:Backup", name, args ?? new BackupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Backup(string name, Input<string> id, BackupState? state = null, CustomResourceOptions? options = null)
            : base("planetscale:index/backup:Backup", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Backup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Backup Get(string name, Input<string> id, BackupState? state = null, CustomResourceOptions? options = null)
        {
            return new Backup(name, id, state, options);
        }
    }

    public sealed class BackupArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The branch being backed up.
        /// </summary>
        [Input("branch", required: true)]
        public Input<string> Branch { get; set; } = null!;

        /// <summary>
        /// The database to which the branch being backed up belongs to.
        /// </summary>
        [Input("database", required: true)]
        public Input<string> Database { get; set; } = null!;

        /// <summary>
        /// The name of the backup.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The organization in which the database branch being backed up belongs to.
        /// </summary>
        [Input("organization", required: true)]
        public Input<string> Organization { get; set; } = null!;

        /// <summary>
        /// The unit for the retention period of the backup policy.
        /// </summary>
        [Input("retentionUnit", required: true)]
        public Input<string> RetentionUnit { get; set; } = null!;

        /// <summary>
        /// A number value for the retention period of the backup policy.
        /// </summary>
        [Input("retentionValue", required: true)]
        public Input<double> RetentionValue { get; set; } = null!;

        public BackupArgs()
        {
        }
        public static new BackupArgs Empty => new BackupArgs();
    }

    public sealed class BackupState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// .
        /// </summary>
        [Input("actor")]
        public Input<Inputs.BackupActorGetArgs>? Actor { get; set; }

        /// <summary>
        /// The policy used by the backup.
        /// </summary>
        [Input("backupPolicy")]
        public Input<Inputs.BackupBackupPolicyGetArgs>? BackupPolicy { get; set; }

        /// <summary>
        /// The branch being backed up.
        /// </summary>
        [Input("branch")]
        public Input<string>? Branch { get; set; }

        /// <summary>
        /// When the backup was created.
        /// </summary>
        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        /// <summary>
        /// The database to which the branch being backed up belongs to.
        /// </summary>
        [Input("database")]
        public Input<string>? Database { get; set; }

        /// <summary>
        /// The estimated storage cost of the backup.
        /// </summary>
        [Input("estimatedStorageCost")]
        public Input<double>? EstimatedStorageCost { get; set; }

        /// <summary>
        /// The name of the backup.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The organization in which the database branch being backed up belongs to.
        /// </summary>
        [Input("organization")]
        public Input<string>? Organization { get; set; }

        /// <summary>
        /// Whether or not the backup policy is required.
        /// </summary>
        [Input("required")]
        public Input<bool>? Required { get; set; }

        [Input("restoredBranches")]
        private InputList<string>? _restoredBranches;

        /// <summary>
        /// Branches that have been restored with this backup.
        /// </summary>
        public InputList<string> RestoredBranches
        {
            get => _restoredBranches ?? (_restoredBranches = new InputList<string>());
            set => _restoredBranches = value;
        }

        /// <summary>
        /// The unit for the retention period of the backup policy.
        /// </summary>
        [Input("retentionUnit")]
        public Input<string>? RetentionUnit { get; set; }

        /// <summary>
        /// A number value for the retention period of the backup policy.
        /// </summary>
        [Input("retentionValue")]
        public Input<double>? RetentionValue { get; set; }

        /// <summary>
        /// The size of the backup.
        /// </summary>
        [Input("size")]
        public Input<double>? Size { get; set; }

        /// <summary>
        /// The current state of the backup.
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        /// <summary>
        /// When the backup was last updated.
        /// </summary>
        [Input("updatedAt")]
        public Input<string>? UpdatedAt { get; set; }

        public BackupState()
        {
        }
        public static new BackupState Empty => new BackupState();
    }
}
