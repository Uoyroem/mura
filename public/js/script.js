
searchBox = document.querySelector('.form-box');

document.querySelector('#search-btn').onclick = () => {

    searchBox.classList.toggle('active');
}

window.onscroll = () => {

    searchBox.classList.remove('active');

    if(window.scrollY > 80){

        document.querySelector('.header .header-2').classList.add('active');
    }
    else
    {
        document.querySelector('.header .header-2').classList.remove('active');
    }
}

window.onabort = () => {

    if(window.scrollY > 80){

        document.querySelector('.header .header-2').classList.add('active');
    }
    else
    {
        document.querySelector('.header .header-2').classList.remove('active');
    }
}


/*----- login form -------- */

var loginForm = document.querySelector('.login-form-container');

document.querySelector('#login-btn').onclick = () =>{

    loginForm.classList.toggle('active');
}

document.querySelector('#close-login-btn').onclick = () =>{

    loginForm.classList.remove('active');
}

/*-------- swiper ----------*/

var swiper = new Swiper(".books-list", {
    
    loop:true,
    centeredSlides:true,
    autoplay:{
        delete:9500,
        disableOnInteraction:false,
    },
    breakpoints: {
     0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
    },
  });

/*-------- featured section start ----------*/

var swiper = new Swiper(".featured-slider", {
    
    spaceBetween:10,
    loop:true,
    centeredSlides:true,
    autoplay:{
        delete:9500,
        disableOnInteraction:false,
    },
    navigation:{
        nextEl:".swiper-button-next",
        prevEl:".swiper-button-prev",
    },
    breakpoints: {
     0: {
        slidesPerView: 1,
      },
      450:{
        slidesPerView: 2,
      },
      768: {
        slidesPerView: 3,
      },
      1024: {
        slidesPerView: 4,
      },
    },
  });


  /*-------- arrivals section start ----------*/
  
  var swiper = new Swiper(".arrivals-slider", {
    spaceBetween: 10,
    loop:true,
    centeredSlides:true,
    autoplay:{
        delete:9500,
        disableOnInteraction:false,
    },
    breakpoints: {  
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
    },
  });