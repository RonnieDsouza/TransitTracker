const bus_list = new XMLHttpRequest();
var schedule_url = '/v2/stops/10064/schedule.json';
var email = "ron99ds@gmail.com";
var key = "9Ld737shDDwqfsXWSZ3m";

bus_list.open("get", schedule_url, false, email, key);

bus_list.onreadystatechange=function(){
    if(this.readyState == 4 && this.status == 200){
        console.log(bus_list.responseText);
    }
}

