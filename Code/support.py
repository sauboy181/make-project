from csv import reader
from os import walk #Walk through the file system
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map,delimiter = ",")
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_folder(path):
    surface_list = [] #Import all these lists

    for _,__, img_files in walk(path): #Folder name 
        for image in img_files: 
            if '.png' not in image:
                continue
            full_path = path + "/" + image #Path to image used to import image
            # print(full_path)
            image_surf = pygame.image.load(full_path).convert_alpha() #Import image (Surface)
            surface_list.append(image_surf) #add to surface_list
        return surface_list
