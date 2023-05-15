import os
import subprocess
# from .yolo_v7.detect_and_track import yolo_detect_and_track

class process_chooser():

    def yolo_v7(self, video_id, video_path, hitbox_name, hitbox_id):
        intersection_name = video_path.split("/")
        detect_func = './BaseApp/modules/yolo_v7/detect_and_track.py'
        if hitbox_name is not None:
            loopfile = f'./BaseApp/intersectionData/{intersection_name[0]}/loops/{hitbox_id}/{hitbox_name}.json'
        else:
            loopfile = f'./BaseApp/modules/yolo_v7/loop.json'
        vdofile = f'./BaseApp/intersectionData/{video_path}'
        project_path = f'./BaseApp/intersectionData/{intersection_name[0]}/detect'
        
        os.system(f"python {detect_func} --source {vdofile} --loop {loopfile} --project {project_path} --name {video_id}")
        # celery -A PumpuyProject worker --loglevel=info -P eventlet
        return "finish"
