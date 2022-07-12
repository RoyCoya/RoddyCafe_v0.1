/*
    通用变量、函数
*/
const getCookie = (name) => document.cookie.match(`[;\s+]?${name}=([^;]*)`)?.pop();
const csrftoken = getCookie('csrftoken');

/* 
    wangeditor 相关 
*/
const { createEditor } = window.wangEditor
//编辑器配置
const editorConfig = {
    readOnly : true,
    onCreated : (editor) => {
        $('input').removeAttr('disabled');
    },
}
const editor = createEditor({
    selector : '#editor_container',
    config : editorConfig,
    html : note_content.replace(/\&lt;/g,'<').replace(/\&gt;/g,'>').replace(/&#x27;/g,"\'").replace(/\&quot;/g,'"').replace(/&amp;/g,'\&'),
    mode : 'default',
})

/*
    页面功能
*/
//切换置顶状态
$("#switch_pintop").click(function (e) { 
    $.ajax({
        type: "post",
        url: url_api_note_switch_pintop,
        data: {"pintop_checked" : this.checked,},
        dataType: "json",
        headers:{'X-CSRFToken': csrftoken}
    });
});
//切换待编辑状态
$("#switch_pending").click(function (e) { 
    $.ajax({
        type: "post",
        url: url_api_note_switch_pending,
        data: {"pending_checked" : this.checked,},
        dataType: "json",
        headers:{'X-CSRFToken': csrftoken}
    });
});