# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# 使用PyInstaller的API来收集numpy和cv2的所有模块和数据文件
from PyInstaller.utils.hooks import collect_all, collect_submodules

# 收集numpy的所有模块和数据文件
numpy_pkgs, numpy_datas, numpy_binaries = collect_all('numpy')

# 收集cv2的所有模块和数据文件
cv2_pkgs, cv2_datas, cv2_binaries = collect_all('cv2')

# 添加隐藏的导入以确保所有依赖项都被包含
hidden_imports = numpy_pkgs + cv2_pkgs + [
    'PIL',
    'PIL._imagingtk',
    'PIL._tkinter_finder',
    'ctypes',
    'webbrowser',
    'pkg_resources',
    'pkg_resources.extern',
    'pkg_resources.extern.six',
    'pkg_resources.extern.six.moves',
    'pkg_resources.extern.packaging',
    'pkg_resources.extern.appdirs',
    'pkg_resources.py2_warn',
    'pyimod03_importers',
    'setuptools',
    'setuptools.extern',
    'setuptools.extern.six',
    'setuptools.extern.six.moves'
]

a = Analysis(['main.py'],
             pathex=[
                 'D:\\新建文件夹 (2)\\个人主页',
                 'C:\\Users\\祝\\AppData\\Roaming\\Python\\Python313\\site-packages'
             ],
             binaries=numpy_binaries + cv2_binaries,
             datas=[
                 ('yolov3.cfg', '.'),
                 ('yolov3.weights', '.'),
                 ('coco.names', '.'),
                 ('yolov3-tiny.cfg', '.'),
                 ('yolov3-tiny.weights', '.')
             ] + numpy_datas + cv2_datas,
             hiddenimports=hidden_imports,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
# 创建无控制台的窗口应用
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='摄像头检测系统',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,  # 暂时启用控制台以便查看错误信息
          icon=None)  # 可以在这里添加图标文件路径