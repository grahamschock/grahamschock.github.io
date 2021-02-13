const { greet, bye, add, myPrint } = wasm_bindgen;

function runApp() {
  //greet('World');
  //bye('all');
  //alert(add(1));
}

function submitText() {
  var x = document.forms["myForm"]["fname"].value;
  (add(x));
}
// Load and instantiate the wasm file, and we specify the source of the wasm
// file here. Once the returned promise is resolved we're ready to go and
// use our imports.
wasm_bindgen('../out/main_bg.wasm').then(runApp).catch(console.error);
