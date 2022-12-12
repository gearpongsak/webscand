#!/usr/bin/env python3
#
# Writen by Pongsakorn
#
# This is free software, licensed under the MIT License.
# See /LICENSE for more information.
#

import conf.conf as conf


def auto_scan():
    print("==============================================")
    print(conf.colored(conf.text2art("Auto Scan", "small"), "cyan"))
    print("==============================================")

    auto_host = input(
        conf.colored("\nEnter target: ", "green", attrs=["bold"]))
    auto_output = input(
        conf.colored(
            f"Enter the output folder - [default: reports/Autoscan/{auto_host}/]: ",
            "green",
            attrs=["bold"],
        ))

    conf.not_valid(auto_scan, auto_host)
    auto_output = conf.dir_output(auto_output, "reports/Autoscan", auto_host)

    conf.create_dir(auto_output)

    if len(auto_host) == 0:
        conf.clear()

        print("Not Valid Choice Try again")
        conf.re_open()

    else:
        conf.os.system(f"nmap -A {auto_host} -o {auto_output}/nmap.txt -oX {auto_output}/nmap.xml")

        if '80/tcp' in open(f"reports/Autoscan/{auto_host}/nmap.txt").read():
            conf.os.system(f"nmap -sV --script=http-enum {auto_host} -o {auto_output}/nmap_http-enum.txt -oX {auto_output}/nmap_http-enum.xml")

        if '443/tcp' in open(f"reports/Autoscan/{auto_host}/nmap.txt").read():
            conf.os.system(f"sslscan --xml={auto_output}/sslscan.xml --no-colour {auto_host} > {auto_output}/sslscan.txt")
    
        conf.os.system(f"nikto -h {auto_host} -output {auto_output}/nikto.txt")

        conf.os.system(f"cmseek -u {auto_host} > {auto_output}/cmseek.txt")
    
        if 'WordPress' in open(f"reports/Autoscan/{auto_host}/cmseek.txt").read():
            #conf.os.system(f"wpscan --url {auto_host} -f cli-no-color --output {auto_output}/wpscan.txt")
            conf.os.system(f"wpscan --url {auto_host} -f cli-no-color --output {auto_output}/wpscan.json --format json")
            conf.os.system(f"nmap -sV --script http-wordpress-enum {auto_host} -o {auto_output}/nmap_wp-enum.txt -oX {auto_output}/nmap_wp-enum.xml")
            

        elif 'Joomla' in open(f"reports/Autoscan/{auto_host}/cmseek.txt").read():
            conf.os.system(f"perl ./modules/joomscan/joomscan.pl -u {auto_host}")
            
    
        elif 'Drupal' in open(f"reports/Autoscan/{auto_host}/cmseek.txt").read():
            conf.os.system(f"droopescan scan drupal -o json -u {auto_host} > {auto_output}/drup.json")
            conf.os.system(f"nmap --script http-drupal-enum {auto_host} -o {auto_output}/nmap_drup-enum.txt -oX {auto_output}/nmap_drup-enum.xml")
    
    
        conf.os.system(f"python3 ~/home/kali/dirsearch/dirsearch.py -u {auto_host} --format json -o '{auto_output}/dirsearch.json'")

    

    
            




