// This file was auto-generated by Fern from our API Definition.

package ir

type ErrorDeclaration struct {
	Docs              *string            `json:"docs,omitempty"`
	Name              *DeclaredErrorName `json:"name,omitempty"`
	DiscriminantValue *NameAndWireValue  `json:"discriminantValue,omitempty"`
	Type              *TypeReference     `json:"type,omitempty"`
	StatusCode        int                `json:"statusCode"`
}
