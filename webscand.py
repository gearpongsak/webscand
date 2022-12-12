import conf.conf as conf

def main():
    while conf.ans:
        print(
            "==================================================================="
        )
        print(conf.colored(conf.text2art("Web Scan D", "big"), "cyan"))
        print(
            conf.colored(">", "red", attrs=["bold"]) +
            conf.colored("Created by : Pongsakorn@Secure D\n", "magenta", attrs=["bold"]))
        
        print(
            "==================================================================="
        )



        print(conf.colored("\n1. Nmap Scan", "yellow", attrs=["bold"]))
        print(conf.colored("2. SSL Scan", "yellow", attrs=["bold"]))
        print(conf.colored("3. Nikto Scan", "yellow", attrs=["bold"]))
        print(conf.colored("4. Word Press Scan", "yellow", attrs=["bold"]))
        print(conf.colored("5. Joomla Scan", "yellow", attrs=["bold"]))
        print(conf.colored("6. Drupal Scan", "yellow", attrs=["bold"]))
        print(conf.colored("7. Dirsearch Scan", "yellow", attrs=["bold"]))
        print(conf.colored("A. Auto Scans", "yellow", attrs=["bold"]))
        print(conf.colored("F. Full Scans", "yellow", attrs=["bold"]))
        print(conf.colored("E. Exit\n", "yellow", attrs=["bold"]))
        print(
            "==================================================================="
        )

        conf.ans = input(
            conf.colored("\nEnter your selection: ",
                         "green")).upper()

        if conf.ans == "1":
            conf.call_def(conf.nmap_scan)
        elif conf.ans == "2":
            conf.call_def(conf.ssl_scan)
        elif conf.ans == "3":
            conf.call_def(conf.nikto_scan)
        elif conf.ans == "4":
            conf.call_def(conf.wp_scan)
        elif conf.ans == "5":
            conf.call_def(conf.joom_scan)
        elif conf.ans == "6":
            conf.call_def(conf.droopes_scan)
        elif conf.ans == "7":
            conf.call_def(conf.dirsearch_scan)
        elif conf.ans == "A":
           conf.call_def(conf.auto_scan)    
        elif conf.ans == "F":
            conf.call_def(conf.full_scan)
        elif conf.ans == "E":
            conf.call_def(conf.exit)
        else:
            conf.not_valid(main, conf.ans, 0)


try:
    main()
except KeyboardInterrupt:
    print("\n \n Keyboard Interrupt. ")
    conf.sys.exit()