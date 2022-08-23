import glob
from datetime import datetime


def analyze_un_org_folder(un_org_folder, file_ext='.jpg' ):
    un_org_files_list = glob.glob(un_org_folder + '/**/*' + file_ext, recursive=True)
    un_org_datetime_list = []

    for file in un_org_files_list:
        date_time_str = file.split('/')[-1].split('.')[0]
        date_time_obj = datetime.strptime(date_time_str, '%Y%m%d_%H%M%S')
        un_org_datetime_list.append(date_time_obj)

    return [un_org_files_list, un_org_datetime_list]

def analyze_org_folder(un_org_folder, file_ext='.jpg'):
    org_files_list = glob.glob(un_org_folder + '/**/*' + file_ext, recursive=True)
    org_folders_list = []
    org_datetime_start_list = []
    org_datetime_end_list = []

    for file in org_files_list:
        folder = file

        date_time_str = file.split('/')[-1].split('.')[0]
        date_time_obj = datetime.strptime(date_time_str, '%Y%m%d_%H%M%S')
        un_org_datetime_list.append(date_time_obj)


def organize(un_org_folder, org_folder):