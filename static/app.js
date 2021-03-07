function onKlikk(){
    if (document.getElementById("inputitem").value != "" && document.getElementById("inputamount").value!= "")
    {
        var osszes = document.getElementById("inputitem").value + "" + document.getElementById("inputamount").value;
        var result =  osszes.replace(" ", "").toLowerCase();
        var count = document.getElementById("itemek").rows.length;
        for (var i=1; i<count; ++i)
        {
            var item = document.getElementById("itemek").rows[i]["cells"][1].innerHTML + document.getElementById("itemek").rows[i]["cells"][2].innerHTML;
            var itemfound = item.replace(" ", "").toLowerCase();
            //alert(itemfound + " " + result);
            if (itemfound == result)
            {
                alert("Már van ilyen tétel a listában")
                return 0;
            }
        }
           
            
        var table = document.getElementById("itemek");
        var row = table.insertRow(-1);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        cell1.innerHTML = '<input type="checkbox">'
        cell2.innerHTML = document.getElementById("inputitem").value;
        cell3.setAttribute("class","mennyiseg");
        cell3.innerHTML = document.getElementById("inputamount").value;

        document.getElementById("inputitem").value = "";
        document.getElementById("inputamount").value="";
            
        
        
    }
    else{
        alert("Nincs megadva tétel/mennyiség")
    }
}
function confirmgomb(){
    var count = document.getElementById("itemek").rows.length;
    for(var i = 1; i < count; ++i)
    {
        if ( document.getElementById("itemek").rows[i]["cells"][0].firstElementChild.checked == true)
        {
            var value = document.getElementById("itemek").rows[i]["cells"][1].innerHTML;
            document.getElementById("itemek").deleteRow(i);
            count = count-1;
            i=i-1;
        }

    }

}