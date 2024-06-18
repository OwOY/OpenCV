import cv2
from threading import Thread


stream_dict = {}

# 製作一個thread來讀取影像
class VideoThread(Thread):
    def __init__(self, camera_id, source):
        Thread.__init__(self)
        self.camera_id = camera_id
        self.source = source
        self._stop = False

    def run(self):
        cap = cv2.VideoCapture(self.source)
        while True:
            if self._stop:
                break
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (720, 480))
            _, img_encoded = cv2.imencode('.jpg', frame)
            stream_dict[self.camera_id] = (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + img_encoded.tobytes() + b'\r\n'
            )
        cap.release()
    
    def stop(self):
        self._stop = True
        del stream_dict[self.camera_id]
        
def get_stream(camera_id):
    while True:
        yield stream_dict.get(camera_id)