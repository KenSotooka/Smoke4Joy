const track = document.getElementById("image-track")
track.dataset.mouseDownAt = "0";
window.onmousedown = e => {
    track.dataset.mouseDownAt = e.clientX;   
}
window.onmouseup = () => {
    track.dataset.mouseDownAt = "0";
    track.dataset.prevPercentage = track.dataset.percentage;
}
window.onmousemove = e => {
    if(track.dataset.mouseDownAt === "0") return;

    const mouseMove = parseFloat(track.dataset.mouseDownAt) - e.clientX;
        maxmove = window.innerWidth/2;

    const percentage = (mouseMove/maxmove) *-75;
    nextPercentageUnconstrained = parseFloat(track.dataset.prevPercentage) + percentage,
    nextpercentage = Math.max(Math.min(nextPercentageUnconstrained, 0), -100);
    track.dataset.percentage = nextpercentage;
    track.style.transform = `translate(${nextpercentage}%,-50%)`;

    track.animate({
        transform: `translate(${nextpercentage}%, -50%)`
      }, { duration: 1200, fill: "forwards" });
      
      for(const image of track.getElementsByClassName("image")) {
        image.animate({
          objectPosition: `${100 + nextpercentage}% center`
        }, { duration: 1200, fill: "forwards" });
      }
}
document.getElementById('image1big').hidden = true;
document.getElementById('image2big').hidden = true;
document.getElementById('image3big').hidden = true;
document.getElementById('image4big').hidden = true;
document.getElementById('image5big').hidden = true;
document.getElementById('image6big').hidden = true;
document.getElementById('image7big').hidden = true;
document.getElementById('image8big').hidden = true;
document.getElementById('image9big').hidden = true;

document.getElementById('info1').hidden = true;
document.getElementById('info2').hidden = true;
//counter = 0;
function big1(){
    
    //counter++; 
    document.getElementById('image1big').hidden = false;document.getElementById('info1').hidden = false;}
function bighide(){document.getElementById('image1big').classList.add("animation");document.getElementById('image1big').hidden = true;document.getElementById('info1').hidden = true;}

function big2(){document.getElementById('image2big').hidden = false;document.getElementById('info2').hidden = false;}
function bighide1(){document.getElementById('image2big').hidden = true;document.getElementById('info2').hidden = true;}

function big3(){document.getElementById('image3big').hidden = false;}
function bighide2(){document.getElementById('image3big').hidden = true;}

function big4(){document.getElementById('image4big').hidden = false;}
function bighide3(){document.getElementById('image4big').hidden = true;}

function big5(){document.getElementById('image5big').hidden = false;}
function bighide4(){document.getElementById('image5big').hidden = true;}

function big6(){document.getElementById('image6big').hidden = false;}
function bighide5(){document.getElementById('image6big').hidden = true;}

function big7(){document.getElementById('image7big').hidden = false;}
function bighide6(){document.getElementById('image7big').hidden = true;}

function big8(){document.getElementById('image8big').hidden = false;}
function bighide7(){document.getElementById('image8big').hidden = true;}

function big9(){document.getElementById('image9big').hidden = false;}
function bighide8(){document.getElementById('image9big').hidden = true;}