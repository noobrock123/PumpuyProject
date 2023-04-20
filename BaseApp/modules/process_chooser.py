import os
import subprocess

class process_chooser:

    def yolo_v7(path, video_file):
        print('------------------------------')
        print(path)
        print(video_file)
        print('------------------------------')
        # os.system(f"python3 BaseApp/modules/yolo_v7/detect_and_track.py --source BaseApp/{video_file} --loop BaseApp/modules/yolo_v7/loop.json")
        return 0