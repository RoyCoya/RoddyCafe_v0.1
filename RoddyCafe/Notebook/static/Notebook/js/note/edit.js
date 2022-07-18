/*
通用方法
*/
// 保存笔记，跳转至url
$.fn.saveNote = function(url){
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
    postData.push({
        'name': 'note_title',
        'value': finalTitle
    })
    $.post(
        url_api_note_save,
        postData,
        function () {
            if (url != 'None') {
                window.location.replace(url);
            }
        },
    );
}

// 定时保存
var toast =  new bootstrap.Toast($("#toast_autosave"))
var saver = setInterval(() => {
    $.fn.saveNote('None')
    toast.show()
}, 1000 * 60 * 3);

/* 
    wangeditor 相关 
*/
const getCookie = (name) => document.cookie.match(`[;\s+]?${name}=([^;]*)`)?.pop();
const csrftoken = getCookie('csrftoken');
const { createEditor, createToolbar } = window.wangEditor
//编辑器配置
const editorConfig = {
    placeholder : '点击返回或每隔3分钟将自动保存笔记。',
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
    headers: {
        'X-CSRFToken': csrftoken
    },
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
    mode: 'simple',
    html : note_content.replace(/\&lt;/g,'<').replace(/\&gt;/g,'>').replace(/&#x27;/g,"\'").replace(/\&quot;/g,'"').replace(/&amp;/g,'\&')
})
//工具栏配置
const toolbarConfig = {
    toolbarKeys : [
        "headerSelect",
        {
            key: "group-justify",
            title: "对齐",
            iconSvg: '<svg viewBox="0 0 1024 1024"><path d="M768 793.6v102.4H51.2v-102.4h716.8z m204.8-230.4v102.4H51.2v-102.4h921.6z m-204.8-230.4v102.4H51.2v-102.4h716.8zM972.8 102.4v102.4H51.2V102.4h921.6z"></path></svg>',
            menuKeys: ["justifyLeft", "justifyRight", "justifyCenter"]
        },
        "|",
        "bold",
        "italic",
        "underline",
        "through",
        "sup", 
        "sub",
        "|", 
        "color",
        "bgColor",
        // {
        //     key: "group-more-style", 
        //     title: "更多",
        //     iconSvg: '<svg viewBox="0 0 1024 1024"><path d="M204.8 505.6m-76.8 0a76.8 76.8 0 1 0 153.6 0 76.8 76.8 0 1 0-153.6 0Z"></path><path d="M505.6 505.6m-76.8 0a76.8 76.8 0 1 0 153.6 0 76.8 76.8 0 1 0-153.6 0Z"></path><path d="M806.4 505.6m-76.8 0a76.8 76.8 0 1 0 153.6 0 76.8 76.8 0 1 0-153.6 0Z"></path></svg>',
        //     menuKeys: ["fontSize", "fontFamily", "lineHeight"]
        // },
        "|",
        "bulletedList",
        "numberedList",
        "todo",
        "blockquote",
        "code",
        "codeBlock",
        "divider",
        "|",
        "insertLink",
        "insertTable",
        {
            key: "group-image",
            title: "图片",
            iconSvg: '<svg viewBox="0 0 1024 1024"><path d="M959.877 128l0.123 0.123v767.775l-0.123 0.122H64.102l-0.122-0.122V128.123l0.122-0.123h895.775zM960 64H64C28.795 64 0 92.795 0 128v768c0 35.205 28.795 64 64 64h896c35.205 0 64-28.795 64-64V128c0-35.205-28.795-64-64-64zM832 288.01c0 53.023-42.988 96.01-96.01 96.01s-96.01-42.987-96.01-96.01S682.967 192 735.99 192 832 234.988 832 288.01zM896 832H128V704l224.01-384 256 320h64l224.01-192z"></path></svg>',
            menuKeys: ["insertImage", "uploadImage"]
        },
        {
            key: "group-video",
            title: "视频",
            iconSvg: '<svg viewBox="0 0 1024 1024"><path d="M981.184 160.096C837.568 139.456 678.848 128 512 128S186.432 139.456 42.816 160.096C15.296 267.808 0 386.848 0 512s15.264 244.16 42.816 351.904C186.464 884.544 345.152 896 512 896s325.568-11.456 469.184-32.096C1008.704 756.192 1024 637.152 1024 512s-15.264-244.16-42.816-351.904zM384 704V320l320 192-320 192z"></path></svg>',
            menuKeys: ["insertVideo", "uploadVideo"]
        },
        "|",
        "undo",
        "redo",
    ],
}
const toolbar = createToolbar({
    editor,
    selector : '#toolbar_container',
    config : toolbarConfig,
    mode : 'default',
})

/*
    页面功能
*/
//保存笔记修改
$('#back').click(function (e) {
    $.fn.saveNote(url_back)
});

//标记为已完成
$('#finish').click(function (e) { 
    $.ajax({
        type: "post",
        url: url_api_note_switch_pending,
        data: {"pending_checked" : false,},
        dataType: "json",
        headers:{'X-CSRFToken': csrftoken},
        async:false,
    });
    $.fn.saveNote(url_back)
});