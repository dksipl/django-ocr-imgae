import fitz, os

def convert_file(f_path):
    
    doc = fitz.open(f_path)
    name = os.path.splitext(os.path.basename(f_path))[0]
    
    for page in doc:
        pix = page.get_pixmap()
        pix.save(name + '-' + str(page.number) + ".png")
          
    print('success!')
        
# convert_file('/home/shreyjain/Desktop/project1/media/file_uploads/-7_gw_10_merged3.pdf')

f_list = os.listdir('/home/shreyjain/Desktop/project1/app1/ss')    

for i in f_list:
    convert_file('/home/shreyjain/Desktop/project1/app1/ss')
    
