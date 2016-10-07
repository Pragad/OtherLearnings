; IMPORTANT INFO ABOUT GETTING STARTED: Lines that start with a
; semicolon, such as this one, are comments.  They are not executed.

; This script has a special filename and path because it is automatically
; launched when you run the program directly.  Also, any text file whose
; name ends in .ahk is associated with the program, which means that it
; can be launched simply by double-clicking it.  You can have as many .ahk
; files as you want, located in any folder.  You can also run more than
; one .ahk file simultaneously and each will get its own tray icon.

; SAMPLE HOTKEYS: Below are two sample hotkeys.  The first is Win+Z and it
; launches a web site in the default browser.  The second is Control+Alt+N
; and it launches a new Notepad window (or activates an existing one).  To
; try out these hotkeys, run AutoHotkey again, which will load this file.
; #z::Run www.autohotkey.com

; Open Notepad when ctrl+alt+n
 ^!n::
IfWinExist Untitled - Notepad
	WinActivate
else
	Run Notepad
return

; MY KEYBOARD SHORTCUTS
*CapsLock::
    Send {Blind}{Ctrl Down}
    cDown := A_TickCount
Return

*CapsLock up::
    If ((A_TickCount-cDown)<200)  ; Modify press time as needed (milliseconds)
        Send {Blind}{Ctrl Up}{Esc}
    Else
        Send {Blind}{Ctrl Up}
Return

; Capslock::Ctrl
; LCtrl::Capslock
; `::Esc
Esc::Capslock

; Backspace not working while renaming a file
; Backspace behaves like Up as in WinXP
; Backspace::
; #IfWinActive, ahk_class CabinetWClass
;    ControlGet renamestatus,Visible,,Edit1,A
;    ControlGetFocus focussed, A
;   if(renamestatus!=1&&(focussed=”DirectUIHWND3″||focussed=SysTreeView321))
;   {
;    SendInput {Alt Down}{Up}{Alt Up}
;  }else{
;      Send {Backspace}
;  }
;#IfWinActive

; Convert Shift keys to type '(' and ')' when presseed separately.
; http://superuser.com/questions/579442/use-autohotkey-to-remap-the-left-shift-to-and-the-right-shift-to-but-i
LShift UP::Send, (
RShift UP::Send, )
LShift & F13::
RShift & F13::

; Correct shift keys
;http://superuser.com/questions/1131820/how-to-trigger-noop-for-key-combinations-in-autohotkey
; Disable left shift, left letter keys
LShift & q::return
LShift & w::return
LShift & e::return
LShift & r::return
LShift & t::return
LShift & a::return
LShift & s::return
LShift & d::return
LShift & f::return
LShift & g::return
LShift & z::return
LShift & x::return
LShift & c::return
LShift & v::return
LShift & b::return
LShift & 1::return
LShift & 2::return
LShift & 3::return
LShift & 4::return
LShift & 5::return
LShift & `::return

; Disable right shift, right letter keys
RShift & y::return
RShift & u::return
RShift & i::return
RShift & o::return
RShift & p::return
RShift & h::return
RShift & j::return
RShift & k::return
RShift & l::return
RShift & `;::return
RShift & n::return
RShift & m::return
RShift & ,::return
RShift & .::return
RShift & /::return
RShift & 6::return
RShift & 7::return
RShift & 8::return
RShift & 9::return
RShift & 0::return
RShift & -::return
RShift & =::return

; Correct Control keys
;http://superuser.com/questions/1131820/how-to-trigger-noop-for-key-combinations-in-autohotkey
; Disable left Control, left letter keys
LCtrl & q::return
LCtrl & w::return
LCtrl & e::return
LCtrl & r::return
LCtrl & t::return
LCtrl & a::return
LCtrl & s::return
LCtrl & d::return
LCtrl & f::return
LCtrl & g::return
LCtrl & z::return
LCtrl & x::return
LCtrl & c::return
LCtrl & v::return
LCtrl & b::return
LCtrl & 1::return
LCtrl & 2::return
LCtrl & 3::return
LCtrl & 4::return
LCtrl & 5::return
LCtrl & `::return

; Disable right Ctrl, right letter keys
RCtrl & y::return
RCtrl & u::return
RCtrl & i::return
RCtrl & o::return
RCtrl & p::return
RCtrl & h::return
RCtrl & j::return
RCtrl & k::return
RCtrl & l::return
RCtrl & `;::return
RCtrl & n::return
RCtrl & m::return
RCtrl & ,::return
RCtrl & .::return
RCtrl & /::return
RCtrl & 6::return
RCtrl & 7::return
RCtrl & 8::return
RCtrl & 9::return
RCtrl & 0::return
RCtrl & -::return
RCtrl & =::return

; Note: From now on whenever you run AutoHotkey directly, this script
; will be loaded.  So feel free to customize it to suit your needs.

; Please read the QUICK-START TUTORIAL near the top of the help file.
; It explains how to perform common automation tasks such as sending
; keystrokes and mouse clicks.  It also explains more about hotkeys.
