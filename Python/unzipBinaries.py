#!/usr/bin python
# Copyright (c) 2018-2019 Oracle and/or its affiliates.  All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown at http://oss.oracle.com/licenses/upl.
#
# Since:        January 2019
# Author:       Bobby Curtis <bobby.curtis@oracle.com>
# Description:  Extract Oracle GoldenGate 18c Microservices Binaries and install
#Preinstalled: Oracle Database 18c Client - Administrator Config
#
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER.
#

import zipfile
import os
import subprocess

from time import sleep

v_oggma = '/home/oracle/software/181000_fbo_ggs_Linux_x64_services_shiphome.zip'
v_orabase = '/opt/app/oracle'
v_orahome = '/opt/app/oracle/product/18.1.0/dbclient_1'
v_ogghome = '/opt/app/oracle/product/18.1.0/oggcore_1'
v_inventory = '/opt/app'

def remove_staged_oggma():
    print('Removing staged Oracle GoldenGate software\n')
    os.system('rm -rf /home/oracle/software/oggma')
    
def oggma_extract():
    print('Unzipping required binaries - '+v_oggma)
    with zipfile.ZipFile(v_oggma,'r') as zip_ref:
        zip_ref.extractall('./oggma')
        
        subprocess.call(['chmod','-R', '0755', './oggma'])
        
        print('Oracle GoldenGate 18c Install Response File\n')
        ofr = open("oggcore.rsp","a")
        ofr.write("oracle.install.responseFileVersion=/oracle/install/rspfmt_ogginstall_response_schema_v12_1_2\n")
        ofr.write("INSTALL_OPTION=ORA18c\n")
        ofr.write("SOFTWARE_LOCATION="+str(v_ogghome)+"\n")
        ofr.write("DATABASE_LOCATION="+str(v_orahome)+"\n")
        ofr.write("INVENTORY_LOCATION="+str(v_inventory)+"/oraInventory\n")
        ofr.write("UNIX_GROUP_NAME=oinstall\n")
        ofr.close

def install_oggma():
   os.system('/home/oracle/software/oggma/fbo_ggs_Linux_x64_services_shiphome/Disk1/runInstaller -silent -responseFile /home/oracle/software/oggcore.rsp')

if __name__ == '__main__':
   print('Installing Oracle GoldenGate 18c Microservices (18.1.0)')
   oggma_extract()
   install_oggma()
   sleep(120)
   remove_staged_oggma()
   print('Setup complete')

