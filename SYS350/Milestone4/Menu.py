import configparser
import time
import json
from configparser import ConfigParser
import ssl, getpass
from pyVim.connect import SmartConnect, vim, Disconnect
    
def menu():
    print("[1] Read data from a file proof")
    print("[2] Data from current pyvmomi session")
    print("[3] Filter all VMs")
    print("[4] List All VM's")
    print("[5] List Vcenter Information")
    print("[6] Exit the Program")

def opt1():
    with open('/home/champuser/Desktop/Tech_Journal/SYS350/Milestone4/config.json', 'r') as jsonfile:
        data = json.load(jsonfile)
    print(data)

def opt2():
    with open('/home/champuser/Desktop/Tech_Journal/SYS350/Milestone4/config.json', 'r') as jsonfile:
        data = json.load(jsonfile)
    passw = getpass.getpass()
    s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    s.verify_mode=ssl.CERT_NONE
    vc = data["vcenter"]
    un = data["username"]
    si=SmartConnect(host=vc, user=un, pwd=passw, sslContext=s)
    for session in si.content.sessionManager.sessionList:
        if session.key == si.content.sessionManager.currentSession.key:
            print(
                "Current Domain and User={0.userName}, |"
                "IP Address={0.ipAddress} |".format(session),
                "Vcenter=", vc
                )
    Disconnect(si)
            

def opt3():
    with open('/home/champuser/Desktop/Tech_Journal/SYS350/Milestone4/config.json', 'r') as jsonfile:
        data = json.load(jsonfile)
    passw = getpass.getpass()
    s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    s.verify_mode=ssl.CERT_NONE
    vc = data["vcenter"]
    un = data["username"]
    si=SmartConnect(host=vc, user=un, pwd=passw, sslContext=s)
    si.RetrieveContent()
    datacenter = si.content.rootFolder.childEntity[0]
    vms = datacenter.vmFolder.childEntity
    vm_name=input("Enter a VM name: ")
    for i in vms:
        if vm_name in str(i.name):
            time.sleep(2)
            print(str(i.name) + "- It is there")
            print(i.guest.guestState + "- Powerstate")
            print(i.config.hardware.numCPU, "- CPUS")
            GB = (i.config.hardware.memoryMB/1000)
            print( GB , "- Memory in GB")
            print(i.summary.guest.ipAddress , "- IP")
            print("__________________")
        elif len(vm_name) == 0:
                opt4()
    Disconnect(si)

def opt4():
    with open('/home/champuser/Desktop/Tech_Journal/SYS350/Milestone4/config.json', 'r') as jsonfile:
        data = json.load(jsonfile)
    passw = getpass.getpass()
    s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    s.verify_mode=ssl.CERT_NONE
    vc = data["vcenter"]
    un = data["username"]
    si=SmartConnect(host=vc, user=un, pwd=passw, sslContext=s)
    si.RetrieveContent()
    datacenter = si.content.rootFolder.childEntity[0]
    vms = datacenter.vmFolder.childEntity
    for i in vms:
        time.sleep(5)
        print(str(i.name) + "- Name")
        print(i.guest.guestState + "- Powerstate")
        print(i.config.hardware.numCPU, "- CPUS")
        GB = (i.config.hardware.memoryMB/1000)
        print( GB , "- Memory in GB")
        print(i.summary.guest.ipAddress)
        print("__________________")
    Disconnect(si)

def opt5():
    with open('/home/champuser/Desktop/Tech_Journal/SYS350/Milestone4/config.json', 'r') as jsonfile:
        data = json.load(jsonfile)
    print(data)
    passw = getpass.getpass()
    s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    s.verify_mode=ssl.CERT_NONE
    vc = data["vcenter"]
    un = data["username"]
    si=SmartConnect(host=vc, user=un, pwd=passw, sslContext=s)
    aboutInfo=si.content.about
    print(aboutInfo.fullName)
    print("The Vcenter Info! from Milestone 2! ", aboutInfo)
    Disconnect(si)
menu()
option = int(input("Enter your option: "))

while option !=0:
    if option == 1:
        opt1()
    elif option == 2:
        opt2()
    elif option == 3:
        opt3()
    elif option == 4:
        opt4()
    elif option == 5:
        opt5()
    elif option == 6:
        exit()
    else:
        print("Please input an option")

    print()
    menu()
    option = int(input("Enter your option: "))
