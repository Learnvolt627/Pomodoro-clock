import time
import ctypes

def prevent_sleep():
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001
    ES_DISPLAY_REQUIRED = 0x00000002

    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)

def play_sound():
    import winsound
    winsound.PlaySound("C:\\Users\\ys47r\\OneDrive\\Desktop\\All Visual Studio Code\\pomodoro_clock\\sample.wav", winsound.SND_FILENAME)
    
        
    

def countdown(seconds):
    while seconds>0:
        mins, secs=divmod(seconds,60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds-=1
    print("00:00\nTime's up!")
    

if __name__ == "__main__":
    prevent_sleep()
    print("work session of 25 minutes")
    countdown(60)
    play_sound()

    print("short break of 5 minutes")
    countdown(60)
    play_sound()
    print("pomodoro session complete!")
    