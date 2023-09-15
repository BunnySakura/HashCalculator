#!/usr/bin/bash
echo "执行 Nuitka 打包……"
python -m nuitka                  \
--standalone                      \
--show-memory                     \
--show-progress                   \
--follow-import-to=need           \
--enable-plugin=pyside6           \
--output-dir=output               \
--windows-icon-from-ico=logo.ico  \
--lto=yes                         \
--onefile main.py
echo "打包完毕。"