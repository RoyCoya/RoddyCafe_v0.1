$("#AFdian").click(function (e) { 
    if($("#form_auth_token").val() != ""){
        window.location.replace(
            url_AFdian + "auth_token=" + $("#form_auth_token").val()
        )
    }
    else{
        alert("请填写信息")
    }
});