#!/usr/bin/env python3
#
# Writen by Pongsakorn
#
# This is free software, licensed under the MIT License.
# See /LICENSE for more information.
#

import conf.conf as conf


def full_scan():
    print("===========================================================")
    print(conf.colored(conf.text2art("Full Scan", "small"), "cyan"))
    print("===========================================================")

    full_host = input(
        conf.colored("\nEnter the target URL (i.e. opensource.com) : ", "green", attrs=["bold"]))
    full_output = input(
        conf.colored(
            f"Enter the output folder - [default: reports/Fullscan/{full_host}/]: ",
            "green",
            attrs=["bold"],
        ))

    conf.not_valid(full_scan, full_host)
    full_output = conf.dir_output(full_output, "reports/Fullscan", full_host)

    conf.create_dir(full_output)

    full_ip = conf.socket.gethostbyname(full_host)

    print(
        "___________________________________________________________________________"
    )

    conf.create_dir(full_output)

    gnome_installed = True if conf.os.path.exists(
        "/usr/bin/gnome-terminal") else False

    if len(full_host) == 0:
        conf.clear()

        print("Not Valid Choice Try again")
        conf.re_open()

        conf.full_host = None
    elif gnome_installed:
        conf.os.system(
            f"gnome-terminal -- bash -c 'nmap -A {full_ip} -o \"{full_output}/nmap.txt\" && bash'"
        )
        conf.clear()

        conf.os.system(
            f"gnome-terminal -- bash -c 'python3 {conf.home}/.local/share/dirsearch/dirsearch.py -u {full_host} --format plain -o \"{full_output}/dirsearch.txt\" && bash'"
        )
        conf.clear()

        conf.os.system(
            f"gnome-terminal -- bash -c 'nikto +h {full_host} -output \"{full_output}/nikto.txt\" && bash'"
        )
        conf.clear()

        conf.os.system(f"wpscan --url {full_host} --output {full_host}/wpscan.txt")
        conf.clear()

    else:
        conf.os.system(f"nmap -A {full_host} -o {full_output}/nmap.txt -oX {full_output}/nmap.xml")

    
        conf.os.system(f"nmap -sV --script=http-enum {full_host} -o {full_output}/nmap_http-enum.txt -oX {full_output}/nmap_http-enum.xml")
        conf.os.system(f"sslscan --xml={full_output}/sslscan.xml --no-colour {full_host} > {full_output}/sslscan.txt")
        conf.os.system(f"nikto +h {full_host} -output {full_output}/nikto.txt")
    
        conf.os.system(f"cmseek -u {full_host} > {full_output}/cmseek.txt")
    
    
        #conf.os.system(f"wpscan --url {full_host} -f cli-no-color --output {full_output}/wpscan.txt")
        conf.os.system(f"wpscan --url {full_host} -f cli-no-color --output {full_output}/wpscan.json --format json")
        conf.os.system(f"nmap -sV --script http-wordpress-enum {full_host} -o {full_output}/nmap_wp-enum.txt -oX {full_output}/nmap_wp-enum.xml")
        
    

        
        conf.os.system(f"perl ./modules/joomscan/joomscan.pl -u {full_host}")
        
    
        
        conf.os.system(f"droopescan scan drupal -o json -u {full_host} > {full_output}/drup.json")
        conf.os.system(f"nmap --script http-drupal-enum {full_host} -o {full_output}/nmap_drup-enum.txt -oX {full_output}/nmap_drup-enum.xml")
    
        
    

        conf.os.system(f"python3 ~/.local/share/dirsearch/dirsearch.py -u {full_host} --format json -o '{full_output}/dirsearch.json'")

