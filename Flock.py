import subprocess, sv_ttk, os
from tkinter import *
from tkinter.ttk import *

def setTime():
    subprocess.run("flock_silent", creationflags=subprocess.CREATE_NO_WINDOW)

auto_start_state = False

flock_auto = """<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.4" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Author>Flock Time Updater</Author>
    <URI>\Flock Auto</URI>
  </RegistrationInfo>
  <Triggers>
    <LogonTrigger>
      <Enabled>true</Enabled>
    </LogonTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>S-1-5-18</UserId>
      <RunLevel>HighestAvailable</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>false</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>true</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <DisallowStartOnRemoteAppSession>false</DisallowStartOnRemoteAppSession>
    <UseUnifiedSchedulingEngine>true</UseUnifiedSchedulingEngine>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT72H</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>"FLOCK_SILENT_EXECUTABLE"</Command>
    </Exec>
  </Actions>
</Task>"""

def main():
    global auto_start_state
    auto_start_state = subprocess.run(["SchTasks", "/query", "/tn", "Flock Auto"], stdout=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW).stdout.decode() != ""
    def toggleStartUp():
        global auto_start_state
        if auto_start_state:
            subprocess.run(["SchTasks", "/delete", "/tn", "Flock Auto", "/f"], creationflags=subprocess.CREATE_NO_WINDOW)
            auto_start_state = False
        else:
            with open("flock_auto.xml", "w+") as fd:
                fd.write(flock_auto.replace("FLOCK_SILENT_EXECUTABLE", os.getcwd()+"\\flock_silent.exe"))
            auto_start_state = "SUCCESS: The scheduled task \"Flock Auto\" has successfully been created." in subprocess.run(["SchTasks", "/create", "/xml", "flock_auto.xml", "/tn", "Flock Auto"], stdout=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW).stdout.decode()

    root = Tk()
    root.title("Flock Time Updater")
    root.resizable(False, False)
    root.attributes("-topmost", True)
    root.wm_attributes("-toolwindow", True)

    window_height = 75
    window_width = 350

    x_cordinate = root.winfo_screenwidth() // 2 - window_width // 2
    y_cordinate = root.winfo_screenheight() // 2 - window_height // 2 - 50

    root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    sv_ttk.set_theme("dark")

    autoStartToggle = Checkbutton(root, text="Tự động đặt giờ khi khởi động máy", style="Switch.TCheckbutton", command=toggleStartUp)
    if auto_start_state: autoStartToggle.state(["selected"])
    autoStartToggle.pack()

    confirm = Button(root, style="Accent.TButton", text="Đặt lại đồng hồ", command=setTime)
    confirm.pack(pady=4)

    root.mainloop()

if __name__ == "__main__":
    main()