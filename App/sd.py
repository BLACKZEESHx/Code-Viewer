import win32gui
import win32con, time
time.sleep(2)

def change_window_border(hwnd):
    # Adjust the extended window style to enable window shadow and rounded corners
    win32gui.SetWindowPos(hwnd, None, 12, 12, 188, 288, win32con.SW_SHOW)
def main():
    # Get the handle of the current window
    hwnd = win32gui.GetForegroundWindow()

    # Change the window border
    change_window_border(hwnd)

if __name__ == "__main__":
    main()
