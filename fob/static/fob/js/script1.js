
// var today = new Date();
// var dd = today.getDate();
// var mm = today.getMonth()+1; //January is 0!
// var yyyy = today.getFullYear();
//
// if(dd<10) {
//     dd = '0'+dd
// }
//
// if(mm<10) {
//     mm = '0'+mm
// }
//
// today = mm + '/' + dd + '/' + yyyy;
//
// document.getElementById("demo").innerHTML = 'Today is the: ' + today;


// Color Saturdays, Sundays gray
// Color ADP inputs light blue

var trTags = document.getElementsByTagName("tr"); //Count how many 'tr' tags are there
for (var i = 0; i < trTags.length; i++) { //loop through all the rows
    var td_position = trTags[i]; //Current row
    var y = td_position.innerText; //

    if ((y.search('Sat')> 0) ||
        (y.search('Sun')> 0)){
        trTags[i].style.backgroundColor = "#F0F8FF"; //Paint the entire row
    }
     if ((y.search('HOLIDAY')> 0) ||
         (y.search('DTO')> 0)){
        trTags[i].style.backgroundColor = "#b3feff";
    }
    if ((y.search('trip')> 0) ||
         (y.search('home')> 0)){
        trTags[i].style.backgroundColor = "#fbeee9";
    }
}


