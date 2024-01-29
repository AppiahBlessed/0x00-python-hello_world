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

// Prints the square
	charPrint(c){
		if (c){
			for (let i = 0; i < this.size; i++){
				console.log('C'.repeat(this.size));
			}
		} else {
			for (let i = 0; i < this.size; i++){
				console.log('X'.repeat(this.size));
			}
		  }
	};
