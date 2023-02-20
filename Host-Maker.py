try:import os;from requests import post;from rich.console import Console;from rich.columns import Columns;from rich.panel import Panel
except Exception as e:print(f'[!] Download The Missing Module ! , {e}');exit()
os.system('cls' if os.name == 'nt' else 'clear')
print("""
██╗  ██╗ ██████╗ ███████╗████████╗   ███╗   ███╗██╗  ██╗
██║  ██║██╔═══██╗██╔════╝╚══██╔══╝   ████╗ ████║██║ ██╔╝
███████║██║   ██║███████╗   ██║█████╗██╔████╔██║█████╔╝ 
██╔══██║██║   ██║╚════██║   ██║╚════╝██║╚██╔╝██║██╔═██╗ 
██║  ██║╚██████╔╝███████║   ██║      ██║ ╚═╝ ██║██║  ██╗
╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝      ╚═╝     ╚═╝╚═╝  ╚═╝
 
              By @TweakPY - @vv1ck
""")
domain=str(input('[?] Domain : '))#Step 1 : instagram
subdomain=['orgfree.com','6te.net','ueuo.com','eu5.org','noads.biz','coolpage.biz','freeoda.com','freevar.com','freetzi.com','xp3.biz']
def get_content(subdomain):
	if subdomain in ['ueuo.com','eu5.org','6te.net','xp3.biz']:
		we_suggest='We Suggest'
		return f"[b]{subdomain}[/b]\n[green]{we_suggest}"
	elif subdomain=='noads.biz':
		we_suggest='Half Good'
		return f"[b]{subdomain}[/b]\n[yellow]{we_suggest}"
	else:
		we_suggest="We Don't Suggest"
		return f"[b]{subdomain}[/b]\n[red]{we_suggest}"
console=Console()
console.print('\nAvailable subdomains :\n',style="green")
sub_renderables=[Panel(get_content(sub), expand=True) for sub in subdomain]
console.print(Columns(sub_renderables))
sdm=int(input("\n[?] Sub Domain [1/10] : "))#Step 2 : instagram.6te.net
if sdm==1:sdm='orgfree.com'
elif sdm==2:sdm='6te.net'
elif sdm==3:sdm='ueuo.com'
elif sdm==4:sdm='eu5.org'
elif sdm==5:sdm='noads.biz'
elif sdm==6:sdm='coolpage.biz'
elif sdm==7:sdm='freeoda.com'
elif sdm==8:sdm='freevar.com'
elif sdm==9:sdm='freetzi.com'
elif sdm==10:sdm='xp3.biz'
rq0=post('https://www.freewebhostingarea.com/cgi-bin/create_account.cgi',headers={'Host': 'www.freewebhostingarea.com','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','Content-Length': '61','Origin': 'https://freewha.com','Referer': 'https://freewha.com/','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'cross-site','Sec-Fetch-User': '?1','Te': 'trailers','Connection': 'close'},data={'action' :"check_domain",'thirdLevelDomain' :f'{domain}','domain' :f"{sdm}"}).text
if ' params = "toolbar=0,";' in rq0:
	rq1=post('https://newserv.freewha.com/cgi-bin/create_ini.cgi',headers={'Host': 'newserv.freewha.com','Cookie': 'FreeWHA-persistent=checked;','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','Content-Length': '134','Origin': 'https://www.freewebhostingarea.com','Referer': 'https://www.freewebhostingarea.com/','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'cross-site','Sec-Fetch-User': '?1','Te': 'trailers'},data={'action' :"validate",'domainName' :f"{domain}.{sdm}",'email' :f"{domain}@gmail.com",'password' :f"{domain}",'confirmPassword' :f"{domain}",'agree' :"1"}).text;weburl=str(domain+"."+sdm)
	if f"http://{str(domain)}.{str(sdm)}" in rq1:
		print(f'''
📂 /home/TweakPY/vv1ck/
┣━━ 📄 username ( {weburl} )
┣━━ 📄 password ( {domain} )
┣━━ 🐍 Server ( {weburl} )
┣━━ 🐍 FTP ( http://{weburl}/ftp/ )
┗━━ 🐍 URL ( http://{weburl} )

📂 /home/
┗━━ 🐍 Home ( JQ )''')#Done : http://instagram.6te.net
	else:exit("[!] Error Creating account !")      
else:exit("[!]  Error : Domain may be Taken !")   
