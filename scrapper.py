import bs4
import requests as rq
# from universal_skid import 2qi
# import skiddage
from os import system, name 
import os
import time


def clear(): 

    if os.name == 'nt': 
        os.system("cls") 

    else: 
        os.system('clear') 

clear() 


def module():
        x = input("Voulez vous importer les modules ? [Y/N] : ")
        if x == "Y":
                import os
                os.system("pip install time")
                os.system("pip install bs4")
                print("[+] INSTALLED --------------------------- BS4")
                os.system("pip install requests")
                print("[+] INSTALLED --------------------------- REQUESTS")
                clear() 
                
                for x in range(2):
                        print(end="\r/")
                        time.sleep(0.5)
                        print(end="\r—")
                        time.sleep(0.5)
                        print(end="\r\\")
                        time.sleep(0.5)
                
        else:
                pass

module()
                









clear() 
print("""	
                               /T /I  
                              / |/ | .-~/  
                          T\ Y  I  |/  /  _ 
         /T               | \I  |  I  Y.-~/    
        I l   /I       T\ |  |  l  |  T  / 
 __  | \l   \l  \I l __l  l   \   `  _. | 
 \ ~-l  `\   `\  \  \\\\ ~\  \   `. .-~   |
  \   ~-. "-.  `  \  ^._ ^. "-.  /  \   |   
.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./
 >--.  ~-.   ._  ~>-"    "\\\\   7   7   ] 
^.___~"--._    ~-{  .-~ .  `\ Y . /    |    
 <__ ~"-.  ~       /_/   \   \I  Y   : | 
   ^-.__           ~(_/   \   >._:   | l______    
       ^--.,___.-~"  /_/   !  `-.~"--l_ /     ~"-.  
              (_/ .  ~(   /'     "~"--,Y   -=b-. _) 
               (_/ .  \  :           / l      c"~o \ 
                \ /    `.    .     .^   \_.-~"~--.  ) 
                 (_/ .   `  /     /       !       )/  
                  / / _.   '.   .':      /        '  
                  ~(_/ .   /    _  `  .-<_  
                    /_/ . ' .-~" `.  / \  \          ,z=. 
                    ~( /   '  :   | K   "-.~-.______//  
                      "-,.    l   I/ \_    __{--->._(==.
                       //(     \  <    ~"~"     //  
                      /' /\     \  \     ,v=.  ((  
                    .^. / /\     "  }__ //===-  `  
                   / / ' '  "-.,__ {---(==-   
                 .^ '       :  T  ~"   ll       #43G  
                / .  .  . : | :!        \\\\    
               (_/  /   | | j-"          ~^ 
                 ~-<_(_.^-~"   


                 ~-<_(_.^-~"
                 
                 
                 [+] Image Scrapper By anito #43G                
""")

def pre_append(list, string):
    temp_list = []
    for item in list:
        temp_item = string + item
        temp_list.append(temp_item)
    return temp_list

def main():
    url = input('Entrez l\'url d\'un site web : ')
    print("|---------------------------------------------| IMAGES TROUVES |---------------------------------------------|")
    r = rq.get(url)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    list_of_urls = []
    for item in images:
        list_of_urls.append(item['src'])
    list_of_urls = pre_append(list_of_urls, '')
    i = 0
    for item in list_of_urls:
        print(item)
    print("|---------------------------------------------| IMAGES TROUVES |---------------------------------------------|")

        

main() 


resez = input("\n\n\nVOULEZ-VOUS RECOMMENCER ? [Y/N] : ")
if resez == "Y":
        main()
        
else:
        pass



