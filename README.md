# SunloginClient_RCE
#### 脚本仅供个人安全检测使用，请勿用于非法渗透活动，否则后果自负
🔆受影响版本 向日葵个人版for Windows <= 11.0.0.33

### 脚本说明
脚本端口扫描使用nmap模块进行扫描，速度可能没有多线程的快（但省事🙆‍♂️）

### 使用说明
```
usage: main.py [-h] [-u HOST] [-p PORT] [-e]

python3 main.py -h 127.0.0.1

optional arguments:
  -h, --help  show this help message and exit
  -u HOST     指定ip
  -p PORT     指定端口或指定扫描端口，默认40000-60000
  -e          使用EXP
```
