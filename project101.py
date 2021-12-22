import dropbox

class TransferData:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken
    def uploadfile(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        with open(filefrom,'rb')as f:
            dbx.files_upload(f.read(),fileto)
def main():
    accesstoken="sl.A-jN6UXYrgZHxxmirOFYOEDMUB3o9YTmkIG5la3JG_ZrigTcpBiIZOYxCJibu1xJX4Uj0qhGgJiRgMD7t6_dIHcSIf6Cl_VwbV0viVkyAQzkyN9-Q3YvKyE-X-FnlMnUcanAQ1LioWu"
    transferData=TransferData(accesstoken)
    filefrom="weirdname.txt"
    fileto="/b/file.txt"
    transferData.uploadfile(filefrom,fileto)
    print("file move was succesful")
main()