import os
import json
from PIL import Image

folder_format = '{:04d}'

#list of forehead bbox point
forehead= []

#iter from 0001 to 0100
for iter in range (1, 100 + 1):
    folder_name = folder_format.format(iter)
    json_path = os.path.join(r'C:\Users\MLPA\Desktop\NIA\NIA_num_100_data\example\01\01', folder_name)
    json_list = os.listdir(json_path)
    
    file_name = json_list[0]
    file_path = os.path.join(json_path, file_name)
    
    
    with open(file_path, 'r', encoding= 'utf-8') as f:
        data = json.load(f)
        value = data.get('images')
        
        
        #forehead bbox point 
        for key, value in value.items():
            if key == 'bbox':
                forehead.append(value)
                print(value)
    
    crop = forehead[iter - 1]
    x1, y1 = crop[0], crop[1]
    x2, y2 = crop[2], crop[3]
    
    img_path = os.path.join(r'C:\Users\MLPA\Desktop\NIA\NIA_num_100_data\masking\01', 
                              folder_name, f'{folder_name}_01_F.jpg')
    
    img = Image.open(img_path)
    
    cropped_img = img.crop((x1, y1, x2, y2))
    
    output_path = os.path.join(r'C:\Users\MLPA\Desktop\NIA\NIA_num_100_data\masking\01', 
                              folder_name, 'cropped_img')
    os.makedirs(output_path, exist_ok=True)
    
    output_path = os.path.join(output_path, f'{folder_name}_01_F_forehead.jpg')
    
    
    cropped_img.save(output_path)

   
    
             
    
    
    