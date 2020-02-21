from ansible import context
from ansible.cli import CLI
from ansible.module_utils.common.collections import ImmutableDict
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager

loader = DataLoader()

inventory = InventoryManager(loader=loader, sources=('/ansible/provision/inventory/myhost'))

context.CLIARGS = ImmutableDict(tags={}, listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh',
                    module_path=None, forks=100, remote_user='root', private_key_file=None,
                    ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True,
                    become_method='sudo', become_user='root', verbosity=True, check=False, start_at_task=None)


variable_manager = VariableManager(loader=loader, inventory=inventory, version_info=CLI.version_info(gitinfo=False))

pbex = PlaybookExecutor(playbooks=['/ansible/provision/maria.yml'], inventory=inventory,  loader=loader , variable_manager=variable_manager , passwords={} )

results = pbex.run()




print ('Services that can be installed by this script:', '\n', 'keystone, nova ,compute,  cinder ,horizon '  ,'\n' )

first_input = input( 'Enter the service to be installed:')
services = ('mohammad' , 'ali' )
storage = ('storage')
compute = ('compute')


if first_input in services:
    ip = input('please enter ip')
    f = open("demofile3.txt", "w")
    f.write("Woops! I have deleted the content!" + '\n' + "sdfsdf"+ '\n'+ "[dd]" + '\n'+ "127.0.0.1" + first_input)
    f.close()
    exit ('ooops')
    print('hello')



elif first_input in storage:
    ip = input('please enter ip')
    types = input('what type is it (1 or 2)')
    if types == ('1'):

    elif types == ('2'):

    else:




elif first_input in compute :
    ip = input('please enter ip')
    types = input('what type is it (1 or 2)')
    if types == '1':

    elif types == '2':

    else:



