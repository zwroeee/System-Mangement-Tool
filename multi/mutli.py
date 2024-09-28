import os
import subprocess
import shutil
import platform
import clipboard  # A library to copy text to the clipboard
from tkinter import messagebox, Tk

# ANSI escape sequences
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"


# You might need to install `pyperclip` for clipboard functionality:
# pip install pyperclip


class SystemOperations:
    @staticmethod
    def shutdown_system():
        os.system("shutdown /s /t 1")

    @staticmethod
    def restart_system():
        os.system("shutdown /r /t 1")

    @staticmethod
    def log_out():
        os.system("shutdown /l")

    @staticmethod
    def safe_mode_boot():
        print("Safe mode boot must be initiated through system settings. Use F8 during boot.")

    @staticmethod
    def check_windows_updates():
        subprocess.run("powershell -Command \"Get-WindowsUpdate -Install -AcceptAll\"", shell=True)


class CleanupOperations:
    @staticmethod
    def pc_cleanup():
        subprocess.run(["cleanmgr"])

    @staticmethod
    def remove_empty_folders(directory):
        for root, dirs, files in os.walk(directory):
            for d in dirs:
                folder_path = os.path.join(root, d)
                try:
                    os.rmdir(folder_path)
                    print(f"Removed empty folder: {folder_path}")
                except OSError:
                    pass  # Skip non-empty folders


class NetworkOperations:
    @staticmethod
    def create_static_ip_address(ip, netmask, gateway):
        config_cmd = f"netsh interface ip set address \"Local Area Connection\" static {ip} {netmask} {gateway}"
        os.system(config_cmd)

    @staticmethod
    def display_ip_address():
        subprocess.run("ipconfig")

    @staticmethod
    def display_host_name():
        print(platform.node())


class DiskOperations:
    @staticmethod
    def show_disks_and_sizes():
        subprocess.run("wmic logicaldisk get size,freespace,deviceid")

    @staticmethod
    def defragment_drives():
        os.system("defrag C:")


class DeviceInfo:
    @staticmethod
    def show_device_specifications():
        subprocess.run("systeminfo")

    @staticmethod
    def battery_info():
        if "battery" in platform.uname().hardware.lower():
            print("Generating battery report...")
            subprocess.run("powercfg /batteryreport /output battery_report.html")
            print("Battery report saved as battery_report.html")
        else:
            print("This device does not have a battery.")


class ManageWindows:
    @staticmethod
    def open_task_manager():
        os.system("taskmgr")

    @staticmethod
    def open_resource_monitor():
        os.system("resmon")

    @staticmethod
    def open_event_viewer():
        os.system("eventvwr")

    @staticmethod
    def open_control_panel():
        os.system("control")

    @staticmethod
    def open_device_manager():
        os.system("devmgmt.msc")

    @staticmethod
    def open_windows_settings():
        os.system("ms-settings:")

    @staticmethod
    def open_command_panel():
        os.system("cmd")

    @staticmethod
    def open_powershell():
        os.system("powershell")

    @staticmethod
    def open_system_configuration():
        os.system("msconfig")

    @staticmethod
    def open_registry_editor():
        os.system("regedit")

    @staticmethod
    def open_services():
        os.system("services.msc")

    @staticmethod
    def open_task_scheduler():
        os.system("taskschd.msc")

    @staticmethod
    def open_firewall():
        os.system("wf.msc")


class MBRtoGPT:
    @staticmethod
    def convert_mbr_to_gpt():
        print("To convert MBR to GPT, use Diskpart. This is a more complex operation.")


class Installer:
    @staticmethod
    def install_program(program_name):
        # Example installation command for common programs (this would require actual installers)
        program_paths = {
            "Notepad++": "C:\\Path\\To\\Notepad++\\installer.exe",
            # Add more programs here
        }
        if program_name in program_paths:
            subprocess.run(program_paths[program_name])
        else:
            print(f"Program {program_name} not found")

    @staticmethod
    def display_installer_options():
        options = [
            "1. Notepad++",
            # Add more options as needed
        ]
        print("Select a program to install:")
        for option in options:
            print(option)


class ClipboardUtility:
    @staticmethod
    def copy_text(text):
        clipboard.copy(text)
        print("Text copied to clipboard!")


class FileBackup:
    @staticmethod
    def backup_files(destination):
        directories = ['Desktop', 'Downloads', 'Pictures', 'Documents', 'Videos']
        user_profile = os.path.expanduser('~')  # Get the user directory
        for folder in directories:
            source = os.path.join(user_profile, folder)
            if os.path.exists(source):
                shutil.copytree(source, os.path.join(destination, folder), ignore=shutil.ignore_patterns('*.tmp'),
                                dirs_exist_ok=True)
                print(f"Backed up {folder} to {destination}")
            else:
                print(f"{folder} does not exist in {user_profile}")


class FFMPEGIntegration:
    @staticmethod
    def delete_audio_track(file_path, track_number):
        command = f"ffmpeg -i {file_path} -map 0 -c copy -vn -n output_{track_number}.mp4"
        os.system(command)  # Note: Adjust the command as necessary for your use case
        print(f"Deleted track {track_number} from {file_path}")


def print_banner():
    banner = f"""
==================================================================================
{RED}███▄ ▄███▓ █    ██ ▄▄▄█████▓ ██▓     ██▓   ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▓██▒▀█▀ ██▒ ██  ▓██▒▓  ██▒ ▓▒▓██▒    ▓██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▓██    ▓██░▓██  ▒██░▒ ▓██░ ▒░▒██░    ▒██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
▒██    ▒██ ▓▓█  ░██░░ ▓██▓ ░ ▒██░    ░██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
▒██▒   ░██▒▒▒█████▓   ▒██▒ ░ ░██████▒░██░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
░ ▒░   ░  ░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▓  ░░▓       ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
░  ░      ░░░▒░ ░ ░     ░    ░ ░ ▒  ░ ▒ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
░      ░    ░░░ ░ ░   ░        ░ ░    ▒ ░     ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
       ░      ░                  ░  ░ ░                  ░ ░      ░ ░      ░  ░{RESET}
==================================================================================
"""

    print(banner)


def print_menu():
    print("\nMenu")
    print("1. Shutdown System           2. Safe Mode Boot            3. Restart System            4. Log Out")
    print(
        "5. PC Clean Up               6. Remove Empty Folders      7. Convert MBR to GPT       8. Check for Windows Updates")
    print(
        "9. Create Static IP Address  10. Display IP Address       11. Display Host Name       12. Show All Disks and Sizes")
    print(
        "13. Show Device Specifications 14. Save and Display Battery Info 15. Open Task Manager   16. Open Resource Monitor")
    print(
        "17. Open Event Viewer        18. Open Control Panel       19. Open Device Manager     20. Open Windows Settings")
    print(
        "21. Open Command Panel       22. Open PowerShell         23. Open System Configuration 24. Open Registry Editor")
    print("25. Open Services            26. Open Task Scheduler      27. Defragment Drives       28. Open Firewall")
    print(
        "29. Install Programs         30. Copy Text to Clipboard   31. Backup Files            32. Edit Users and Groups")
    print("33. FFMPEG Delete Track      0. Exit")


def main_menu():
    print_banner()  # Display the custom banner at the start
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            SystemOperations.shutdown_system()
        elif choice == '2':
            SystemOperations.safe_mode_boot()
        elif choice == '3':
            SystemOperations.restart_system()
        elif choice == '4':
            SystemOperations.log_out()
        elif choice == '5':
            CleanupOperations.pc_cleanup()
        elif choice == '6':
            dir_path = input("Enter directory to remove empty folders: ")
            CleanupOperations.remove_empty_folders(dir_path)
        elif choice == '7':
            MBRtoGPT.convert_mbr_to_gpt()
        elif choice == '8':
            SystemOperations.check_windows_updates()
        elif choice == '9':
            ip = input("Enter IP Address: ")
            netmask = input("Enter Netmask: ")
            gateway = input("Enter Gateway: ")
            NetworkOperations.create_static_ip_address(ip, netmask, gateway)
        elif choice == '10':
            NetworkOperations.display_ip_address()
        elif choice == '11':
            NetworkOperations.display_host_name()
        elif choice == '12':
            DiskOperations.show_disks_and_sizes()
        elif choice == '13':
            DeviceInfo.show_device_specifications()
        elif choice == '14':
            DeviceInfo.battery_info()
        elif choice == '15':
            ManageWindows.open_task_manager()
        elif choice == '16':
            ManageWindows.open_resource_monitor()
        elif choice == '17':
            ManageWindows.open_event_viewer()
        elif choice == '18':
            ManageWindows.open_control_panel()
        elif choice == '19':
            ManageWindows.open_device_manager()
        elif choice == '20':
            ManageWindows.open_windows_settings()
        elif choice == '21':
            ManageWindows.open_command_panel()
        elif choice == '22':
            ManageWindows.open_powershell()
        elif choice == '23':
            ManageWindows.open_system_configuration()
        elif choice == '24':
            ManageWindows.open_registry_editor()
        elif choice == '25':
            ManageWindows.open_services()
        elif choice == '26':
            ManageWindows.open_task_scheduler()
        elif choice == '27':
            DiskOperations.defragment_drives()
        elif choice == '28':
            ManageWindows.open_firewall()
        elif choice == '29':
            Installer.display_installer_options()
            program_name = input("Enter program to install: ")
            Installer.install_program(program_name)
        elif choice == '30':
            text_to_copy = input("Enter text to copy to clipboard: ")
            ClipboardUtility.copy_text(text_to_copy)
        elif choice == '31':
            backup_dest = input("Enter backup destination folder: ")
            FileBackup.backup_files(backup_dest)
        elif choice == '32':
            print("Edit Users and Groups functionality is not implemented yet.")
        elif choice == '33':
            audio_file = input("Enter the path of the audio file: ")
            track_number = input("Enter the track number to delete: ")
            FFMPEGIntegration.delete_audio_track(audio_file, track_number)
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main_menu()