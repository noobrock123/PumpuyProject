import os

class process_chooser():

    def yolo_v7(path, video_file):
        os.system(f"python3 ./yolo_v7/detect_and_track.py --source ../{path}")
        return 0