__author__ = 'arnab'

# SMTP CONFIGURATION

SMTP_USERNAME = 'ME'
SMTP_PASSWORD = 'MYPASSWORD'
SMTP_HOST = 'WHOAMI'
SMTP_SENDER = 'NOREPLY@EXAMPLE.COM'

# POP3 CONFIGURATION

POP3_USERNAME = 'ME'
POP3_PASSWORD = 'MYPASSWORD'
POP3_SSL = 'WHOAMI'
POP3_RECEIVER = 'NOREPLY@EXAMPLE.COM'

# IMAP CONFIGURATION

IMAP_USERNAME = 'ME'
IMAP_PASSWORD = 'MYPASSWORD'
IMAP_SSL = 'WHOAMI'
IMAP_RECEIVER = 'NOREPLY@EXAMPLE.COM'

try:
    from _config import *  #my configuration
except:
    pass