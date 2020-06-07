#!/bin/sh
set -e
python ../../Python/SKBB-Solidstep-install/make_ansible_hosts.py
cp /etc/ansible/hosts /etc/ansible/hosts.bak
rm -rf /etc/ansible/hosts
mv ../../Temporary/hosts /etc/ansible/
#ansibl-playbook ../../Ansible/SKBB-Solidstep-install/playbook.yml
ansible -m ping all