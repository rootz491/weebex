btns = document.querySelectorAll('.down');


for (let btn of btns) {
    btn.addEventListener('click', (e)=>{
        that = e.target.parentElement;
        let ul = e.target.parentElement.parentElement.nextElementSibling
        if(ul.classList != "collapse") {
            ul.classList.add("collapse");
            that.classList.add("rotate");
        }
        else {
            ul.classList.remove("collapse");
            that.classList.remove("rotate");
        }
    })
}