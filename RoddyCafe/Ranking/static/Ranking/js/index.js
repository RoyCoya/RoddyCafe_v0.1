$(document).ready(function () {
    $('#rank_type').val(type);
});

$("#rank_type").change(function (e) { 
    window.location.replace(url_change_rank_type + $(this).val())
});