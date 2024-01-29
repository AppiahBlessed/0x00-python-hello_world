#!/usr/bin/node
/**
* This is a new class, square, that inherits from Rectangle class
*/

class Square extends Rectangle(){
// Declaring the class
	constructor(size){
		super(w, h);
		this.size = size;
	}
};
