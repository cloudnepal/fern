// This file was auto-generated by Fern from our API Definition.

package ir

type ApiAuth struct {
	Docs        *string                `json:"docs,omitempty"`
	Requirement AuthSchemesRequirement `json:"requirement,omitempty"`
	Schemes     []*AuthScheme          `json:"schemes,omitempty"`
}
