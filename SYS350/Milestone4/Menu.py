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
    print("[7] Turn a VM [OFF]")
    print("[8] Turn a VM [ON]")
    print("[9] Make a snapshot")
    print("[10] Delete a VM")
    print("[11] Modify VM specs")
    print("[12] Rename a VM")
    print("[13] Exit the Program")
    
    

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
            GB = (i.config.hardware.memoryMB/1024)
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
        GB = (i.config.hardware.memoryMB/1024)
        print( GB , "- Memory in GB")
        print(i.summary.guest.ipAddress)
        print("__________________")
    Disconnect(si)

def opt5():
    with open('/home/champuser/Desktop/Tech_Journal/SYS350/Milestone4/config.json', 'r') as jsonfile:
        data = json.load(jsonfile)
    passw = getpass.getpass()
    s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    s.verify_mode=ssl.CERT_NONE
    vc = data["vcenter"]
    un = data["username"]
    si=SmartConnect(host=vc, user=un, pwd=passw, sslContext=s)
    aboutInfo=si.content.about
    print("The Vcenter Info! from Milestone 2! ", aboutInfo)
    time.sleep(2)
    print(aboutInfo.osType)
    Disconnect(si)

def opt7():
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
        if vm_name == i.name:
            print("Turning the VM off!")
            i.PowerOff()
            time.sleep(5)
    Disconnect(si)
def opt8():
    #https://github.com/vmware/pyvmomi-community-samples/blob/master/samples/vm_power_on.py
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
        if vm_name == i.name:
            print("Turning the VM on!")
            i.PowerOn()
            time.sleep(5)
    Disconnect(si)

def opt9():
    #https://github.com/vmware/pyvmomi-community-samples/blob/master/samples/create_snapshot.py
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
    s_Name=input("Enter what the snapshot should be named")
    descript=input("Please put in a description")
    for i in vms:
        if vm_name == i.name:
            i.CreateSnapshot_Task(name=s_Name, memory=True, quiesce=False)
    Disconnect(si)
def opt10():
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
   #vm_name=input("Enter a VM name: ")
    name_c=input("Enter the name of the machine to be deleted: ")
    for i in vms:
        if name_c == i.name:
            i.PowerOff()
            time.sleep(10)
            print("Deleting the VM")
            i.Destroy_Task()
            time.sleep(10)
    Disconnect(si)
    13

def opt11():
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
    vm_name=input("Enter a VM name to reconfigure CPU for: ")
    for i in vms:
        if vm_name == i.name:
            print("You have chosen to reconfigure the CPU's. Powering the VM off.")
            i.PowerOff()
            print("Power is off Proceeding to reconfigure.")
            number = input("Input the number of CPU's you would like to set: ")
            time.sleep(2)
            core = input("Enter the number of Cores you would want: ")
            time.sleep(2)
            print("Configuring...")
            spec = vim.vm.ConfigSpec()
            spec.numCPUs=int(number)
            spec.numCoresPerSocket=int(core)
            i.Reconfigure(spec)
            print("VM CPU update complete")
            time.sleep(5)
    Disconnect(si)

def opt12():
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
    new_name=input("Please enter a name to change the VM name to: ")
    for i in vms:
        if vm_name == i.name:
            print("Renaming Now...")
            i.Rename(new_name)
            time.sleep(2)
            print("Name has been changed")
            time.sleep(2)
    Disconnect(si)



menu()
option = int(input("Enter your option: "))

while option !=0 :
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
        menu2()
    elif option == 7:
        opt7()
    elif option == 8:
        opt8()
    elif option == 9:
        opt9()
    elif option == 10:
        opt10()
    elif option == 11:
        opt11()
    elif option == 12:
        opt12()
    elif option == 13:
        exit()
    else:
        print("Please input an option")

    
    menu()
    option = int(input("Enter your option: "))
