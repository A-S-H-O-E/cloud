from importlib.resources import open_binary
import dropbox
accesstoken = 'sl.BG_gOeaI_I6IX8mjPsw2GhtvMoZzZIaWTjKRTogWMPoxaXioQhANYAgshJvNmmYKV7nsw_VNkSUMEW0Zz-nCBTiWuuA0I7K6nw0XWrAAjwiXTlxlbhy3RcfOXxi-bvkyKPiM_PK6Hhc'
dbx = dropbox.Dropbox(accesstoken)
f = open('file.txt', 'rb')
f1 = open('family.jpg', 'rb')
# dbx.files_upload(f.read(),'/Aashrith/file.txt')
dbx.files_upload(f1.read(),'/Aashrith/family.jpg')
print('file uploaded successfully')
