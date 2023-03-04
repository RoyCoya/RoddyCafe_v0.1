/*
    通用变量、函数
*/
const getCookie = (name) => document.cookie.match(`[;\s+]?${name}=([^;]*)`)?.pop();
const csrftoken = getCookie('csrftoken');

// 页面初始化
$(document).ready(function () {
    time()
});