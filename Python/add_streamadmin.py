import requests

#global variables and lists
gg_servers_admin = ['localhost', '16001', 'localhost', '17001']
gg_payload = ['credential', 'Welcome1', 'info', 'Stream Admin', 'type', 'Basic', 'user', 'streamadmin']
gg_header = ['cache-control', 'no-cache']
vlist = []
vPayload = []
vHeader = []
vcURL = []

#Get server and port number from list
for i in range(0, len(gg_servers_admin),2):
    vlist.append(gg_servers_admin[i] + ':' + gg_servers_admin[i+1])

#Get payload information
for p in range(0,len(gg_payload),2):
    vPayload.append('"' + gg_payload[p] + '":"' + gg_payload[p+1] + '"')

#Get header information
for h in range(0, len(gg_header),2):
    vHeader.append('"' + gg_header[h] + '":"' + gg_header[h+1] + '"')

#Build cURL components
for x in vlist:
    vUrl = 'https://'
    vEndPoint = '/services/v2/authorizations/'
    vRole = 'Administrator'
    vUser = 'streamadmin'

    vurl = vUrl + x + vEndPoint + vRole + '/' + vUser

    vcURL.append(vurl)

    #Build Payload
    vpayload = '{'

    for y in vPayload:
        vpayload = vpayload + y + ','
        vpayload = vpayload.rstrip(',')
    
    vpayload = vpayload + '}'
    
    vcURL.append(vpayload)

    vheader = '{'

    #Build Header
    for z in vHeader:
        vheader = vheader + z + ','
        vheader = vheader.rstrip(',')

    vheader = vheader + '}'
    
    vcURL.append(vheader)  

for c in vcURL:
    print c

#response = requests.request("POST", vurl, data=vpayload, headers=vheader)

#print (response.text)