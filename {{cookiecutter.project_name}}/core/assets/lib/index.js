import 'whatwg-fetch'

var formregister = document.getElementById('form');
var formlogin = document.getElementById('formlogin');

formregister.addEventListener('submit', function(event) {

event.preventDefault();


fetch('/api/accounts/register/', {
  method: 'POST',
  body: new FormData(form)

}).then(function(response) {
const promise1 = response.json()
 promise1.then((value) => { 
   if(response.ok) {
      token = value.token;
  } else {
  // Response.error();
  alert(Object.values(value));
  //console.log('Mauvaise réponse du réseau'  + error.message );
  }
  console.log('Mauvaise réponse du réseau')
});
})
.catch(function(error) {
  console.log('Il y a eu un problème avec l\'opération fetch: ' + error.message);
});

});



formlogin.addEventListener('submit', function(event) {
fetch('/api/accounts/login/', {
  method: 'POST',
  body: new FormData(form)

}).then(function(response) {
const promise1 = response.json()
 promise1.then((value) => { 
   if(response.ok) {
      alert(Object.values(value));
      token = value.token;
     // myImage.src = objectURL;
  } else {
  // Response.error();
    alert(Object.values(value));
    //console.log('Mauvaise réponse du réseau'  + error.message );
  }
    console.log('Mauvaise réponse du réseau')
  // expected output: "foo"
});

 
})
.catch(function(error) {
  console.log('Il y a eu un problème avec l\'opération fetch: ' + error.message);
});

});

