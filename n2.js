var next = document.getElementById("next");
var left = document.getElementById("left");
var center = document.getElementById("center");
var right = document.getElementById("right");

function is_black(c) {
  return (c == "i" || c == "I");
}

/* you may use this table :-) */
var table = [{ " ":" ", "i":"T", "T":"i", "I":"I" },
  { " ":"i", "i":"I", "T":" ", "I":"T" }];
  function update_box() {
    var count = 0;
    if ( is_black(left.value) ) { count ++; }
    if ( is_black(right.value) ) { count ++; }
    next.value = table[count%2][center.value];
  }
