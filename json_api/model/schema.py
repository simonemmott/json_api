from json_model import JsonModel
from .xml import Xml
from .external_docs import ExternalDocs

class Schema(JsonModel):
    id = JsonModel.field(str)
    title = JsonModel.field(str)
    multipleOf = JsonModel.field(int)
    maximum = JsonModel.field(int)
    exclusiveMaximum = JsonModel.field(int)
    minimum = JsonModel.field(int)
    exclusiveMinimum = JsonModel.field(int)
    maxLength = JsonModel.field(int)
    minLength = JsonModel.field(int)
    pattern = JsonModel.field(str)
    maxItems = JsonModel.field(int)
    minItems = JsonModel.field(int)
    uniqueItems = JsonModel.field(bool)
    maxProperties = JsonModel.field(int)
    minPropoerties = JsonModel.field(int)
    required = JsonModel.list(str)
    enum = JsonModel.list(str)
    allOf = JsonModel.list('json_api.model.Schema')
    anyOf = JsonModel.list('json_api.model.Schema')
    oneOf = JsonModel.list('json_api.model.Schema')
    _not = JsonModel.list('json_api.model.Schema', 'not')
    items = JsonModel.field('json_api.model.Schema')
    properties = JsonModel.dict('json_api.model.Schema')
    additionalProperties = JsonModel.dict('json_api.model.Schema')
    description = JsonModel.field(str)
    format = JsonModel.field(str)
    nullable = JsonModel.field(bool)
    readOnly = JsonModel.field(bool)
    writeOnly = JsonModel.field(bool)
    xml = JsonModel.field(Xml)
    externalDocs = JsonModel.field(ExternalDocs)
    deprecated = JsonModel.field(bool)
    
    


