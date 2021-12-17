function onload() {
    
        $.ajax({
            type: 'GET',
            url: "https://herokuoksi.herokuapp.com/api/snake/list",
            //url: "http://127.0.0.1:8000/api/esp/list",
            success: function (response) {

                Object.keys(response).forEach(function(element){
                    document.getElementById("oxygen").innerHTML =  response[element].oksi
                    })
                // let oxygen = response[0].oksi
                // document.getElementById("oxygen").innerHTML = oxygen;
                //"<li>" + element + " :" + response[element].oksi + "</li>";
                debugger;
 
            },
            error: function (response) {
                //alert("NO DATA");
            }
            
        });
    
}



onload();
setInterval(onload,1000);