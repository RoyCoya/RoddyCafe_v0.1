/*
    通用变量、函数
*/
const getCookie = (name) => document.cookie.match(`[;\s+]?${name}=([^;]*)`)?.pop();
const csrftoken = getCookie('csrftoken');

$("#save_token").click(function (e) { 
    if($("#form_auth_token").val() != ""){
        $.ajax({
            type: "post",
            url: url_api_save_auth_token,
            data: {
                "auth_token" : $("#form_auth_token").val(),
            },
            // TODO:返回不是JSON内容时这里会走error。之后改成JSON
            error : function(){
                window.location.replace(location)
            },
            dataType: "json",
            headers:{'X-CSRFToken': csrftoken}
        });
    }
    else alert("请输入auth_token")
});