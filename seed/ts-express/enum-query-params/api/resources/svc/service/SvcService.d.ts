/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as SeedApi from "../../..";
import express from "express";
export interface SvcServiceMethods {
    test(req: express.Request<never, string, never, {
        "some-enum"?: SeedApi.MyEnum;
    }>, res: {
        send: (responseBody: string) => Promise<void>;
        cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
        locals: any;
    }): void | Promise<void>;
}
export declare class SvcService {
    private readonly methods;
    private router;
    constructor(methods: SvcServiceMethods, middleware?: express.RequestHandler[]);
    addMiddleware(handler: express.RequestHandler): this;
    toRouter(): express.Router;
}