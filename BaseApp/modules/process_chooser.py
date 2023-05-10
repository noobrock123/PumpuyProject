import os
import subprocess
# from .yolo_v7.detect_and_track import yolo_detect_and_track

class process_chooser():

    def yolo_v7(self, video_id, video_path):
        intersection_name = video_path.split("/")
        detect_func = './BaseApp/modules/yolo_v7/detect_and_track.py'
        loopfile = './BaseApp/modules/yolo_v7/loop.json'
        vdofile = f'./BaseApp/intersectionData/{video_path}'
        project_path = f'./BaseApp/intersectionData/{intersection_name[0]}/detect/{video_id}'
        # yolo_detect_and_track(cmd=False,custom_arg=['--loop',loopfile,'--source',vdofile])
        os.system(f"python {detect_func} --source {vdofile} --loop {loopfile} --project {project_path} --name video{video_id}")
        # ./BaseApp/intersectionData/1/videos/video2.mp4
        # python ./BaseApp/modules/yolo_v7/detect_and_track.py --source ./BaseApp/intersectionData/1/videos/video2.mp4 --loop ./BaseApp/modules/yolo_v7/loop.json
        # celery -A PumpuyProject worker --loglevel=info -P eventlet
        return "finish"
