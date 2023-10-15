function deleteAsteriskFields(){
    document.querySelectorAll('.asteriskField').forEach((item)=>{
        item.remove()
    })
}
function leftSmallUl(){
    document.getElementById('hint_id_password1').querySelector('ul').style.paddingLeft = '0';
}

function itemFormRow ()
{
    document.getElementById('add_car').querySelectorAll('.form-group').forEach((item)=>{
        item.classList.add('mx-3')
    })
}

function clicks(){
    alert('Успешно добавлено!')
}

function record(){
    alert('Записано')
}