app_config = {
    "API_TITLE": "Backend Expense App",
    "API_VERSION": "V1",
    "OPENAPI_VERSION": "3.0.2"
}
swagger_config = {
    "OPENAPI_JSON_PATH": "api-spec.json",
    "OPENAPI_URL_PREFIX": "/",
    "OPENAPI_REDOC_PATH": "/redoc",
    "OPENAPI_REDOC_URL": (
        "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    ),
    "OPENAPI_SWAGGER_UI_PATH": "/swagger-ui",
    "OPENAPI_SWAGGER_UI_URL": "https://cdn.jsdelivr.net/npm/swagger-ui-dist/",
    "OPENAPI_RAPIDOC_PATH": "/rapidoc",
    "OPENAPI_RAPIDOC_URL": "https://unpkg.com/rapidoc/dist/rapidoc-min.js"
}


def initialize_app(app):
    app.config.from_mapping({**app_config, **swagger_config})
