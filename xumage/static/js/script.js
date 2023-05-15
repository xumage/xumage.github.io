if(document.querySelector('.slideshow.swiper')) {
	new Swiper('.slideshow', {
		autoplay: {
			delay: 4000,
		 },
		navigation: {
			nextEl: '.swiper-button-next',
			prevEl: '.swiper-button-prev',
		},
	});
}
if(document.querySelector('.menu-info__categories.swiper')) {
	new Swiper('.menu-info__categories', {
		pagination: {
			el: '.menu-info__categories_pagination',
			type: 'progressbar'
		},
		spaceBetween: 15,
		slidesPerView:'auto',
		breakpoints: {
			650: {
				spaceBetween:50
			}
		}
	});
}

//menu
let menuBtn = document.querySelector('.burger')
let menu = document.querySelector('.mobile-menu')
menuBtn.addEventListener('click', toggleMenu)
function toggleMenu() {
	menu.classList.toggle('active')
	menuBtn.classList.toggle('active')
	document.querySelector('html').classList.toggle('no-scroll')
}
//menu