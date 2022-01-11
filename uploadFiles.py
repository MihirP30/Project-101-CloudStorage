import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

            # enumerate local files recursively
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                    # construct the full local path
                local_path = os.path.join(root, filename)

                    # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                    # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A_49_vKs8TkPCRSjAwW32pnH-oDZkzUQL_NPxFar28PEeHuOEfXEoxCH7B31lOyeeclEf3jSE-CpIZDFm3V24BvDwtbn7GTFC86yUMhSxF3zvkI2ftE0Lo-Rj3e9EPplmSZb69k'
    transferData = TransferData(access_token)

    file_from = 'D:/mihir/Extra Curricular/WHJ/Projects/P101/'
    file_to = '/P-101-CloudStorage/'

    # API v2
    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")

main()