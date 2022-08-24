# This software organize pictures from unorganized folders to organized ones.
# Useful when you organize your pictures from your phone and then your mate
# or friend gives you a bunch of pictures from past date

import pypictureorganizer_core

un_org_folder = '/media/fco/DATA/Cloud/Fotos_Org/'
org_folder = '/media/fco/DATA/Cloud/Fotos/'

pypictureorganizer_core.organize(un_org_folder, org_folder, extension='.jpg')
pypictureorganizer_core.organize(un_org_folder, org_folder, extension='.mkv')
pypictureorganizer_core.organize(un_org_folder, org_folder, extension='.mp4')