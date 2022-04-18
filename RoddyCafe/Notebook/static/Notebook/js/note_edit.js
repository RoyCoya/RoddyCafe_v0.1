/* 
    wangeditor 相关 
*/
const { createEditor, createToolbar } = window.wangEditor
//编辑器配置
const editorConfig = {
    placeholder : '请输入内容……',
    autoFocus : true,
    onChange : (editor) => {
        const content = editor.children
        const html = editor.getHtml()
        document.getElementById('note_content').value = html
    },
    MENU_CONF : {},
}
const getCookie = (name) => document.cookie.match(`[;\s+]?${name}=([^;]*)`)?.pop();
const csrftoken = getCookie('csrftoken');
editorConfig.MENU_CONF['uploadImage'] = {
    // 上传图片的配置
    server : url_api_Notebook_userfile_upload,
    headers: {
        'X-CSRFToken': csrftoken
    },
    maxFileSize: 10 * 1024 * 1024,
}
const editor = createEditor({
    selector : '#editor_container',
    config : editorConfig,
    html : note_content,
    mode : 'default',
})
//工具栏配置
const toolbarConfig = {
    
}
const toolbar = createToolbar({
    editor,
    selector : '#toolbar_container',
    config : toolbarConfig,
    mode : 'default'
})



$('#save').click(function (e) { 
    $.post(
        url_api_note_save,
        $('#form_note').serializeArray(),
        function (data, textStatus, jqXHR) {
            window.location.replace(url_note_detail);
        },
    );
});