import paramiko
import re

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.1.94', username='root', password='root')

data = {}

stdin, stdout, stderr = client.exec_command('nmcli device status')
nmcli = stdout

stdin, stdout, stderr = client.exec_command('ip add')
ipadd = stdout

for line in stdout:
    data[i] = {line.strip('\n')}
    i = i+1

i=0
#stdin, stdout, stderr = client.exec_command(mac)
#for line in stdout:
    #data[i][

print(data)



client.close()