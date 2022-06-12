'''通用方法'''

from django.contrib.auth import logout

#获取删除目录时所需要删除的本体和其所有子目录，返回列表
def func_getDirsToDelete_list(dir,deleteList):
    deleteList.append(dir)
    if dir.first_child:
        func_getDirsToDelete_list(dir.first_child,deleteList)
    if dir.next_brother:
        func_getDirsToDelete_list(dir.next_brother,deleteList)
    return deleteList