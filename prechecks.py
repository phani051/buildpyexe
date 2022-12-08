import os
import math

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
data_size = input("Data Size as per CoC: ")
file_count = input("File count as per CoC: ")
# mapping_dir = input("Path of Mapping File: ")
data_dir = input("Path of Data: ")
data_dir = data_dir.replace("\\","/")
data_size = float(data_size)


# Data Validation ======================================

print(" \n****************************** \n\t Data Validation \n ******************************")

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


input(" \n Press enter to exit;")