function add_class(element, name) {
	var classes = element.className.split(" ");
	var new_classes = name.split(" ");
	for (var i = 0; i < new_classes.length; i++) {
		if (classes.indexOf(new_classes[i]) == -1) {
			element.className += " " + new_classes[i];
		}
	}
}


function remove_class(element, name) {
	var classes = element.className.split(" ");
	var old_classes = name.split(" ");
	for (var i = 0; i < old_classes.length; i++) {
		while (classes.indexOf(old_classes[i]) > -1) {
			classes.splice(classes.indexOf(old_classes[i]), 1);
		}
	}
	element.className = classes.join(" ");
}

function toggle_card(name) {
	var image_loc = document.getElementById("card-display");
	image_loc.src = "done_cards/".concat(name, ".png");
	image_loc = document.getElementById("card-display2");
	image_loc.src = "";
	image_loc = document.getElementById("card-display1");
	image_loc.src = "";
	image_loc = document.getElementById("card-display0");
	image_loc.src = "";
	add_class(document.getElementById("text-shuffle"), "hide");

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
	add_class(document.getElementById("text-shuffle"), "hide");
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
	remove_class(document.getElementById("text-shuffle"), "hide");
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
	remove_class(document.getElementById("text-shuffle"), "hide");
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


function add_filter(filter_colour, filter_other) {
	elements = document.getElementsByClassName("card");
	filters_colours = filter_colour.split(" ");
	filters_others = filter_other.split(" ");
	for (var i = 0; i < elements.length; i++) {
		remove_class(elements[i], "card-show");
		for (var j = 0; j < filters_colours.length; j++) {
			if (elements[i].className.indexOf(filters_colours[j]) > -1) {
				for (var k = 0; k < filters_others.length; k++) {
					if (elements[i].className.indexOf(filters_others[k]) > -1) {
						add_class(elements[i], "card-show");
					}
				}
			}
		}
	}
}


var colours_selected = []
var selected = []

function toggle_colour(obj, colour) {
	var c = "colour-".concat(colour)
	if (colours_selected.indexOf(c) == -1) {
		colours_selected.push(c);
		add_class(obj, "button-".concat(colour, "-selected"))
		remove_class(obj, "button-".concat(colour, "-unselected"))
	} else {
		colours_selected = colours_selected.filter(x => x !== c);
		add_class(obj, "button-".concat(colour, "-unselected"))
		remove_class(obj, "button-".concat(colour, "-selected"))
	}
	add_filter(colours_selected.join(" "), selected.join(" "));
}




function toggle_type(obj, kind) {
	var t = "type-".concat(kind)
	if (selected.indexOf(t) == -1) {
		selected.push(t);
		remove_class(obj, "button-card-unselected")
		add_class(obj, "button-card-selected")
	} else {
		selected = selected.filter(x => x !== t);
		add_class(obj, "button-card-unselected")
		remove_class(obj, "button-card-selected")
	}
	add_filter(colours_selected.join(" "), selected.join(" "));
}


function toggle_item(obj, kind) {
	var t = "type-".concat(kind)
	if (selected.indexOf(t) == -1) {
		selected.push(t);
		remove_class(obj, "button-item-unselected")
		add_class(obj, "button-item-selected")
	} else {
		selected = selected.filter(x => x !== t);
		add_class(obj, "button-item-unselected")
		remove_class(obj, "button-item-selected")
	}
	add_filter(colours_selected.join(" "), selected.join(" "));
}


function search() {
	var field = document.getElementById("card-search");
	var text = field.value.toUpperCase();
	var elements = document.getElementsByClassName("card");

	for (var i = 0; i < elements.length; i++) {
		var t  = elements[i].getElementsByClassName("name")[0].textContent;
		if (t.toUpperCase().indexOf(text) > -1) {
			elements[i].style.display = "flex";
		} else {
			elements[i].style.display = "none";
		}
	}
}


