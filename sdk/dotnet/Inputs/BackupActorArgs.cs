// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Planetscale.Inputs
{

    public sealed class BackupActorArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The URL of the actor's avatar
        /// </summary>
        [Input("avatarUrl")]
        public Input<string>? AvatarUrl { get; set; }

        /// <summary>
        /// The name of the actor
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// The ID of the actor
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        public BackupActorArgs()
        {
        }
        public static new BackupActorArgs Empty => new BackupActorArgs();
    }
}
