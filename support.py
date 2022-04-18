from csv import reader
from os import walk # walk through the file system
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map,delimiter = ",")
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_folder(path):
    surface_list = [] # import all these lists

    for _,__, img_files in walk(path): # folder name 
        for image in img_files: 
            full_path = path + "/" + image # path to image used to import image
            image_surf = pygame.image.load(full_path).convert_alpha() # import image (surface)
            surface_list.append(image_surf) # add to surface_list
        return surface_list
