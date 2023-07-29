from pydantic import BaseModel


class SnapshotRequestSchema(BaseModel):
    username: str
    password: str
    host: str
    port: int
    path: str
