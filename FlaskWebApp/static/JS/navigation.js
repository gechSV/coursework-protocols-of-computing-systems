let flagArrow = false;


function onClickArrowButton()
{
    if (flagArrow){
        var button = document.getElementById("arrowButton");
        button.style.transform = 'rotate(0deg)';
        flagArrow = false;
    }
    else
    {
        var button = document.getElementById("arrowButton");
        button.style.transform = 'rotate(90deg)';
        flagArrow = true;
    }
}