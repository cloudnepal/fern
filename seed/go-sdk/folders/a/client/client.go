// This file was auto-generated by Fern from our API Definition.

package client

import (
	bclient "github.com/folders/fern/a/b/client"
	cclient "github.com/folders/fern/a/c/client"
	core "github.com/folders/fern/core"
	option "github.com/folders/fern/option"
	http "net/http"
)

type Client struct {
	baseURL string
	caller  *core.Caller
	header  http.Header

	B *bclient.Client
	C *cclient.Client
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
		B:      bclient.NewClient(opts...),
		C:      cclient.NewClient(opts...),
	}
}