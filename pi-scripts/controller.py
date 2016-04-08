import sys
import time
sys.path.append('lib/')

from myo import Myo
from camera import Camera
from pibot import Bot
from print_pose_listener import PrintPoseListener
from vibration_type import VibrationType

def main():
    print('Start Myo for Linux')

    listener = PrintPoseListener()
    myo = Myo()
    
    try:
        myo.connect()
        myo.add_listener(listener)
        myo.vibrate(VibrationType.SHORT)
        while True:
            myo.run()
            print(listener.getPose())
            time.sleep(2)
            

    except KeyboardInterrupt:
        pass
    except ValueError as ex:
        print(ex)
    finally:
        myo.safely_disconnect()
        print('Finished.')

if __name__ == '__main__':
    main()
