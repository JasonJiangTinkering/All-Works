function NameColor()
{
    let name = document.getElementById('name');

    if(name.innerHTML == "Lemonade")
    {
        name.style.color = "yellow";
    }
    else if(name.innerHTML == "Naan")
    {
        name.style.color = "brown";
    }
    else if(name.innerHTML == "Alfredo Sauce")
    {
        name.style.color = "white";
    }
}
