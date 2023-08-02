// This file was auto-generated by Fern from our API Definition.

package ir

type Package struct {
	Docs               *string                  `json:"docs,omitempty"`
	FernFilepath       *FernFilepath            `json:"fernFilepath,omitempty"`
	Service            *ServiceId               `json:"service,omitempty"`
	Types              []TypeId                 `json:"types,omitempty"`
	Errors             []ErrorId                `json:"errors,omitempty"`
	Subpackages        []SubpackageId           `json:"subpackages,omitempty"`
	HasEndpointsInTree bool                     `json:"hasEndpointsInTree"`
	NavigationConfig   *PackageNavigationConfig `json:"navigationConfig,omitempty"`
}
