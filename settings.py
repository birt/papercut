#!/usr/bin/env python
# Copyright (c) 2002 Joao Prado Maia. See the LICENSE file for more information.
# $Id: settings.py,v 1.14 2002-08-02 05:33:05 jpm Exp $
import time
import sys
import os

#
# The following configuration settings should be pretty self-explanatory, but
# please let me know if this is not complete or if more information / examples
# are needed.
#

#
# GENERAL PATH INFORMATION
#

# full path for where Papercut will store the log file
log_path = "/home/papercut/logs/"
# the actual log filename
log_file = log_path + "papercut.log"


#
# HOSTNAME / PORT OF THE SERVER
#

# hostname that Papercut will bind against
nntp_hostname = 'nntp.domain.com'
# usually 119, but use 563 for an SSL server
nntp_port = 119

# type of server ('read-only' or 'read-write')
server_type = 'read-write'


#
# NNTP AUTHENTICATION SUPPORT
#

# does the server need authentication ? ('yes' or 'no')
nntp_auth = 'no'
# backend that Papercut will use to authenticate the users
auth_backend = ''
# needed for phorum_mysql_users auth module
PHP_CRYPT_SALT_LENGTH = 2


#
# STORAGE MODULE
#

# backend that Papercut will use to get (and store) the actual articles content
storage_backend = "phorum_mysql"

# for the forwarding_proxy backend, set the next option to the remote nntp server
forward_host = 'news.remotedomain.com'


#
# PHORUM STORAGE MODULE OPTIONS
#

# full path to the directory where the Phorum configuration files are stored
phorum_settings_path = "/home/papercut/www/domain.com/phorum_settings/"
# the version for the installed copy of Phorum
phorum_version = "3.3.2a"

# configuration values for 'backends/phorum_mysql.py'
# database connection variables
dbhost = "localhost"
dbname = "phorum"
dbuser = "anonymous"
dbpass = "anonymous"



# check for the appropriate options
if nntp_auth == 'yes' and auth_backend == '':
    sys.exit("Please configure the 'nntp_auth' and 'auth_backend' options correctly")

# check for the trailing slash
if phorum_settings_path[-1] != '/':
    phorum_settings_path = phorum_settings_path + '/'


# helper function to log information
def logEvent(msg):
    f = open(log_file, "a")
    f.write("[%s] %s\n" % (time.strftime("%a %b %d %H:%M:%S %Y", time.gmtime()), msg))
    f.close()
