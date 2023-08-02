// This file was auto-generated by Fern from our API Definition.

package ir

type PathParameter struct {
	Docs      *string               `json:"docs,omitempty"`
	Name      *Name                 `json:"name,omitempty"`
	ValueType *TypeReference        `json:"valueType,omitempty"`
	Location  PathParameterLocation `json:"location,omitempty"`
	Variable  *VariableId           `json:"variable,omitempty"`
}
