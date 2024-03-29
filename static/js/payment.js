function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }

$(document).ready(function () {
    $("#to-confirmation").click(function(event) {
          $.ajax({
                headers: { "X-CSRFToken": getCookie("csrftoken") },
                url:'/payment/overview/',
                type: 'POST',
                success: function(resp){
                    document.location.href = '/payment/confirmation/'
                },
                error: function(xhr, status, error) {
                        //TODO: show toestr
                    console.error(error);
                }
        });
    });
});