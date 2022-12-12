#!/usr/bin/env python3
#
# Writen by Pongsakorn
#
# This is free software, licensed under the MIT License.
# See /LICENSE for more information.
#
import conf.conf as conf

def ssl_scan():
    print("==============================================")
    print(conf.colored(conf.text2art("SSL Scan", "small"), "cyan"))
    print("==============================================")

    ssl_host = input(
        conf.colored("\nEnter target: ", "green", attrs=["bold"]))
    ssl_output = input(
        conf.colored(
            f"Enter the output folder - [default: reports/SSLscan/{ssl_host}/]: ",
            "green",
            attrs=["bold"],
        ))

    conf.not_valid(ssl_scan, ssl_host)
    ssl_output = conf.dir_output(ssl_output, "reports/SSLscan", ssl_host)

    conf.create_dir(ssl_output)

    conf.os.system(f"sslscan --xml={ssl_output}/sslscan.xml {ssl_host}")
    


    print(
        "______________________________________________________________________"
    )   
