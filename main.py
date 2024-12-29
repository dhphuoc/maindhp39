import requests, socket, os
from pystyle import Write, Colors, Colorate
from datetime import datetime
from time import sleep
red = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lam = "\033[1;36m"
trang = "\033[1;37m"

def banner():
    os.system('cls' if os.name=='nt' else 'clear')
    Write.Print('''            ██████╗ ██╗  ██╗██████╗  ██████╗ ███████╗
            ██╔══██╗██║  ██║██╔══██╗██╔═████╗╚════██║
            ██║  ██║███████║██████╔╝██║██╔██║    ██╔╝
            ██║  ██║██╔══██║██╔═══╝ ████╔╝██║   ██╔╝ 
            ██████╔╝██║  ██║██║     ╚██████╔╝   ██║  
            ╚═════╝ ╚═╝  ╚═╝╚═╝      ╚═════╝    ╚═╝   
    ''',Colors.blue_to_cyan,interval=0.0001)
    Write.Print('''                CopyRight: © DHP07-TOOL\n''',Colors.red_to_purple,interval=0.0001)
    print(red+"-"*70)
    print(f'''{red}[{luc}<>{red}] {tim}Admin{trang}: {lam}Đàm Hữu Phước
{red}[{luc}<>{red}] {vang}Box Zalo{trang}: {trang} https://zalo.me/g/ixhzva608
{red}[{luc}<>{red}] {luc}Youtube{trang}: {trang} https://www.youtube.com/@fuockutii
{red}[{luc}<>{red}] {lam}Web Dvmxh{trang}: {trang} https://sharegiare.xyz''')
    print(red+"-"*70)

def Ketnoi():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except:
        return False

def keyfree(token):
    key_file = "key.txt"
    nhapkey = None
    if os.path.exists(key_file):
        with open(key_file, "r") as file:
            nhapkey = file.read().strip()
        check = requests.post('https://www.dhphuoc21.xyz/key', data={'key': nhapkey}).json()
        if check['status'] == 'success':
            name = check['name']
            ip = check['ip']
            time = check['time']
            keycode = nhapkey[:3] + '*' * 10
            banner()
            print(f'{Colorate.Horizontal(Colors.purple_to_blue,"┌───────────────────────────────┐")}')
            print(f'{Colorate.Horizontal(Colors.purple_to_blue,"│")}{Colorate.Horizontal(Colors.blue_to_cyan,"        Thông Tin key        ")}{Colorate.Horizontal(Colors.blue_to_purple,"  │")}')
            print(f'{Colorate.Horizontal(Colors.purple_to_blue,"└───────────────────────────────┘")}')
            print(f'{red}[{trang}<>{red}] {luc}Số IP Chủ Key{trang}: {vang}{ip}')
            print(f'{red}[{trang}<>{red}] {luc}Key Tool{trang}: {vang}{keycode}{nhapkey[:0]}')
            print(f'{red}[{trang}<>{red}] {luc}Họ Và Tên Chủ key{trang}: {vang}{name}')
            print(f'{red}[{trang}<>{red}] {luc}Số Giờ Còn Lại{trang}: {vang}{time}')
            print(red + "-" * 70)
            with open(key_file, "w") as file:
                file.write(nhapkey)
                return
        else:
            print(f'{Colorate.Horizontal(Colors.red_to_purple,"Key Không Tồn Tại hoặc Hết Hạn")}')
            quit()
    taokey = requests.get('https://dhphuoc21.xyz/key').json()
    if taokey['status'] == 'success':
        key = taokey['key']
        link = requests.get(f'https://yeumoney.com/QL_api.php?token={token}&format=json&url=https://www.dhphuoc21.xyz/test.php?key={key}').json()
        if link['status'] == 'success':
            get = link['shortenedUrl']
            banner()
            print(f'\n{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.blue_to_purple,"Link Vượt Key Là")}{trang}: {luc}{get}')
    else:
        print(f'{Colorate.Horizontal(Colors.red_to_purple,"Server Key Free Bị Lỗi Rồi Xài Phí Đi")}')
        quit()
    dem = 0
    while dem < 3:
        nhapkey = input(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_cyan,"Nhập Key Đã Vượt")}: ')
        check = requests.post('https://www.dhphuoc21.xyz/key', data={'key': nhapkey}).json()
        if check['status'] == 'success':
            name = check['name']
            ip = check['ip']
            time = check['time']
            keycode = nhapkey[:3] + '*' * 10
            banner()
            print(f'{Colorate.Horizontal(Colors.purple_to_blue,"┌───────────────────────────────┐")}')
            print(f'{Colorate.Horizontal(Colors.purple_to_blue,"│")}{Colorate.Horizontal(Colors.blue_to_cyan,"        Thông Tin key        ")}{Colorate.Horizontal(Colors.blue_to_purple,"  │")}')
            print(f'{Colorate.Horizontal(Colors.purple_to_blue,"└───────────────────────────────┘")}')
            print(f'{red}[{trang}<>{red}] {luc}Số IP Chủ Key{trang}: {vang}{ip}')
            print(f'{red}[{trang}<>{red}] {luc}Key Tool{trang}: {vang}{keycode}{nhapkey[:0]}')
            print(f'{red}[{trang}<>{red}] {luc}Họ Và Tên Chủ key{trang}: {vang}{name}')
            print(f'{red}[{trang}<>{red}] {luc}Số Giờ Còn Lại{trang}: {vang}{time}')
            print(red + "-" * 70)
            with open(key_file, "w") as file:
                file.write(nhapkey)
            return
        else:
            dem += 1
            print(f'{Colorate.Horizontal(Colors.red_to_purple,f"Key Không Tồn Tại hoặc Hết Hạn, Đã Nhập {dem} Lần")}')
            if dem == 3:
                print(f'{Colorate.Horizontal(Colors.red_to_purple,"Bạn Đã Nhập Sai Key 3 Lần Rồi!")}')
                quit()
banner()
keyfree('41a298c8aedb12765b2d4f23cd60f7fee0da6cb85bfb2317e37840f7ea20fd16')
print(f'{Colorate.Horizontal(Colors.purple_to_blue,"┌───────────────────────────────┐")}')
print(f'{Colorate.Horizontal(Colors.purple_to_blue,"│")}{Colorate.Horizontal(Colors.blue_to_cyan,"         Trao Đổi Sub        ")}{Colorate.Horizontal(Colors.blue_to_purple,"  │")}')
print(f'{Colorate.Horizontal(Colors.purple_to_blue,"└───────────────────────────────┘")}')
print(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Nhập")} {red}[{vang}1.1{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Để Chọn Chế Độ Facebook Thường")}')
print(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Nhập")} {red}[{vang}1.2{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Để Chọn Chế Độ Instagram")}')
print(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Nhập")} {red}[{vang}1.3{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Để Chọn Chế Độ Facebook Page")} {vang}({red}bảo Trì{vang})')
print(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Nhập")} {red}[{vang}1.4{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Để Chọn Chế Độ TikTok")} {vang}({red}bảo Trì{vang})')
print(red+"-"*70)
print(f'{Colorate.Horizontal(Colors.purple_to_blue,"┌───────────────────────────────┐")}')
print(f'{Colorate.Horizontal(Colors.purple_to_blue,"│")}{Colorate.Horizontal(Colors.blue_to_cyan,"        Tương Tác Chéo        ")}{Colorate.Horizontal(Colors.blue_to_purple," │")}')
print(f'{Colorate.Horizontal(Colors.purple_to_blue,"└───────────────────────────────┘")}')
print(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Nhập")} {red}[{vang}2.1{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Để Chọn Chế Độ Facebook Thường")}')
print(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Nhập")} {red}[{vang}2.2{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Để Chọn Chế Độ Instagram")} {vang}({red}bảo Trì{vang})')
print(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Nhập")} {red}[{vang}2.3{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Để Chọn Chế Độ Facebook Page")}')
print(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Nhập")} {red}[{vang}2.4{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Để Chọn Chế Độ TikTok")}')
print(red+"-"*70)
chon = input(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.blue_to_white,"Chọn Chế Độ")}: ')
try:
    if chon == '1.1':
        run = requests.get(f'https://raw.githubusercontent.com/dhphuoc/maindhp39/refs/heads/main/tdsfb.py').text
    elif chon == '1.2':
        run = requests.get(f'https://raw.githubusercontent.com/dhphuoc/maindhp39/refs/heads/main/tdsig.py').text
    elif chon == '1.3':
        run = requests.get(f'').text
    elif chon == '1.4':
        run = requests.get(f'').text
    elif chon == '2.1':
        run = requests.get(f'https://raw.githubusercontent.com/dhphuoc/maindhp39/refs/heads/main/ttcfb.py').text
    elif chon == '2.2':
        run = requests.get(f'').text
    elif chon == '2.3':
        run = requests.get(f'https://raw.githubusercontent.com/dhphuoc/maindhp39/refs/heads/main/ttcpage.py').text 
    elif chon == '2.4':
        run = requests.get(f'https://raw.githubusercontent.com/dhphuoc/maindhp39/refs/heads/main/ttctiktok.py').text 
    else:
        run = print(f'{Colorate.Horizontal(Colors.red_to_purple,"Lựa Chọn Không Xác Định")}')
except:
    if not Ketnoi():
        print(f'{Colorate.Horizontal(Colors.red_to_purple,"Hãy Kiểm Tra Kết Nối Mạng !!!")}')
    else:
        print(f'{Colorate.Horizontal(Colors.red_to_purple,"Sever Gặp Lỗi Hãy Liên Hệ Admin !!!")}')
    exit()
exec(run)
