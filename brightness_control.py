# Import the `get_brightness` & `set_brightness` functions from the `screen_brightness_control` module
from screen_brightness_control import set_brightness
import serial
import time
from playsound import playsound
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import vlc

def calmDownSounds():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume.SetMute(1, None)

        """
        if session.Process and session.Process.name() == "chrome.exe":
            volume.SetMute(1, None)
        else:
            volume.SetMute(0, None)
            playsound("brownnoise.wav")
        """

def soundOn():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume.SetMute(0, None)

# new brightness level for screen
new_brightness = 0

try:
    # make sure the 'COM#' is set according the Windows Device Manager
    ser = serial.Serial('COM4', 115200, timeout=1)
    time.sleep(2)
    while True:
            lines = ser.readline().strip()
            readable = lines.decode()
            print(readable)
            if readable == "1":
                 # replace this value with the desired brightness level
                set_brightness(new_brightness)
                calmDownSounds()
                
                # Play soothing video
                video = vlc.MediaPlayer("loop.mp4")  
 
                # playing video  
                video.play()  

                time.sleep(3) # Or however long you expect it to take to open vlc
                while video.is_playing():
                    time.sleep(10)
                video.stop()

            elif readable == "0":
                print("no issues")
                soundOn()
                pass
                
except:
    serial.Serial("COM4", 115200).close()
    print("ERROR")
    print("check port")

print("broken")
