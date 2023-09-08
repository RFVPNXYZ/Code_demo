import requests
import os
import time
import sys
os.system('clear')

xanhnhat = "\033[1;36m"
trang = "\033[1;37m"
pcmcute = "\033[0;37m"

banner = f"""
{xanhnhat}███╗   ███╗   ████████╗ ██████╗  ██████╗ ██╗
{trang}████╗ ████║   ╚══██╔══╝██╔═══██╗██╔═══██╗██║
{xanhnhat}██╔████╔██║{xanhnhat}█{trang}█{xanhnhat}█{trang}█{xanhnhat}█╗{xanhnhat}██║   ██║   ██║██║   ██║██║
{trang}██║╚██╔╝██║{xanhnhat}╚════╝{trang}██║   ██║   ██║██║   ██║██║
{xanhnhat}██║ ╚═╝ ██║      ██║   ╚██████╔╝╚██████╔╝███████╗
{trang}╚═╝     ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

    \033[1;32mTOOL DẸC DẠNG BERSERKER
{pcmcute}= = = = = = = = = = = = = = = = = = = = = = = = = = = = 
"""

for x in banner:
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.00130)
    
while True:
    try:
        choice = input("\033[1;34mNhập Url Hoặc File Cần Dẹc\033[1;31m: \033[0;37m")
        print(xanhnhat+'='*50,'\033[0;33m')
        if 'http' in choice:
            code = requests.get(choice).text
        else:
            with open(choice, "r") as f:
                code = f.read()
        break
    except Exception as e:
        print(str(e))
        continue
try:
    code_so = code.split(":exit()if")[1].split('join(')[0]
    dec_cd_so = code_so.replace('[15]', '[12]')
    code_chu = code.split(':str(')[1].split('%list(')[0]
    dec_cd_chu = code_chu.replace(',', ')/').split('/')[0]
    tach = dec_cd_chu.replace('f"', 'f"/').split('/')[0]
    tach2 = dec_cd_chu.replace('}', '}print').split('}')[1]
    dec_chu = tach + tach2 + '"'
    dec_full = code.replace(code_so, dec_cd_so).replace(code_chu, dec_chu)
    exec(dec_full)
except Exception as e:
    print(str(e))