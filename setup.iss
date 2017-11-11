; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "LoL Rune Manager"
#define MyAppVersion "1.1"
#define MyAppPublisher "Wazzaps"
#define MyAppURL "https://github.com/Wazzaps/LoLRuneManager"
#define MyAppExeName "import.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{BDAD0B76-BCA3-4324-92E7-B29FD946D9AE}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={userappdata}\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
OutputBaseFilename=lolrunemanager_setup
Compression=lzma
SolidCompression=yes
InfoAfterFile=README - instructions.txt

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\import.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\api-ms-win-crt-convert-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\api-ms-win-crt-environment-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\api-ms-win-crt-filesystem-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\api-ms-win-crt-heap-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\api-ms-win-crt-locale-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\api-ms-win-crt-math-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\api-ms-win-crt-runtime-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\api-ms-win-crt-stdio-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\api-ms-win-crt-string-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\api-ms-win-crt-time-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\api-ms-win-crt-utility-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\editbtn.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\editbtn_large.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\Example page 1.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\Example page 2.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\export.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\mfc140u.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\pathmask.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\python3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\python36.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\pythoncom36.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\pywintypes36.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\README - instructions.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\runemask.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\VCRUNTIME140.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\David\PycharmProjects\runes\build\exe.win32-3.6\lib\*"; DestDir: "{app}\lib"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\Rune Importer"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\Rune Exporter"; Filename: "{app}\{#MyAppExeName}"

[Registry]
Root: HKCR; Subkey: "runeimport"; ValueType: "string"; ValueData: "URL:runeimport Protocol"; Flags: uninsdeletekey
Root: HKCR; Subkey: "runeimport"; ValueType: "string"; ValueName: "URL Protocol"; ValueData: ""
Root: HKCR; Subkey: "runeimport\DefaultIcon"; ValueType: "string"; ValueData: "{app}\import.exe,0"
Root: HKCR; Subkey: "runeimport\shell\open\command"; ValueType: "string"; ValueData: "cmd /c start /D ""{app}"" import.exe ""%1"""

