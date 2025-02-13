# Uses python3
import sys

## function dependencies


def dependencies(line):
    dependencis = []
    dependencis = line.split()
    for i in range(2, len(dependencis), 1):
        if dependencis[1] in depends:
            depends[dependencis[1]].append(dependencis[i])
        else:
            depends[dependencis[1]] = [dependencis[i]]

## Register install


def register_install(install_input):
    if install_input in install_list:
        pass
    if not install_input:
        pass
    else:
        install_list[install_input] = "Y"

## function install

def install(line):
    install_input = (line.split())[-1]
    if install_input in install_list:
        pass
    else:
        if install_input in depends:
            for j in depends[install_input]:
                if not j in install_list:
                    install(j)
                    register_install(j)
                else:
                    pass
            print("installing " + install_input)
            register_install(install_input)

        else:
            print("installing " + install_input)
            register_install(install_input)

## Print list

def print_list():
    list = install_list.keys()
    for item in list:
        print(item)

def aloha(lines):
    for line in lines:

        if line.startswith("DEPENDS"):
            dependencies(line)

        if line.startswith("INSTALL"):
            install(line)

        if line.startswith("LIST"):
            print_list()

        if line.startswith("REMOVE"):
            dependencies(line)

        if line.startswith("END"):
            break

## Initialize
depends = {}
dep_list = []
install_list = {}
lines = []
#hashmap for dependencies
if __name__ == '__main__':
    while True:

        try:
            line = input()
            if line != "END":
                lines.append(line)
            else:
                break
        except:
            pass
    aloha(lines)
