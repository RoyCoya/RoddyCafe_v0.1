/*
popover提示框初试化
*/
var tooltipTriggerList = Array.prototype.slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})

/*
新目录表单
*/
//选择目录插入点的ui变化
$('[id^=insertDir_]').click(function (e) {
    $('#isFormFilled').removeClass("text-danger");
    $('#isFormFilled').addClass("text-success");
    $('#isFormFilled').text("已选择");
    $('[id^=insertDir_]').removeClass("choosed-postion");
    $('[id^=insertDir_]').find('span').addClass("invisible");
    $(this).addClass("choosed-postion");
    $(this).find('span').removeClass("invisible");
    $('#form_new_directory_position').val($(this).attr("id"));
});
//提交表单
$('#form_new_directory').submit(function (e) {
    var postData = $('#form_new_directory').serializeArray()
    $.post(
        url_api_directory_new_save,
        postData,
        function (data, textStatus, jqXHR) {
            window.location.replace(url_page_all_directory);
        },
    );
});