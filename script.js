const veriler="April 28, 2023 11:16:00";
const sonuc = "April 28, 2023 11:16:00";
const xhr = new XMLHttpRequest();
xhr.open('GET', 'anket.json', true);
xhr.onload = function() {
  try {
    if (xhr.status === 200) {
      const veriler = JSON.parse(xhr.responseText);
      console.log(veriler.anket_suresi);
      const tarih = new Date(veriler.anket_suresi);
     const options = {
    year: 'numeric',
  month: 'long',
  day: 'numeric',
  hour: 'numeric',
  minute: 'numeric',
  second: 'numeric'
};
const sonuc = tarih;
var dateObj = new Date( sonuc);
var year = dateObj.getFullYear();
var month = dateObj.toLocaleString('default', { month: 'long' });
var day = dateObj.getDate();
var hours = dateObj.getHours();
var minutes = dateObj.getMinutes();
var seconds = dateObj.getSeconds();
var formattedDate = month + " " + padZero(day) + ", " + year + " " + padZero(hours) + ":" + padZero(minutes) + ":" + padZero(seconds);
function padZero(value) {
  return value < 10 ? "0" + value : value;
}
console.log("formatteddt",formattedDate);
console.log("sonuc",sonuc); // "April 27, 2023 13:46:00"
 var tarihSiniri = new Date("April 27, 2023 13:46:00").getTime();
    var tarihSiniri2 = new Date(formattedDate).getTime();
   console.log("tarihSiniri1",tarihSiniri);
     console.log("tarihSiniri1sonuc",tarihSiniri2);
    var interval = setInterval(function() {
    var simdikiZaman = new Date().getTime();
    var fark = tarihSiniri2 - simdikiZaman;
    var gun = Math.floor(fark / (1000 * 60 * 60 * 24));
    var saat = Math.floor((fark % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var dakika = Math.floor((fark % (1000 * 60 * 60)) / (1000 * 60));
    var saniye = Math.floor((fark % (1000 * 60)) / 1000);
    //document.getElementById("geriSayim").innerHTML = gun + " gün " + saat + " saat " + dakika + " dakika " + saniye + " saniye kaldı.";
    if (fark < 0) {
      clearInterval(interval);
      document.getElementById("sayfa").style.display = "none";
    }
  }, 1000);
    }
  } catch (e) {
    console.error("Bir hata oluştu: " + e.message);
  }
};
xhr.send();