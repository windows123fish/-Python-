# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['test.py'],
             pathex=['D:\\新建文件夹 (2)\\个人主页'],
             binaries=[],
             datas=[('yolov3-tiny.cfg', '.'), ('yolov3-tiny.weights', '.'), ('yolov3.cfg', '.'), ('yolov3.weights', '.'), ('coco.names', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='test',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
