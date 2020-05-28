function toggle_card(name) {
	var image_loc = document.getElementById("card-display");
	image_loc.src = "done_cards/".concat(name, ".png");
	image_loc = document.getElementById("card-display2");
	image_loc.src = "";
	image_loc = document.getElementById("card-display1");
	image_loc.src = "";
}


function toggle_card2(name1, name2) {
	var image_loc = document.getElementById("card-display");
	image_loc.src = "done_cards/".concat(name1, ".png");
	image_loc = document.getElementById("card-display2");
	image_loc.src = "done_cards/".concat(name2, ".png");
	image_loc = document.getElementById("card-display1");
	image_loc.src = "";
}


function toggle_card3(name1, name2, name3) {
	var image_loc = document.getElementById("card-display");
	image_loc.src = "done_cards/".concat(name1, ".png");
	image_loc = document.getElementById("card-display2");
	image_loc.src = "done_cards/".concat(name2, ".png");
	image_loc = document.getElementById("card-display1");
	image_loc.src = "done_cards/".concat(name3, ".png");
}

