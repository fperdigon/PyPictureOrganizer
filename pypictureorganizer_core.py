import glob
from datetime import datetime, timedelta
import os
import shutil


def analyze_un_org_folder(un_org_folder, file_ext='.jpg'):
    un_org_files_list = glob.glob(un_org_folder + '/**/*' + file_ext, recursive=True)
    un_org_files_list_final = []
    un_org_datetime_list = []


    for file in un_org_files_list:
        try:
            date_time_str = file.split('/')[-1].split('.')[0].split('IMG_')[-1].split('VID_')[-1].split('_')[0:2]
            date_time_str = date_time_str[0] + '_' + date_time_str[1][0:6]
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
            date_time_str = file.split('/')[-1].split('.')[0].split('IMG_')[-1].split('VID_')[-1].split('_')[0:2]
            date_time_str = date_time_str[0] + '_' + date_time_str[1][0:6]
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
            # print(folder)
            # print(date_time_str)
            pass

    return [org_folders_list, org_datetime_start_list, org_datetime_end_list]


def organize(un_org_folder, org_folder, extension='.jpg'):
    print('Starting Organization ' + extension + ' files')
    [un_org_files_list, un_org_datetime_list] = analyze_un_org_folder(un_org_folder, file_ext=extension)
    [org_folders_list, org_datetime_start_list, org_datetime_end_list] = analyze_org_folder(org_folder,
                                                                                            file_ext='.jpg')
    move_list = []
    t = datetime.strptime("6:00:00", "%H:%M:%S")
    min_time_delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
    t = datetime.strptime("00:00:00", "%H:%M:%S")
    max_time_delta = timedelta(hours=t.hour, minutes=t.minute, seconds=432000)  # 5d  432000  3d  259200

    for un_org_ind in range(len(un_org_files_list)):
        # Select the organized folder with smaller range
        folder_path = []
        folder_range = []
        for org_ind in range(len(org_folders_list)):
            # This if add the files that are between date start and date end
            if org_datetime_start_list[org_ind] < un_org_datetime_list[un_org_ind] and \
                un_org_datetime_list[un_org_ind] < org_datetime_end_list[org_ind]:
                if abs(org_datetime_start_list[org_ind] - org_datetime_end_list[org_ind]) < max_time_delta:
                    time_diff = org_datetime_end_list[org_ind] - org_datetime_start_list[org_ind]
                    folder_path.append(org_folders_list[org_ind])
                    folder_range.append(time_diff)
            # This if sentence add the files that are min_time_delta (6h) away eom date start and date end

            elif abs(org_datetime_start_list[org_ind] - un_org_datetime_list[un_org_ind]) < min_time_delta or \
                    abs(un_org_datetime_list[un_org_ind] - org_datetime_end_list[org_ind]) < min_time_delta:
                if abs(org_datetime_start_list[org_ind] - org_datetime_end_list[org_ind]) < max_time_delta:
                    folder_path.append(org_folders_list[org_ind])
                    folder_range.append(min_time_delta)

        if len(folder_range) > 0:
            selected_item = min(folder_range)
            selected_ind = folder_range.index(selected_item)
            folder, file = os.path.split(os.path.abspath(un_org_files_list[un_org_ind]))
            source_path = un_org_files_list[un_org_ind]
            dest_path = os.path.join(folder_path[selected_ind], file)

            move_list.append([source_path, dest_path])


    print(str(len(move_list)) + ' files will be organized!')


    for move in move_list:
        os.replace(move[0], move[1])

    f = open("move.txt", "a")
    for move in move_list:
        f.write(str(move) + '\n')
    f.close()


    print('Organization done')

