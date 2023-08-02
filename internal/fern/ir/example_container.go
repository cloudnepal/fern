// This file was auto-generated by Fern from our API Definition.

package ir

import (
	json "encoding/json"
	fmt "fmt"
)

type ExampleContainer struct {
	Type     string
	List     []*ExampleTypeReference
	Set      []*ExampleTypeReference
	Optional *ExampleTypeReference
	Map      []*ExampleKeyValuePair
}

func NewExampleContainerFromList(value []*ExampleTypeReference) *ExampleContainer {
	return &ExampleContainer{Type: "list", List: value}
}

func NewExampleContainerFromSet(value []*ExampleTypeReference) *ExampleContainer {
	return &ExampleContainer{Type: "set", Set: value}
}

func NewExampleContainerFromOptional(value *ExampleTypeReference) *ExampleContainer {
	return &ExampleContainer{Type: "optional", Optional: value}
}

func NewExampleContainerFromMap(value []*ExampleKeyValuePair) *ExampleContainer {
	return &ExampleContainer{Type: "map", Map: value}
}

func (e *ExampleContainer) UnmarshalJSON(data []byte) error {
	var unmarshaler struct {
		Type string `json:"type"`
	}
	if err := json.Unmarshal(data, &unmarshaler); err != nil {
		return err
	}
	e.Type = unmarshaler.Type
	switch unmarshaler.Type {
	case "list":
		var valueUnmarshaler struct {
			List []*ExampleTypeReference `json:"list,omitempty"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		e.List = valueUnmarshaler.List
	case "set":
		var valueUnmarshaler struct {
			Set []*ExampleTypeReference `json:"set,omitempty"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		e.Set = valueUnmarshaler.Set
	case "optional":
		var valueUnmarshaler struct {
			Optional *ExampleTypeReference `json:"optional,omitempty"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		e.Optional = valueUnmarshaler.Optional
	case "map":
		var valueUnmarshaler struct {
			Map []*ExampleKeyValuePair `json:"map,omitempty"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		e.Map = valueUnmarshaler.Map
	}
	return nil
}

func (e ExampleContainer) MarshalJSON() ([]byte, error) {
	switch e.Type {
	default:
		return nil, fmt.Errorf("invalid type %s in %T", e.Type, e)
	case "list":
		var marshaler = struct {
			Type string                  `json:"type"`
			List []*ExampleTypeReference `json:"list,omitempty"`
		}{
			Type: e.Type,
			List: e.List,
		}
		return json.Marshal(marshaler)
	case "set":
		var marshaler = struct {
			Type string                  `json:"type"`
			Set  []*ExampleTypeReference `json:"set,omitempty"`
		}{
			Type: e.Type,
			Set:  e.Set,
		}
		return json.Marshal(marshaler)
	case "optional":
		var marshaler = struct {
			Type     string                `json:"type"`
			Optional *ExampleTypeReference `json:"optional,omitempty"`
		}{
			Type:     e.Type,
			Optional: e.Optional,
		}
		return json.Marshal(marshaler)
	case "map":
		var marshaler = struct {
			Type string                 `json:"type"`
			Map  []*ExampleKeyValuePair `json:"map,omitempty"`
		}{
			Type: e.Type,
			Map:  e.Map,
		}
		return json.Marshal(marshaler)
	}
}

type ExampleContainerVisitor interface {
	VisitList([]*ExampleTypeReference) error
	VisitSet([]*ExampleTypeReference) error
	VisitOptional(*ExampleTypeReference) error
	VisitMap([]*ExampleKeyValuePair) error
}

func (e *ExampleContainer) Accept(v ExampleContainerVisitor) error {
	switch e.Type {
	default:
		return fmt.Errorf("invalid type %s in %T", e.Type, e)
	case "list":
		return v.VisitList(e.List)
	case "set":
		return v.VisitSet(e.Set)
	case "optional":
		return v.VisitOptional(e.Optional)
	case "map":
		return v.VisitMap(e.Map)
	}
}
