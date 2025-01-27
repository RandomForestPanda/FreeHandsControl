import subprocess

def SetMasterVolume(volume):

    subprocess.run(['osascript', '-e', f'set volume output volume {volume}'])


# SetMasterVolume(8)
