function toggle_card(name) {
	var image_loc = document.getElementById("card-display");
	image_loc.src = "done_cards/".concat(name, ".png");
	image_loc = document.getElementById("card-display2");
	image_loc.src = "";
	image_loc = document.getElementById("card-display1");
	image_loc.src = "";
	image_loc = document.getElementById("card-display0");
	image_loc.src = "";
}


function toggle_card2(name1, name2) {
	var image_loc = document.getElementById("card-display");
	image_loc.src = "done_cards/".concat(name1, ".png");
	image_loc = document.getElementById("card-display2");
	image_loc.src = "done_cards/".concat(name2, ".png");
	image_loc = document.getElementById("card-display1");
	image_loc.src = "";
	image_loc = document.getElementById("card-display0");
	image_loc.src = "";
}


function toggle_card3(name1, name2, name3) {
	var image_loc = document.getElementById("card-display");
	image_loc.src = "done_cards/".concat(name1, ".png");
	image_loc = document.getElementById("card-display2");
	image_loc.src = "done_cards/".concat(name2, ".png");
	image_loc = document.getElementById("card-display1");
	image_loc.src = "done_cards/".concat(name3, ".png");
	image_loc = document.getElementById("card-display0");
	image_loc.src = "";
}


function toggle_card4(name1, name2, name3, name4) {
	var image_loc = document.getElementById("card-display");
	image_loc.src = "done_cards/".concat(name1, ".png");
	image_loc = document.getElementById("card-display2");
	image_loc.src = "done_cards/".concat(name2, ".png");
	image_loc = document.getElementById("card-display1");
	image_loc.src = "done_cards/".concat(name3, ".png");
	image_loc = document.getElementById("card-display0");
	image_loc.src = "done_cards/".concat(name4, ".png");
}


function rotate_cards() {
	var image_loc1 = document.getElementById("card-display2");
	src1 = image_loc1.src
	var image_loc2 = document.getElementById("card-display1");
	src2 = image_loc2.src
	var image_loc3 = document.getElementById("card-display0");
	src3 = image_loc3.src

	if (!(image_loc2.getAttribute('src') == "")) {
		if (!(image_loc3.getAttribute('src') == "")) {
			image_loc1.src = src2
			image_loc2.src = src3
			image_loc3.src = src1
		} else {
			image_loc1.src = src2
			image_loc2.src = src1
		}
	}
}


