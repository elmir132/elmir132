const shareBtn1 = document.querySelector('.share-btn1');
const shareOptions1 = document.querySelector('.share-options1');

shareBtn1.addEventListener('click', () => {
    shareOptions1.classList.toggle('active');
})