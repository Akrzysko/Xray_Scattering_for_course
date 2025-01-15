# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:35:16 2021

@author: anthony.krzysko
"""
### takes in a folder path to detector output files
from pathlib import Path
import re
from xray_scattering_tools.gsd_detector import GsdOutput
from xray_scattering_tools.point_detector_new import PointOutput
import pandas as pd


# directory_in_str = r"C:\Users\Anthony.Krzysko\Documents\Data\2021-0809_compton_strip_11IDC\sep_bat_charged"
# directory_in_str = r"C:\Users\Anthony.Krzysko\Documents\Data\2021-0422 Compton Scattering\all_data\Krzysko_2\2021-0415 compton\vertical_Li_scan_renamed"

def get_detector_objects_from_folder(folder_path, detector_type, incident_energy=105.7, angle=88):
    pathlist = Path(folder_path).rglob("*")
    file_list = []
    imported_object_list = []

    for path in pathlist:
         # because path is object not string
         path_in_str = str(path)
         file_list.append(path_in_str)
         
    # file_list_sorted = sorted(file_list, key=lambda x: int(re.search(r'\d+$',x).group()))
    file_list_sorted = file_list
    # file_list_sorted = sort_nicely(list(file_list))
    i=0
    for file in file_list_sorted:
        i += 1
        if detector_type == "gsd":
            imported_object = GsdOutput(file, incident_energy=incident_energy, angle=angle)
            if imported_object.meta_data["total_counts"] > 0:
                imported_object_list.append(imported_object)
        elif detector_type == "point":
            imported_object = PointOutput(file, incident_energy=incident_energy, angle=angle)
            imported_object_list.append(imported_object)
            
        
    return imported_object_list

def get_dataframe_from_objects_list(obj_list):
    first_obj = obj_list[0]
    df = pd.DataFrame(list(first_obj.meta_data.items()), columns=["meta data key", first_obj.meta_data["scan_name"]])
    for obj in obj_list[1:]:
        df[obj.meta_data["scan_name"]] = list(obj.meta_data.values())
        
    return(df)
    
    
    
    
# obj_list = get_detector_objects_from_folder(directory_in_str, "point")

# for obj in obj_list:
#     print(obj.meta_data["file_path"])