#!/usr/bin/env python

import cv2
import json

img = cv2.imread('nyan.png')
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(hsv)

h = (h * (100.0 / 180.0)).astype(int)
s = (s * (100.0 / 255.0)).astype(int)
v = (v * (100.0 / 255.0)).astype(int)

color_data = h.flatten().tolist()
brightness_data = v.flatten().tolist()
saturation_data = s.flatten().tolist()

project_file = None

with open('Painter/project.json') as f:
    project_file = json.load(f)

for key in project_file['targets'][0]['lists']:
    if project_file['targets'][0]['lists'][key][0] == 'ColorData':
        project_file['targets'][0]['lists'][key][1] = color_data
    if project_file['targets'][0]['lists'][key][0] == 'BrightnessData':
        project_file['targets'][0]['lists'][key][1] = brightness_data
    if project_file['targets'][0]['lists'][key][0] == 'SaturationData':
        project_file['targets'][0]['lists'][key][1] = saturation_data

with open('Painter/project.json', 'w') as f:
    json.dump(project_file, f)
