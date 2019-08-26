// HTML5 Web Storage (https://www.w3schools.com/html/html5_webstorage.asp)
- HTML web storage; better than cookies.
// 2 types:
* window.localStorage - stores data with no expiration date
* window.sessionStorage - stores data for one session (data is lost when the browser tab is closed)
// Store
localStorage.setItem("lastname", "Smith");
localStorage.lastname = "Smith";
// Retrieve
document.getElementById("result").innerHTML = localStorage.getItem("lastname");
document.getElementById("result").innerHTML = localStorage.lastname;
// Remove
localStorage.removeItem("lastname");

// HTML5 Web Worker (https://www.w3schools.com/html/html5_webworkers.asp)
//------------------------------------------------------------------------------------

// NOTE
// Don’t use arrow functions on an options property or callback,
// such as created: () => console.log(this.a) or vm.$watch('a', newValue => this.myMethod()) .
// Since an arrow function doesn’t have a this

// delete item from array (by index)
array_var.splice(index, 1);

// delete item from array (by key value)
let id_to_exclude = '0002';
array_var = array_var.find( user => user.id != id_to_exclude );

// delete property from object
var Employee = { firstname: "John", lastname: "Doe" }
delete Employee.firstname;
//------------------------------------------------------------------------------------

// typeof
if (typeof(Storage) !== "undefined") {...}

// find item by key
let users = [
	{id: '0001', name: 'edward'},
	{id: '0002', name: 'jose'},
	{id: '0003', name: 'ardy'},
	{id: '0004', name: 'emir'},
];
let find_user = users.find( user => user.id == '0002' );
// find_user:
// {id: "0002", name: "jose"}


// get index of item to find (array of objects)
let users = [
	{id: '0001', name: 'edward'},
	{id: '0002', name: 'jose'},
	{id: '0003', name: 'ardy'},
	{id: '0004', name: 'emir'},
];
let find_index = users.findIndex( user => user.id == '0002' );
// find_index:
// 1


// check string in array of strings
var fruits = ["Banana", "Orange", "Apple", "Mango"];
var n = fruits.includes("Mango");
// n is true


// filter
let myArray = [3.14, 2.718, 1.618]
const result = myArray.filter( x => x < 3 );
console.log(result)
// [2.718, 1.618]


// NOTES
Array.prototype.find() – find and return an item
Array.prototype.findIndex() – find and return an index
Array.prototype.includes() – test whether a value exists in the array
Array.prototype.filter() – find all matching elements and return an array
Array.prototype.every() – test all elements together
Array.prototype.some() – test at least one element


// indexOf
var str = "Hello world, welcome to the universe.";
var n = str.indexOf("welcome");
//------------------------------------------------------------------------------------

// AXIOS
// <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
// GET
let url = API_SERVER + '/mobile/licenses'
axios.get(url)
.then(response => {
	this.licenses = response.data.licenses
})
.catch(error => {
	console.log(error)
	this.isFetchError = true
})
.finally(() => this.isLoading = false )

// Optionally the request above could also be done as
axios.get(url, {
	params: {
		ID: 12345
	}
})
.then(response => {
	this.licenses = response.data.licenses
})
.catch(error => {
	console.log(error)
	this.isFetchError = true
})
.finally(() => this.isLoading = false )

// POST
axios.post(url, {
	firstName: 'Fred',
	lastName: 'Flintstone'
})
.then(response => {
	this.licenses = response.data.licenses
})
.catch(error => {
	console.log(error)
	this.isFetchError = true
})
.finally(() => this.isLoading = false )
//------------------------------------------------------------------------------------

// arrow functions
// single statement inside
.catch(() => console.log(error))
//- no parameter
.catch(() => {
	...
})
//- 1 parameter
.catch(error => {
	console.log(error)
	this.isFetchError = true
})
//- 2 parameters
.catch((error, error2) => {
	console.log(error)
	this.isFetchError = true
})
//------------------------------------------------------------------------------------

// # JSON
// a) To String
JSON.stringify(user_acl)
// b) To Object
JSON.parse(sel_acl)
//------------------------------------------------------------------------------------

// # Check if key in json var
if (resp.hasOwnProperty('error')) {}
//------------------------------------------------------------------------------------

// # Sleep
setTimeout(function() {
	$("#main_content").load("/pre_config/function.php?type="+type+"piz&count=1", successCallback );
}, 3000);
//------------------------------------------------------------------------------------

// # Array to Comma-delimited string
var arr = ["Zero", "One", "Two"];
console.log(arr.join(", "));
// --> "Zero, One, Two"
var arr = [0,1,2,3];
console.log(arr.join(,));
// --> "0,1,2,3"
//------------------------------------------------------------------------------------

// # Comma-delimited to array
var c = "0,1,2,3";
console.log(c.split(','))
// --> Array [ "0", "1", "2", "3" ]
//------------------------------------------------------------------------------------

//------------------
// Array Oprations
//------------------
// Map
// Give me a new array of all values multiplied by 10.
let newArr = [5, 6, 7, 8, 900].map( x => x * 10 );
// [50, 60, 70, 80, 9000]

// Map array of objects
let tableData = [
	{firstName: 'edward', lastName: 'abd'},
	{firstName: 'lincoln', lastName: 'def'},
	{firstName: 'murphy', lastName: 'ghi'},
]
return tableData.map(item => {
	item.lastName = 'jose'
	return item
})
//---------------------------------------------

// forEach
// Create links to specs and drop them into #links.
myArray.forEach(function(item, index) {
	console.log(index);
	console.log(item);
});
//---------------------------------------------

// loop objects
var object1 = {a: 1, b: 2, c: 3};
for (var property1 in object1) {
	console.log(property1, object1[property1]);
}
//------------------------------------------------------------------------------------

// string utilities
// <script data-script-name="string utilities">
String.prototype.format=function(){var a=arguments;return this.replace(/\{(\d+)\}/g,function(m,n){return a[n];});};
String.prototype.jinjaFormat=function(){var a=arguments[0],z=arguments[1];return (a===undefined)?this:(a.constructor===Object)?(this.replace(/\{\{ *[a-zA-Z0-9_.]+ *\}\}/g,function(x){var k=x.replace(/\{|\}|\ /g, '').split('.'),b=a;while(k.length&&(b=b[k.shift()]));return (b===undefined && z!==undefined)?z:b;})):this;};
String.prototype.titleCase=function(){var s=this.toLowerCase().split(' ');for(var i=0;i<s.length; i++){s[i]='{0}{1}'.format(s[i].charAt(0).toUpperCase(),s[i].slice(1));}return s.join(' ');};
String.prototype.in=function(){return (arguments[0]===undefined)?false:(arguments[0].constructor===Array)?(arguments[0].indexOf(String(this))===-1)?false:true:false;};
// </script>
// <script data-script-name="object utilities">
"function"!=typeof Object.assign&&Object.defineProperty(Object,"assign",{value:function(e,t){"use strict";if(null==e)throw new TypeError("Cannot convert undefined or null to object");for(var n=Object(e),r=1;r<arguments.length;r++){var o=arguments[r];if(null!=o)for(var c in o)Object.prototype.hasOwnProperty.call(o,c)&&(n[c]=o[c])}return n},writable:!0,configurable:!0});
function merge_objects(b,t){if(b.constructor===Object&&t.constructor===Object){for(p in t){if(b.hasOwnProperty(p)){b[p]=merge_objects(b[p],t[p])}else{b[p]=t[p];}}}else{b=t;}return b;}
// </script>
// <script data-script-name="csrf protection">
var csrf_key = '{{ session["csrf_key"] }}';
var csrf_token = '{{ session["csrf_token"] }}';
// </script>

// merge objects
const emp = { "name": "Roy", "age": "30" }
const empDetails = { "currentLocation": "Dubai", "country": "USA" }
let result = { ...emp, ...empDetails }
console.log(result);


// trim string
let a = 'hello '
a.trim()
// result: 'hello'

// replace variable in string / string format
let a = `account created for ${user.email}`
//------------------------------------------------------------------------------------

// promise test (https://codeburst.io/a-simple-guide-to-es6-promises-d71bacd2e13a)
const promise1 = new Promise((resolve, reject) => {
	setTimeout(() => {
		const raffle = Math.round(Math.random());
		if (raffle == 1)
		resolve('resolved!');
		else
		reject('rejected!');
	}, 1500);
});

promise1
	.then((value) => {
		console.log(value);
	})
	.catch((value) => {
		console.log(value);
	})
	.finally(() => {
		console.log('finally:');
	});
//------------------------------------------------------------------------------------

// Random generator
Math.random();              // returns a random number (ex: 0.2375854977177696)
Math.floor(Math.random() * 10);     // returns a random integer from 0 to 9
Math.floor(Math.random() * 10) + 1;  // returns a random integer from 1 to 10

function getRndInteger(min, max) {
	return Math.floor(Math.random() * (max - min + 1) ) + min;
}
//------------------------------------------------------------------------------------

// Append dictionary as part of new dictionary
// - use 3 dots
projects.push({
	id: change.doc.id,
	...other_projects_obj
})
//------------------------------------------------------------------------------------

/* *******************************************************************************************
* GLOBAL OBJECTS > OBJECT
* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object
* ******************************************************************************************* */

// Global object: properties
Object.length                                        // length is a property of a function object, and indicates how many arguments the function expects, i.e. the number of formal parameters. This number does not include the rest parameter. Has a value of 1.
Object.prototype                                     // Represents the Object prototype object and allows to add new properties and methods to all objects of type Object.

// Methods of the Object constructor
Object.assign(target, ...sources)                    // Copies the values of all enumerable own properties from one or more source objects to a target object. method is used to copy the values of all enumerable own properties from one or more source objects to a target object. It will return the target object
Object.create(MyObject)                              // Creates a new object with the specified prototype object and properties. The object which should be the prototype of the newly-created object.
Object.defineProperty(obj, prop, descriptor)         // Adds the named property described by a given descriptor to an object.
Object.defineProperties(obj, props)                  // Adds the named properties described by the given descriptors to an object.
Object.entries(obj)                                  // Returns an array containing all of the [key, value] pairs of a given object's own enumerable string properties.
Object.freeze(obj)                                   // Freezes an object: other code can't delete or change any properties.
Object.getOwnPropertyDescriptor(obj, prop)           // Returns a property descriptor for a named property on an object.
Object.getOwnPropertyDescriptors(obj)                // Returns an object containing all own property descriptors for an object.
Object.getOwnPropertyNames(obj)                      // Returns an array containing the names of all of the given object's own enumerable and non-enumerable properties.
Object.getOwnPropertySymbols(obj)                    // Returns an array of all symbol properties found directly upon a given object.
Object.getPrototypeOf(obj)                           // Returns the prototype of the specified object.
Object.is(value1, value2);                           // Compares if two values are the same value. Equates all NaN values (which differs from both Abstract Equality Comparison and Strict Equality Comparison).
Object.isExtensible(obj)                             // Determines if extending of an object is allowed.
Object.isFrozen(obj)                                 // Determines if an object was frozen.
Object.isSealed(obj)                                 // Determines if an object is sealed.
Object.keys(obj)                                     // Returns an array containing the names of all of the given object's own enumerable string properties.
Object.preventExtensions(obj)                        // Prevents any extensions of an object.
Object.seal(obj)                                     // Prevents other code from deleting properties of an object.
Object.setPrototypeOf(obj, prototype)                // Sets the prototype (i.e., the internal [[Prototype]] property).
Object.values(obj)                                   // Returns an array containing the values that correspond to all of a given object's own enumerable string properties.

// Object instances and Object prototype object (Object.prototype.property or Object.prototype.method())
// Properties
obj.constructor                                      // Specifies the function that creates an object's prototype.
obj.__proto__                                        // Points to the object which was used as prototype when the object was instantiated.

// Methods
obj.hasOwnProperty(prop)                             // Returns a boolean indicating whether an object contains the specified property as a direct property of that object and not inherited through the prototype chain.
prototypeObj.isPrototypeOf(object)                   // Returns a boolean indicating whether the object this method is called upon is in the prototype chain of the specified object.
obj.propertyIsEnumerable(prop)                       // Returns a boolean indicating if the internal ECMAScript [[Enumerable]] attribute is set.
obj.toLocaleString()                                 // Calls toString().
obj.toString()                                       // Returns a string representation of the object.
object.valueOf()                                     // Returns the primitive value of the specified object.

/* *******************************************************************************************
* GLOBAL OBJECTS > ARRAY
* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
* ******************************************************************************************* */

// Global object: properties
Array.length                                         // Reflects the number of elements in an array.
Array.prototype                                      // Represents the prototype for the Array constructor and allows to add new properties and methods to all Array objects.

// Global object: methods
Array.from(arrayLike[, mapFn[, thisArg]])            // Creates a new Array instance from an array-like or iterable object.
Array.isArray(obj)                                   // Returns true if a variable is an array, if not false.
Array.of(element0[, element1[, ...[, elementN]]])    // Creates a new Array instance with a variable number of arguments, regardless of number or type of the arguments.

// Instance: properties
arr.length                                           // Reflects the number of elements in an array.

// Instance: mutator methods
arr.copyWithin(target, start, end)                   // Copies a sequence of array elements within the array.
arr.fill(value, start, end)                          // Fills all the elements of an array from a start index to an end index with a static value.
arr.pop()                                            // Removes the last element from an array and returns that element.
arr.push([element1[, ...[, elementN]]])              // Adds one or more elements to the end of an array and returns the new length of the array.
arr.reverse()                                        // Reverses the order of the elements of an array in place — the first becomes the last, and the last becomes the first.
arr.shift()                                          // Removes the first element from an array and returns that element.
arr.sort()                                           // Sorts the elements of an array in place and returns the array.
array.splice(start, deleteCount, item1, item2, ...)  // Adds and/or removes elements from an array.
arr.unshift([element1[, ...[, elementN]]])           // Adds one or more elements to the front of an array and returns the new length of the array.

// Instance: accessor methods
arr.concat(value1[, value2[, ...[, valueN]]])        // Returns a new array comprised of this array joined with other array(s) and/or value(s).
arr.includes(searchElement, fromIndex)               // Determines whether an array contains a certain element, returning true or false as appropriate.
arr.indexOf(searchElement[, fromIndex])              // Returns the first (least) index of an element within the array equal to the specified value, or -1 if none is found.
arr.join(separator)                                  // Joins all elements of an array into a string.
arr.lastIndexOf(searchElement, fromIndex)            // Returns the last (greatest) index of an element within the array equal to the specified value, or -1 if none is found.
arr.slice(begin, end)                                // Extracts a section of an array and returns a new array.
arr.toString()                                       // Returns a string representing the array and its elements. Overrides the Object.prototype.toString() method.
arr.toLocaleString(locales, options)                 // Returns a localized string representing the array and its elements. Overrides the Object.prototype.toLocaleString() method.

// Instance: iteration methods
arr.entries()                                        // Returns a new Array Iterator object that contains the key/value pairs for each index in the array.
arr.every(callback[, thisArg])                       // Returns true if every element in this array satisfies the provided testing function.
arr.filter(callback[, thisArg])                      // Creates a new array with all of the elements of this array for which the provided filtering function returns true.
arr.find(callback[, thisArg])                        // Returns the found value in the array, if an element in the array satisfies the provided testing function or undefined if not found.
arr.findIndex(callback[, thisArg])                   // Returns the found index in the array, if an element in the array satisfies the provided testing function or -1 if not found.
arr.forEach(callback[, thisArg])                     // Calls a function for each element in the array.
arr.keys()                                           // Returns a new Array Iterator that contains the keys for each index in the array.
arr.map(callback[, initialValue])                    // Creates a new array with the results of calling a provided function on every element in this array.
arr.reduce(callback[, initialValue])                 // Apply a function against an accumulator and each value of the array (from left-to-right) as to reduce it to a single value.
arr.reduceRight(callback[, initialValue])            // Apply a function against an accumulator and each value of the array (from right-to-left) as to reduce it to a single value.
arr.some(callback[, initialValue])                   // Returns true if at least one element in this array satisfies the provided testing function.
arr.values()                                         // Returns a new Array Iterator object that contains the values for each index in the array.
//------------------------------------------------------------------------------------

// Format Date
formatDate (date) {
	if (!date) return null
	const [year, month, day] = date.split('-')
	return `${month}/${day}/${year}`
},
parseDate (date) {
	if (!date) return null
	const [month, day, year] = date.split('/')
	return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
}
//------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------
