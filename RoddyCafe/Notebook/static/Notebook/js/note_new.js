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