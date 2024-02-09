"""
Copies data pack (dp) to a Minecraft world named `Data Pack Testing`.
Tests if Minecraft world's directory name exists before copying.
"""

import os
import shutil
import sys


MC_DIR = os.path.join(os.getenv('appdata'), '.minecraft')
WORLD_DIR = os.path.join(MC_DIR, 'saves\\Data Pack Testing')
DP_DIR = os.path.join(WORLD_DIR, 'datapacks\\projectSEKAI')
CDP_DIR = os.path.join(os.getcwd(), 'projectSEKAI')


def main():
    # Check directory.
    if not os.path.exists(WORLD_DIR):
        err_msg = \
        "Minecraft world `Data Pack Testing` not found!\n" \
        "Please create the world with the highlighted\n" \
        "name and try again. Press Return to exit.."
        input(err_msg)
        sys.exit()

    # Erase data pack if it exists in the world folder.
    if os.path.exists(DP_DIR):
        shutil.rmtree(DP_DIR)

    # Copy data pack to world folder.
    shutil.copytree(CDP_DIR, DP_DIR)
    print('Script Successful. Data pack now ready to be tested.')


if __name__ == '__main__':
    main()
