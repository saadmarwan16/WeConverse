dropdown = document.querySelector('.dropdown-btn');

dropdown.addEventListener ('click', () => {

    dropdownList = document.querySelector('.dropdown-list');
    dropdownList.classList.toggle('active');
})