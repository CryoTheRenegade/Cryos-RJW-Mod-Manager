import os
import subprocess


def pull(path):
    os.chdir(path)
    ogdir = os.getcwd()
    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]
    for i in subfolders:
        os.chdir(i)
        subprocess.call(["git", "pull"])
        os.chdir(ogdir)


def clone(lst):
    for i in lst:
        subprocess.call(["git", "clone", i])


def gitssh():
    sshlst = ["git@ssh.gitgud.io:Ed86/rjw.git", "git@ssh.gitgud.io:Ed86/rjw-ex.git", "git@ssh.gitgud.io:Abraxas/rjw-race-support.git", "git@ssh.gitgud.io:Ed86/rjw-mc.git",
              "git@ssh.gitgud.io:c0ffeeeeeeee/rimworld-animations.git", "git@ssh.gitgud.io:Tory/rjwanimaddons-animalpatch.git", "git@ssh.gitgud.io:Tory/rjwanimaddons-xtraanims.git",
              "git@ssh.gitgud.io:Tory/animaddons-voicepatch.git", "git@ssh.gitgud.io:John-the-Anabaptist/licentia-labs.git", "git@ssh.gitgud.io:HiveBro/nephila-rjw.git",
              "git@github.com:/moreoreganostodump/RJW_Menstruation.git", "git@gitlab.com:Hazzer/s16s-extension.git", "git@ssh.gitgud.io:c0ffeeeeeeee/rjw-events.git",
              "git@ssh.gitgud.io:SpiritCookieCake/scc-lewd-sculptures.git", "git@gitlab.com:Nabber/rimvore-2", "git@github.com:/WolfoftheWest/Rimnosis.git",
              "git@ssh.gitgud.io:c0ffeeeeeeee/coffees-rjw-ideology-addons.git", "git@github.com:/moreoreganostodump/RJW-Sexperience.git",
              "git@ssh.gitgud.io:c0ffeeeeeeee/rjw-toys-and-masturbation.git"]
    print("Good on you for using SSH")
    keysetup = input(
        "Have you setup Github, GitLab, and GitGud with your SSH key(s)? (Y/N) \n")
    if keysetup == "Y" or keysetup == "y":
        agentsetup = input(
            "Good, is your ssh-agent setup to send those keys? (Y/N) \n")
        if agentsetup == "Y" or agentsetup == "y":
            print("Awesome! Lets get some Mods!")
            InstallYN = input("Do you want to clone or update the mods? \n")
            if InstallYN == "clone" or InstallYN == "Clone":
                print(os.getcwd())
                pathyeeornaw = input(
                    "Is this the path you would like to install the mods to? (Y/N) \n")
                if pathyeeornaw == "Y" or pathyeeornaw == "y":
                    clone(sshlst)
                elif pathyeeornaw == "N" or pathyeeornaw == "n":
                    modpath = input(
                        "What dir should I install the mods to? \n")
                    os.chdir(modpath)
                    clone(sshlst)
                else:
                    print("I wanted to know if that was the correct dir, not THAT!")
                    exit()
            elif InstallYN == "update" or InstallYN == "Update":
                print("Awesome, lets get you the latest and greatest")
                print(os.getcwd())
                GoodDir = input(
                    "Is this the correct path to the mods? (Y/N) \n")
                if GoodDir == "Y" or GoodDir == "y":
                    pull(os.getcwd())
                elif GoodDir == "N" or GoodDir == "n":
                    modpath = input("What dir should I go to? \n")
                    os.chdir(modpath)
                    pull(modpath)
                else:
                    print("That isnt a choice")
                    return(0)
            else:
                print("That is not an option")
                exit()
        elif agentsetup == "N" or agentsetup == "n":
            print("Please setup ssh-agent before you attempt to clone from git.")
            exit()
        else:
            print("That isnt a choice")
            return(0)
    elif keysetup == "N" or keysetup == "n":
        print("Then I Highly Reccomend You Do So")
        return(0)
    else:
        print("That isnt a choice")
        return(0)


def githttps():
    httplst = ["https://gitgud.io/Ed86/rjw.git", "https://gitgud.io/Ed86/rjw-ex.git", "https://gitgud.io/Abraxas/rjw-race-support.git", "https://gitgud.io/Ed86/rjw-mc.git",
               "https://gitgud.io/c0ffeeeeeeee/rimworld-animations.git", "https://gitgud.io/Tory/rjwanimaddons-animalpatch.git", "https://gitgud.io/Tory/rjwanimaddons-xtraanims.git",
               "https://gitgud.io/Tory/animaddons-voicepatch.git", "https://gitgud.io/John-the-Anabaptist/licentia-labs.git", "https://gitgud.io/HiveBro/nephila-rjw.git",
               "https://github.com/moreoreganostodump/RJW_Menstruation.git", "https://gitlab.com/Hazzer/s16s-extension.git", "https://gitgud.io/c0ffeeeeeeee/rjw-events.git",
               "https://gitgud.io/SpiritCookieCake/scc-lewd-sculptures.git", "https://gitlab.com/Nabber/rimvore-2", "https://github.com/WolfoftheWest/Rimnosis.git",
               "https://gitgud.io/c0ffeeeeeeee/coffees-rjw-ideology-addons.git", "https://github.com/moreoreganostodump/RJW-Sexperience.git","https://gitgud.io/c0ffeeeeeeee/rjw-toys-and-masturbation.git"]
    print("Connecting with HTTPS")
    InstallYN = input("Do you want to clone or update the mods? \n")
    if InstallYN == "clone" or InstallYN == "Clone":
        print(os.getcwd())
        pathyeeornaw = input(
            "Is this the path you would like to install the mods to? (Y/N) \n")
        if pathyeeornaw == "Y" or pathyeeornaw == "y":
            clone(httplst)
        elif pathyeeornaw == "N" or pathyeeornaw == "n":
            modpath = input(
                "What dir should I install the mods to? \n")
            os.chdir(modpath)
            clone(httplst)
        else:
            print("I wanted to know if that was the correct dir, not THAT!")
            exit()
    elif InstallYN == "update" or InstallYN == "Update":
        print("Awesome, lets get you the latest and greatest")
        print(os.getcwd())
        GoodDir = input(
            "Is this the correct path to the mods? (Y/N) \n")
        if GoodDir == "Y" or GoodDir == "y":
            pull(os.getcwd())
        elif GoodDir == "N" or GoodDir == "n":
            modpath = input("What dir should I go to? \n")
            os.chdir(modpath)
            pull(modpath)
    else:
        print("That is not an option, try again")
        exit()


def main():
    print("Hey Guys, Gals, and All of the above. This is a semi-personal project that was inspired by c0ffee's batch script for RJW addons. This implementation is for our peeps on Linux, MacOS, and Windows using either ssh or https to connect to the git hosts. It will most certainly be updated with better, cleaner code than I write.")
    choice = int(input("Do you want to use HTTPS(1) or SSH(2)? \n"))
    if choice == 1:
        githttps()
    elif choice == 2:
        gitssh()
    else:
        print("That isn't one of your choices, you horndog, try again.")
        main()
        return(0)
    print("Thank you for using Cryo's Mod Installer and Updater for RJW!")


if __name__ == "__main__":
    main()
