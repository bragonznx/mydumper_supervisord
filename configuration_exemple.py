## settings the MySQL servers to backup here
#mysql = ['hostname','user','password','daily']
## rename me into configuration.py

MYSQL_BINARY = '/usr/bin/bkp_mydumper' # dumper binary here, example: /usr/bin/mysqldump

servers = {
        'mysql1': ['mysql1.bragon.info', 'define_user', 'password', '43200'], #every 12h
        'mysql2': ['mysql2.bragon.info', 'define_user', 'password', '3600'], #every hours
        'mysql3': ['mysql3.bragon.info', 'bragonette', 'BragonPass3', '86400'] #every day
}
