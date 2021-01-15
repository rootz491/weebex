let btns = document.querySelectorAll('.deleteMsg');
let btns2 = document.getElementsByClassName('deleteMsg');
console.log(btns);
console.log(btns2);

for(let btn of btns) {
    btn.addEventListener('click', deleteNow)

}



function deleteNow(e) {
    e.preventDefault();
    msg = e.target.parentElement.parentElement;
    console.log(msg, 'deleted!');
    msg.remove();
}
