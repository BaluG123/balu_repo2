function randomcolor(){
  letters='0123456789ABCDEF'
  color="#"
  for (var i=0;i<6;i++){
    var r=Math.floor(Math.random()*16)
    color=color+letters[r]
  }
  return color
}
function change(){
var god=document.querySelector('#god');
god.style.color=randomcolor()
var music=document.querySelector('#music')
music.style.color=randomcolor()
var video=document.querySelector('#video')
video.style.color=randomcolor()
//var brand=document.querySelector('#thebrand')
//brand.style.background=randomcolor()
}
setInterval(change,1000)
