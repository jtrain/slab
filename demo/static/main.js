(function() {

var TIMEOUT = 10000;

function showError(message) {
  var notify = document.getElementById('notifications');
  if (message !== undefined) {
    notify.innerHTML = "<div class='alert'><p>" + message + "</p></div>";
  } else {
    notify.innerHTML = "";
  }
}

function checkActive() {
  var request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (request.readyState === XMLHttpRequest.DONE) {
      if (request.status !== 200) {
        showError("Unable to connect. Please start run.py")
      }
    } else {
      showError()
    }
  }
  request.open('GET', '/active');
  request.timeout = TIMEOUT;
  request.ontimeout = function() {
    showError("Unable to connect. Please start run.py")
  }
  request.send();
}

setInterval(checkActive, 10000);

})();
