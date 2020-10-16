from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


gauth = GoogleAuth()
gauth.LocalWebserverAuth()
# if gauth.credentials is None:
#     gauth.LocalWebserverAuth()
# elif gauth.access_token_expired:
#     gauth.Refresh()
# else:
#     gauth.Authorize()

#gauth.SaveCredentialsFile("client_secrets.json")

drive = GoogleDrive(gauth)


def list_files():
    # View all folders and file in your Google Drive
    fileList = drive.ListFile(
        {'q': "'root' in parents and trashed=false"}).GetList()
    for file in fileList:
        print('Uploaded: Title: %s, ID: %s' % (file['title'], file['id']))
        # Get the folder ID that you want
        if(file['title'] == "Shared With Me"):
            fileID = file['id']

def get_files():
    fileList = drive.ListFile(
        {'q': "'root' in parents and trashed=false"}).GetList()
    return fileList

#file meta: dict e.g. {'title':'data.txt'}
def create_file(file_meta):
    file1 = drive.CreateFile(file_meta)
    file1.Upload()  # Upload the file.
    print('title: %s, id: %s' % (file1['title'], file1['id']))

def trash_file(file):
    file.Trash()

def delete_file(file):
    file.Delete()

def untrash_file(file):
    file.UnTrash()

def pull_file_content(destination_filename, drive_file, mimetype):
    
    files = get_files()
    print(files)

#list_files()

    
