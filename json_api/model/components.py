from json_model import JsonModel
from .schema import Schema
from .response import Response
from .parameter import Parameter
from .example import Example
from .request_body import RequestBody
from .header import Header
from .security_scheme import SecurityScheme
from .link import Link
from .callback import Callback
from .refernce import Reference

class Components(JsonModel):
    schemas = JsonModel.dict(oneOf=[Schema, Reference])
    responses = JsonModel.dict(oneOf=[Response, Reference])
    parameters = JsonModel.dict(oneOf=[Parameter, Reference])
    examples = JsonModel.dict(oneOf=[Example, Reference])
    requestBodies = JsonModel.dict(oneOf=[RequestBody, Reference])
    headers = JsonModel.dict(oneOf=[Header, Reference])
    securitySchemes = JsonModel.dict(oneOf=[SecurityScheme, Reference])
    links = JsonModel.dict(oneOf=[Link, Reference])
    callbacks = JsonModel.dict(oneOf=[Callback, Reference])


