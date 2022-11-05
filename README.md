# kivygui

Get-ExecutionPolicy

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force


# kivy pycharm

https://github.com/kivy/kivy/wiki/Setting-Up-Kivy-with-various-popular-IDE's


# pyinstaller

```
pyinstaller calc.py -w
```

### update spec file
```
from kivy_deps import sdl2, glew

# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['calc.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

a.datas += [('Code\calc.kv',
'I:\\Tanulas\\PycharmProjects\\kivygui\\exp\\calc\calc.kv',
'DATA')]

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='calc',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    Tree('I:\\Tanulas\\PycharmProjects\\kivygui\\exp\\calc'),
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='calc',
)
```


```
pyinstaller calc.spec -y
```


