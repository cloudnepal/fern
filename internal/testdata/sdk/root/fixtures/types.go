// This file was auto-generated by Fern from our API Definition.

package api

import (
	json "encoding/json"
	fmt "fmt"
	strconv "strconv"
)

type Bar struct {
	Id      *Id      `json:"id,omitempty"`
	Name    *string  `json:"name,omitempty"`
	List    *string  `json:"list,omitempty"`
	Type    *FooType `json:"type,omitempty"`
	Request *Request `json:"request,omitempty"`
	Delay   *string  `json:"delay,omitempty"`
}

type Baz struct {
	Id          *Id     `json:"id,omitempty"`
	Name        *string `json:"name,omitempty"`
	List        *string `json:"list,omitempty"`
	Description *string `json:"description,omitempty"`
	// This field has documentation, so it should be rendered
	// just above the field.
	// Note: Newlines should be preserved.
	HasDocs *string `json:"hasDocs,omitempty"`
}

type Error struct {
	Message   *string   `json:"message,omitempty"`
	Recursive *[]*Error `json:"recursive,omitempty"`
}

type Foo struct {
	Id      *Id      `json:"id,omitempty"`
	Name    *string  `json:"name,omitempty"`
	List    *string  `json:"list,omitempty"`
	Type    *FooType `json:"type,omitempty"`
	Request *Request `json:"request,omitempty"`
	Delay   *string  `json:"delay,omitempty"`
}

type FooType uint8

const (
	FooTypeOne FooType = iota + 1
	FooTypeTwo
	FooTypeThree
	FooTypeFour
)

func (f FooType) String() string {
	switch f {
	default:
		return strconv.Itoa(int(f))
	case FooTypeOne:
		return "one"
	case FooTypeTwo:
		return "two"
	case FooTypeThree:
		return "three"
	case FooTypeFour:
		return "four"
	}
}

func (f FooType) MarshalJSON() ([]byte, error) {
	return []byte(fmt.Sprintf("%q", f.String())), nil
}

func (f *FooType) UnmarshalJSON(data []byte) error {
	var raw string
	if err := json.Unmarshal(data, &raw); err != nil {
		return err
	}
	switch raw {
	case "one":
		value := FooTypeOne
		*f = value
	case "two":
		value := FooTypeTwo
		*f = value
	case "three":
		value := FooTypeThree
		*f = value
	case "four":
		value := FooTypeFour
		*f = value
	}
	return nil
}

type Request struct {
	Url     string          `json:"url"`
	Headers *map[string]any `json:"headers,omitempty"`
	Body    *string         `json:"body,omitempty"`
}

type Id = string
