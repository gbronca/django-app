// // Create a Stripe client.
// var stripe = Stripe('pk_test_7F4RnUeljkLYXFILdB7xoeyb00uU4KfSwO');

// var submitButton = document.getElementById('card-button');

// submitButton.addEventListener('click', function (ev) {
// 	stripe.confirmCardPayment(clientSecret, {
// 		payment_method: {
// 			card: card,
// 			// billing_details: {
// 			// 	name: 'Jenny Rosen'
// 			// }
// 		}
// 	}).then(function (result) {
// 		if (result.error) {
// 			// Show error to your customer (e.g., insufficient funds)
// 			console.log(result.error.message);
// 		} else {
// 			// The payment has been processed!
// 			if (result.paymentIntent.status === 'succeeded') {
// 				// Show a success message to your customer
// 				// There's a risk of the customer closing the window before callback
// 				// execution. Set up a webhook or plugin to listen for the
// 				// payment_intent.succeeded event that handles any business critical
// 				// post-payment actions.
// 			}
// 		}
// 	});
// });

$(function () {
	$('#payment-form').submit(function () {
		var form = this;
		var card = {
			number: $('#id_credit_card_number').val(),
			expMonth: $('#id_expiry_month').val(),
			expYear: $('#id_expiry_year').val(),
			cvc: $('#id_cvv').val()
		};

		Stripe.createToken(card, function (status, response) {
			if (status === 200) {
				$('#credit-card-errors').hide();
				$('#id_stripe_id').val(response.id);

				//Prevent the Credit card Details from being submitted to our server
				$('#id_credit_card_number').removeAttr('name');
				$('#id_cvv').removeAttr('name');
				$('#id_expiry_month').removeAttr('name');
				$('#id_expiry_year').removeAttr('name');

				form.submit();

			} else {
				$('#stripe-error-message').text(response.error.message);
				$('#credit-card-errors').show();
				$('#validate_card_btn').attr('disabled', false);
			}
		});
		return false;
	});
});