def get_hosts():
    selected_hosts = []
    for host in raw_input("Hosts (eg: 0 1): ").split():
        selected_hosts.append(env.hosts[int(host)])
    return selected_hosts
    
def menu():
    for num, desc in enumerate(["List Hosts", "Run Command", "Open Shell", "Exit"]):
        print "[" + str(num) + "] " + desc
        
     choice = int(raw_input('\n' + PROMPT))
     while (choice != 3):
         list_hosts()
         
         if choice == 1;
         cmd = raw_input("Command: ")
         
         for host, result in execute(run_command, cmd, hosts=get_hosts()).iteritems():
             print"[" + host + "]: " + cmd
             print ('_' * 80) + '\n' + result + '\n'
             
         elif choice == 2:
             host = int(raw_input("Host: "))
             execute(open_shell, host=env.hosts[host])
         for enum, desc in enumerate(["List Hosts", "Run Command", "Open Shell", "Exit"]):
             print"[" + str(num) + "]" + desc
         choice = int(raw_input('\n' + PROMPT))
         
if __name__ == "__main__":
    fill_hosts()
    check_hosts()
    menu()
    