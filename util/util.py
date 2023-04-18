import os


class util:
    def __init__(self):
        pass

    def list_files(self,current_dir):
        files_list = os.listdir(current_dir)
        print(files_list)
