$("#set_cookie").click(function (e) { 
    if($("#form_auth_token").val() != ""){
        Cookies.set('AFdian_auth_token', $("#form_auth_token").val());
        window.location.replace(location)
    }
    else alert("请输入auth_token")
});