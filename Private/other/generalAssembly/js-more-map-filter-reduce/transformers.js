// console.log('transformers.js is connected!');

// const transformers = [{
//     name: 'Optimus Prime',
//     form: 'Freightliner Truck',
//     form_type: 'vehicle',
//     team: 'Autobot',
//     photo: 'http://tfwiki.net/mediawiki/images2/2/2b/Shadowplay2_no_frikkin_way.jpg',
//   },
//   {
//     name: 'Megatron',
//     form: 'Gun',
//     form_type: 'object',
//     team: 'Decepticon',
//     photo: 'http://tfwiki.net/mediawiki/images2/thumb/9/92/MTMTE50_megatron_class_dismissed.jpg/562px-MTMTE50_megatron_class_dismissed.jpg',
//   },
//   {
//     name: 'Bumblebee',
//     form: 'VW Beetle',
//     form_type: 'vehicle',
//     team: 'Autobot',
//     photo: 'http://tfwiki.net/mediawiki/images2/4/4d/Bumblebee_car_Hawk_Among_the_Sparrows.jpg',
//   },
//   {
//     name: 'Soundwave',
//     form: 'Walkman',
//     form_type: 'object',
//     team: 'Decepticon',
//     photo: 'http://tfwiki.net/mediawiki/images2/8/8d/Soundwaves-allofustogether.jpg',
//   },
//   {
//     name: 'Starscream',
//     form: 'Fighter Jet',
//     form_type: 'vehicle',
//     team: 'Decepticon',
//     photo: 'http://tfwiki.net/mediawiki/images2/3/33/Ongoing13_sad_starscream_is_sad.jpg',
//   },
//   {
//     name: 'Rodimus Prime',
//     form: 'Ford GT',
//     form_type: 'vehicle',
//     team: 'Autobot',
//     photo: 'http://tfwiki.net/mediawiki/images2/thumb/f/f6/SpotlightHotRod-HotRodcvrAexcerpt.jpg/470px-SpotlightHotRod-HotRodcvrAexcerpt.jpg',
//   }
// ];

// /**
//  * PART 1
//  *
//  * 1. Use `map` to return a new array of transformers' names.
//  * 2. Use `filter` to return a new array of only Autobots.
//  * 3. Use `filter` to return a new array of transformers with
//  *    only vehicle forms.
//  * 4. Use `map` to return an array of objects that have a `name`
//  *    and a `photo` property. Then, loop through the new array
//  *    and append an `h1` with the name and an `img` with the photo
//  *    to the DOM in `index.html`. **Do not use jQuery to do this!**
//  *
//  */

// const transformersNames = transformers.map(arr => arr.name);
// console.log(transformersNames);

// const Autobots = transformers.filter(arr => arr.team === 'Autobot');
// console.log(Autobots);

// const VehicleForm = transformers.filter(arr => arr.form_type === 'vehicle');
// console.log(VehicleForm);

// function showNameAndPic() {
//   const body = document.querySelector('body');
//   const names = transformers.map(x => x.name);
//   const photos = transformers.map(x => x.photo);
//   console.table(names);
//   for (let i = 0; i < transformers.length; i++) {
//     const h1 = document.createElement('h1');
//     h1.innerHTML = `${names[i]}`;
//     body.appendChild(h1);
//     const img = document.createElement('img');
//     img.src = `${photos[i]}`;
//     body.appendChild(img);
//   }
// }



/**
 * PART 2: BONUS!!!!!
 * 
 * Reduce the Constructicons to form Devastator!
 * The Devastator object should look like this:
 { 
    name: 'Devastator',
    team: 'Decepticons',
    form: {
      rightLeg: 'Scrapper',
      upperTorso: 'Hook',
      leftArm: 'Bonecrusher',
      rightArm: 'Scavenger',
      leftLeg: 'Mixmaster',
      lowerTorso: 'Long Haul',
     },
    }
  * Remember, when using `reduce`, you can pass in two
  * arguments: the callback and the initial value of the
  * accumulator. How can you leverage this to create the
  * initial structure of the Devastator object?
 */

const constructicons = [{
    name: 'Scrapper',
    form: 'Freightliner Truck',
    team: 'Decepticon',
    bodyPart: 'rightLeg'
  },
  {
    name: 'Hook',
    form: 'Mobile Crane',
    team: 'Decepticon',
    bodyPart: 'upperTorso'
  },
  {
    name: 'Bonecrusher',
    form: 'Bulldozer',
    team: 'Decepticon',
    bodyPart: 'leftArm'
  },
  {
    name: 'Scavenger',
    form: 'Excavator',
    team: 'Decepticon',
    bodyPart: 'rightArm'
  },
  {
    name: 'Mixmaster',
    form: 'Concrete Mixer',
    team: 'Decepticon',
    bodyPart: 'leftLeg'
  },
  {
    name: 'Long Haul',
    form: 'Dump Truck',
    team: 'Decepticon',
    bodyPart: 'lowerTorso'
  }
];


const createDevastator = (arr) => {
  return arr.reduce((acc, val) => {
    acc.name = "Devastator"
    acc.team = val.team;
    acc
    console.log(acc);
    return acc;
  }, {form: {}})
};
createDevastator(constructicons);
