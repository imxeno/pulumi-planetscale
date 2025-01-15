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
    public sealed class GetPasswordRegionResult
    {
        /// <summary>
        /// Name of the region.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// Whether or not the region is currently active.
        /// </summary>
        public readonly bool Enabled;
        /// <summary>
        /// The ID of the region.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Location of the region.
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// Provider for the region (ex. AWS).
        /// </summary>
        public readonly string Provider;
        /// <summary>
        /// Public IP addresses for the region.
        /// </summary>
        public readonly ImmutableArray<string> PublicIpAddresses;
        /// <summary>
        /// The slug of the region.
        /// </summary>
        public readonly string Slug;

        [OutputConstructor]
        private GetPasswordRegionResult(
            string displayName,

            bool enabled,

            string id,

            string location,

            string provider,

            ImmutableArray<string> publicIpAddresses,

            string slug)
        {
            DisplayName = displayName;
            Enabled = enabled;
            Id = id;
            Location = location;
            Provider = provider;
            PublicIpAddresses = publicIpAddresses;
            Slug = slug;
        }
    }
}
