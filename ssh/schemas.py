from pydantic import BaseModel

class RemoteClientSchema(BaseModel):
    host: str
    user: str
    password: str
    ssh_key_filepath: str
    commands: list