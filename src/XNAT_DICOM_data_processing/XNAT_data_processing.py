import xnat
import pydicom
import os


def add_days_to_tags(tag_num:list, num_days: int) -> None:
    for i in tag_num:
        dataset[i].value = str(int(dataset[i].value) + num_days) 
        
def remove_tag_val(tag_num:list) -> None:
    for i in tag_num:
        dataset[i].value = None

def change_study_desc() -> None:
    dataset[0x0008, 0x1030].value = 'This is a test study description'
    
def reconfigure_subject_session(folder_dir:str) -> str:
    folder_dir.split('GSTT000030')
    

if __name__=='__main__':
    # connect to xnat testproject using session
    with xnat.connect('http://localhost',user='admin', password='admin') as session:
        testproject=session.projects['testproject']
        #select subject
        subject = testproject.subjects['GSTT000030']
        #download subject directory
        subject.download_dir('/mnt/c/Repos/196-LIS8437-EP/dev-data/DICOM_temp/')

        # loop over directory files to change each dicom file
        dir = '/mnt/c/Repos/196-LIS8437-EP/dev-data/DICOM_temp/GSTT000030/'
        for root, dirs, files in os.walk(dir):
            for name in files:
                
                file = os.path.join(root, name)
                dataset = pydicom.dcmread(file)
                add_days_to_tags([[0x0008, 0x0020], [0x0008, 0x0022], [0x0008, 0x0012]], 11)
                remove_tag_val([[0x0008, 0x0030], [0x0008, 0x0032], [0x0008, 0x0013]])
                change_study_desc()


                #create new session folder and save edited dicom files
                path_split = file.split('69c22ac9-0343-4c32-8b4b-5941883f3177')
                print(file)
                new_file = path_split[0] + 'SessionA' + path_split[1]
                filepath = new_file.rsplit('/', 1)[0]
                if not os.path.exists(filepath):
                    os.makedirs(filepath)
                os.chdir(filepath)
                dataset.save_as(new_file)
                print(new_file)
                
        # next step is to push the new session to XNAT
        


            































