/* 
wangeditor 相关 
*/
const { createEditor } = window.wangEditor
//编辑器配置
const editorConfig = {
    readOnly : true
}
const editor = createEditor({
    selector : '#editor_container',
    config : editorConfig,
    html : note_content.replace(/\&lt;/g,'<').replace(/\&gt;/g,'>').replace(/&#x27;/g,"\'").replace(/\&quot;/g,'"').replace(/&amp;/g,'\&'),
    mode : 'default',
})