function onKlikk(){
    if (document.getElementById("inputitem").value != "" && document.getElementById("inputamount").value!= "")
    {
        var table = document.getElementById("itemek");
        var row = table.insertRow(-1);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        cell1.innerHTML = '<input type="checkbox"> onclick="confirmgomb()"'
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

    confirm("Biztos ki akarod körölni a tételt?")



}