import openpyxl
import os

#Variables
values = []
svr_name = []
svr_ip = []
svr_ssh_port = []
svr_usr = []
svr_pw = []
ws_data = []
listres = []

#Directories
os.chdir('../..')
dir_srcfile = os.getcwd() + '/Source/SKBB_Install_Solidstep/src.xlsx'
dir_ansfile = os.getcwd() + '/Ansible/SKBB_Install_Solidstep/'
dir_tmp = os.getcwd() + '/Temporary'
dir_shfile = os.getcwd()+'/Shell/SKBB_Install_Solidstep/'

#Load Account Sheets
load_acc_wb = openpyxl.load_workbook(dir_srcfile)
ws_data = load_acc_wb.get_sheet_names()
load_acc_ws = load_acc_wb[ws_data[0]]

#Create Result yml File
res_txt = open(dir_tmp+'/hosts', 'w')

for row in load_acc_ws.rows:
    row_value = []
    for cell in row:
        row_value.append(cell.value)
    svr_name.append(row_value[0])
    svr_ip.append(row_value[1])
    svr_ssh_port.append(row_value[2])
    svr_usr.append(row_value[3])
    svr_pw.append(row_value[4])

for tag in range(0,len(svr_name),1):
    res_txt.write(svr_name[tag])
    res_txt.write(' ansible_ssh_host=')
    res_txt.write(svr_ip[tag])
    res_txt.write(' ansible_ssh_port=')
    res_txt.write(str(svr_ssh_port[tag]))
    res_txt.write(' ansible_ssh_user=')
    res_txt.write(svr_usr[tag])
    res_txt.write(' ansible_ssh_pass=')
    res_txt.write(svr_pw[tag])
    res_txt.write('\n')

listres = os.listdir(dir_tmp)
if listres.__contains__('hosts'):
    print('System: Conversion Completed at ' + dir_tmp)