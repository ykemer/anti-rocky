import mediapipe as mp
import cv2
import vlc
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import treshhold as ths

# camera you use
MAIN_CAMERA = 2
TRESHHOLD_TIME = 60

base_options = python.BaseOptions(model_asset_path='lite-model_efficientdet_lite0_detection_metadata_1.tflite')
options = vision.ObjectDetectorOptions(base_options=base_options,
                                       score_threshold=0.5)
detector = vision.ObjectDetector.create_from_options(options)


def do_shit(detection_result):
    dog_found = False
    person_found = False
    for detection in detection_result.detections:
        print(detection.categories[0].category_name)

        if detection.categories[0].category_name == 'dog':
            dog_found = True
        if detection.categories[0].category_name == 'person':
            person_found = True

    if dog_found and not person_found and th.can_be_used():
        p.stop()
        p.play()


# audio file with your voice
p = vlc.MediaPlayer("scream.mp3")
th = ths.treshhold(TRESHHOLD_TIME)
if __name__ == '__main__':
    cap = cv2.VideoCapture(MAIN_CAMERA)
    while True:
        success, img = cap.read()

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=imgRGB)

        detection_result = detector.detect(mp_image)
        do_shit(detection_result)

        cv2.imshow("Image", img)
        cv2.waitKey(1)
