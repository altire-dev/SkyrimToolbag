# ===================================================================================================
# Imports: External
# ===================================================================================================
import shutil
import os
import re

# ===================================================================================================
# Imports: Internal
# ===================================================================================================

# ===================================================================================================
# Builder Properties
# ===================================================================================================
ADDON_NAME      = "bl_skyrim_toolbag"
VERSION_FILE    = "./version"
OUTPUT_DIR      = "./builds"

# ===================================================================================================
# Builder Methods
# ===================================================================================================
def get_version():
    '''
    Fetches the build version number from the version file

    :return: Tuple containing Major, Minor and Patch version Number
    '''
    with open("./version", "r") as version_file:
        contents = version_file.read().rstrip("\r").rstrip("\n")
        maj, min, patch = contents.split(".")
    return maj, min, patch

def set_addon_version(maj, min, patch):
    '''
    Updates the addon's version information

    :param maj: The Major number
    :type maj: int
    :param min: The Minor number
    :type min: int
    :param patch: The Patch number
    :type patch: int
    '''
    log("Updating Addon version information")

    # Update Version in Add-on
    with open("./%s/__init__.py" % ADDON_NAME, "r") as addon_init_file:
        content = addon_init_file.read()

    new_content = re.sub(
        r'"version": \([^\)]*\)',
        '"version": (%s, %s, %s)' % (maj, min, patch),
        content,
        flags=re.DOTALL
    )

    # Write new config
    with open("./%s/__init__.py" % ADDON_NAME, "w") as addon_init_file:
        addon_init_file.write(new_content)

    log("Version information updated")


def log(message):
    '''
    Prints a message to the Console

    :param message: The message to print
    :type message: str
    '''
    print("[+] %s" % message)

# ===================================================================================================
# MAIN: Build Add-on
# ===================================================================================================
if __name__ == "__main__":
    log("Starting Addon Build: %s" % ADDON_NAME)

    v_maj, v_min, v_patch = get_version()
    log("Addon Version: %s.%s.%s" % (v_maj, v_min, v_patch))
    set_addon_version(v_maj, v_min, v_patch)

    if not os.path.isdir(OUTPUT_DIR):
        log("Creating Output Directory")
        os.mkdir(OUTPUT_DIR)

    archive_file_name = "%s_%s_%s_%s" % (ADDON_NAME, v_maj, v_min, v_patch)
    archive_file_path = os.path.join(OUTPUT_DIR, archive_file_name)


    if os.path.isfile(archive_file_path):
        os.remove(archive_file_path)
    shutil.make_archive("./%s" % archive_file_path, "zip", "./", "./%s" % ADDON_NAME)
    log("Addon successfully built: %s" % archive_file_path)
