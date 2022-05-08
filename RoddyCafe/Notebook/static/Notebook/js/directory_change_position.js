/*
    选择新目录位置时列表的ui变化
*/
$('.move-dir').click(function (e) {
    $('.move-dir').removeClass("choosed-postion");
    $('.move-dir').find('span').addClass("invisible");
    $(this).addClass("choosed-postion");
    $(this).find('span').removeClass("invisible");
});