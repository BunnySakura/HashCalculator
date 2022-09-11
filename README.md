# 哈希计算器
*粗略搜了下，GitHub似乎没有比较趁手的MD5以及SHA的图形化计算工具，顺手做了一个。这是C++使用wxWidgets框架写的。*

## 1. 环境配置  
  参考《[C++开源库 - 包管理工具Vcpkg安装使用教程](https://www.cnblogs.com/linuxAndMcu/p/14696542.html "C++开源库 - 包管理工具Vcpkg安装使用教程")》安装`vcpkg`，并执行以下命令安装所需库的**静态库**：
  ```bash
  .\vcpkg.exe install wxwidgets:x64-windows-static
  .\vcpkg.exe install openssl:x64-windows-static
  ```

  如果还存在环境问题就执行：
  ```bash
  .\vcpkg.exe integrate install
  ```

  使用**VS2022**打开项目文件夹，进行如下设置：
  - 启用vcpkg安装的第三方库：设置 **`CMake toolchain file`** 为`path to vcpkg/scripts/buildsystems/vcpkg.cmake`

  - 添加Debug和Release两种编译模式：默认为Debug模式，便于调试但编译的程序较大且效率较低。克隆一份配置，并修改 **`Configuration type`** 参数，由`Debug`改为`Release`。
  
  
  因为使用静态库进行静态打包，故还须注意如下配置内容：
  - **`VCPKG_TARGET_TRIPLET`** 改为`x64-windows-static`，以符合vcpkg安装的第三方库类型。

  - **`CMake command arguments`** 根据编译模式进行如下修改：
    - `Debug`: `-DCMAKE_MSVC_RUNTIME_LIBRARY=MultiThreadedDebug`
    - `Release`: `-DCMAKE_MSVC_RUNTIME_LIBRARY=MultiThreaded`

## 2. 编译  
  所用库皆为跨平台库，理论上可以实现跨平台，但仅测试过Windows 10下编译。
  
  - Windows 10用VS2022打开项目文件夹，点**项目**->**删除缓存并重新配置**即可编译。
  
  - Linux可尝试以下命令进行编译：
    ```bash
    ./build.sh
    ```

## 3. 原理说明
SHA目前有SHA-0、SHA-1、SHA-2、SHA-3四个算法版本，目前广泛使用的是**SHA-2**。

<table class="wikitable" style="margin-top: 0px; width:100%">
<caption>SHA函数对比
</caption>
<tbody><tr style="vertical-align:bottom;">
<th colspan="2">算法和变体
</th>
<th>输出散列值长度<br>（bits）
</th>
<th>中继散列值长度<br>（bits）
</th>
<th>资料区块长度<br>（bits）
</th>
<th>最大输入消息长度<br>（bits）
</th>
<th>循环次数
</th>
<th>使用到的运算符
</th>
<th>碰撞攻击<br>（bits）
</th>
<th>性能示例<sup id="cite_ref-3" class="reference"><a href="#cite_note-3">[3]</a></sup><br>(<a href="/wiki/Mebibyte" title="Mebibyte">MiB</a>/s)
</th></tr>
<tr style="text-align:center;vertical-align:top;">
<td colspan="2"><b><a href="/wiki/MD5" title="MD5">MD5</a></b>（作为参考）</td>
<td>128</td>
<td>128<br><span class="nowrap">(4 × 32)</span></td>
<td>512</td>
<td>无限<sup id="cite_ref-4" class="reference"><a href="#cite_note-4">[4]</a></sup></td>
<td>64</td>
<td>And, Xor, Rot, <span class="nowrap">Add (mod&nbsp;2<sup>32</sup>),</span> Or</td>
<td class="table-no" style="text-align:center; background:#FF9090">≤18<br>（发现碰撞）</td>
<td>335
</td></tr>
<tr style="text-align:center;vertical-align:top;">
<td colspan="2"><b><span class="nowrap"><a href="/wiki/SHA-0" class="mw-redirect" title="SHA-0">SHA-0</a></span></b></td>
<td>160</td>
<td>160<br><span class="nowrap">(5 × 32)</span></td>
<td>512</td>
<td>2<sup>64</sup> − 1</td>
<td>80</td>
<td rowspan="2">And, Xor, Rot, <span class="nowrap">Add (mod&nbsp;2<sup>32</sup>),</span> Or</td>
<td class="table-no" style="text-align:center; background:#FF9090">&lt;34<br>（发现碰撞）</td>
<td>-
</td></tr>
<tr style="text-align:center;vertical-align:top;">
<td colspan="2"><b><span class="nowrap"><a href="/wiki/SHA-1" title="SHA-1">SHA-1</a></span></b></td>
<td>160</td>
<td>160<br><span class="nowrap">(5 × 32)</span></td>
<td>512</td>
<td>2<sup>64</sup> − 1</td>
<td>80</td>
<td class="table-no" style="text-align:center; background:#FF9090">&lt;63<sup id="cite_ref-5" class="reference"><a href="#cite_note-5">[5]</a></sup><br>（发现碰撞<sup id="cite_ref-6" class="reference"><a href="#cite_note-6">[6]</a></sup>）</td>
<td>192
</td></tr>
<tr style="text-align:center;vertical-align:top;">
<td rowspan="2"><b><span class="nowrap"><a href="/wiki/SHA-2" title="SHA-2">SHA-2</a></span></b></td>
<td><i>SHA-224</i><br><i>SHA-256</i></td>
<td>224<br>256</td>
<td>256<br><span class="nowrap">(8 × 32)</span></td>
<td>512</td>
<td>2<sup>64</sup> − 1</td>
<td>64</td>
<td>And, Xor, Rot, <span class="nowrap">Add (mod&nbsp;2<sup>32</sup>),</span> Or, Shr</td>
<td style="background: #99FF99; color: black; vertical-align: middle; text-align: center;" class="yes table-yes2">112 <br> 128</td>
<td>139
</td></tr>
<tr style="text-align:center;vertical-align:top;">
<td><i>SHA-384</i><br><i>SHA-512</i><br><i><span class="nowrap">SHA-512/224</span></i><br><i><span class="nowrap">SHA-512/256</span></i></td>
<td>384<br>512<br>224 <br>256</td>
<td>512<br><span class="nowrap">(8 × 64)</span></td>
<td>1024</td>
<td>2<sup>128</sup> − 1</td>
<td>80</td>
<td>And, Xor, Rot, <span class="nowrap">Add (mod&nbsp;2<sup>64</sup>),</span> Or, Shr</td>
<td style="background: #99FF99; color: black; vertical-align: middle; text-align: center;" class="yes table-yes2">192<br>256<br>112<br>128</td>
<td>154
</td></tr>
<tr style="text-align:center;vertical-align:top;">
<td rowspan="2"><b><span class="nowrap"><a href="/wiki/SHA-3" title="SHA-3">SHA-3</a></span></b></td>
<td><i>SHA3-224</i><br><i>SHA3-256</i><br><i>SHA3-384</i><br><i>SHA3-512</i></td>
<td>224<br>256<br>384<br>512</td>
<td rowspan="2">1600<br><span class="nowrap">(5 × 5 × 64)</span></td>
<td>1152<br>1088<br>832<br>576</td>
<td rowspan="2">无限<sup id="cite_ref-7" class="reference"><a href="#cite_note-7">[7]</a></sup></td>
<td rowspan="2">24<sup id="cite_ref-8" class="reference"><a href="#cite_note-8">[8]</a></sup></td>
<td rowspan="2">And, Xor, Rot, Not</td>
<td style="background: #99FF99; color: black; vertical-align: middle; text-align: center;" class="yes table-yes2">112<br>128<br>192<br>256</td>
<td>-
</td></tr>
<tr style="text-align:center;vertical-align:top;">
<td><i>SHAKE128</i><br><i>SHAKE256</i></td>
<td><span class="nowrap"><i>d</i> (arbitrary)</span><br><span class="nowrap"><i>d</i> (arbitrary)</span></td>
<td>1344<br>1088</td>
<td style="background: #99FF99; color: black; vertical-align: middle; text-align: center;" class="yes table-yes2">min(<i>d</i>/2, 128)<br>min(<i>d</i>/2, 256)</td>
<td>-
</td></tr></tbody></table>

由于SHA-2算法的各种变体除了生成摘要的长度 、循环运行的次数等一些微小差异外，算法的基本结构是一致的，且网上关于SHA256的算法解析较多，故在此以SHA256作简要说明。

原文引自《[一文读懂SHA256算法原理及其实现](https://zhuanlan.zhihu.com/p/94619052 "一文读懂SHA256算法原理及其实现")》。为便于理解，提供[SHA256算法步骤可视化](https://sha256algorithm.com/ "SHA256算法步骤可视化")，推荐对照可视化步骤逐步进行理解。

## 3.1. 常量初始化
初始哈希值$H^{(0)}$取自自然数中前面8个素数$(2,3,5,7,11,13,17,19)$的平方根的小数部分，并且取前面的32位。下面举个例子：$\sqrt{2}$小数部分约为$0.414213562373095048$，而其中

$$0.414213562373095048\approx6*16^{-1}+a*16^{-2}+0*16^{-3}+\cdots$$

于是，质数2的平方根的小数部分取前32位就对应`0x6a09e667`。

以此类推，初始哈希值$H^{(0)}$由以下8个32位的哈希初值构成：

$$H_{1}^{(0)}=6a09e667$$
$$H_{2}^{(0)}=bb67ae85$$
$$H_{3}^{(0)}=3c6ef372$$
$$H_{4}^{(0)}=a54ff53a$$
$$H_{5}^{(0)}=510e527f$$
$$H_{6}^{(0)}=9b05688c$$
$$H_{7}^{(0)}=1f83d9ab$$
$$H_{8}^{(0)}=5be0cd19$$

SHA256算法当中还使用到64个常数，取自自然数中前面64个素数的立方根的小数部分的前32位，如果用16进制表示，则相应的常数序列如下:
```
428a2f98 71374491 b5c0fbcf e9b5dba5
3956c25b 59f111f1 923f82a4 ab1c5ed5
d807aa98 12835b01 243185be 550c7dc3
72be5d74 80deb1fe 9bdc06a7 c19bf174
e49b69c1 efbe4786 0fc19dc6 240ca1cc
2de92c6f 4a7484aa 5cb0a9dc 76f988da
983e5152 a831c66d b00327c8 bf597fc7
c6e00bf3 d5a79147 06ca6351 14292967
27b70a85 2e1b2138 4d2c6dfc 53380d13
650a7354 766a0abb 81c2c92e 92722c85
a2bfe8a1 a81a664b c24b8b70 c76c51a3
d192e819 d6990624 f40e3585 106aa070
19a4c116 1e376c08 2748774c 34b0bcb5
391c0cb3 4ed8aa4a 5b9cca4f 682e6ff3
748f82ee 78a5636f 84c87814 8cc70208
90befffa a4506ceb bef9a3f7 c67178f2
```

## 3.2. 消息预处理
首先对消息进行补位处理，使得最终的长度是512位的倍数。然后以512位为一组对消息进行分块为：$M^{(1)},M^{(2)},\cdots,M^{(N)}$。

假设消息$M$的二进制编码长度为$l$位. 首先在消息末尾补上一位“$1$”，然后再补上$k$个“$0$”，其中$k$为下列方程的最小非负整数:

$$l+1+k=448\ mod\ 512$$

因为最后需要将长度$l$转换为64位二进制补位在消息最后，所以此处补位至$512-64=448$位，以确保补位后消息二进制位数的长度是$512$的整数倍。

这里需要注意的两点是
- 不管原来的消息长度是多少，即使长度已经满足对512取模后余数是448，补位也必须要进行，这时要填充512位。
- 另外，考虑到最后要将消息长度$l$转换为64位二进制编码，因此，长度的必须小于$2^{64}$，绝大多数情况，这个值足够大了。

将补码处理后的消息以512位为单位分块为：$M^{(1)},M^{(2)},\cdots,M^{(N)}$，其中第$i$个消息块的前32位表示为：$M_{0}^{(i)}$，接着32位为：$M_{1}^{(i)}$，以此类推，最后32位的消息块可表示为：$M_{15}^{(i)}$。我们采用$Big\ endian$（大端）约定对数据进行编码，即认为第一个字节是最高位字节，因此，对于每一个32位字节，最最左边的比特是最大的比特位。

## 3.3. 摘要计算主循环
为便于表示，约定如下算符（以下所有的操作都是针对32位二进制数据）：
|   算符   | 操作                   |
| :------: | :--------------------- |
| $\oplus$ | 按位异或               |
| $\wedge$ | 按位与                 |
|  $\vee$  | 按位或                 |
|  $\neg$  | 补位                   |
|   $+$    | 相加以后对$2^{32}$求余 |
| $R^{n}$  | 右移$n$位              |
| $S^{n}$  | 循环右移$n$位          |

约定如下函数：
$$Ch(x,y,z)=(x \wedge y) \oplus (\neg x \wedge z)$$
$$M_{aj}(x,y,z)=(x \wedge y) \oplus (x \wedge z) \oplus (y \wedge z)$$
$$\Sigma_{0}(x)=S^{2}(x) \oplus S^{13}(x) \oplus S^{22}(x)$$
$$\Sigma_{1}(x)=S^{6}(x) \oplus S^{11}(x) \oplus S^{25}(x)$$
$$\sigma_{0}(x)=S^{7}(x) \oplus S^{18}(x) \oplus R^{3}(x)$$
$$\sigma_{1}(x)=S^{17}(x) \oplus S^{19}(x) \oplus R^{10}(x)$$

### 3.3.1. 扩展消息块计算
对源消息分块后的每个块$M^{(i)}$由512位扩展至2048位进行计算，其中每32个二进制位为一个$W_{j}$。

扩展消息块$W_{0},W_{1},\cdots,W_{63}$的计算方式如下：
- $for\ j = 0 \rightarrow 15$
$$W_{j}=M_{j}^{(i)}$$

- $for\ j = 16 \rightarrow 63$
$$W_{j}=W_{j-16}+\sigma_{0}(W_{j-15})+W_{j-7}+\sigma_{1}(W_{j-2})$$

全部计算完毕后进入下一步。

### 3.3.2. 中间哈希值计算
在[常量初始化](#21-常量初始化 "常量初始化")一节给出了初始哈希值$H^{(0)}$以及64个常数$K_{0},K_{1},\cdots,K_{63}$，在本节的计算中将会用到。同时在此引出$a,b,c,d,e,f,g,h$作为工作变量。

- $for\ i = 1 \rightarrow N（N=补位后消息块个数）$
  $$a=H_{1}^{(i-1)}$$
  $$b=H_{2}^{(i-1)}$$
  $$\vdots$$
  $$h=H_{8}^{(i-1)}$$

  也即对于第一个块（当$i=1$时），用$H^{(0)}$初始化$a,b,c,d,e,f,g,h$，对于其后的每个块都用中间哈希值$H^{(i-1)}$初始化$a,b,c,d,e,f,g,h$。

  - $for\ j = 0 \rightarrow 63$

    首先给出$T_{1},T_{2}$的计算方法：
    $$T_{1}=h+\Sigma_{1}(e)+Ch(e,f,g)+K_{j}+W_{j}$$
    $$T_{2}=\Sigma_{0}(a)+M_{aj}(a,b,c)$$

    对于扩展消息块$W_{0},W_{1},\cdots,W_{63}$的每一个$W_{j}$，进行一次如下运算：
    $$h=g$$
    $$g=f$$
    $$f=e$$
    $$e=d+T_{1}$$
    $$d=c$$
    $$c=b$$
    $$b=a$$
    $$a=T_{1}+T_{2}$$

    全部计算完毕后，得出该块内$a,b,c,d,e,f,g,h$的终值，进行如下运算：
    $$H_{1}^{(i)}=a+H_{1}^{(i-1)}$$
    $$H_{2}^{(i)}=b+H_{2}^{(i-1)}$$
    $$\vdots$$
    $$H_{8}^{(i)}=h+H_{8}^{(i-1)}$$

    $H_{1}^{(i)},H_{2}^{(i)},\cdots,H_{8}^{(i)}$即为该块中间哈希值结果，同时也是下一个块$a,b,c,d,e,f,g,h$的初值。

## 3.4. 得出哈希结果
对补位后的每个512位消息块进行上述计算，最终得出$H_{1}^{(N)},H_{2}^{(N)},\cdots,H_{8}^{(N)}$。以16进制表示并拼接在一起，以$H_{1}^{(N)}$作为最高位，其后依次是$H_{2}^{(N)},H_{3}^{(N)},\cdots,H_{8}^{(N)}$，其中$H_{8}^{(N)}$为最低位。拼接后得出的16进制数据即为结果，表示为大端模式。

## 3.5. 汇总
**SHA256**算法汇总如下：
- 对消息进行补位使其最终的长度是512位的整数倍，然后以512位为单位进行分块。
- 从一个固定的初始哈希$H^{(0)}$开始逐个处理消息区块，进行如下计算：
  $$H^{(i)}=H^{(i-1)}+C_{M^{(i)}}(H^{(i-1)})$$
  其中$C$是SHA256的压缩函数，$+$是$mod\ 2^{32}$加法，即将两个数字加在一起，结果对$2^{32}$取余，$H^{(N)}$是消息区块的哈希值。

## 引用
- [一文读懂SHA256算法原理及其实现](https://zhuanlan.zhihu.com/p/94619052 "一文读懂SHA256算法原理及其实现")
- [SHA256算法步骤可视化](https://sha256algorithm.com/ "SHA256算法步骤可视化")
- [SHA512头文件](https://github.com/anwenhu/CrptoLib/tree/master/SHA512 "SHA512头文件")
