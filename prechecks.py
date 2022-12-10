import os
import math
import pandas as pd

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# acc_name = input("Account name as per Manage portal: ")
# acc_datacentre = input("Data Centre: ")
data_size = input("Data Size as per CoC in GB: ")
file_count = input("File count as per CoC: ")
# mapping_dir = input("Path of Mapping File: ")
data_dir = input("Path of Data: ")
data_dir = data_dir.replace("\\","/")
data_size = float(data_size)

mappingfile_path = input('Please enter path of mapping file: ')
accounts_path = input('Please enter path of accounts file: ')

mappingfile_path = mappingfile_path.replace("\\","/")
accounts_path = accounts_path.replace("\\","/")

mappingfile = pd.read_excel(mappingfile_path)
accounts = pd.read_excel(accounts_path)



# Data Validation ======================================

print(" \n****************************** \n\t Data Validation \n******************************")

size = 0
# get size
for path, dirs, files in os.walk(data_dir):
    for f in files:
        fp = os.path.join(path, f)
        size += os.stat(fp).st_size
 
# display size   
size = round(size / 1073741824, 2 )  #converting bytes to GB

# data size comparision

data_status = math.isclose(data_size, size,abs_tol=0.09999999999999964)

print(str(data_status) + "--data status")
print("Data size: " + str(size) + " GB")

# File Count validation **********************************

count = 0
for root_dir, cur_dir, files in os.walk(data_dir):
    count += len(files)
print('file count:', count)

file_status = (count == int(file_count))

print(str(file_status) + " -- File status")

status = (data_status & file_status)

if status:
    print("Validation Status: " + bcolors.OKGREEN + "Pass" + bcolors.ENDC)
else:
    print("Validation Status: " + bcolors.FAIL + "Fail" + bcolors.ENDC)



# User ========================== Validation ======================================

print(" \n****************************** \n\t User Validation \n ******************************")

# print('****************************** ','\n Mapping File \n',mappingfile, '\n','****************************** ','\n Accounts \n',accounts[['Name']])

comparission = (pd.merge(mappingfile,accounts, how='outer',indicator='position'))
missingusers = comparission.loc[comparission['position'] == 'left_only']
if missingusers.empty:
    print("Validation Status: " + bcolors.OKGREEN + 'Successful' + bcolors.ENDC)
else:
    print('****************************** ',"\nValidation Status: " + bcolors.FAIL + 'Failed' + + bcolors.ENDC  ,'\n Missing Users \n',missingusers[['Name']])


input("Press enter to exit;")