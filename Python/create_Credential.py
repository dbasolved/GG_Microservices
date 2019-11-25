
#!/usr/bin python
# Copyright (c) 2018-2019 Oracle and/or its affiliates.  All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown at http://oss.oracle.com/licenses/upl.
#
# Since:        Oct 2019
# Author:       Bobby Curtis <bobby.curtis@oracle.com>
# Description:  Oracle GoldenGate Microservices - Add Credentials
#
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER.
#

import requests
import json

vHost = "localhost"
vPort = "16001"
vURL = "https://"
vEndPoint = "/services/v2/credentials/"
vDomain = "OracleGoldenGate"
vId = ""
vUserId = raw_input("What user to connect with: ")
vAddress = raw_input("Hostname or IP Address and Port Number of Database: ")
vService = raw_input("Oracle Database Service: ")
vPwd = raw_input("Password: ")
vAlias = raw_input("Alias used: ")
#vOggadmin = raw_input("GoldenGate Login: ")
#vGGAPwd = raw_input("GoldenGate Login Password ")

def create_credential():

    vId = vUserId + '@' + vAddress + '/' + vService
    vPayload = json.dumps({'password': vPwd, 'userid': vId})
    vDest = vURL + vHost + ':' + vPort + vEndPoint + vDomain + '/' + vAlias
    
    #vEncode = 'echo -n ' + vOggadmin + ':' + vGGAPwd + ' | base64'
    #vEncode1 = eval(vEncode)

    vHeaders = {'cache-control': 'no-cache', 'authorization': 'Basic b2dnYWRtaW46V2VsY29tZTEh'}
    #print (vHeaders + "\n")

    response = requests.request("POST", vDest, data=vPayload, headers=vHeaders)

    print(response.text)

if __name__ == '__main__':
    create_credential()