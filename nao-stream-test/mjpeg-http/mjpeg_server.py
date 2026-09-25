from flask import Flask, Response
import cv2

app = Flask(__name__)

camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = camera.read()

        if not success:
            break

        # Compression JPEG
        success, buffer = cv2.imencode(
            ".jpg",
            frame,
            [int(cv2.IMWRITE_JPEG_QUALITY), 80]
        )

        if not success:
            continue

        frame_bytes = buffer.tobytes()

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" +
            frame_bytes +
            b"\r\n"
        )

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NAO Stream Test</title>
    </head>

    <body style="
        margin:0;
        background:black;
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
    ">
        <img
            src="/video"
            style="
                max-width:100%;
                max-height:100%;
                object-fit:contain;
            "
        >
    </body>
    </html>
    """

@app.route("/video")
def video():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )

if __name__ == "__main__":
    print("Serveur lancé.")
    print("Sur le PC : http://127.0.0.1:5000")
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        threaded=True
    )