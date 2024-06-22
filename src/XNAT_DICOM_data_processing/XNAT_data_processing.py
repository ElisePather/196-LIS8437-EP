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
    

if __name__=='__main__':
    with xnat.connect('http://localhost',user='admin', password='admin') as session:
        testproject=session.projects['testproject']
        print(testproject)
        print(testproject.subjects)
        subject = testproject.subjects['GSTT000030']
        subject.download_dir('./')

        r = []
        dir = '/mnt/c/Repos/196-LIS8437-EP/GSTT000030/'
        for root, dirs, files in os.walk(dir):
            for name in files:
                r.append(os.path.join(root, name))
                file = os.path.join(root, name)
                dataset = pydicom.dcmread(file)
                print(file)
                print(dataset[0x0008, 0x0020], dataset[0x0008, 0x0022], dataset[0x0008, 0x0012])
                add_days_to_tags([[0x0008, 0x0020], [0x0008, 0x0022], [0x0008, 0x0012]], 11)
                print(dataset[0x0008, 0x0020], dataset[0x0008, 0x0022], dataset[0x0008, 0x0012])



                print(dataset[0x0008, 0x0030], dataset[0x0008, 0x0032], dataset[0x0008, 0x0013])
                remove_tag_val([[0x0008, 0x0030], [0x0008, 0x0032], [0x0008, 0x0013]])
                print(dataset[0x0008, 0x0030], dataset[0x0008, 0x0032], dataset[0x0008, 0x0013])


                
                print(dataset[0x0008, 0x1030].value)
                change_study_desc()
                print(dataset[0x0008, 0x1030].value)

































