from fastapi import FastAPI, HTTPException, status
from fastapi.responses import FileResponse

from schemas import SnapshotRequestSchema
from utils import capture_frame_from_rtsp

app = FastAPI()


@app.get("/")
def root():
    return {"ping": "pong"}


@app.post(
    "/snap",
    response_class=FileResponse,
    status_code=status.HTTP_200_OK,
    summary="Get a snapshot",
)
def snapshot(snapshot_request: SnapshotRequestSchema):
    image_path = "snapshot.jpg"
    success = capture_frame_from_rtsp(
        f"rtsp://{snapshot_request.username}:{snapshot_request.password}@{snapshot_request.host}:{snapshot_request.port}{snapshot_request.path}",
        image_path,
    )
    if success:
        return FileResponse(image_path)
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
