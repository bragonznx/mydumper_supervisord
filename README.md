# mydumper_supervisord

This script backup the schema of a MariaDB / MySQL with Mysqldump

After that the script is doing a full backup for all databases with mydumper

The script is running a cleaning for the old files and do an archive each week

*Setup*

Configure the list of MySQL serveur to backup in configuration.py

Launch run.py within supervisord with the configuration gave as exemple into supervisor directory

<code> sudo mkdir -p /var/log/mydumper </code>

<code> ln -s /coderepository/mydumper_supervisord/bkp_mydumper /usr/bin/bkp_mydumper </code>

<code> chmod +x /usr/bin/bkp_mydumper </code>

<code> cp supervisor/bkp_mydumper.conf /etc/supervisor/conf.d/ </code>


*dependancy*

python3

mailx

mydumper / mysqldump (commint usualy with mysql-client or mariadb-client)


*On MYSQL/MariaDB/Percona to backup*
<code>
% mysql --user=root mysql
CREATE USER 'mydumper'@'ip_of_mydumper_server' IDENTIFIED BY 'toor';
GRANT ALL PRIVILEGES ON *.* TO 'mydumper'@'ip_of_mydumper_server' WITH GRANT OPTION;
</code>
