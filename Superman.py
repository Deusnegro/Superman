
"Codeed Omidranjbar(ZED)"
"my team : Zedlasec"
import requests,sys,os,platform,time
from colorama import Fore
def clear():
    if platform.uname()[0] == "Linux" :
        os.system("clear")
    else:
        os.system("cls")

def Banner():
    print(Fore.RED+"""
                     /////           
                //////////////
            /////////////////////
       ////////////"""+Fore.CYAN+"""////////"""+Fore.RED+"""//////////
   ///////////"""+Fore.CYAN+"""////////////////"""+Fore.RED+"""/////////
  ////////"""+Fore.CYAN+"""///////"""+Fore.RED+"""//////////"""+Fore.CYAN+"""///////"""+Fore.RED+"""///////
 //////"""+Fore.CYAN+"""/////////"""+Fore.RED+"""///////////"""+Fore.CYAN+"""////////"""+Fore.RED+"""///////
 //////"""+Fore.CYAN+"""////"""+Fore.RED+"""///////////////////////////////
 //////"""+Fore.CYAN+"""////"""+Fore.RED+"""///////////////////////////////
 //////"""+Fore.CYAN+"""/////////////////////////////"""+Fore.RED+"""//////
 //////"""+Fore.CYAN+"""/////////////////////////////"""+Fore.RED+"""//////
 ///////////////////////////////"""+Fore.CYAN+"""////"""+Fore.RED+"""//////
 /////////"""+Fore.CYAN+"""///"""+Fore.RED+"""/////////////////"""+Fore.CYAN+"""//////"""+Fore.RED+"""//////
 ////////"""+Fore.CYAN+"""////////"""+Fore.RED+"""////////"""+Fore.CYAN+"""/////////"""+Fore.RED+"""////////
  ///////////"""+Fore.CYAN+"""/////////////////"""+Fore.RED+"""////////////  
      ////////////"""+Fore.CYAN+"""//////////"""+Fore.RED+"""////////////    """+Fore.CYAN+""" 'ZELDASEC'"""+Fore.RED+"""
          ////////////////////////         """+Fore.CYAN+"""SUPER MAN TOOLS"""+Fore.RED+""" 
              ///////////////                   """+Fore.CYAN+""" ZED"""+Fore.RED+"""
                   /////              
                   """)
def liststart():
    print(Fore.LIGHTCYAN_EX+"  Please Turn On Your 'Filter Beaker'\n")
    time.sleep(0.1)
    print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"1"+Fore.CYAN+"] "+Fore.RED+" Start ")
    time.sleep(0.1)
    print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"2"+Fore.CYAN+"] "+Fore.RED+" Help ")
    time.sleep(0.1)
    print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"3"+Fore.CYAN+"] "+Fore.RED+" Developer ")
    time.sleep(0.1)
    print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"4"+Fore.CYAN+"] "+Fore.RED+" Exit \n")

def listproxy():
    time.sleep(0.1)
    print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"1"+Fore.CYAN+"] "+Fore.RED+" Create Proxy HTTP and HTTPS ")
    time.sleep(0.1)
    print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"2"+Fore.CYAN+"] "+Fore.RED+" Create Proxy SOCKS5 ")
    time.sleep(0.1)
    print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"3"+Fore.CYAN+"] "+Fore.RED+" Create Proxy SOCKS4 \n")
    
def devloper():
    try:
        print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"1"+Fore.CYAN+"]  "+Fore.RED+" Contact Us : "+Fore.LIGHTCYAN_EX+"@Deusnegro")
        time.sleep(0.1)
        print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"2"+Fore.CYAN+"]  "+Fore.RED+" Developer : "+Fore.LIGHTCYAN_EX+"OmidRanjbar(Zed)")
        time.sleep(0.1)
        print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"3"+Fore.CYAN+"]  "+Fore.RED+" Backup section : "+Fore.LIGHTCYAN_EX+"https://t.me/Deusnegro")
        time.sleep(0.1)
        print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"4"+Fore.CYAN+"]  "+Fore.RED+" My Team ;) : "+Fore.LIGHTCYAN_EX+"@blackhatinfo & @Zedla_sec")
        time.sleep(0.1)
        print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"5"+Fore.CYAN+"]  "+Fore.RED+" Web site : "+Fore.LIGHTCYAN_EX+"wwww.zelda_sec.ir")
        try:
            input(Fore.CYAN+"\n   Back To Menu (Press Enter...) ")
        except:
            clear()
            Banner()
            sys.exit()
    except KeyboardInterrupt:
        clear()
        Banner()
        sys.exit()



def help():
    try:
        print(Fore.LIGHTCYAN_EX+"""  The Superman tool is a tool for creating a proxy list and has
  been developed and developed by the"""+Fore.RED+""" Zelda security"""+Fore.LIGHTCYAN_EX+""" team.
  it is the responsibility of the consumer to pay attention to the
  incorrect use of the tool
  
  Explanation:
   if you turn on the filter beaker while 
   creating a proxy, turn it on""")
        try:
            input(Fore.CYAN+"\n   Back To Menu (Press Enter...) ")
        except:
            clear()
            Banner()
            sys.exit()

    except KeyboardInterrupt:
        clear()
        Banner()
        sys.exit()
    
def http():
    try:
        proxy = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all").text.encode("utf-8")
        with open("Proxylist_http.txt","wb") as op:
            op.write(proxy)
        print(Fore.CYAN+"  - Please Wite")
        time.sleep(5)
        print(Fore.RED+"  100%")
        print(Fore.LIGHTCYAN_EX+"\n Your Proxylist Created Succsesfully\n")
        print(Fore.LIGHTCYAN_EX+" Please Check Superman File \n")
        try:
            input(Fore.CYAN+"\n   Back To Menu (Press Enter...) ")
            main()
        except:
            print("") 
            sys.exit()
    except KeyboardInterrupt:
        clear()
        sys.exit()    
def s5():
    try:
        proxy = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text.encode("utf-8")
        with open("Proxylist_socks5.txt","wb") as op:
            op.write(proxy)
        print(Fore.CYAN+"  - Please Wite")
        time.sleep(5)
        print(Fore.RED+"  100%")
        print(Fore.LIGHTCYAN_EX+"\n Your Proxylist Created Succsesfully\n")
        print(Fore.LIGHTCYAN_EX+" Please Check Superman File \n")
        try:
            input(Fore.CYAN+"\n   Back To Menu (Press Enter...) ")
            main()
        except:
            print("") 
            sys.exit()
    except KeyboardInterrupt:
        clear()
        sys.exit()

def s4():
    try:
        proxy = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all&ssl=all&anonymity=all").text.encode("utf-8")
        with open("Proxylist_socks4.txt","wb") as op:
            op.write(proxy)
        print(Fore.CYAN+"  - Please Wite")
        time.sleep(5)
        print(Fore.RED+"  100%")
        print(Fore.LIGHTCYAN_EX+"\n Your Proxylist Created Succsesfully\n")
        print(Fore.LIGHTCYAN_EX+" Please Check Superman File \n")
        try:
            input(Fore.CYAN+"\n   Back To Menu (Press Enter...) ")
            main()
        except:
            print("") 
            sys.exit()
    except KeyboardInterrupt:
        clear()
        sys.exit()

def main():
    try:
        clear()
        Banner()
        liststart()
        start = input(Fore.LIGHTCYAN_EX+"  C://SuperMan_> "+Fore.RED)
        if start == '1':
            try:
                clear()
                Banner()
                listproxy()
                op = input(Fore.LIGHTCYAN_EX+"  C://SuperMan_> "+Fore.RED)
                if op == '1':
                    clear()
                    Banner()
                    http()
                elif op == '2':
                    clear()
                    Banner()
                    s5()
                elif op == '3':
                    clear()
                    Banner()
                    s4()
                elif op == '':
                    input(Fore.RED+'\n    Enter Data |: ')
                    main()
            except KeyboardInterrupt:
                clear()
                Banner()
                sys.exit()
        elif start == '2':
            try:
                clear()
                Banner()
                help()
            except KeyboardInterrupt:
                clear()
                Banner()
                sys.exit()
        elif start == '3':
            clear()
            Banner()
            devloper()
        elif start == '4':
            clear()
            print(Fore.RED+"Century Breaker ;)"+Fore.WHITE)
            sys.exit()
        elif start == '':
            input(Fore.RED+'\n    Enter Data |: ')
            main()
    except KeyboardInterrupt:
        clear()
        Banner()
        sys.exit()

while True:
    main()

