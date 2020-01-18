let bugsctx = document.getElementById('bugsChart').getContext('2d');
let featuresctx = document.getElementById('featuresChart').getContext('2d');

let bugsChart = new Chart(bugsctx, {
	type: 'pie',
	data: {
		labels: ['Pending', 'In Progress', 'Completed'],
		datasets: [{
			label: '# of bugs',
			data: bugs,
			backgroundColor: [
				'rgba(220, 53, 69, 0.6)',
				'rgba(255, 193, 7, 0.6)',
				'rgba(40, 167, 69, 0.6)'
			],
			borderColor: [
				'rgba(220, 53, 69, 1)',
				'rgba(255, 193, 7, 1)',
				'rgba(40, 167, 69, 1)'
			],
			borderWidth: 1
		}]
	},
	options: {
		// title: {
		// 	display: true,
		// 	text: 'Bugs'
		// },
		responsive: true,
		maintainAspectRatio: true
	}
});

let featuresChart = new Chart(featuresctx, {
	type: 'pie',
	data: {
		labels: ['Pending', 'In Progress', 'Completed'],
		datasets: [{
			label: '# of features',
			data: features,
			backgroundColor: [
				'rgba(220, 53, 69, 0.6)',
				'rgba(255, 193, 7, 0.6)',
				'rgba(40, 167, 69, 0.6)'
			],
			borderColor: [
				'rgba(220, 53, 69, 1)',
				'rgba(255, 193, 7, 1)',
				'rgba(40, 167, 69, 1)'
			],
			borderWidth: 1
		}]
	},
	options: {
		// title: {
		// 	display: true,
		// 	text: 'Features'
		// },
		responsive: true,
		maintainAspectRatio: true
	}
});