function clicked(anId) {
  //1. fetch data from JSONPlaceholder website...
  //2. get data they responded with
  //3. inject response back into page

  let theURL='/posts/'+anId;
  fetch(theURL)
    .then(response => response.json())
    .then(function(response) {
      console.log(response);
      for(let key in response) {
        document.getElementById(key).innerHTML=
          response[key];
      }
    }
  );

}
