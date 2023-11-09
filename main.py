import mediapipe as mp
import cv2
import vlc
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import treshhold as ths

# camera you use
MAIN_CAMERA = 2
TRESHHOLD_TIME = 60
DOG_CLASS_NAME = 'dog'
PERSON_CLASS_NAME = 'person'
YELLING_MP3 = 'scream.mp3' #should be in the same folder

base_options = python.BaseOptions(model_asset_path='lite-model_efficientdet_lite0_detection_metadata_1.tflite')
options = vision.ObjectDetectorOptions(base_options=base_options,
                                       score_threshold=0.5)
detector = vision.ObjectDetector.create_from_options(options)


def make_recognition(detection_result):
    dog_detected = False
    person_detected = False
    for detection in detection_result.detections:
        if detection.categories[0].category_name == DOG_CLASS_NAME:
            dog_detected = True
        if detection.categories[0].category_name == PERSON_CLASS_NAME:
            person_detected = True

    if not person_detected and dog_detected and th.can_be_used():
        p.stop()
        p.play()


# audio file with your voice
p = vlc.MediaPlayer(YELLING_MP3)
th = ths.treshhold(TRESHHOLD_TIME) #uses treshhold not to spam with audio

if __name__ == '__main__':
    cap = cv2.VideoCapture(MAIN_CAMERA)
    while True:
        success, img = cap.read()

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=imgRGB)

        detection_result = detector.detect(mp_image)
        make_recognition(detection_result)

        cv2.imshow("Image", img)
        cv2.waitKey(1)
