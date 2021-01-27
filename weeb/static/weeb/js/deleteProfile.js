const profileOpenBtn = document.querySelector('#deleteProfile');
const profileForm = document.querySelector('.deleteProfile');
const HTMLContainer = document.querySelector('.container');
const profileExitBtn = document.querySelector('#closeBtn');
let isProfileFormHidden = true;

profileOpenBtn.addEventListener('click', showForm);
profileExitBtn.addEventListener('click', hideForm);


function showForm(e) {
    if (isProfileFormHidden) {
        profileForm.hidden = false;
        HTMLContainer.style.opacity = 20+'%';
        HTMLContainer.style.pointerEvents = 'none';
        isProfileFormHidden = !isProfileFormHidden;
    }
}

function hideForm(e) {
    if (!isProfileFormHidden) {
        profileForm.hidden = true;
        HTMLContainer.style.opacity = 100+'%';
        HTMLContainer.style.pointerEvents = 'initial';
        isProfileFormHidden = !isProfileFormHidden;
    }
}
