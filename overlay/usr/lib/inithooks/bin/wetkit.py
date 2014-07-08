#!/usr/bin/python
"""Set Wetkit admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import sys
import getopt

from dialog_wrapper import Dialog
from mysqlconf import MySQL

from executil import system

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError, e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Wetkit Password",
            "Enter new password for the Wetkit 'admin' account.  Be sure that it meets the password policy for WET: must contain one each of lowercase, uppercase, digit;  must be at least 8 characters in length;  must contain at least 2 letters.",
            "^(?=(.*\d){2})(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z\d]).{8,}$")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "Wetkit Email",
            "Enter email address for the Wetkit 'admin' account.",
            "admin@example.com")

    m = MySQL()
    m.execute('UPDATE wetkit.users SET mail=\"%s\" WHERE name=\"admin\";' % email)
    m.execute('UPDATE wetkit.users SET init=\"%s\" WHERE name=\"admin\";' % email)
    system("/usr/bin/drush --root=/var/www/wetkit variable-set site_mail %s" % email)
    system("/usr/bin/drush --root=/var/www/wetkit variable-set update_notify_emails %s" % email)
    system("/usr/bin/drush --root=/var/www/wetkit user-password admin --password='%s'" % password)
	
if __name__ == "__main__":
    main()

