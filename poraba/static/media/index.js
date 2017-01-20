/**
 * Created by vid on 1/20/17.
 */

    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


            function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

                $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });


        $(document).ready(function() {
                    $('#znamka_choose').click(function (event) {
                        var a = $("#znamka_choose option:selected")
                        if ( a.index() != 0) {
                            q = a.val();
                            //$("#Model").post( "{% url 'demo_car_search' %}?q=" + q );
                             $.ajax({
                                url: 'car',
                                type: 'POST',
                                data: {'car': q},
                                  success: function(data) {
                                      $('#refresh').data("avto", data);
                                  }
                             });
                             /*
                             var postUrl = "{% url 'demo_car_search' %}";
                            $.post(postUrl, {'car': q}, function(result){
                            }).fail(function (data, status, xhr) {
                                alert(xhr.status);
                                alert(thrownError);
                            });
                            */
                            //$( "#result" ).load( "{% url 'demo_car_search' %}?q=" + q );
                    }});
        });