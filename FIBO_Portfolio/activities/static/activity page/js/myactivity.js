//section1

function openModal() {
  document.getElementById('myModal').style.display = "block";
}

function closeModal() {
  document.getElementById('myModal').style.display = "none";
}

var slideIndex = 1;
showSlides(slideIndex);


function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;

}
//end section1

//section2
function openModal2() {
  document.getElementById('myModal2').style.display = "block";
}

function closeModal2() {
  document.getElementById('myModal2').style.display = "none";
}

var slideIndex2 = 1;
showSlides2(slideIndex2);

function plusSlides2(n) {
  showSlides2(slideIndex2 += n);
}

function currentSlide2(n) {
  showSlides2(slideIndex2 = n);
}

function showSlides2(n) {
  var j;
  var slides2 = document.getElementsByClassName("mySlides2");
  var dots2 = document.getElementsByClassName("demo2");
  var captionText2 = document.getElementById("caption2");
  if (n > slides2.length) {slideIndex2 = 1}
  if (n < 1) {slideIndex2 = slides2.length}
  for (j = 0; j < slides2.length; j++) {
      slides2[j].style.display = "none";
  }
  for (j = 0; j < dots2.length; j++) {
      dots2[j].className = dots2[j].className.replace(" active", "");
  }
  slides2[slideIndex2-1].style.display = "block";
  dots2[slideIndex2-1].className += " active";
  captionText2.innerHTML = dots2[slideIndex2-1].alt;
}
//end section2

// section3
function openModal3() {
  document.getElementById('myModal3').style.display = "block";
}

function closeModal3() {
  document.getElementById('myModal3').style.display = "none";
}

var slideIndex3 = 1;
showSlides3(slideIndex3);

function plusSlides3(n) {
  showSlides3(slideIndex3 += n);
}

function currentSlide3(n) {
  showSlides3(slideIndex3 = n);
}

function showSlides3(n) {
  var k;
  var slides3 = document.getElementsByClassName("mySlides3");
  var dots3 = document.getElementsByClassName("demo3");
  var captionText3 = document.getElementById("caption3");
  if (n > slides3.length) {slideIndex3 = 1}
  if (n < 1) {slideIndex3 = slides3.length}
  for (k = 0; k < slides3.length; k++) {
      slides3[k].style.display = "none";
  }
  for (k = 0; k < dots3.length; k++) {
      dots3[k].className = dots3[k].className.replace(" active", "");
  }
  slides3[slideIndex3-1].style.display = "block";
  dots3[slideIndex3-1].className += " active";
  captionText3.innerHTML = dots3[slideIndex3-1].alt;
}
