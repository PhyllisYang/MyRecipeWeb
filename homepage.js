
/*import wixData from "wix-data"
//let debounceTimer;
console.log($w('#iTitle').value)
export function iTitle_keyPress(event, $w) {
	filter($w('#iTitle').value);
	//if(debounceTimer){
	//	clearTimeout(debounceTimer);
	//	debounceTimer = undefined;
	//}
	
}
//let lastFilterTitle;
function filter(ingredients){
	//if(lastFilterTitle !== ingredients){
	$w('#recipe_database').setFilter(wixData.filter().contains('ingredients',ingredients));
		//lastFilterTitle = ingredients;
	//}
	
	
}

export function button2_click(event, $w) {
	//Add your code for this event here: 
	
}*/

import wixData from 'wix-data';
$w.onReady(function(){
	//TODO: impot wixData from ixi
});

export function SearchButton_click(event, $w) {
	wixData.query('recipe_database').contains('ingredients', $w('#iTitle').value)
	.find()
	.then(res => {
		$w('#table1').rows = res.items;
	});
	
}











