import os
import subprocess
from ..models import Video

class process_chooser():

    def yolo_v7(path, video_file: Video):
        print('------------------------------')
        print(video_file.video_file.name)
        print('------------------------------')
        os.system(f"python3 BaseApp/modules/yolo_v7/detect_and_track.py --source {video_file.video_file.name} --loop BaseApp/modules/yolo_v7/loop.json")

        return 0