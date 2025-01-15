// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Planetscale.Inputs
{

    public sealed class BranchRegionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the region.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// Whether or not the region is currently active.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The ID of the region.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Location of the region.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Provider for the region (ex. AWS).
        /// </summary>
        [Input("provider")]
        public Input<string>? Provider { get; set; }

        [Input("publicIpAddresses")]
        private InputList<string>? _publicIpAddresses;

        /// <summary>
        /// Public IP addresses for the region.
        /// </summary>
        public InputList<string> PublicIpAddresses
        {
            get => _publicIpAddresses ?? (_publicIpAddresses = new InputList<string>());
            set => _publicIpAddresses = value;
        }

        /// <summary>
        /// The slug of the region.
        /// </summary>
        [Input("slug")]
        public Input<string>? Slug { get; set; }

        public BranchRegionArgs()
        {
        }
        public static new BranchRegionArgs Empty => new BranchRegionArgs();
    }
}
