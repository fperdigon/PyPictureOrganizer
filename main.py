# This software organize pictures from unorganized folders to organized ones.
# Useful when you organize your pictures from your phone and then your mate
# or friend gives you a bunch of pictures from past date

import pypicureorganizer_core

un_org_folder = '/media/fco/DATA/Cloud/Fotos_Org/Org 2018/'
org_folder = '/media/fco/DATA/Cloud/Fotos/'

pypicureorganizer_core.organize(un_org_folder, org_folder)