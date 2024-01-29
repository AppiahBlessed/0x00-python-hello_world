#!/usr/bin/node
/**
* The continuation of the Rectangle class
*/
class Rectangle {
// Class declaration
	constructor(w, h){
		if (w > 0 || h > 0) {
			this.width = w;
			this.heigth = h;
		}
	}
	
// Method prints a square
	print(){
		for (let i = 0; i < this.heigth; i++){
			console.log('X'.repeat(this.width));
		}
	}
};
