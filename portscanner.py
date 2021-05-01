import socket
from IPy import IP
import pyfiglet

try:
    # banner design
    ascii_banner = pyfiglet.figlet_format("HushScan" + "\n")

    # scanning port
    def scan(target,port_num):
        converted_ip = check_ip(target)
        
        print('\n' + '[ Scanning Target - ' +str(target)  +' ]' + '\n')    
        for port in range(1,port_num):
            scan_port(converted_ip,port)
        print("\n" + "Scan Completed!" + '\n')    

    #convert domain to IP
    def check_ip(ip):
        try:
            IP(ip)
            return(ip)

        except ValueError:
            return socket.gethostbyname(ip)

    #banner grab
    def get_banner(s):
        return s.recv(1024)

    #Connecting socket
    def scan_port(ipaddr, port):
        try:
            sock = socket.socket()
            
            #scan time
            if scan_type == 'Intense':
                sock.settimeout(0.8)
            elif scan_type == 'Normal':   
                sock.settimeout(0.5)
            elif scan_type == 'Fast':   
                sock.settimeout(0.2)
            else:  
                sys.exit()

            sock.connect((ipaddr, port))
            try:
                banner = get_banner(sock)
                print("[+] Found Open Port " + str(port) + " : " + str(banner.decode().strip('\n')))
            except:
                print("[+] Found Open Port " + str(port))
        except:
            pass

    #loop through multiple targets
    if __name__ == "__main__":
        
        #printing banner
        print(ascii_banner)
        print(" --- A Port Scanning Tool --- " + "\n" )
        print("-" * 60)
    
        #taking inputs
        print("Enter the Target/s to scan (split multple with ',') : ")
        targets = input(' ')

        print('\n' + 'Enter the numbers of ports you want to scan (Eg. 500 will scan first 500 ports) : ')
        port_num = int(input(' '))

        print('\n' + 'Enter the speed of scan (Eg. Intense, Normal, Fast | Normal is recommended for more precise results) : ')
        scan_type = input(' ')
        
        print("-" * 60)

        #looping through multiple targets   
        if ',' in targets:
            for ip_add in targets.split(','):
                    scan(ip_add.strip(' '),port_num)                
        else:
            scan(targets,port_num)

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    exit()

except socket.error:
    print("Couldn't connect to server")
    exit()