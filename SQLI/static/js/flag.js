document.addEventListener("DOMContentLoaded", function () {
    var flag = document.getElementById("flag").value;
    if (flag && flag != "" && flag != "None") {
        alert("Flag get! "+flag);
    }
});