<p align="center">
    <img src="img/logo.png" width='300px'>
</p>

# How to use  

## 影像處理
- 影像串流串接
    ```python
    import cv2


    def run(self, source):
        cap = cv2.VideoCapture(source) # 可為RTSP網址或影像檔路徑
        while True:
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
    ```
- 若串流影像速度慢，有以下幾種方式處理
    1. 壓縮影像，將串流影像resize  
        sample:
        ```python
        frame = cv2.resize(frame, (720, 480))
        ```
    2. 使用多線程序處理串流影像(丟幀處理)
        參閱[Sample](sample/service.py)