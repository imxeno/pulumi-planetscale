// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package planetscale

import (
	"context"
	"reflect"

	"github.com/imxeno/pulumi-planetscale/sdk/go/planetscale/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A PlanetScale branch.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/imxeno/pulumi-planetscale/sdk/go/planetscale"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			example, err := planetscale.LookupBranch(ctx, &planetscale.LookupBranchArgs{
//				Organization: "example.com",
//				Database:     "example_db",
//				Name:         "main",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("branch", example)
//			return nil
//		})
//	}
//
// ```
func LookupBranch(ctx *pulumi.Context, args *LookupBranchArgs, opts ...pulumi.InvokeOption) (*LookupBranchResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupBranchResult
	err := ctx.Invoke("planetscale:index/getBranch:getBranch", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getBranch.
type LookupBranchArgs struct {
	// The database this branch belongs to.
	Database string `pulumi:"database"`
	// The name of the branch.
	Name string `pulumi:"name"`
	// The organization this branch belongs to.
	Organization string `pulumi:"organization"`
}

// A collection of values returned by getBranch.
type LookupBranchResult struct {
	// The access host URL for the branch. This is a legacy field, use `mysqlEdgeAddress`.
	AccessHostUrl string `pulumi:"accessHostUrl"`
	// The actor who created this branch.
	Actor GetBranchActor `pulumi:"actor"`
	// The SKU representing the branch's cluster size.
	ClusterRateName string `pulumi:"clusterRateName"`
	// When the branch was created.
	CreatedAt string `pulumi:"createdAt"`
	// The database this branch belongs to.
	Database string `pulumi:"database"`
	// Planetscale app URL for the branch.
	HtmlUrl string `pulumi:"htmlUrl"`
	// The ID of the branch.
	Id string `pulumi:"id"`
	// The ID of the backup from which the branch was restored.
	InitialRestoreId string `pulumi:"initialRestoreId"`
	// The MySQL address for the branch.
	MysqlAddress string `pulumi:"mysqlAddress"`
	// The address of the MySQL provider for the branch.
	MysqlEdgeAddress string `pulumi:"mysqlEdgeAddress"`
	// The name of the branch.
	Name string `pulumi:"name"`
	// The organization this branch belongs to.
	Organization string `pulumi:"organization"`
	// The name of the parent branch from which the branch was created.
	ParentBranch string `pulumi:"parentBranch"`
	// Whether or not the branch is a production branch.
	Production bool `pulumi:"production"`
	// Whether or not the branch is ready to serve queries.
	Ready bool `pulumi:"ready"`
	// The region in which this branch lives.
	Region GetBranchRegion `pulumi:"region"`
	// When a user last marked a backup restore checklist as completed.
	RestoreChecklistCompletedAt string                      `pulumi:"restoreChecklistCompletedAt"`
	RestoredFromBranch          GetBranchRestoredFromBranch `pulumi:"restoredFromBranch"`
	// When the schema for the branch was last updated.
	SchemaLastUpdatedAt string `pulumi:"schemaLastUpdatedAt"`
	// The number of shards in the branch.
	ShardCount float64 `pulumi:"shardCount"`
	// Whether or not the branch is sharded.
	Sharded bool `pulumi:"sharded"`
	// When the branch was last updated.
	UpdatedAt string `pulumi:"updatedAt"`
}

func LookupBranchOutput(ctx *pulumi.Context, args LookupBranchOutputArgs, opts ...pulumi.InvokeOption) LookupBranchResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupBranchResultOutput, error) {
			args := v.(LookupBranchArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("planetscale:index/getBranch:getBranch", args, LookupBranchResultOutput{}, options).(LookupBranchResultOutput), nil
		}).(LookupBranchResultOutput)
}

// A collection of arguments for invoking getBranch.
type LookupBranchOutputArgs struct {
	// The database this branch belongs to.
	Database pulumi.StringInput `pulumi:"database"`
	// The name of the branch.
	Name pulumi.StringInput `pulumi:"name"`
	// The organization this branch belongs to.
	Organization pulumi.StringInput `pulumi:"organization"`
}

func (LookupBranchOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBranchArgs)(nil)).Elem()
}

// A collection of values returned by getBranch.
type LookupBranchResultOutput struct{ *pulumi.OutputState }

func (LookupBranchResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBranchResult)(nil)).Elem()
}

func (o LookupBranchResultOutput) ToLookupBranchResultOutput() LookupBranchResultOutput {
	return o
}

func (o LookupBranchResultOutput) ToLookupBranchResultOutputWithContext(ctx context.Context) LookupBranchResultOutput {
	return o
}

// The access host URL for the branch. This is a legacy field, use `mysqlEdgeAddress`.
func (o LookupBranchResultOutput) AccessHostUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBranchResult) string { return v.AccessHostUrl }).(pulumi.StringOutput)
}

// The actor who created this branch.
func (o LookupBranchResultOutput) Actor() GetBranchActorOutput {
	return o.ApplyT(func(v LookupBranchResult) GetBranchActor { return v.Actor }).(GetBranchActorOutput)
}

// The SKU representing the branch's cluster size.
func (o LookupBranchResultOutput) ClusterRateName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBranchResult) string { return v.ClusterRateName }).(pulumi.StringOutput)
}

// When the branch was created.
func (o LookupBranchResultOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBranchResult) string { return v.CreatedAt }).(pulumi.StringOutput)
}

// The database this branch belongs to.
func (o LookupBranchResultOutput) Database() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBranchResult) string { return v.Database }).(pulumi.StringOutput)
}

// Planetscale app URL for the branch.
func (o LookupBranchResultOutput) HtmlUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBranchResult) string { return v.HtmlUrl }).(pulumi.StringOutput)
}

// The ID of the branch.
func (o LookupBranchResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBranchResult) string { return v.Id }).(pulumi.StringOutput)
}

// The ID of the backup from which the branch was restored.
func (o LookupBranchResultOutput) InitialRestoreId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBranchResult) string { return v.InitialRestoreId }).(pulumi.StringOutput)
}

// The MySQL address for the branch.
func (o LookupBranchResultOutput) MysqlAddress() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBranchResult) string { return v.MysqlAddress }).(pulumi.StringOutput)
}

// The address of the MySQL provider for the branch.
func (o LookupBranchResultOutput) MysqlEdgeAddress() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBranchResult) string { return v.MysqlEdgeAddress }).(pulumi.StringOutput)
}

// The name of the branch.
func (o LookupBranchResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBranchResult) string { return v.Name }).(pulumi.StringOutput)
}

// The organization this branch belongs to.
func (o LookupBranchResultOutput) Organization() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBranchResult) string { return v.Organization }).(pulumi.StringOutput)
}

// The name of the parent branch from which the branch was created.
func (o LookupBranchResultOutput) ParentBranch() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBranchResult) string { return v.ParentBranch }).(pulumi.StringOutput)
}

// Whether or not the branch is a production branch.
func (o LookupBranchResultOutput) Production() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupBranchResult) bool { return v.Production }).(pulumi.BoolOutput)
}

// Whether or not the branch is ready to serve queries.
func (o LookupBranchResultOutput) Ready() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupBranchResult) bool { return v.Ready }).(pulumi.BoolOutput)
}

// The region in which this branch lives.
func (o LookupBranchResultOutput) Region() GetBranchRegionOutput {
	return o.ApplyT(func(v LookupBranchResult) GetBranchRegion { return v.Region }).(GetBranchRegionOutput)
}

// When a user last marked a backup restore checklist as completed.
func (o LookupBranchResultOutput) RestoreChecklistCompletedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBranchResult) string { return v.RestoreChecklistCompletedAt }).(pulumi.StringOutput)
}

func (o LookupBranchResultOutput) RestoredFromBranch() GetBranchRestoredFromBranchOutput {
	return o.ApplyT(func(v LookupBranchResult) GetBranchRestoredFromBranch { return v.RestoredFromBranch }).(GetBranchRestoredFromBranchOutput)
}

// When the schema for the branch was last updated.
func (o LookupBranchResultOutput) SchemaLastUpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBranchResult) string { return v.SchemaLastUpdatedAt }).(pulumi.StringOutput)
}

// The number of shards in the branch.
func (o LookupBranchResultOutput) ShardCount() pulumi.Float64Output {
	return o.ApplyT(func(v LookupBranchResult) float64 { return v.ShardCount }).(pulumi.Float64Output)
}

// Whether or not the branch is sharded.
func (o LookupBranchResultOutput) Sharded() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupBranchResult) bool { return v.Sharded }).(pulumi.BoolOutput)
}

// When the branch was last updated.
func (o LookupBranchResultOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBranchResult) string { return v.UpdatedAt }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupBranchResultOutput{})
}
