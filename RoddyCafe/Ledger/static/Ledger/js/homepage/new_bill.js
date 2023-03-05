// 收入支出切换
$("#bill_type").change(function (e) { 
    switch ($(this).val()) {
        case 'payout':{
            $("#bill_value_span").removeClass("text-success");
            $("#calculator button").removeClass("btn-outline-success");
            $("#bill_value_span").addClass("text-warning");
            $("#calculator button").addClass("btn-outline-warning");
            $("#calculator_submit").text("支出");
            $("#bill_value_type_span").text("-");
            break;
        }
        case 'income':{
            $("#bill_value_span").removeClass("text-warning");
            $("#calculator button").removeClass("btn-outline-warning");
            $("#bill_value_span").addClass("text-success");
            $("#calculator button").addClass("btn-outline-success");
            $("#calculator_submit").text("收入");
            $("#bill_value_type_span").text("+");
            break;
        }
        default: break;
    }
});

// 加数字
$("#calculator .calculator_number").click(function (e) { 
    if($("#bill_value").text() == '0'){
        if(!($(this).text() == '0' || $(this).text() == '00')) $("#bill_value").text($(this).text());
    }
    else{
        $("#bill_value").text($("#bill_value").text() + $(this).text())
        decimal_index = $("#bill_value").text().indexOf('.')
        if($("#bill_value").text().substr(decimal_index, $("#bill_value").text().length-1).length > 2){
            $("#bill_value").text($("#bill_value").text().substr(0, decimal_index + 3))
        }
    }
});

// 退格
$("#calculator_delete").click(function (e) { 
    if(!$("#bill_value").text() == '0'){
        $("#bill_value").text($("#bill_value").text().substr(
            0,
            $("#bill_value").text().length - 1
        ))
        if($("#bill_value").text() == '') $("#bill_value").text('0')
    }
});

// 加小数点
$("#calculator_decimal").click(function (e) { 
    if($("#bill_value").text().indexOf('.') == -1) $("#bill_value").text($("#bill_value").text() + ".")
});

// 提交记录
$("#calculator_submit").click(function (e) { 
    $.ajax({
        type: "post",
        url: api_bill_submit,
        data: {
            "type" : $("#bill_type").val(),
            "value" : $("#bill_value").text(),
            "classification_id" : $("#classification_id").text(),
            "remark" : $("#bill_remark").val(),
        },
        // TODO:返回不是JSON内容时这里会走error。之后改成JSON
        error : function(){
            window.location.replace(location)
        },
        dataType: "json",
        headers:{'X-CSRFToken': csrftoken}
    });
});