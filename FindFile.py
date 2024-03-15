import sys
import os


class FileSystem(object):
    video_file_name: str = ""
    video_file_name_list: list = []
    video_file_path: str = ''
    video_file_path_list: list = []
    video_container: str = ''

    save_container_path: str = ''
    save_container_path_list: list = []

    def __init__(self, video_container):
        self.video_container = video_container

        for root, ds, fs in os.walk(self.video_container):
            i = 0
            for vfn in fs:
                if vfn != ".DS_Store":
                    self.video_file_name = vfn
                    self.video_file_name_list.append(self.video_file_name)
                    self.video_file_path = video_container + '/' + self.video_file_name
                    self.video_file_path_list.append(self.video_file_path)
                    #remove_suffix = self.video_file_name.strip(".mov")
                    self.save_container_path = root + '/' + self.video_file_name.strip('.mov')
                    self.save_container_path_list.append(self.save_container_path)

        self.video_file_path_list.sort()
        self.save_container_path_list.sort()
        self.video_file_name_list.sort()

    def create_captue_container(self):
        for index_container in self.save_container_path_list:
            if os.path.exists(index_container):
                print("已经存在该目录！")
                continue
            else:
                os.makedirs(index_container)

'''''
def test():
    # reload(sys)
    encodes = sys.getdefaultencoding()
    print("encodes:", encodes)
    videoContainer = r'filesys.create_captue_container()'
    # video_container_list: list = []
    filesys = FileSystem(videoContainer)
    print("vfnl:", filesys.video_file_name_list)
    print("vfpl:", filesys.video_file_path_list)
    print("scpl:", filesys.save_container_path_list)

    filesys.create_captue_container()


test()
''''''''
full_video_name = os.path.join(root, f).split("/")[7]
    # error_store = "/Users/liqiuheng/Documents/downie/05.数列/1.数列/-DS_Store"
    if len(full_video_name) > 5:
        # fullname = fullname + "/capture/"
        save_path_0 = full_video_name.split(".")[0]
        save_path_1 = full_video_name.split(".")[1]
        save_path = save_path_0 + "-" + save_path_1
        print(save_path)

        whole_save_path = vp + save_path

        lists.append(whole_save_path)
        error_store = "/Users/liqiuheng/Documents/downie/05.数列/1.数列/-DS_Store"
        if error_store in lists:
            lists.remove(error_store)

        print("截图保存路径列表：", lists)

        isExists = os.path.exists(whole_save_path)
        if not isExists:
            os.makedirs(whole_save_path)
        else:
            print("目录已经存在！")

        print("截图存储路径sp:", whole_save_path)
LS = lists
LV = listv
# print(list_save, list_video)
return lists, listv
'''''
