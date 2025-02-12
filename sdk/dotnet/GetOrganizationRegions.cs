// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Planetscale
{
    public static class GetOrganizationRegions
    {
        /// <summary>
        /// A list of PlanetScale regions for the organization.
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Planetscale = Pulumi.Planetscale;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Planetscale.GetOrganizationRegions.Invoke(new()
        ///     {
        ///         Organization = "example",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["orgRegions"] = example,
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Task<GetOrganizationRegionsResult> InvokeAsync(GetOrganizationRegionsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetOrganizationRegionsResult>("planetscale:index/getOrganizationRegions:getOrganizationRegions", args ?? new GetOrganizationRegionsArgs(), options.WithDefaults());

        /// <summary>
        /// A list of PlanetScale regions for the organization.
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Planetscale = Pulumi.Planetscale;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Planetscale.GetOrganizationRegions.Invoke(new()
        ///     {
        ///         Organization = "example",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["orgRegions"] = example,
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetOrganizationRegionsResult> Invoke(GetOrganizationRegionsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetOrganizationRegionsResult>("planetscale:index/getOrganizationRegions:getOrganizationRegions", args ?? new GetOrganizationRegionsInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// A list of PlanetScale regions for the organization.
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Planetscale = Pulumi.Planetscale;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Planetscale.GetOrganizationRegions.Invoke(new()
        ///     {
        ///         Organization = "example",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["orgRegions"] = example,
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetOrganizationRegionsResult> Invoke(GetOrganizationRegionsInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetOrganizationRegionsResult>("planetscale:index/getOrganizationRegions:getOrganizationRegions", args ?? new GetOrganizationRegionsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetOrganizationRegionsArgs : global::Pulumi.InvokeArgs
    {
        [Input("organization", required: true)]
        public string Organization { get; set; } = null!;

        public GetOrganizationRegionsArgs()
        {
        }
        public static new GetOrganizationRegionsArgs Empty => new GetOrganizationRegionsArgs();
    }

    public sealed class GetOrganizationRegionsInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("organization", required: true)]
        public Input<string> Organization { get; set; } = null!;

        public GetOrganizationRegionsInvokeArgs()
        {
        }
        public static new GetOrganizationRegionsInvokeArgs Empty => new GetOrganizationRegionsInvokeArgs();
    }


    [OutputType]
    public sealed class GetOrganizationRegionsResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Organization;
        public readonly ImmutableArray<Outputs.GetOrganizationRegionsRegionResult> Regions;

        [OutputConstructor]
        private GetOrganizationRegionsResult(
            string id,

            string organization,

            ImmutableArray<Outputs.GetOrganizationRegionsRegionResult> regions)
        {
            Id = id;
            Organization = organization;
            Regions = regions;
        }
    }
}
