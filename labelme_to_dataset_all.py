#import subprocess
import os
import pdb

classPath = "/home/yxq/Desktop/segementation/"

i = 0

    
for files in os.walk(classPath):
        for fileName in files[2]:
            fileName.replace("\n", "")
           
            cmd = 'labelme_json_to_dataset' + ' '+ classPath + '/'+fileName
            #cmd = 'pwd'
            #os.chdir('/home/yxq/Desktop/json/')
            #subprocess.call(['cd /home/ymh',cmd])
            #os.system('cd /home/ymh')
            os.system(cmd)
            #subprocess.check_output(cmd)  
            #pdb.set_trace()
            i += 1

