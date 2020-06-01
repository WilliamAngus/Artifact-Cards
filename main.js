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

function toggle_card(obj, name) {
	show_lore(obj)
	show_keywords(obj);
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


function toggle_card2(obj, name1, name2) {
	show_lore(obj)
	show_keywords(obj);
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


function toggle_card3(obj, name1, name2, name3) {
	show_lore(obj)
	show_keywords(obj);
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


function toggle_card4(obj, name1, name2, name3, name4) {
	show_lore(obj)
	show_keywords(obj);
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




function add_filter(filter_colour, filter_other, filter_item) {
	elements = document.getElementsByClassName("card");
	filters_colours = filter_colour.split(" ");
	filters_others = filter_other.split(" ");
	filters_items = filter_item.split(" ");
	for (var i = 0; i < elements.length; i++) {
		remove_class(elements[i], "card-show");
		add_class(elements[i], "hide");
		if (!(filter_colour === "" && filter_other === "" && filter_item !== "")) {
			for (var j = 0; j < filters_colours.length; j++) {
				if (elements[i].className.indexOf(filters_colours[j]) > -1) {
					for (var k = 0; k < filters_others.length; k++) {
						if (elements[i].className.indexOf(filters_others[k]) > -1) {
							add_class(elements[i], "card-show");
							remove_class(elements[i], "hide");
						}
					}
				}
			}
		}
		if (filter_item === "") {
			continue;
		}
		for (var j = 0; j < filters_items.length; j++) {
			if (elements[i].className.indexOf(filters_items[j]) > -1) {
				add_class(elements[i], "card-show");
				remove_class(elements[i], "hide");
			}
		}
	}
}


var colours_selected = []
var selected = []
var items_selected = []

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
	add_filter(colours_selected.join(" "), selected.join(" "), items_selected.join(" "));
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
	add_filter(colours_selected.join(" "), selected.join(" "), items_selected.join(" "));
}


function toggle_item(obj, kind) {
	var t = "type-".concat(kind)
	if (items_selected.indexOf(t) == -1) {
		items_selected.push(t);
		remove_class(obj, "button-item-unselected")
		add_class(obj, "button-item-selected")
	} else {
		items_selected = items_selected.filter(x => x !== t);
		add_class(obj, "button-item-unselected")
		remove_class(obj, "button-item-selected")
	}
	add_filter(colours_selected.join(" "), selected.join(" "), items_selected.join(" "));
}


function search() {
	var field = document.getElementById("card-search");
	var text = field.value.toUpperCase();
	var elements = document.getElementsByClassName("card");

	for (var i = 0; i < elements.length; i++) {
		var t  = elements[i].getElementsByClassName("name")[0].textContent;
		if (t.toUpperCase().indexOf(text) > -1) {
			remove_class(elements[i], "hide-search")
		} else {
			var t  = elements[i].getElementsByClassName("keywords")[0].className.replace("keywords", "");
			if (t.toUpperCase().indexOf(text.replace(/\s+/g, '-')) > -1) {
				remove_class(elements[i], "hide-search")
			} else {
				add_class(elements[i], "hide-search")
			}
		}
	}
}


var undraftable = false
function toggle_draftable(obj) {
	if (undraftable) {
		var elements = document.getElementsByClassName("card-undraftable");
		for (var i = 0; i < elements.length; i++) {
			remove_class(elements[i], "card-show-undraftable");
		}
		undraftable = false
		add_class(obj, "button-card-selected")
		remove_class(obj, "button-card-unselected")
	} else {
		var elements = document.getElementsByClassName("card-undraftable");
		for (var i = 0; i < elements.length; i++) {
			add_class(elements[i], "card-show-undraftable");
		}
		undraftable = true
		remove_class(obj, "button-card-selected")
		add_class(obj, "button-card-unselected")
	}
}

function show_lore(obj) {
	document.getElementById("lore-display").innerHTML = obj.getElementsByClassName("lore")[0].innerHTML;
}


function show_keywords(obj) {
	text = "";
	l = obj.getElementsByClassName("keywords")[0].className.replace("keywords ", "").split(" ");
	for (var i = 0; i < l.length; i++) {
		o = document.getElementById("keyword" + l[i]);
		if (!!o) {
			text = text.concat("<p><b>", l[i].replace("-", " "), ":</b> ", o.innerHTML, "</p>");
		}
	}
	document.getElementById("keyword-holder-inner").innerHTML = text;
}

