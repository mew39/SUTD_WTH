import vlc
from time import sleep

# Play soothing video
# creating vlc media player object
# media_player = vlc.MediaPlayer()
 
# media object
video = vlc.MediaPlayer("loop.mp4")  
 
# playing video  
video.play()  

sleep(5) # Or however long you expect it to take to open vlc
while video.is_playing():
     sleep(1)