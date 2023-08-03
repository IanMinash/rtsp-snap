# RTSP Capture
This is a simple webservice that captures a snapshot from an RTSP stream and returns the image in a HTTP response.

The service has the following endpoint:

- `[POST] /snap`

    Get a snapshot from an RTSP stream

    Request body
    ```json
    {
    "username": "string", // Username of account authorized to view the RTSP stream
    "password": "string", // Password of account authorized to view the RTSP stream
    "host": "string", // Host of the RTSP stream
    "port": 0, // Port number of the RTSP stream
    "path": "string" // Path to access the RTSP stream
    }
    ```

    If the snapshot was captured successfuly, the service will respond with the image in the response body.


## Running it
You can quickly bring up an instance of the service using docker.
1. Pull the image:
    ```shell
    docker pull mnsh25/rtsp-snap:latest
    ```

2. Run it:
    ```shell
    docker run -p <host_port>:8000 mnsh25/rtsp-snap
    ```
    You can now access it on `localhost:<host_port>`