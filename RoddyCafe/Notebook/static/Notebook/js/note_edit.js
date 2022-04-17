/* 
    wangeditor 相关 
*/
const { createEditor, createToolbar } = window.wangEditor
const editorConfig = {}
editorConfig.placeholder = '请输内容'
editorConfig.autoFocus = true
// 当编辑器选区、内容变化时，即触发
editorConfig.onChange = (editor) => {
    const content = editor.children
    const html = editor.getHtml()
    document.getElementById('note_content').value = html
}
// 创建编辑器
const editor = createEditor({
    selector: '#editor_container',
    config: editorConfig,
    mode: 'default',
    html: note_content,
})
// 创建工具栏
const toolbar = createToolbar({
    editor,
    selector: '#toolbar_container',
    mode: 'default'
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