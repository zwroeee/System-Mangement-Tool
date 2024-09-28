# System Management Tool

A comprehensive system management tool written in Python that allows users to monitor system performance, manage files, control user accounts, and perform various administrative tasks.

## Features

- **Scheduled Tasks**
  - Schedule shutdowns and other tasks.

- **Disk Cleanup Options**
  - Temporary file cleanup.
  
- **Security Features**
  - Manage Windows Firewall settings.
  
- **File Management**
  - Batch file renaming.
  - Duplicate file finder.
  
- **User Account Management**
  - Change user roles and manage accounts.
  
- **System Backup and Restore**
  - Create full backups of the system.

- **Automation Scripts**
  - Execute custom scripts easily.
  
- **Health Checks and Diagnostics**
  - Generate system health reports.
 
 ![Captudddre](https://github.com/user-attachments/assets/96d8650c-4c39-49d3-a68d-fafacb8c7350)

## Requirements

To run this project, you need:

- Python 3.x
- Required libraries:
  - `psutil`
  - `schedule`

You can install the required libraries using pip:

```bash
pip install psutil schedule
```

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/zwroeee/system-management-tool.git
   ```

2. Change directory to the project folder:

   ```bash
   cd system-management-tool
   ```

3. Run the main script:

   ```bash
   python main.py
   ```

### Examples

- To monitor system resource usage:

```python
from system_monitor import SystemMonitor
SystemMonitor.display_resource_usage()
```

- To perform a disk cleanup:

```python
from disk_cleanup import DiskCleanup
DiskCleanup.clear_temp_files()
```

- To find duplicate files in a directory:

```python
from duplicate_finder import DuplicateFinder
DuplicateFinder.find_duplicates("path/to/directory")
```

- To change a user's role:

```python
from user_account_management import UserAccountManagement
UserAccountManagement.change_user_role("username", "admin")
```

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/MyFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/MyFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes
- Be sure to replace `yourusername` in the clone URL with your actual GitHub username.
- Adjust any paths, descriptions, or installations steps specific to your project. 

Feel free to customize this README further as per your project’s requirements! If you have any other specific sections you'd like to add or modify, let me know!
