# Flock
A small tool to automatically set current time on a computer.

Set the Windows system's time to the current real-time using NTP service from [time.google.com](https://developers.google.com/time) and have the option to set it every time the system booted up.

This will come in handy when the CMOS battery is dead and you're lazy or don't know how to change the battery.

## Download
You can download the built version in [releases](https://github.com/Neurs12/Flock/releases), or clone it and build one for yourself!

## Build
- Clone the repo.
- Open termial in the cloned folder and run:
```
pip install -r requirements.txt
```
- Convert `flock_silent.py` to executable file using pyinstaller, requires:
  - `onefile` flag.
  - `windowed` flag.
  - `uac-admin` flag.

Example:
```
pyinstaller --noconfirm --onefile --windowed --uac-admin  "flock_silent.py"
```

- Convert `Flock.py` to executable file using pyinstaller, requires:
  - `onedir` flag.
  - `windowed` flag.
  - `uac-admin` flag.
  - `add-data` flag:
    - `sv_ttk` folder
    - `flock_silent.exe`

Example:
```
pyinstaller --noconfirm --onedir --windowed --uac-admin --add-data "flock_silent.exe;." --add-data "sv_ttk;sv_ttk/"  "Flock.py"
```
