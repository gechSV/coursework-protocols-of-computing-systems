let flagArrow = false;

// выполняется при нажатии кнопки развёртывания каталога категорий
function onClickArrowButton()
{
    var button = document.getElementById("arrowButton");
    var conteiner = document.getElementById("otherCategories");
    if (flagArrow){
        button.style.transform = 'rotate(0deg)';
        flagArrow = false;
        conteiner.style.display = 'none';
    }
    else
    {
        button.style.transform = 'rotate(90deg)';
        flagArrow = true;
        conteiner.style.display = 'flex';
    }
}