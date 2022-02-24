# SunloginClient_RCE
#### 脚本仅供个人安全检测使用，请勿用于非法渗透活动，否则后果自负
🔆受影响版本 向日葵个人版for Windows <= 11.0.0.33

### 脚本说明
```
1，脚本端口扫描使用nmap模块进行扫描，速度可能没有多线程的快（但省事🙆‍♂️）
2，脚本没有写扫IP段的功能（主要没想过要大范围扫）
```
### 🔆使用说明
```
usage: main.py [-h] [-u HOST] [-p PORT] [-e]

python3 main.py -h 127.0.0.1

optional arguments:
  -h, --help  show this help message and exit
  -u HOST     指定ip
  -p PORT     指定端口或指定扫描端口，默认40000-60000
  -e          使用EXP
```

### 🔆端口检测
##### 默认40000-60000，范围可以使用-p参数指定
![](https://github.com/1rm/SunloginClient_RCE/blob/main/images/PocScan.png)

### 🔆命令执行
##### 加上-p指定漏洞端口后使用-e参数来进入命令执行模式
![](https://github.com/1rm/SunloginClient_RCE/blob/main/images/EXP.png)
