from google_drive_downloader import GoogleDriveDownloader as gdd
from os.path import exists

def check_for_creds(id, path):

    file_exists = exists(path)

    if file_exists:
        pass
    else:
        gdd.download_file_from_google_drive(
        file_id=id,
        dest_path= path
    )