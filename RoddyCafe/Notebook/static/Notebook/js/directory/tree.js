/*
    全局变量
*/
theme_color = 'rgb(0, 124, 77)';

/*
    popover提示框初试化
*/
var tooltipTriggerList = Array.prototype.slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})

/*
    页面功能
*/
//新增目录->选择目录插入点的ui变化（包括从总目录中新建和从指定目录中新建子目录）
$('[id^=insertDir_]').click(function (e) {
    $('#isFormFilled').removeClass("bg-danger");
    $('#isFormFilled').addClass("bg-success");
    $('#isFormFilled').text("已选择插入点");
    $('[id^=insertDir_]').css('color', '');
    $('[id^=insertDir_] i').removeClass("text-light");
    $('[id^=insertDir_]').css('background-color', '');
    $('[id^=insertDir_]').find('span').addClass("invisible");
    $(this).css('color', 'white');
    $(this).css('background-color', theme_color);
    $(this).find('span').removeClass("invisible");
    $(this).find('i').addClass("text-light");
    $('#form_new_directory_position').val($(this).attr("id"));
    $("#new_directory_confirm").removeAttr('hidden','hidden');
});

//移动目录->选择新目录位置时列表的ui变化
$('.move-dir').click(function (e) {
    $('.move-dir').removeClass("choosed-postion");
    $('.move-dir').find('span').addClass("invisible");
    $(this).addClass("choosed-postion");
    $(this).find('span').removeClass("invisible");
});