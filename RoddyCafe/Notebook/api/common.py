'''通用方法'''
from Notebook.models import note

#获取删除目录时所需要删除的本体和其所有子目录，输入需要删除的最顶层目录、待删列表，返回完整待删列表
def directories_to_delete(dir,deleteList):
    deleteList.append(dir)
    if dir.first_child:
        directories_to_delete(dir.first_child,deleteList)
    if dir.next_brother:
        directories_to_delete(dir.next_brother,deleteList)
    return deleteList

# 获取tabbar的各个提醒红点计数
# TODO：获取到期提醒数量（加在未完成笔记数量上）、共享信息数量
def get_notification_count(user):
    todo = 0
    share = 0
    
    todo += note.objects.filter(isUnfinished=True,directory__user=user).count()
    
    return todo, share