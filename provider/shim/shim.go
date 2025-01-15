package shim

import (
	tfpf "github.com/hashicorp/terraform-plugin-framework/provider"
	"github.com/planetscale/terraform-provider-planetscale/internal/provider"
)

func NewProvider() tfpf.Provider {
	return provider.New("test", false)()
}