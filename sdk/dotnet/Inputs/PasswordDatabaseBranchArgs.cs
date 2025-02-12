// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Planetscale.Inputs
{

    public sealed class PasswordDatabaseBranchArgs : global::Pulumi.ResourceArgs
    {
        [Input("accessHostUrl")]
        public Input<string>? AccessHostUrl { get; set; }

        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("mysqlEdgeAddress")]
        public Input<string>? MysqlEdgeAddress { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("production")]
        public Input<bool>? Production { get; set; }

        public PasswordDatabaseBranchArgs()
        {
        }
        public static new PasswordDatabaseBranchArgs Empty => new PasswordDatabaseBranchArgs();
    }
}
