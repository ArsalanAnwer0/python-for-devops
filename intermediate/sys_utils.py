# Blue Print / Template
import os
import platform
import subprocess

class Utilities:
    
    def show_disk_space(self):
        try:
            if platform.system() == "Windows":
                
                result = subprocess.run(["wmic", "logicaldisk", "get", "size,freespace,caption"], 
                                      capture_output=True, text=True)
                print(result.stdout)
            else:
                
                os.system("df -h")
        except Exception as e:
            print(f"Error showing disk space: {e}")
    
    def show_ram(self):
        try:
            if platform.system() == "Windows":
                
                result = subprocess.run(["wmic", "OS", "get", "TotalVisibleMemorySize,FreePhysicalMemory"], 
                                      capture_output=True, text=True)
                print(result.stdout)
            else:
               
                os.system("free -h")
        except Exception as e:
            print(f"Error showing RAM info: {e}")
    
    def show_sys_details(self):
        try:
            
            system_name = platform.system()
            print(f"Operating System: {system_name}")
            print(f"Platform: {platform.platform()}")
            print(f"Architecture: {platform.architecture()[0]}")
        except Exception as e:
            print(f"Error showing system details: {e}")
        
machine_a = Utilities() # object
machine_a.show_disk_space() 
machine_b = Utilities() # object
machine_b.show_ram()
machine_c = Utilities()
machine_c.show_sys_details()