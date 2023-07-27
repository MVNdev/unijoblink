const navMenu = document.getElementById('nav-responsive');
const buttonToggle = document.getElementById('toggle');
const filterOpen = document.getElementById('filter-open');
const filterClose = document.getElementById('filter-close');
const filter = document.getElementById('filter');

const showFilter = () => {
    console.log("Press");
    const contain = filter.classList.contains("-right-full")
    if (contain) {
        filter.classList.remove("-right-full");
        filter.classList.add("right-0");
    } else {
        filter.classList.remove("right-0");
        filter.classList.add("-right-full");
    }
};

buttonToggle.addEventListener('click', () => {
    const contain = navMenu.classList.contains("-top-48")
    if (contain) {
        navMenu.classList.remove("-top-48");
        navMenu.classList.add("top-20");
    } else {
        navMenu.classList.remove("top-20");
        navMenu.classList.add("-top-48");
    }
});

filterOpen.addEventListener('click', () => showFilter());
filterClose.addEventListener('click', () => showFilter());