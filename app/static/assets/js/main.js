function search(){
    let name = document.getElementById("floatingInput").value;
    fetch("/api?" + name)
        .then(response => response.json())
        .then(json => console.log(JSON.stringify(json)))
}