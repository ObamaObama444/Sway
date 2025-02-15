
import cv2
from flask import Flask, render_template, Response
from ultralytics import YOLO

app = Flask(__name__)

# Загрузка модели YOLOv8. Укажите корректный путь к вашей модели.
model = YOLO("yolov8m.pt")

def skolko_kamer(max_index=10):
    cams = []
    for i in range(max_index):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            cams.append(i)
            cap.release()
    return cams

def SHISHKA(cam_index):
    cap = cv2.VideoCapture(cam_index)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

    
        try:
            results = model(frame, verbose=False)
            annotated_frame = results[0].plot()  
        except Exception as e:
            print(f"Ошибка на камере {cam_index}: {e}")
            annotated_frame = frame

        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        if not ret:
            continue
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    cap.release()
    

@app.route('/')
def index():
    cameras = skolko_kamer()
    return render_template('index.html', cameras=cameras)

@app.route('/video_feed/<int:cam_id>')
def video_feed(cam_id):
    return Response(SHISHKA(cam_id),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)


'''

import cv2
from flask import Flask, render_template, Response
from ultralytics import YOLO

app = Flask(__name__)

model = YOLO("yolov8m.pt")

def get_cameras():
    cams = []
    for i in range(3):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            cams.append(i)
            cap.release()
    return cams

def generate_frames(cam_index):
    cap = cv2.VideoCapture(cam_index)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            results = model(frame, verbose=False)
            annotated_frame = results[0].plot()
        except Exception as e:
            print(f"Ошибка на камере {cam_index}: {e}")
            annotated_frame = frame

        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        if not ret:
            continue
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    cameras = get_cameras()
    return render_template('index.html', cameras=cameras)

@app.route('/video_feed/<int:cam_id>')
def video_feed(cam_id):
    return Response(generate_frames(cam_id),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
    ''''''import cv2
from flask import Flask, render_template, Response
from ultralytics import YOLO

app = Flask(__name__)

# Загрузка модели YOLOv8. Укажите корректный путь к вашей модели.
model = YOLO("yolov8m.pt")

def get_cameras(max_index=3):
    """Простая функция для обнаружения доступных камер с индексами от 0 до max_index-1."""
    cams = []
    for i in range(max_index):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            cams.append(i)
            cap.release()
    return cams

def generate_video(cam_index):
    """Генератор, который захватывает кадры, выполняет детекцию и возвращает их в формате видео."""
    cap = cv2.VideoCapture(cam_index)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Выполнение детекции с использованием YOLOv8
        try:
            results = model(frame, verbose=False)
            annotated_frame = results[0].plot()  # получение аннотированного кадра
        except Exception as e:
            print(f"Ошибка на камере {cam_index}: {e}")
            annotated_frame = frame

        # Отображение результата
        ##cv2.imshow('Output', annotated_frame)

        # Кодирование кадра в формат видео
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        if not ret:
            continue
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

@app.route('/')
def index():
    cameras = get_cameras()
    return render_template('index.html', cameras=cameras)

@app.route('/video_feed/<int:cam_id>')
def video_feed(cam_id):
    return Response(generate_video(cam_id),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)'''



























