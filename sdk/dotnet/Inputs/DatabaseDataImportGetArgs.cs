// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Planetscale.Inputs
{

    public sealed class DatabaseDataImportGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Connection information for the source of the data for the import.
        /// </summary>
        [Input("dataSource")]
        public Input<Inputs.DatabaseDataImportDataSourceGetArgs>? DataSource { get; set; }

        /// <summary>
        /// When the import finished.
        /// </summary>
        [Input("finishedAt")]
        public Input<string>? FinishedAt { get; set; }

        /// <summary>
        /// Errors encountered while preparing the import.
        /// </summary>
        [Input("importCheckErrors")]
        public Input<string>? ImportCheckErrors { get; set; }

        /// <summary>
        /// When the import started.
        /// </summary>
        [Input("startedAt")]
        public Input<string>? StartedAt { get; set; }

        /// <summary>
        /// The state of the import, one of: pending, queued, in_progress, complete, cancelled, error.
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        public DatabaseDataImportGetArgs()
        {
        }
        public static new DatabaseDataImportGetArgs Empty => new DatabaseDataImportGetArgs();
    }
}
