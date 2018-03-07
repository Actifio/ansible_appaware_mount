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

| Variable Name    | Description | Required (Y/N) |
|------------------|---|---|
| act_appliance    | Actifio Appliance IP or FQDN. | Y               |
| act_user         | Actifio username. This should be a Actifio user with System Manage priviledges | Y
| act_pass         | Password for the Actifio User | Y
| act_vendorkey    | Vendor key can be obtained by the customer through opening a Support Case with the CSE. | Y
| act_restoretime  | Desired time to recover the database to. Based on the time specified, the appropriate image will be selected (if an image is not specified). If a recovery image is not availble for the stipulated restore time, and if the strict_policy is set to no, then the closest image to the restore time will be selected. | N
| strict_policy    | See act_restoretime | N
| act_dest_host    | Destination host to mount the database. If not specified, it will default to the ansible_host | N
| act_appname 	   | Application name | Y
| act_src_host 	   | Source host where the application is protected from. | Y
| act_job_class    | snapshot, dedup, dedupasync, liveclone, syncback and OnVault. If not specified would select any based on the Restore time, without any preference to the jobclass. | N
| ora_home         | Oracle Home Directory | Y
| ora_db_name      | Oracle DB Name, or the new SID | Y
| ora_tns_admin    | Oracle TNS_ADMIN path. If not specified would assume ORALCLE_HOME/network/admin | N
| ora_db_mem       | Amount of memory to be set as the Memory Target. Defaults to 512MB. | N
| ora_sga_pct 	   | Percentage of SGA form the total memory. | N
| ora_redo_size    | Redo Log size in MB, defaults to 500. | N
| ora_shared_pool 	| Oracle Shared Pool size. | N
| ora_db_cache_size 	| Oracle DB Cache size. | N
| ora_recover_dest_size	| Oracle Parameter db_recover_dest_size. Defaults to 5000. | N
| ora_diagnostic_dest 	| Oracle Diagnostic Destination. | N
| ora_nprocs    	| Num of Max processes. | N
| ora_open_cursors 	| Number of open_cursors. defaults to 1000. | N
| ora_char_set 	| Characterset. Defaults to 'AL32UTF8'. | N
| ora_tns_ip 	| TNS IP Address. | N
| ora_tns_port 	| TNS Port. | N
| ora_tns_domain 	| TNS Domain. | N
| ora_no_nid 	| Do not change the DBID of the new clone. Will maintain same DBID as the source. Defaults to FALSE. | N
| ora_no_tns_update 	| Do not update TNS records. Defaults to FALSE. | N
| ora_restore_recov 	| Recover the oracle database. Defaults to TRUE. | N
| ora_no_rac 	| Treat as Oracle RAC. Defaults to TRUE. | N

Example Playbook
----------------

```
- name: testng mount points
  hosts: "{{ host_group }}"
  become: yes
  become_method: sudo
  roles:
    - { role: ansible_appaware_mount, act_appliance: my-actifio, act_user: ansible, act_pass: mypassword }
  vars:
    act_vendorkey: "{{ contact CSE to get yours }}"
    act_dest_host: "my-dev-server"
    act_appname: "BEAST"
    act_src_host: "beast-host"
    act_job_class: "OnVault"
    ora_home: "/u01/app/oracle/product/11.2.0/ora_1"
    ora_db_name: "MYDEVBEAST" 
```

License
-------

Copyright 2018 <Kosala Atapattu kosala.atapattu@actifio.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
