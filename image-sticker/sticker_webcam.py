import dlib
import cv2
import numpy as np


face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
video_capture = cv2.VideoCapture(0)

DEBUG = True

try:
    while True:
        # capture frame-by-frame
        _, frame = video_capture.read()
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image_height, image_width = frame.shape[:2]
        face_rects = face_detector(image_rgb, 1)
        face_landmarks = [landmark_predictor(image_rgb, rect) for rect in face_rects]

        if DEBUG:
            if face_rects:
                print("Face detected!!")
            else:
                print("Face not detected..")

        for rect, landmark in zip(face_rects, face_landmarks):
            # 1. 얼굴 크기에 맞게 스티커 이미지를 resize
            face_width = rect.width()
            face_height = rect.height()
            sticker_image = cv2.imread("images/sticker.png")
            resized_sticker_width = min(face_width, face_height)
            sticker_image = cv2.resize(sticker_image, (resized_sticker_width, resized_sticker_width))

            # 2. 코 위치에 스티커 위치를 올긴다
            sticker_image_height, sticker_image_width = sticker_image.shape[:2]
            nose_point = landmark.part(33) # 코 위치 (참고: face_landmark.png)
            sticker_image_x = nose_point.x - sticker_image_width // 2
            sticker_image_y = nose_point.y - sticker_image_height // 2

            # 3. 스티커 그리기
            # 스티커 위쪽이 벗어나는 경우
            if sticker_image_y < 0:
                sticker_image = sticker_image[-sticker_image_y:, :]
                sticker_image_y = 0

            # 스티커 아래가 벗어나는 경우
            sticker_image_y_to = sticker_image_y + sticker_image.shape[0]
            if image_height < sticker_image_y_to:
                sticker_image = sticker_image[:image_height - sticker_image_y, :]
                sticker_image_y_to = image_height

            # 스티커 왼쪽이 벗어나는 경우
            if sticker_image_x < 0:
                sticker_image = sticker_image[:, -sticker_image_x:]
                sticker_image_x = 0

            # 스티커 오른쪽이 벗어나는 경우
            sticker_image_x_to = sticker_image_x + sticker_image.shape[1]
            if image_width < sticker_image_x_to:
                sticker_image = sticker_image[:, :image_width - sticker_image_x]
                sticker_image_x_to = image_width

            mask_area = frame[
                sticker_image_y:sticker_image_y_to,
                sticker_image_x:sticker_image_x_to
            ]
            sticker_mask = np.where(sticker_image == 255, mask_area, sticker_image).astype(np.uint8)

            frame[
                sticker_image_y:sticker_image_y+sticker_image_height,
                sticker_image_x:sticker_image_x+sticker_image_width
            ] = sticker_mask

            if DEBUG:
                cv2.rectangle(frame, (rect.left(),rect.top()), (rect.right(),rect.bottom()), (0,255,0), 2, lineType=cv2.LINE_AA) # 시작점의 좌표와 종료점 좌표로 직각 사각형을 그림
                cv2.circle(frame, (nose_point.x, nose_point.y), 2, (0, 255, 0), -1) # 코의 위치
                cv2.circle(frame, (sticker_image_x, sticker_image_y), 2, (255, 0, 0), -1)

        cv2.imshow("Video", frame)

        # quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    # release resources
    video_capture.release()
    cv2.destroyAllWindows()
