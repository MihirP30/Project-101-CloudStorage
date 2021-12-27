import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A83LefZuGTGvsiXClxG0e2x37x-ChyLKCN8w4JZzxlbzpHxh96s-xkO7GOjyHcIKQeInzyeC7bsdccIUmcKuxlU9P12d-qw-YaWCz6FLBZ_n2SoDkSjYLqpSUZUbD44Oi9MHzIY'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path for the transfer: ")
    file_to =input("Enter the destination where to upload in the dropbox: ")
    # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    transferData.upload_file(file_from, file_to)
    print("The file has been moved")

main()