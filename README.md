# 哈希计算器

*粗略搜了下，GitHub似乎没有比较趁手的MD5以及SHA的图形化计算工具，顺手做了一个。*

## 1. 使用方法

![image](https://user-images.githubusercontent.com/48341563/189543307-8702fe2f-81bf-42f7-893e-41916ff37219.png)

如图，选择一个文件，选择摘要算法，点计算输出结果，会自动复制到剪贴板，有需要直接黏贴就行。

## 2. 环境配置

推荐使用PyCharm或者虚拟环境，隔离其他已安装的第三方库，避免打包体积过大。

仅依赖第三方库`PySide6`，安装如下：

```shell
pip install PySide6
```

然后运行就可以看到窗口了。

## 3. 打包

- `pyinstaller`
    - 安装：
      ```shell
      pip install pyinstaller
      ```

    - 打包：
      ```shell
      pyinstaller --clean -F main.py -w -i logo.ico -n HashCalculator
      ```

- `nuitka`
  - 安装：
    ```shell
    pip install nuitka
    pip install zstandard
    ```
    
  - 打包：
    ```shell
    ./build.sh
    ```