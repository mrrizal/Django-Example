$(document).ready( function() {
	// ajax get
	$('body').on('click', '.get-more', function() {
		$.ajax({
			url : 'more',
			type : 'GET',
			success : function(data) {
				for (var i = 0; i < data.length; i++) {
					$('ul').append('<li>'+data[i]+'</li>');
				}
			}
		});
		
	});

    // ajax post
    $('body').on('click', '.add-todo', function() {
    	$.ajax({
    		url : '/add/',
    		type : 'POST',
    		data : {
    			'item' : $('.todo-item').val(),
    		},
    		success : function(data) {
    			alert(data.message)
    		}
    	});
    });

    // csrf token
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
		crossDomain : false,
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type)) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});
    
});
