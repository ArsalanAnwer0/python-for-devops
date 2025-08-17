import os
import platform

print(dir(os))


system_name = platform.system()
if system_name == "Darwin":
    print("Using MAC")
elif system_name == "Windows":
    print("Using Windows")
elif system_name == "Linux":
    print("Using Linux")
else:
    print(f"Using {system_name}")

def check_os(opsystem):
    if opsystem == "Windows":
        print("Switch to Linux")
    elif opsystem == "Linux" or opsystem == "Mac":
        print("You are good to go!")
        

# for i in range(1,5):
#     check_os("Mac")