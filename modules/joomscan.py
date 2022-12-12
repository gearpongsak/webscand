#!/usr/bin/env python3
#
# Writen by Pongsakorn
#
# This is free software, licensed under the MIT License.
# See /LICENSE for more information.
#
import conf.conf as conf

def joom_scan():
    print("==============================================")
    print(conf.colored(conf.text2art("Joom Scan", "small"), "cyan"))
    print("==============================================")

    joom_host = input(
        conf.colored("\nEnter target: ", "green", attrs=["bold"]))
    joom_output = input(
        conf.colored(
            f"Enter the output folder - [default: reports/Joomscan/{joom_host}/]: ",
            "green",
            attrs=["bold"],
        ))

    conf.not_valid(joom_scan, joom_host)
    joom_output = conf.dir_output(joom_output, "reports/Joomscan", joom_host)

    conf.create_dir(joom_output)

    conf.os.system(f"perl ./modules/joomscan/joomscan.pl -u {joom_host}")
    

    print(
        "______________________________________________________________________"
    )   
