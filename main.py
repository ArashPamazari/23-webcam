import cv2
import cvzone

class EffectType:
    NONE = 0
    FACE_EMOJI = 1
    LIP_EYE_EMOJI = 2
    CHECKERED_FACE = 3
    ROTATE_FACE = 4

class FaceEffects:
    def __init__(self):
        self.face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.eye_detector = cv2.CascadeClassifier('haarcascade_eye.xml')
        self.lip_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

        self.face_sticker = cv2.imread('face.png', cv2.IMREAD_UNCHANGED)
        self.eye_sticker = cv2.imread('eye.png', cv2.IMREAD_UNCHANGED)
        self.smile_sticker = cv2.imread('lip.png', cv2.IMREAD_UNCHANGED)

    def apply_face_emoji(self, frame):
        faces = self.face_detector.detectMultiScale(frame, 1.3, minSize=(50, 50))
        for (x, y, w, h) in faces:
            face_sticker_resize = cv2.resize(self.face_sticker, (w, h))
            frame = cvzone.overlayPNG(frame, face_sticker_resize, [x, y])
        return frame

    def apply_lip_eye_emoji(self, frame):
        eyes = self.eye_detector.detectMultiScale(frame, 1.3, minNeighbors=15)
        for (x, y, w, h) in eyes:
            eye_sticker_resize = cv2.resize(self.eye_sticker, (w, h))
            frame = cvzone.overlayPNG(frame, eye_sticker_resize, [x, y])

        lip = self.lip_detector.detectMultiScale(frame, 1.3, minNeighbors=20)
        for (x, y, w, h) in lip:
            smile_sticker_resized = cv2.resize(self.smile_sticker, (w, h))
            frame = cvzone.overlayPNG(frame, smile_sticker_resized, [x, y])

        return frame

    def apply_checkered_face(self, frame):
        faces = self.face_detector.detectMultiScale(frame, 1.3, minSize=(100, 100))
        for (x, y, w, h) in faces:
            checkered = cv2.resize(frame[y:y+h, x:x+w], (20, 20))
            result = cv2.resize(checkered, (w, h), interpolation=cv2.INTER_NEAREST)
            frame[y:y+h, x:x+w] = result
        return frame

    def apply_rotate_face(self, frame):
        faces = self.face_detector.detectMultiScale(frame, 1.3, minSize=(100, 100))
        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            frame[y:y+h, x:x+w] = cv2.flip(face, 0)
        return frame

def main():
    video_capture = cv2.VideoCapture(0)
    face_effects = FaceEffects()
    effect_type = EffectType.NONE

    while True:
        ret, frame = video_capture.read()

        if not ret:
            break

        frame = cv2.resize(frame, (650, 500))

        key = cv2.waitKey(1)
        if key == ord('5'):
            break
        elif key == ord('1'):
            effect_type = EffectType.FACE_EMOJI
        elif key == ord('2'):
            effect_type = EffectType.LIP_EYE_EMOJI
        elif key == ord('3'):
            effect_type = EffectType.CHECKERED_FACE
        elif key == ord('4'):
            effect_type = EffectType.ROTATE_FACE

        if effect_type == EffectType.FACE_EMOJI:
            frame = face_effects.apply_face_emoji(frame)
        elif effect_type == EffectType.LIP_EYE_EMOJI:
            frame = face_effects.apply_lip_eye_emoji(frame)
        elif effect_type == EffectType.CHECKERED_FACE:
            frame = face_effects.apply_checkered_face(frame)
        elif effect_type == EffectType.ROTATE_FACE:
            frame = face_effects.apply_rotate_face(frame)

        cv2.imshow('output', frame)

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
