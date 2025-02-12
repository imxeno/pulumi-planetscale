// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Planetscale.Inputs
{

    public sealed class GetDatabaseRegionArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the region.
        /// </summary>
        [Input("displayName", required: true)]
        public string DisplayName { get; set; } = null!;

        /// <summary>
        /// Whether or not the region is currently active.
        /// </summary>
        [Input("enabled", required: true)]
        public bool Enabled { get; set; }

        /// <summary>
        /// The ID of the region.
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        /// <summary>
        /// Location of the region.
        /// </summary>
        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        /// <summary>
        /// Provider for the region (ex. AWS).
        /// </summary>
        [Input("provider", required: true)]
        public string Provider { get; set; } = null!;

        [Input("publicIpAddresses", required: true)]
        private List<string>? _publicIpAddresses;

        /// <summary>
        /// Public IP addresses for the region.
        /// </summary>
        public List<string> PublicIpAddresses
        {
            get => _publicIpAddresses ?? (_publicIpAddresses = new List<string>());
            set => _publicIpAddresses = value;
        }

        /// <summary>
        /// The slug of the region.
        /// </summary>
        [Input("slug", required: true)]
        public string Slug { get; set; } = null!;

        public GetDatabaseRegionArgs()
        {
        }
        public static new GetDatabaseRegionArgs Empty => new GetDatabaseRegionArgs();
    }
}
