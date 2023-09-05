import os
import json

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
            if key=='bbox':
                forehead.append(value)
                print(value)
                

print(forehead)   
                