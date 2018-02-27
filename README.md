# mydumper_supervisord

This script backup the schema of a MariaDB / MySQL with Mysqldump
After that the script is doing a full backup for all databases with mydumper
The script is running a cleaning for the old files and do an archive each week

*Setup*
Configure the timming of the backup inside conf.py
Launch run.py within supervisord with the configuration gave as exemple into supervisor directory
