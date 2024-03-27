from ninja.openapi.docs import DocsBase, Swagger, Redoc


class MixedDocs(DocsBase):
    def __init__(self) -> None:
        super().__init__()
        self.swagger = Swagger()
        self.redoc = Redoc(settings={"disableSearch": True, "hideDownloadButton": True})

    def render_page(self, request, api, **kwargs):
        engine_name = kwargs.pop("engine")
        engine = {
            "swagger": self.swagger,
            "redoc": self.redoc,
        }.get(engine_name)
        return engine.render_page(request, api, **kwargs)
