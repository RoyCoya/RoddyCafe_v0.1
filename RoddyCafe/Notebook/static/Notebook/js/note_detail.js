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
    html : note_content,
    mode : 'default',
})