#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Pennywise
# Date : 14 maret 2021
# 
import os

class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print (f"""{color.OKCYAN}
        .--.       .--.
    _  `    \     /    `  _
     `\.===. \.^./ .===./`
            \/`"`\/
         ,  | HTB |  ,
        / `\|;-.-'|/` \
       /    |::\  |    \
    .-' ,-'`|:::; |`'-, '-.
        |   |::::\|   | 
        |   |::::;|   |
        |   \:::://   |
        |    `.://'   |
       .'             `.
    _,'                 `,_ \n
==============================
{color.OKGREEN}    HACK THE BOX TOOL CLI
{color.OKCYAN}==============================\n
1. Masukan api key
2. Lihat list box yg ada
3. Lihat info box 
4. Setel ulang box 
5. Submit flag \n

NB: Sebelum menggunakan tool ini 
setting dulu config dengan apikey yg  
kalian daftarin di web : https://www.hackthebox.eu/home/settings \n untuk lebih lengkapnya klik menu 1
    """)

    
def main():
    menu = int(input(f"{color.WARNING}Masukan nomor yg anda pilih#~>"))
    if (menu == 1):
        print("""
        1. Daftar dulu di web : https://www.hackthebox.eu/register
        2. Kalo udah tinggal masuk ke :  https://www.hackthebox.eu/home/settings
        3. scroll ke bawah trus copy apikey dulu
        4. Kalo udah disalin masukin kesini
        """)
        apikey = input(f"{color.OKGREEN}Masukin apiKey nya disi :")
        os.system("htb config --lab free --apiKey "+apikey)
        main()
    elif (menu == 2):
        os.system("htb list")
        main()
        
    elif (menu == 3):
        box = input("masukan nama box : ")
        os.system("htb info "+box)
        main()
        
    elif (menu == 4):
        res = input("masukan nama box yg ingin di reset : ")
        os.system("htb reset "+res)
        main()
        
    elif (menu == 5):
        flag = input("masukan flag :")
        dif = int(input("masukan tingkat kesulitan [1-10] :"))
        kotak = input("masukan nama kotak :")
        os.system("htb own --flag="+ flag +"--difficulty="+ dif + kotak)
        main()
    else:
        print(f"kao masukan apa? \n  {color.HEADER}menu nya cuma ada 5 bodoh!!! -_")
        main()

main()

