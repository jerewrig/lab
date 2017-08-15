import subprocess
import webbrowser
import sys

url = 'https://www.youtube.com/watch?v=MMh8V04s7Ts'
if sys.platform == 'darwin':    # in case of OS X
    subprocess.Popen(['open', url])
else:
    webbrowser.open_new_tab(url)