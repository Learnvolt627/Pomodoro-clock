import time


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
    print("work session of 25 minutes")
    countdown(5)
    play_sound()

    print("short break of 5 minutes")
    countdown(5)
    play_sound()