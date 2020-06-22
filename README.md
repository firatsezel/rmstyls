
# rmstyls

#### Description

A python&Bash Script program for removing unused jsx style codes from your project

## How to run?

`$ chmod +x rmstyls.sh`
`$ ./rmstyls.sh`

### Dependencies

`Python 2.7.16 or higher`

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

// After Running rmstyls.sh styles.js should like this

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

  