\NOTE: Not Operational Yet, Check back in a week :).

ansible_appaware_mount
======================

This is a ansible role to perform Actifio AppAware mounts for Oracle DB, for UNIX/Linux like operating systems.

Requirements
------------

Oracle Binaries installed on the host. You can use "kosalaat.oracle_install" role from Ansible Galaxy, to install the Database. 

NOTE: for the Actifio AppAware mount would not need a DB created, for the above role, install_mode=INSTALL_DB_SWONLY would be enough.

Role Variables
--------------

Following variables are accepted/required for this role. 

| Variable Name  | Description | Required (Y/N) |
|----------------|---|---|
| act_appliance  | Actifio Appliance IP or FQDN. | Y               |
| act_user       | Actifio username. This should be a Actifio user with System Manage priviledges | Y
| act_pass       | Password for the Actifio User | Y
| act_vendorkey  | Vendor key can be obtained by the customer through opening a Support Case with the CSE. | Y
| ora_home       | Oracle Home Directory | Y
| ora_db_name    | Oracle DB Name, or the new SID | Y
| ora_tns_admin  | Oracle TNS_ADMIN path. If not specified would assume ORALCLE_HOME/network/admin | N


Example Playbook
----------------

Yet to come...

License
-------

Copyright 2018 <Kosala Atapattu kosala.atapattu@actifio.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.