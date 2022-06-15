/* 
    通用变量、函数
*/
url_note_detail = "/notebook/note/note_id/"

/*
    wangeditor相关
*/
const { createEditor, createToolbar } = window.wangEditor
const getCookie = (name) => document.cookie.match(`[;\s+]?${name}=([^;]*)`)?.pop();
const csrftoken = getCookie('csrftoken');
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
editorConfig.MENU_CONF['uploadImage'] = {
    // 上传图片的配置
    server : url_api_Notebook_wangeditor_upload_img,
    fieldName: 'img_uploaded',
    headers: {'X-CSRFToken': csrftoken},
    maxFileSize: 20 * 1024 * 1024,
}
editorConfig.MENU_CONF['uploadVideo'] = {
    //上传视频的配置
    server : url_api_Notebook_wangeditor_upload_video,
    fieldName: 'video_uploaded',
    maxFileSize: 200 * 1024 * 1024, 
    maxNumberOfFiles: 10,
    headers: {'X-CSRFToken': csrftoken},
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
    finalTitle = '未命名笔记'
    $.each(titlePriorityCheckList, function (index, value) { 
         if (value != '') finalTitle = value;
    });
    //组装post内容
    var postData = $('#form_note').serializeArray()
    postData.push({'name': 'note_title','value':finalTitle})
    $.post(
        url_api_note_new_save,
        postData,
        function (data) {
            window.location.replace(url_note_detail.replace('note_id',data.toString()));
        },
    );
});