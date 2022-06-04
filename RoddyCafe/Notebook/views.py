import imp


from Notebook.api import note, directory, wangeditor
from Notebook.page import pages

'''页面'''
# 主页
def index(request): return pages.index(request)

# 目录
def all_directory(request): return pages.all_directory(request)
def directory_notelist(request,directory_id): return pages.directory_notelist(request,directory_id)

# 笔记
def note_detail(request,note_id): return pages.note_detail(request,note_id)
def note_edit(request,note_id): return pages.note_edit(request,note_id)
def note_new(request,directory_id): return pages.note_new(request,directory_id)

'''接口'''

# 目录
def api_directory_new_save(request, directory_id): return directory.api_directory_new_save(request, directory_id)
def api_directory_delete(request,directory_id): return directory.api_directory_delete(request,directory_id)
def api_directory_change_position(request,dir_to_move_id,parent_id,child_id,is_first_child): return directory.api_directory_change_position(request,dir_to_move_id,parent_id,child_id,is_first_child)
def api_directory_change_discription(request,directory_id): return directory.api_directory_change_discription(request,directory_id)

# 笔记
def api_note_new(request,directory_id): return note.api_note_new(request,directory_id)
def api_note_delete(request,note_id): return note.api_note_delete(request,note_id)
def api_note_edit(request,note_id): return note.api_note_edit(request,note_id)
def api_note_change_directory(request,note_id,directory_id): return note.api_note_change_directory(request,note_id,directory_id)
def api_note_switch_pintop(request,note_id): return note.api_note_switch_pintop(request,note_id)
def api_note_switch_pending(request,note_id): return note.api_note_switch_pending(request,note_id)

# wangeditor
def api_userfile_upload_img(request): return wangeditor.api_userfile_upload_img(request)
def api_userfile_upload_video(request): return wangeditor.api_userfile_upload_video(request)