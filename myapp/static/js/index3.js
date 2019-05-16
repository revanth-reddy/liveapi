var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: [],
        datasets: [{
            label: 'Live Status 3',
            backgroundColor: 'skyblue',
            borderColor: 'rgb(255, 99, 132)',
            data: []
        }]
    },

    // Configuration options go here
    options: {
        responsive: true,
    }
});


function addData(chart, label, data) {
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    chart.update();
    setTimeout(updateData, 1000);
}

updateData();

async function updateData() {
	let response = await fetch('https://canvasjs.com/services/data/datapoints.php?xstart=1&ystart=10&type=json');
    let data = await response.json();
    let speed = data[0][1];

    let response2 = await fetch('https://cors.io/?http://api.holfuy.com/live/?s=759&pw=h1u5l4kka&m=JSON&tu=C&su=m/s');
    let data2 = await response2.json();
    let time = data2.dateTime.split(" ")[1];
    addData(chart,time,speed);
}

// fetch("https://cors.io/?http://api.holfuy.com/live/?s=759&pw=h1u5l4kka&m=JSON&tu=C&su=m/s")
// .then((resp) => resp.json()) // Transform the data into json
//   .then(function(data) {
//     console.log(data.wind.speed)
//     })

// let response = await fetch('https://cors.io/?http://api.holfuy.com/live/?s=759&pw=h1u5l4kka&m=JSON&tu=C&su=m/s');
// let data = await response.json();