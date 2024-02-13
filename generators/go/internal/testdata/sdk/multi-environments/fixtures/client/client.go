// This file was auto-generated by Fern from our API Definition.

package client

import (
	auth "github.com/fern-api/fern-go/internal/testdata/sdk/multi-environments/fixtures/auth"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/multi-environments/fixtures/core"
	option "github.com/fern-api/fern-go/internal/testdata/sdk/multi-environments/fixtures/option"
	plant "github.com/fern-api/fern-go/internal/testdata/sdk/multi-environments/fixtures/plant"
	http "net/http"
)

type Client struct {
	baseURL string
	caller  *core.Caller
	header  http.Header

	Auth  *auth.Client
	Plant *plant.Client
}

func NewClient(opts ...option.RequestOption) *Client {
	options := core.NewRequestOptions(opts...)
	return &Client{
		baseURL: options.BaseURL,
		caller: core.NewCaller(
			&core.CallerParams{
				Client:      options.HTTPClient,
				MaxAttempts: options.MaxAttempts,
			},
		),
		header: options.ToHeader(),
		Auth:   auth.NewClient(opts...),
		Plant:  plant.NewClient(opts...),
	}
}