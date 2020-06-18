
# rmstyls

#### Description

A python program for removing unused jsx style codes from your project

## How to run?

`$ python main.py`

### Dependencies

`Python 2.7.16`

## Example
```javascript

For Android:

unusedStyle: { 
	flex: 1, 
},
container: {
	flex: 1,
	paddingHorizontal: 10,
	backgroundColor: colors.page_bg_color,
},
emptyText: {
	textAlign: 'center',
	marginTop: 20,
},
unusedStyle2: {

},
lottieStyle: {
	alignSelf: 'center',
	width: 70,
	height: 70,
},
unusedStyle3: {
	flex: 1,
	paddingHorizontal: 10,
	backgroundColor: colors.page_bg_color,
},

// After Running main.py styles.js should like this

container: {
	flex: 1,
	paddingHorizontal: 10,
	backgroundColor: colors.page_bg_color,
},
emptyText: {
	textAlign: 'center',
	marginTop: 20,
},
lottieStyle: {
	alignSelf: 'center',
	width: 70,
	height: 70,
},

```

  