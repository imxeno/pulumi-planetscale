// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package planetscale

import (
	"context"
	"reflect"

	"github.com/imxeno/pulumi-planetscale/sdk/go/planetscale/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The schema of a PlanetScale branch.
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
//			example, err := planetscale.GetBranchSchema(ctx, &planetscale.GetBranchSchemaArgs{
//				Organization: "example.com",
//				Database:     "example_db",
//				Branch:       "main",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("branchSchema", example)
//			return nil
//		})
//	}
//
// ```
func GetBranchSchema(ctx *pulumi.Context, args *GetBranchSchemaArgs, opts ...pulumi.InvokeOption) (*GetBranchSchemaResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetBranchSchemaResult
	err := ctx.Invoke("planetscale:index/getBranchSchema:getBranchSchema", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getBranchSchema.
type GetBranchSchemaArgs struct {
	Branch       string  `pulumi:"branch"`
	Database     string  `pulumi:"database"`
	Keyspace     *string `pulumi:"keyspace"`
	Organization string  `pulumi:"organization"`
}

// A collection of values returned by getBranchSchema.
type GetBranchSchemaResult struct {
	Branch   string `pulumi:"branch"`
	Database string `pulumi:"database"`
	// The provider-assigned unique ID for this managed resource.
	Id           string                 `pulumi:"id"`
	Keyspace     *string                `pulumi:"keyspace"`
	Organization string                 `pulumi:"organization"`
	Tables       []GetBranchSchemaTable `pulumi:"tables"`
}

func GetBranchSchemaOutput(ctx *pulumi.Context, args GetBranchSchemaOutputArgs, opts ...pulumi.InvokeOption) GetBranchSchemaResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetBranchSchemaResultOutput, error) {
			args := v.(GetBranchSchemaArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("planetscale:index/getBranchSchema:getBranchSchema", args, GetBranchSchemaResultOutput{}, options).(GetBranchSchemaResultOutput), nil
		}).(GetBranchSchemaResultOutput)
}

// A collection of arguments for invoking getBranchSchema.
type GetBranchSchemaOutputArgs struct {
	Branch       pulumi.StringInput    `pulumi:"branch"`
	Database     pulumi.StringInput    `pulumi:"database"`
	Keyspace     pulumi.StringPtrInput `pulumi:"keyspace"`
	Organization pulumi.StringInput    `pulumi:"organization"`
}

func (GetBranchSchemaOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetBranchSchemaArgs)(nil)).Elem()
}

// A collection of values returned by getBranchSchema.
type GetBranchSchemaResultOutput struct{ *pulumi.OutputState }

func (GetBranchSchemaResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetBranchSchemaResult)(nil)).Elem()
}

func (o GetBranchSchemaResultOutput) ToGetBranchSchemaResultOutput() GetBranchSchemaResultOutput {
	return o
}

func (o GetBranchSchemaResultOutput) ToGetBranchSchemaResultOutputWithContext(ctx context.Context) GetBranchSchemaResultOutput {
	return o
}

func (o GetBranchSchemaResultOutput) Branch() pulumi.StringOutput {
	return o.ApplyT(func(v GetBranchSchemaResult) string { return v.Branch }).(pulumi.StringOutput)
}

func (o GetBranchSchemaResultOutput) Database() pulumi.StringOutput {
	return o.ApplyT(func(v GetBranchSchemaResult) string { return v.Database }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetBranchSchemaResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetBranchSchemaResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetBranchSchemaResultOutput) Keyspace() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetBranchSchemaResult) *string { return v.Keyspace }).(pulumi.StringPtrOutput)
}

func (o GetBranchSchemaResultOutput) Organization() pulumi.StringOutput {
	return o.ApplyT(func(v GetBranchSchemaResult) string { return v.Organization }).(pulumi.StringOutput)
}

func (o GetBranchSchemaResultOutput) Tables() GetBranchSchemaTableArrayOutput {
	return o.ApplyT(func(v GetBranchSchemaResult) []GetBranchSchemaTable { return v.Tables }).(GetBranchSchemaTableArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetBranchSchemaResultOutput{})
}
