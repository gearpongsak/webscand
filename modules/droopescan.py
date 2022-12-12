#!/usr/bin/env python3
#
# Writen by Pongsakorn
#
# This is free software, licensed under the MIT License.
# See /LICENSE for more information.
#
import conf.conf as conf

def droopes_scan():
    print("==============================================")
    print(conf.colored(conf.text2art("Droopes Scan", "small"), "cyan"))
    print("==============================================")

    droo_host = input(
        conf.colored("\nEnter target: ", "green", attrs=["bold"]))
    droo_output = input(
        conf.colored(
            f"Enter the output folder - [default: reports/Droopescan/{droo_host}/]: ",
            "green",
            attrs=["bold"],
        ))

    conf.not_valid(droopes_scan, droo_host)
    droo_output = conf.dir_output(droo_output, "reports/Droopescan", droo_host)

    conf.create_dir(droo_output)

    conf.os.system(f"droopescan scan drupal -o json -u {droo_host} > {droo_output}/drup.json")

    print(
        "______________________________________________________________________"
    )   
