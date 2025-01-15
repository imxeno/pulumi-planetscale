// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Planetscale.Outputs
{

    [OutputType]
    public sealed class BackupActor
    {
        /// <summary>
        /// The URL of the actor's avatar
        /// </summary>
        public readonly string? AvatarUrl;
        /// <summary>
        /// The name of the actor
        /// </summary>
        public readonly string? DisplayName;
        /// <summary>
        /// The ID of the actor
        /// </summary>
        public readonly string? Id;

        [OutputConstructor]
        private BackupActor(
            string? avatarUrl,

            string? displayName,

            string? id)
        {
            AvatarUrl = avatarUrl;
            DisplayName = displayName;
            Id = id;
        }
    }
}
