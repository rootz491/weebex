const postBtn = document.getElementById('newPostBtn');
const form = document.querySelector('.newPost');
const container = document.querySelector('.container');
const exitBtn = document.querySelector('#exitPost');
let isFormHidden = true;

postBtn.addEventListener('click', showForm);
exitBtn.addEventListener('click', hideForm);


function showForm(e) {
    if (isFormHidden) {
        form.hidden = false;
        container.style.opacity = 20+'%';
        container.style.pointerEvents = 'none';
        isFormHidden = !isFormHidden;
    }
}

function hideForm(e) {
    if (!isFormHidden) {
        form.hidden = true;
        container.style.opacity = 100+'%';
        container.style.pointerEvents = 'initial';
        isFormHidden = !isFormHidden;
    }
}
