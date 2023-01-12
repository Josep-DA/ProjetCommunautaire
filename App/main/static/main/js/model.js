// Teh code for the arrow that brings the user up.

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}


var return_top = document.getElementById('return-top');
var return_top_i = document.getElementById('return_top_i');


window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 740 || document.documentElement.scrollTop > 740) {
    return_top.style.display = "block";
    return_top_i.style = "color: white; background-color: black;";

    return_top_i.addEventListener("mouseover", () => {
      return_top_i.style = "color: black; background-color: white;";
    });

    return_top_i.addEventListener("mouseout", () => {
      return_top_i.style = "color: white; background-color: black;";
    });

  } else if (document.body.scrollTop > 450 || document.documentElement.scrollTop > 450) {
    return_top.style.display = "block";
    return_top_i.style = "border: 2px solid black;";

    return_top_i.addEventListener("mouseover", () => {
      return_top_i.style = "color: white; background-color: black;";
    });

    return_top_i.addEventListener("mouseout", () => {
      return_top_i.style = "color: black; background-color: white;";
    });

  } else {
    return_top.style.display = "none";
  }
}
