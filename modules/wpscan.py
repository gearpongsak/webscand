#!/usr/bin/env python3
#
# Writen by Pongsakorn
#
# This is free software, licensed under the MIT License.
# See /LICENSE for more information.
#
import conf.conf as conf

def wp_scan():
    print("==============================================")
    print(conf.colored(conf.text2art("WP Scan", "small"), "cyan"))
    print("==============================================")

    wp_host = input(
        conf.colored("\nEnter target: ", "green", attrs=["bold"]))
    wp_output = input(
        conf.colored(
            f"Enter the output folder - [default: reports/Wpscan/{wp_host}/]: ",
            "green",
            attrs=["bold"],
        ))

    conf.not_valid(wp_scan, wp_host)
    wp_output = conf.dir_output(wp_output, "reports/Wpscan", wp_host)

    conf.create_dir(wp_output)

    conf.os.system(f"wpscan --url {wp_host} -f cli-no-color --output {wp_output}/wpscan.txt")
    conf.os.system(f"wpscan --url {wp_host} -f cli-no-color --output {wp_output}/wpscan.json --format json")

    print(
        "______________________________________________________________________"
    )   
