$(document).ready(function () {
    $('#rank_type option[value=' + type + ']').attr('selected', 'selected');
});

$("#rank_type").change(function (e) { 
    window.location.replace(url_change_rank_type + $(this).val())
});