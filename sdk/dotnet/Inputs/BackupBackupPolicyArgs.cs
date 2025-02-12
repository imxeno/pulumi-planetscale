// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Planetscale.Inputs
{

    public sealed class BackupBackupPolicyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// When the backup policy was created.
        /// </summary>
        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        /// <summary>
        /// The unit for the frequency of the backup policy. Not configurable for now.
        /// </summary>
        [Input("frequencyUnit")]
        public Input<string>? FrequencyUnit { get; set; }

        /// <summary>
        /// A number value for the frequency of the backup policy. Not configurable for now.
        /// </summary>
        [Input("frequencyValue")]
        public Input<double>? FrequencyValue { get; set; }

        /// <summary>
        /// The ID of the backup policy.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// When the backup was last run.
        /// </summary>
        [Input("lastRanAt")]
        public Input<string>? LastRanAt { get; set; }

        /// <summary>
        /// The name of the backup policy.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// When the backup will next run.
        /// </summary>
        [Input("nextRunAt")]
        public Input<string>? NextRunAt { get; set; }

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

        /// <summary>
        /// Day of the week that the backup is scheduled.
        /// </summary>
        [Input("scheduleDay")]
        public Input<string>? ScheduleDay { get; set; }

        /// <summary>
        /// Week of the month that the backup is scheduled.
        /// </summary>
        [Input("scheduleWeek")]
        public Input<string>? ScheduleWeek { get; set; }

        /// <summary>
        /// Whether the backup policy is for a production or development database, or for a database branch.
        /// </summary>
        [Input("target")]
        public Input<string>? Target { get; set; }

        /// <summary>
        /// When the backup policy was last updated.
        /// </summary>
        [Input("updatedAt")]
        public Input<string>? UpdatedAt { get; set; }

        public BackupBackupPolicyArgs()
        {
        }
        public static new BackupBackupPolicyArgs Empty => new BackupBackupPolicyArgs();
    }
}
