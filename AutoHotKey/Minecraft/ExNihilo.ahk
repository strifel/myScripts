#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
SetCapsLockState, alwaysoff
CapsLock & y::Click % "right " (GetKeyState("RButton") ? "Up" : "Down")
CapsLock & x::
  Loop
  { sleep 200
    Send {1}
    Click, R
    sleep 300
    Send {2}
    Click Down
    Sleep 500 ; Change to 900 for Cobblestone with Stone Hammer
    Click Up
    If (GetKeyState("RButton","p"))
      break
  }
  Return
