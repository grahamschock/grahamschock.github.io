// Current prelude for using `wasm_bindgen`, and this'll get smaller over time!
#![feature(proc_macro, wasm_custom_section, wasm_import_module)]
extern crate wasm_bindgen;
extern crate genpdf;
use wasm_bindgen::prelude::*;
use std::char;
use genpdf::*;

// Here we're importing the `alert` function from the browser, using
// `#[wasm_bindgen]` to generate correct wrappers.
#[wasm_bindgen]
extern {
    fn alert(s: &str);
}

// Here we're exporting a function called `greet` which will display a greeting
// for `name` through a dialog.
#[wasm_bindgen]
pub fn greet(name: &str) {
    alert(&format!("Hello, {}!", name));
}

#[wasm_bindgen]
pub fn bye(name: &str) {
    alert(&format!("Bye, {}!", name));
}

#[wasm_bindgen]
pub fn add(s: &str) {
  let sum = 0;
  let mut vec: Vec<char> = vec![];
  for c in s.chars() {
    let mut i = c as u32;
    i = i + 1;
    let c1 = char::from_u32(i);
    vec.push(c1.unwrap());
  }
  let s: String = vec.iter().collect();
  alert(&format!("int value {:?}!", s));
}