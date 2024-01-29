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
		for (let i = 0; i < this.h; i++){
			console.log('X'.repeat(this.w));
		}
	}

// This method rotates the rectangle
	rotate(){
		print(this.heigth, this.width)
	}
// This method doubles the height and width
	double(){
		this.width = this.width * 2;
		this.height = this.height * 2;
	}
};
