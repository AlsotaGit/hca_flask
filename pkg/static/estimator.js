
const concreteMixes = [
    {'standard concrete mix': [{'cement': 300, 'sand': 600, 'aggregate': 900}]},
    {'high-strength concrete mix': [{'cement': 350, 'sand': 525, 'aggregate': 700}]},
    {'lean concrete mix': [{'cement': 200, 'sand': 600, 'aggregate': 1200}]}
];

const water_cement = [{'standard ration' : 0.5, 'tiling ratio' : 0.45}]  //UNIT IN KG
const waterMix = water_cement[0]

const standard_mix = [{'cement' : 450, 'sand' : 750, 'aggregate' : 1200}]  //UNIT IN KG
const standardMix = standard_mix[0]

const block_types = [{"nine" : 0.10125, "six" : 0.675, "cement" : 0.033}]
const blockType = block_types[0]

const tile_mix = [{"tile gap" : 0.10, "cement per sqm" : 0.7, "sand per sqm" : 0.033, "water" : 0.45}]
const tileMix = tile_mix[0]


let userLength= parseFloat(document.getElementById("uLen").value);
let userWidth= parseFloat(document.getElementById("uWid").value);
let userHeight = parseFloat(document.getElementById("uHei").value);
let userCubic = parseFloat(document.getElementById("uCub").value);
let userSqm = parseFloat(document.getElementById("uSqm").value);
let unit_length = parseFloat(document.getElementById("unit_length").value);
let unit_width = parseFloat(document.getElementById("unit_width").value);


export let concrete = () => {
	if (userLength !== 0 && userWidth !== 0 && userHeight !== 0 && userCubic === 0) {
		let uCubic = userLength * userWidth * userHeight;
		uCubic = $('#uCub').onkeyup.innerText(uCubic);
		let kg_cement = standardMix.cement * uCubic;
		let kg_sand = standardMix.sand * uCubic;
		let kg_agg = standardMix.aggregate * uCubic;
		let num_cm_bag = kg_cement/50;
		let mun_sd_bag = kg_sand/50;
		let num_ag_bag = kg_agg/50;

		return "Cement: " + num_cm_bag.toFixed(2) + " bags\n" + "Sand: " + mun_sd_bag.toFixed(2) +
			" bags\n" + "Aggregate: " + num_ag_bag.toFixed(2) + " bags"

	}
	else if (userCubic !== 0 && userLength === 0 || userWidth === 0 || userHeight === 0) {
		let kg_cement = standardMix.cement * userCubic;
		let kg_sand = standardMix.sand * userCubic;
		let kg_agg = standardMix.aggregate * userCubic;
		let num_cm_bag = kg_cement/50;
		let mun_sd_bag = kg_sand/50;
		let num_ag_bag = kg_agg/50;
	}
	else {
		return "Input appropriate fields"
	}
}

let block = () =>  {
	if (userLength !== 0 && userWidth !== 0 && userSqm === 0) {
		let uSqm = userLength * userWidth;
		uSqm = $('#uSqm').onkeyup.innerText(uSqm);
		let num_of_block = uSqm / blockType.nine
		let num_cm_bag = num_of_block * blockType.cement
		let kg_cm_blk = num_cm_bag * 50
	}
}


let tiling = () => {
	if (userLength !== 0 && userWidth !== 0 && userSqm === 0) {
		if (unit_length !== 0 && userWidth !== 0) {
			let uSqm = userLength * userWidth;
			uSqm = $('#uSqm').onkeyup.innerText(uSqm);
			let unitSqm = unit_width * unit_length;
			let num_tiles = uSqm / unitSqm;
		}
	}
}