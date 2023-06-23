# CLEANER OS

It is a small script to remove junk files from our windows operating system such as logs or temporary files that fill our storage.

## Used technologies

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PowerShell](https://img.shields.io/badge/PowerShell-%235391FE.svg?style=for-the-badge&logo=powershell&logoColor=white)

## Supported operating systems

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

## Install

1 - Download the repository.

2 - Change the path to your download folder in the file **cleanOS.py**.

3 - According to your operating system open the  cleanOS file with the extension .bat (windows) with a text editor.

4 - Change the path to the address where the project is downloaded.

## Run

1 - Click on the modified .bat file with the path to your download folder.

## Automatic task (Optional)

1 - Open the Task Scheduler. You can look for it in the Start menu or open it from the Control Panel.

2 - In the left navigation pane, select "Create task".

3 - In the "General" tab, assign a descriptive name to the task in the "Name" field.

4 - Go to the "Triggers" tab and click "New" to configure the task execution frequency.

5 - In the "Actions" tab, click on "New" and select "Start a program". Enter the full path to the Python interpreter followed by the full path to the Python script file you wish to run.

6 - Configure any additional options you want for the task, such as conditions and advanced settings.

7 - Click "OK" to save the scheduled task.
