#!/usr/bin/env python3

"""
Programme pour accèder aux variables d'environnement

Par Olivier Dubreuil
"""

import getpass
import os



def main() -> None:
    """Fonction principale"""
    print(f"Il y a {len(os.environ)} variables d'environnement")
    print(f" - OS: {os.getenv('OS', 'Non défini')}")
    print(F" - HOME: {os.getenv('HOMEPATH', os.gentv('HOME','Non défini'))}")

    print()
    print("Code Portable:")
    print(f" - {os.name=}")
    print(f" - user: {getpass.getuser()}")
    print(f" - home: {os.path.expanduser('~')}")

    # print()
    # pprint.pprint(dict(os.environ), width=40)

    pass


if __name__ == '__main__':
    main()