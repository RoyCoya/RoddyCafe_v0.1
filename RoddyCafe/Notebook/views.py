from Notebook.api import note as api_note, directory as api_directory, wangeditor as api_wangeditor
from Notebook.page import index as page_index, note as page_note, directory as page_directory

'''页面'''
# 主页
def index_homepage(request): return page_index.homepage(request)

# 目录
def directory_all(request): return page_directory.all(request)
def directory_specific(request,directory_id): return page_directory.specific(request,directory_id)
# 笔记
def note_new(request,directory_id): return page_note.new(request,directory_id)
def note_detail(request,note_id): return page_note.detail(request,note_id)
def note_edit(request,note_id): return page_note.edit(request,note_id)

'''接口'''
# 目录
def api_directory_new(request, directory_id): return api_directory.new(request, directory_id)
def api_directory_delete(request,directory_id): return api_directory.delete(request,directory_id)
def api_directory_move(request,dir_to_move_id,parent_id,child_id,is_first_child): return api_directory.move(request,dir_to_move_id,parent_id,child_id,is_first_child)
def api_directory_edit_discription(request,directory_id): return api_directory.edit_discription(request,directory_id)

# 笔记
def api_note_new(request,directory_id): return api_note.new(request,directory_id)
def api_note_delete(request,note_id): return api_note.delete(request,note_id)
def api_note_edit(request,note_id): return api_note.edit(request,note_id)
def api_note_move(request,note_id,directory_id): return api_note.move(request,note_id,directory_id)
def api_note_switch_pintop(request,note_id): return api_note.switch_pintop(request,note_id)
def api_note_switch_pending(request,note_id): return api_note.switch_pending(request,note_id)

# wangeditor
def api_wangeditor_upload_img(request, note_id): return api_wangeditor.upload_img(request, note_id)
def api_wangeditor_upload_video(request, note_id): return api_wangeditor.upload_video(request, note_id)