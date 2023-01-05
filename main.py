from fastapi import FastAPI, HTTPException
from ssh.models import RemoteClient
from ssh.schemas import RemoteClientSchema
import uvicorn

app = FastAPI()

@app.post("/execute-commands")
async def execute_commands(RemoteClientSchema: RemoteClientSchema):
    client = RemoteClient(RemoteClientSchema.host, RemoteClientSchema.user, RemoteClientSchema.password, RemoteClientSchema.ssh_key_filepath)
    try:
        client.execute_commands(RemoteClientSchema.commands)
        return {"status": "success"}    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))   

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True, log_level="debug")