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
    public sealed class GetDatabaseReadOnlyRegionsRegionResult
    {
        /// <summary>
        /// The actor that created the read-only region.
        /// </summary>
        public readonly Outputs.GetDatabaseReadOnlyRegionsRegionActorResult Actor;
        /// <summary>
        /// When the read-only region was created.
        /// </summary>
        public readonly string CreatedAt;
        /// <summary>
        /// The name of the read-only region.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// The ID of the read-only region.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Whether or not the read-only region is ready to serve queries.
        /// </summary>
        public readonly bool Ready;
        /// <summary>
        /// When the read-only region was ready to serve queries.
        /// </summary>
        public readonly string ReadyAt;
        /// <summary>
        /// The details of the read-only region.
        /// </summary>
        public readonly Outputs.GetDatabaseReadOnlyRegionsRegionRegionResult Region;
        /// <summary>
        /// When the read-only region was last updated.
        /// </summary>
        public readonly string UpdatedAt;

        [OutputConstructor]
        private GetDatabaseReadOnlyRegionsRegionResult(
            Outputs.GetDatabaseReadOnlyRegionsRegionActorResult actor,

            string createdAt,

            string displayName,

            string id,

            bool ready,

            string readyAt,

            Outputs.GetDatabaseReadOnlyRegionsRegionRegionResult region,

            string updatedAt)
        {
            Actor = actor;
            CreatedAt = createdAt;
            DisplayName = displayName;
            Id = id;
            Ready = ready;
            ReadyAt = readyAt;
            Region = region;
            UpdatedAt = updatedAt;
        }
    }
}
