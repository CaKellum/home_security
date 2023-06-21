import cv2
from cv2 import VideoCapture, imshow, destroyAllWindows, waitKey
import typing
from numpy import ndarray

## builds frame named video that will display the computers the first default camera

def get_video_capture() -> VideoCapture:
    return cv2.VideoCapture(0)

def get_frame(video_capture: VideoCapture) -> ndarray:
    _, frame = video_capture.read()
    return frame


def start_camera(video_capture: VideoCapture, window_title: str = "Video") -> None:
    while True:
        frame = get_frame(video_capture)
        imshow(window_title, frame)
        if waitKey(1) & 0xFF == ord('q'):
            break

def main() -> None:
    video_feed = get_video_capture()
    start_camera(video_capture=video_feed)
    video_feed.release()
    destroyAllWindows()


if __name__ == "__main__":
    main()