import requests 


#url = 'http://www.mospi.gov.in/sites/default/files/NSS7612dws/R76120L01.TXT'

for i in range(1,10):
    url = f"http://www.mospi.gov.in/sites/default/files/NSS7612dws/R76120L0{i}.TXT"
    r = requests.get(url)
    open(f"R76120L0{i}.TXT", 'wb').write(r.content)
