from os import listdir, path, getmtime, getctime, makedirs, rename
import datetime


def identify_recent_files(current_dir):
    """
    Identifies files created or modified in the last 24 hours.

    Args:
        current_dir: The directory to scan for files.

    Returns:
        A list of file paths that were created or modified in the last 24 hours.
    """
    recent_files = []
    now = datetime.datetime.now()
    one_day_ago = now - datetime.timedelta(days=1)

    for filename in listdir(current_dir):
        filepath = path.join(current_dir, filename)
        if path.isfile(filepath):
            file_mtime = datetime.datetime.fromtimestamp(getmtime(filepath))
            file_ctime = datetime.datetime.fromtimestamp(getctime(filepath))

            if file_mtime >= one_day_ago or file_ctime >= one_day_ago:
                recent_files.append(filepath)

    return recent_files


def update_files(filepath):
    """
    Updates a file by appending a timestamp to its content.

    Args:
        filepath: The path to the file to update.
    """
    with open(filepath, "a") as f:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\nUpdated at: {now}")


def move_files(recent_files, target_dir):
    """
    Moves files to a specified directory while renaming them with prefixes.

    Args:
        recent_files: A list of file paths to move.
        target_dir: The destination directory to move the files to.
    """
    # Create the target directory if it doesn't exist
    if not path.exists(target_dir):
        makedirs(target_dir)

    for filepath in recent_files:
        filename = path.basename(filepath)
        # Prepend current date and time to the filename
        new_filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{filename}"
        destination = path.join(target_dir, new_filename)

        # Use rename to move and rename the file in one step
        rename(filepath, destination)


if __name__ == "__main__":
    current_dir = "."
    target_dir = "last_24hours"

    recent_files = identify_recent_files(current_dir)

    for filepath in recent_files:
        update_files(filepath)

    move_files(recent_files, target_dir)

    print(f"Moved {len(recent_files)} files to '{target_dir}'")

