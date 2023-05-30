// Generated by Fern. Do not edit.

package ir

// Complete representation of the API schema
type IntermediateRepresentation struct {
	// This is the human readable unique id for the API.
	ApiName        *Name    `json:"apiName"`
	ApiDisplayName *string  `json:"apiDisplayName"`
	ApiDocs        *string  `json:"apiDocs"`
	Auth           *ApiAuth `json:"auth"`
	// API Wide headers that are sent on every request
	Headers []*HttpHeader `json:"headers"`
	// The types described by this API
	Types map[TypeId]*TypeDeclaration `json:"types"`
	// The services exposed by this API
	Services                    map[ServiceId]*HttpService    `json:"services"`
	Errors                      map[ErrorId]*ErrorDeclaration `json:"errors"`
	Subpackages                 map[SubpackageId]*Subpackage  `json:"subpackages"`
	RootPackage                 *Package                      `json:"rootPackage"`
	Constants                   *Constants                    `json:"constants"`
	Environments                *EnvironmentsConfig           `json:"environments"`
	BasePath                    *HttpPath                     `json:"basePath"`
	PathParameters              []*PathParameter              `json:"pathParameters"`
	ErrorDiscriminationStrategy *ErrorDiscriminationStrategy  `json:"errorDiscriminationStrategy"`
	SdkConfig                   *SdkConfig                    `json:"sdkConfig"`
	Variables                   []*VariableDeclaration        `json:"variables"`
}
