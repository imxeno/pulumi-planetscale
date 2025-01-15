// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package planetscale

import (
	"context"
	"reflect"

	"github.com/imxeno/pulumi-planetscale/sdk/go/planetscale/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A PlanetScale database password.
func LookupPassword(ctx *pulumi.Context, args *LookupPasswordArgs, opts ...pulumi.InvokeOption) (*LookupPasswordResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupPasswordResult
	err := ctx.Invoke("planetscale:index/getPassword:getPassword", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPassword.
type LookupPasswordArgs struct {
	// The branch this password belongs to..
	Branch string `pulumi:"branch"`
	// The database this branch password belongs to.
	Database string `pulumi:"database"`
	// The ID for the password.
	Id string `pulumi:"id"`
	// The organization this database branch password belongs to.
	Organization string `pulumi:"organization"`
	// If the password is for a read-only region, the ID of the region.
	ReadOnlyRegionId *string `pulumi:"readOnlyRegionId"`
}

// A collection of values returned by getPassword.
type LookupPasswordResult struct {
	// The host URL for the password.
	AccessHostUrl string `pulumi:"accessHostUrl"`
	// The actor that created this branch.
	Actor GetPasswordActor `pulumi:"actor"`
	// The branch this password belongs to..
	Branch string `pulumi:"branch"`
	// When the password was created.
	CreatedAt string `pulumi:"createdAt"`
	// The database this branch password belongs to.
	Database string `pulumi:"database"`
	// The branch this password is allowed to access.
	DatabaseBranch GetPasswordDatabaseBranch `pulumi:"databaseBranch"`
	// When the password was deleted.
	DeletedAt string `pulumi:"deletedAt"`
	// When the password will expire.
	ExpiresAt string `pulumi:"expiresAt"`
	// The ID for the password.
	Id string `pulumi:"id"`
	// The display name for the password.
	Name string `pulumi:"name"`
	// The organization this database branch password belongs to.
	Organization string `pulumi:"organization"`
	// If the password is for a read-only region, the ID of the region.
	ReadOnlyRegionId *string `pulumi:"readOnlyRegionId"`
	// The region in which this password can be used.
	Region GetPasswordRegion `pulumi:"region"`
	// Whether or not the password can be renewed.
	Renewable bool `pulumi:"renewable"`
	// The role for the password.
	Role string `pulumi:"role"`
	// Time to live (in seconds) for the password. The password will be invalid and unrenewable when TTL has passed.
	TtlSeconds float64 `pulumi:"ttlSeconds"`
	// The username for the password.
	Username string `pulumi:"username"`
}

func LookupPasswordOutput(ctx *pulumi.Context, args LookupPasswordOutputArgs, opts ...pulumi.InvokeOption) LookupPasswordResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupPasswordResultOutput, error) {
			args := v.(LookupPasswordArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("planetscale:index/getPassword:getPassword", args, LookupPasswordResultOutput{}, options).(LookupPasswordResultOutput), nil
		}).(LookupPasswordResultOutput)
}

// A collection of arguments for invoking getPassword.
type LookupPasswordOutputArgs struct {
	// The branch this password belongs to..
	Branch pulumi.StringInput `pulumi:"branch"`
	// The database this branch password belongs to.
	Database pulumi.StringInput `pulumi:"database"`
	// The ID for the password.
	Id pulumi.StringInput `pulumi:"id"`
	// The organization this database branch password belongs to.
	Organization pulumi.StringInput `pulumi:"organization"`
	// If the password is for a read-only region, the ID of the region.
	ReadOnlyRegionId pulumi.StringPtrInput `pulumi:"readOnlyRegionId"`
}

func (LookupPasswordOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPasswordArgs)(nil)).Elem()
}

// A collection of values returned by getPassword.
type LookupPasswordResultOutput struct{ *pulumi.OutputState }

func (LookupPasswordResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPasswordResult)(nil)).Elem()
}

func (o LookupPasswordResultOutput) ToLookupPasswordResultOutput() LookupPasswordResultOutput {
	return o
}

func (o LookupPasswordResultOutput) ToLookupPasswordResultOutputWithContext(ctx context.Context) LookupPasswordResultOutput {
	return o
}

// The host URL for the password.
func (o LookupPasswordResultOutput) AccessHostUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPasswordResult) string { return v.AccessHostUrl }).(pulumi.StringOutput)
}

// The actor that created this branch.
func (o LookupPasswordResultOutput) Actor() GetPasswordActorOutput {
	return o.ApplyT(func(v LookupPasswordResult) GetPasswordActor { return v.Actor }).(GetPasswordActorOutput)
}

// The branch this password belongs to..
func (o LookupPasswordResultOutput) Branch() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPasswordResult) string { return v.Branch }).(pulumi.StringOutput)
}

// When the password was created.
func (o LookupPasswordResultOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPasswordResult) string { return v.CreatedAt }).(pulumi.StringOutput)
}

// The database this branch password belongs to.
func (o LookupPasswordResultOutput) Database() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPasswordResult) string { return v.Database }).(pulumi.StringOutput)
}

// The branch this password is allowed to access.
func (o LookupPasswordResultOutput) DatabaseBranch() GetPasswordDatabaseBranchOutput {
	return o.ApplyT(func(v LookupPasswordResult) GetPasswordDatabaseBranch { return v.DatabaseBranch }).(GetPasswordDatabaseBranchOutput)
}

// When the password was deleted.
func (o LookupPasswordResultOutput) DeletedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPasswordResult) string { return v.DeletedAt }).(pulumi.StringOutput)
}

// When the password will expire.
func (o LookupPasswordResultOutput) ExpiresAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPasswordResult) string { return v.ExpiresAt }).(pulumi.StringOutput)
}

// The ID for the password.
func (o LookupPasswordResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPasswordResult) string { return v.Id }).(pulumi.StringOutput)
}

// The display name for the password.
func (o LookupPasswordResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPasswordResult) string { return v.Name }).(pulumi.StringOutput)
}

// The organization this database branch password belongs to.
func (o LookupPasswordResultOutput) Organization() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPasswordResult) string { return v.Organization }).(pulumi.StringOutput)
}

// If the password is for a read-only region, the ID of the region.
func (o LookupPasswordResultOutput) ReadOnlyRegionId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPasswordResult) *string { return v.ReadOnlyRegionId }).(pulumi.StringPtrOutput)
}

// The region in which this password can be used.
func (o LookupPasswordResultOutput) Region() GetPasswordRegionOutput {
	return o.ApplyT(func(v LookupPasswordResult) GetPasswordRegion { return v.Region }).(GetPasswordRegionOutput)
}

// Whether or not the password can be renewed.
func (o LookupPasswordResultOutput) Renewable() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupPasswordResult) bool { return v.Renewable }).(pulumi.BoolOutput)
}

// The role for the password.
func (o LookupPasswordResultOutput) Role() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPasswordResult) string { return v.Role }).(pulumi.StringOutput)
}

// Time to live (in seconds) for the password. The password will be invalid and unrenewable when TTL has passed.
func (o LookupPasswordResultOutput) TtlSeconds() pulumi.Float64Output {
	return o.ApplyT(func(v LookupPasswordResult) float64 { return v.TtlSeconds }).(pulumi.Float64Output)
}

// The username for the password.
func (o LookupPasswordResultOutput) Username() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPasswordResult) string { return v.Username }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPasswordResultOutput{})
}
