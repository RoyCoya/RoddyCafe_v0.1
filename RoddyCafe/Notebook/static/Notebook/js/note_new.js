/* 
    wangeditor 相关 
*/
const { createEditor, createToolbar } = window.wangEditor
const editorConfig = {}
editorConfig.placeholder = '请输入内容……'
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
})
// 创建工具栏
const toolbar = createToolbar({
    editor,
    selector: '#toolbar_container',
    mode: 'default'
})



/*
    页面功能
*/

//保存新笔记
$('#save').click(function (e) {
    //自动产生title
    var titlePriorityCheckList = []
    titlePriorityCheckList.push($($('#note_content').val()).filter('p').first().text().substr(0,15))
    titlePriorityCheckList.push($($('#note_content').val()).filter('h5').first().text())
    titlePriorityCheckList.push($($('#note_content').val()).filter('h4').first().text())
    titlePriorityCheckList.push($($('#note_content').val()).filter('h3').first().text())
    titlePriorityCheckList.push($($('#note_content').val()).filter('h2').first().text())
    titlePriorityCheckList.push($($('#note_content').val()).filter('h1').first().text())
    finalTitle = ''
    $.each(titlePriorityCheckList, function (index, value) { 
         if (value != '') finalTitle = value;
    });
    //组装post内容
    var postData = $('#form_note').serializeArray()
    postData.push({'name': 'note_title','value':finalTitle})
    $.post(
        url_api_note_new_save,
        postData,
        function (data, textStatus, jqXHR) {
            window.location.replace(url_note_detail.replace('note_id',data.toString()));
        },
    );
});