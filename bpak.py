#!/usr/bin/env python3

import sys
import subprocess
import getpass
import os

user = getpass.getuser()

if len(sys.argv) < 2:
    print("Hi",user,", welcome to bpak")
    print("Usage: bpak <command> [package]")
    sys.exit(1)

cmd = sys.argv[1]

# Các lệnh cần quyền root
ROOT_COMMANDS = [
    "install",
    "remove",
    "update",
    "upgrade",
    "autoremove",
    "purge",
    "clean",
    "full-upgrade"
]

if cmd in ROOT_COMMANDS and os.geteuid() != 0:
	print("ERROR: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)")
	print("ERROR: We couldn't enter the Debian's Magical Repository, it refused us 'cause we aren't root")
	print("HINT: Please, give us superuser =( ")
	sys.exit(1)


match cmd:

    case "install":
        if len(sys.argv) < 3:
            print("What do you want to install,")
            print("Usage: bpak install <package>")
            sys.exit(1)

        package = sys.argv[2]
        print("Hello",user,"we are going to install:")
        print(package)
        subprocess.run([
            "apt",
            "install",
            package
        ])
        
        result = subprocess.run([...])
        
        if result == 0:
            print("OK now")
            print(package,"now existed in your computer")
            print("Enjoy it =)")
        else:
            print("Something went wrong, but we can't install",package)
            print("Maybe it not exsits in Debian's Magical Repo")
    case "remove":
        if len(sys.argv) < 3:
            print("What package you want to delete?")
            print("Usage: bpak remove <package>")
            sys.exit(1)

        package = sys.argv[2]

        print("We are going to delete")
        print(package)

        subprocess.run([
            "apt",
            "remove",
            package
        ])
        print("OK")
        print(package,"is no longer in your computer, but can reinstall if you want =)")

    case "search":
        if len(sys.argv) < 3:
            print("What do you find?")
            print("Usage: bpak search <package>")
            sys.exit(1)

        package = sys.argv[2]
		
        print("We are finding something you want")
        subprocess.run([
            "apt",
            "search",
            package
        ])
        
    case "purge":
        if len(sys.argv) < 3:
            print("What to you want to purge?")
            print("Usage: sudo bpak purge <package>")
            sys.exit(1)
        
        package = sys.argv
        
        print("We will delete this package, also earse all memory about you and this pacakge")
        subprocess.run([
			"apt",
			"purge",
			package
		])
        print("Ok, we done delete",package,"out of your computer")
        
        

    case "update":
        print("We are traveling to the world of repo rn! <3")
        
        subprocess.run([
            "apt",
            "update"
        ])
        result = subprocess.run(
            ["apt", "list", "--upgradable"],
            capture_output=True,
            text=True
        )

        lines = result.stdout.strip().splitlines()

        # Dòng đầu là "Listing..."
        count = max(0, len(lines) - 1)
        if count == 0:
            print("Our journey is over.")
            print("We found none package ready for updgrae, seem like you are up to date <3")
        else:
            print("Our journey is over.")
            print(f"We found {count} package(s) ready for an upgrade")


    case "upgrade":
        print("We are going to upgrade all package ")
        
        subprocess.run([
            "apt",
            "upgrade"
        ])
        
        print("Done! Now package has up-to-date and very powerful!")
    case "autoremove":
        print("We are finding dependency and lonely packages")
        
        
        subprocess.run([
			"apt",
			"autoremove"
		])
		
        print("Done, we had sent lonely dependency and packages go to Debian Magical Repository, hope they find a good home")
    case "clean":
        print("We are cleaning are .deb in our cache...")
        
        subprocess.run([
			"apt",
			"clean"
		])
        print("done")
		
    case "autoclean":
        print("We are cleaning some old .deb in our cache...")
		
        subprocess.run([
            "apt"
            "autoclean"
        ])
        print("done")
    case "help":
        print("""\
bpak commands

sudo install <pkg>
sudo remove <pkg>
search <pkg>
sudo update
sudo upgrade
help
""")

    case _:
        print(f"Unknown command: {cmd}")
