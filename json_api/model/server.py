from json_model import JsonModel
from .server_variables import ServerVariables

class Server(JsonModel):
    url = JsonModel.field(str)
    description = JsonModel.field(str)
    variables = JsonModel.dict(ServerVariables)


