import os
import smtplib
import sys
from datetime import datetime
#email sender needs some revisions
def mail_sender(msg):
    fromaddr = 'minhooyoon1991@gmail.com'
    toaddrs  = 'amir.shabanpoor92@gmail.com'
    username = 'minhooyoon1991@gmail.com'
    password = 'zludiratqagdzcso'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

min_list = [25,45,65,85,105,125,150,175,200,250,300] #min of kinematic values
max_list = ['45d0','65d0','85d0','105d0','125d0','150d0','175d0','200d0','250d0','300d0','400d0'] #max of kinematic values
for i in range(0,len(min_list)):
    rc_ed = '  ' + str(min_list[i]) + '	= ptgmin ! Min photon transverse momentum\n'
    replace_line('Cards/run_card.dat',154,rc_ed)
    cc_ed = '            if(ptg.lt.ptgmin.or.ptg.gt.'+ max_list[i] +')then\n'
    replace_line('SubProcesses/cuts.f',315,cc_ed)
    os.system('./bin/generate_events')
print('done')    
