import os
from pathlib import Path
from shutil import move, rmtree
from getpass import getuser
from PIL import Image

USER = getuser()
DOWNLOADS_FOLDER = Path(f"/Users/{USER}/Downloads")
PICTURES_FOLDER = Path(f"/Users/{USER}/Pictures")
MUSIC_FOLDER = Path(f"/Users/{USER}/Music")
VIDEO_FOLDER = Path(f"/Users/{USER}/Videos")
TABS_FOLDER = Path(f"/Users/{USER}/Tabs")
PDF_FOLDER = Path(f"/Users/{USER}/Documentos/PDFs")

print(f"Organizing the user {USER} download folder")


def check_dir(path):
    path.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    for file in DOWNLOADS_FOLDER.iterdir():
        if file.is_dir():
            rmtree(file)
            print(f"Deleted folder: {file}")
            continue

        name, extension = os.path.splitext(file.name)

        if extension.lower() in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(file)
            picture.save(PICTURES_FOLDER / f"compressed_{file.name}", optimized=True, quality=60)
            os.remove(file)
            print(f"Moved picture: {file}")

        elif extension.lower() in [".mp3", ".wav"]:
            check_dir(MUSIC_FOLDER)
            move(file, MUSIC_FOLDER / file.name)
            print(f"Moved music: {file}")

        elif extension.lower() == '.mp4':
            check_dir(VIDEO_FOLDER)
            move(file, VIDEO_FOLDER / file.name)
            print(f"Moved video: {file}")

        elif extension.lower() in ['.gp5', ".gpx"]:
            check_dir(TABS_FOLDER)
            move(file, TABS_FOLDER / file.name)
            print(f"Moved tab: {file}")

        elif extension.lower() == '.pdf':
            check_dir(PDF_FOLDER)
            move(file, PDF_FOLDER / file.name)
            print(f"Moved PDF: {file}")

        else:
            os.remove(file)
            print(f"Deleted file: {file}")
