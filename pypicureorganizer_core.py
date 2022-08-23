import glob
from datetime import datetime
import os


def analyze_un_org_folder(un_org_folder, file_ext='.jpg'):
    un_org_files_list = glob.glob(un_org_folder + '/**/*' + file_ext, recursive=True)
    un_org_files_list_final = []
    un_org_datetime_list = []


    for file in un_org_files_list:
        try:
            date_time_str = file.split('/')[-1].split('.')[0].split('_')[0:2]
            date_time_str = date_time_str[0] + '_' + date_time_str[1]
            date_time_obj = datetime.strptime(date_time_str, '%Y%m%d_%H%M%S')
            un_org_datetime_list.append(date_time_obj)
            un_org_files_list_final.append(file)
        except:
            pass

    return [un_org_files_list_final, un_org_datetime_list]

def analyze_org_folder(org_folder, file_ext='.jpg'):
    org_files_list = glob.glob(org_folder + '/**/*' + file_ext, recursive=True)
    org_folders_list = []
    org_datetime_start_list = []
    org_datetime_end_list = []

    for file in org_files_list:

        try:
            folder, _ = os.path.split(os.path.abspath(file))
            date_time_str = file.split('/')[-1].split('.')[0].split('_')[0:2]
            date_time_str = date_time_str[0] + '_' + date_time_str[1]
            date_time_obj = datetime.strptime(date_time_str, '%Y%m%d_%H%M%S')

            if folder in org_folders_list:
                folder_ind = org_folders_list.index(folder)
                if date_time_obj < org_datetime_start_list[folder_ind]:
                    org_datetime_start_list[folder_ind] = date_time_obj
                if date_time_obj > org_datetime_end_list[folder_ind]:
                    org_datetime_end_list[folder_ind] = date_time_obj

            else:

                org_folders_list.append(folder)
                org_datetime_start_list.append(date_time_obj)
                org_datetime_end_list.append(date_time_obj)
        except:
            pass

    return [org_folders_list, org_datetime_start_list, org_datetime_end_list]


def organize(un_org_folder, org_folder):
    [un_org_files_list, un_org_datetime_list] = analyze_un_org_folder(un_org_folder, file_ext='.jpg')
    [org_folders_list, org_datetime_start_list, org_datetime_end_list] = analyze_org_folder(org_folder,
                                                                                            file_ext='.jpg')
    print('DEBUG')

