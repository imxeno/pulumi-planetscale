// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Planetscale
{
    public static class GetOauthApplications
    {
        /// <summary>
        /// A list of PlanetScale OAuth applications. (requires feature flag)
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
        ///     // requires a feature flag, contact support to enable it
        ///     var example = Planetscale.GetOauthApplications.Invoke(new()
        ///     {
        ///         Organization = examplePlanetscaleOrganization.Name,
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["oauthApps"] = example,
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Task<GetOauthApplicationsResult> InvokeAsync(GetOauthApplicationsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetOauthApplicationsResult>("planetscale:index/getOauthApplications:getOauthApplications", args ?? new GetOauthApplicationsArgs(), options.WithDefaults());

        /// <summary>
        /// A list of PlanetScale OAuth applications. (requires feature flag)
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
        ///     // requires a feature flag, contact support to enable it
        ///     var example = Planetscale.GetOauthApplications.Invoke(new()
        ///     {
        ///         Organization = examplePlanetscaleOrganization.Name,
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["oauthApps"] = example,
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetOauthApplicationsResult> Invoke(GetOauthApplicationsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetOauthApplicationsResult>("planetscale:index/getOauthApplications:getOauthApplications", args ?? new GetOauthApplicationsInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// A list of PlanetScale OAuth applications. (requires feature flag)
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
        ///     // requires a feature flag, contact support to enable it
        ///     var example = Planetscale.GetOauthApplications.Invoke(new()
        ///     {
        ///         Organization = examplePlanetscaleOrganization.Name,
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["oauthApps"] = example,
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetOauthApplicationsResult> Invoke(GetOauthApplicationsInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetOauthApplicationsResult>("planetscale:index/getOauthApplications:getOauthApplications", args ?? new GetOauthApplicationsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetOauthApplicationsArgs : global::Pulumi.InvokeArgs
    {
        [Input("organization", required: true)]
        public string Organization { get; set; } = null!;

        public GetOauthApplicationsArgs()
        {
        }
        public static new GetOauthApplicationsArgs Empty => new GetOauthApplicationsArgs();
    }

    public sealed class GetOauthApplicationsInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("organization", required: true)]
        public Input<string> Organization { get; set; } = null!;

        public GetOauthApplicationsInvokeArgs()
        {
        }
        public static new GetOauthApplicationsInvokeArgs Empty => new GetOauthApplicationsInvokeArgs();
    }


    [OutputType]
    public sealed class GetOauthApplicationsResult
    {
        public readonly ImmutableArray<Outputs.GetOauthApplicationsApplicationResult> Applications;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Organization;

        [OutputConstructor]
        private GetOauthApplicationsResult(
            ImmutableArray<Outputs.GetOauthApplicationsApplicationResult> applications,

            string id,

            string organization)
        {
            Applications = applications;
            Id = id;
            Organization = organization;
        }
    }
}
