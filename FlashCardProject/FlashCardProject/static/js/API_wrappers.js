function addNew(word, definition){
    word = document.getElementById("word").value;
    definition = document.getElementById("definition").value;
    console.log("workin a");
    $.ajax({
        type:"POST",
        url:"/app/api/addNewCard",
        dataType:"json",
        contentType: 'application/json',
        data:JSON.stringify({
            "word": word,
            "definition": definition 
        }),
        success: function(data){
        },
        error:function(){
            alert("Error Occured")
        }
    })

}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
beforeSend: function(xhr, settings) {
        // Send the token to same-origin, relative URLs only.
        // Send the token only if the method warrants CSRF protection
        // Using the CSRFToken value acquired earlier
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});