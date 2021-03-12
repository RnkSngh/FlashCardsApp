function addNew(word, definition){
    word = document.getElementById("word").value;
    definition = document.getElementById("definition").value;
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

function switchVisible() {
    if (document.getElementById('Front')) {

        if (document.getElementById('Front').style.display == 'none') {
            document.getElementById('Front').style.display = 'block';
            document.getElementById('Back').style.display = 'none';
        }
        else {
            document.getElementById('Front').style.display = 'none';
            document.getElementById('Back').style.display = 'block';
        }
    }
}

function getWord(){
var tmp = null;
$.ajax({
    type:"GET",
    url:"/app/api/getWord",
    dataType:"json",
    cache:false,
    success: function(data){
        newWord = data.word
        newDef = data.definition
        if (newWord==undefined){
            document.getElementById("Front").innerHTML=data;
        }
        else{
            document.getElementById("WordFront").innerHTML=newWord;
            document.getElementById("WordBack").innerHTML=newWord;
            document.getElementById("Definition").innerHTML=newDef;
        }
    },
    error:function(){
        alert("Error Occured")
    }
});

}

function markCorrect(correct){
word = document.getElementById("WordBack").innerHTML;
$.ajax({
    type:"POST",
    cache:false,
    url:"/app/api/markCorrect",
    dataType:"json",
    contentType: 'application/json',
    data:JSON.stringify({
        "word": word,
        "correct": correct 
    }),
    success: function(data){
        getWord();
        switchVisible();
    },
    error:function(){
        alert("Error Occured")
    }
})

}

function getCards(){
    $.ajax({
        type:"GET",
        url:"/app/api/getCards",
        dataType:"json",
        contentType: 'application/json',
        success: function(data){
          buildTable(data);
        },
        error:function(){
            alert("Error Occured")
        }
    })

}

function buildTable(data){

    for(var i=0; i<data.length; i++){
      var row = data[i];
      var rowTr$ = $('<tr/>');
      // for (var key in row){
      //   if(key in ["word", "wordBin", "incorrect"]){
      rowTr$.append($('<th/>').html(row["word"]))
      rowTr$.append($('<th/>').html(row["wordBin"]))
      rowTr$.append($('<th/>').html(row["incorrect"]))
      //}
      $( "#cardTable" ).append(rowTr$);
    }
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