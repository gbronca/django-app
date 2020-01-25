// Code from https://github.com/jessepollak/card

$('#id_expiry_month, #id_expiry_year').on('change', function () {
	// Set the value of a hidden input field for Card
	$('#expiry-date').val($('#id_expiry_month').val() + '/' + $('#id_expiry_year').val());
	// Trigger the "change" event manually
	var evt = document.createEvent('HTMLEvents');
	evt.initEvent('change', false, true);
	document.getElementById('expiry-date').dispatchEvent(evt);
});

var card = new Card({
	// a selector or DOM element for the form where users will
	// be entering their information
	form: 'form', // *required*
	// a selector or DOM element for the container
	// where you want the card to appear
	container: '.card-wrapper', // *required*

	formSelectors: {
		numberInput: 'input#id_credit_card_number', // optional — default input[name="number"]
		expiryInput: 'input#expiry-date',// optional — default input[name="expiry"]
		cvcInput: 'input#id_cvv', // optional — default input[name="cvc"]
		nameInput: 'input#id_name' // optional - defaults input[name="name"]
	},

	width: 250, // optional — default 350px
	formatting: true, // optional - default true

	// Strings for translation - optional
	messages: {
		validDate: 'valid\ndate', // optional - default 'valid\nthru'
		monthYear: 'mm/yyyy', // optional - default 'month/year'
	},

	// Default placeholders for rendered fields - optional
	placeholders: {
		number: '•••• •••• •••• ••••',
		// name: 'Full Name',
		expiry: '••/••••',
		cvc: '•••'
	},

	masks: {
		cardNumber: '•' // optional - mask card number
	},

	// if true, will log helpful messages for setting up Card
	debug: true // optional - default false
});
