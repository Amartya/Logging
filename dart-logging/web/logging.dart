import 'dart:html';
import 'dart:convert';

void main() {
  querySelector("#submit-btn")
      ..text = "Submit"
      ..onClick.listen(sendData);
}

void sendData(MouseEvent event) {
  InputElement appId = document.querySelector("#app-id");
  InputElement appData = document.querySelector("#app-data");

  HttpRequest request = new HttpRequest(); // create a new XHR

  // add an event handler that is called when the request finishes
  request.onReadyStateChange.listen((_) {
    if (request.readyState == HttpRequest.DONE &&
       (request.status == 200 || request.status == 0)) {
      // data saved OK.
      print(request.responseText); // output the response from the server
    }
  });

  //Store form data
  Map data = new Map();
  data['app_id'] = appId.value;
  data['app_data'] = appData.value;


  //setup to POST data to the server
  //request.open("POST","http://54.69.228.220/reese/", async: false);
  request.open("POST","http://127.0.0.1:8000/reese/", async: true);

  //we can set the content type to "application/x-www-form-urlencoded; charset=UTF-8"
  //otherwise the Django side gets an empty POST Query dictionary,
  //If we set the content-type to application/json, we can use the request.body
  //variable in Django
  //request.setRequestHeader("Content-type","application/x-www-form-urlencoded; charset=UTF-8");

  request.setRequestHeader("Content-type","application/json");

  request.send(JSON.encode(data)); // perform the async POST
}
