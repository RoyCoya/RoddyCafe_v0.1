function time(){
    var datetime=new Date();
    var year = datetime.getFullYear();
    var month = datetime.getMonth() + 1;
    var day = datetime.getDate();
    var hour = datetime.getHours();
    var minutes = datetime.getMinutes();
    var second = datetime.getSeconds();
    hour = check_time(hour)
    minutes = check_time(minutes)
    second = check_time(second)
    var date = year + " 年 " + month + " 月 " + day + " 日"
    var time = hour + ' : ' + minutes + ' : ' + second
    $("#date_span").text(date);
    $("#time_span").text(time);
    setTimeout('time()',1000);
}
function check_time(i){ 
    if(i < 10){ 
        i = '0' + i; 
    } 
    return i; 
} 