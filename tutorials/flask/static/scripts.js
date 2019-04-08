function setupChart() {
  const ctx = document.getElementById('myChart').getContext('2d');
  new Chart(ctx, {
    // The type of chart we want to create
    type: 'bar',
    // The data for our dataset
    data: {
      labels: ['5', '4', '3', '2', '1'],
      datasets: [{
        label: '',
        backgroundColor: ['rgba(213, 0, 0, 0.4)', 'rgba(255, 109, 0, 0.4)', 'rgba(255, 214, 0, 0.4)',
          'rgba(174, 234, 0, 0.4)', 'rgba(0, 200, 83, 0.4)'],
        data: getTodosImportance(todos)
      }]
    },
    // Configuration options go here
    options: {
      scales: {
        yAxes: [{
          display: true,
          stacked: true,
          ticks: {
            min: 0, // minimum value
            max: todos.length, // maximum value
            callback: function (value) {
              if (value % 1 === 0) {
                return value;
              }
            }
          }
        }]
      },
      legend: {
        display: false
      },
      tooltips: {
        callbacks: {
          label: function (tooltipItem) {
            return tooltipItem.yLabel;
          }
        }
      }
    }
  });
}

function getTodosImportance(todos) {

  let todosImportances = todos.map(todo => todo.importance)
  const impCounts = new Map([...new Set(todosImportances)].map(
    x => [x, todosImportances.filter(y => y === x).length]
  ));
  return [impCounts.get(5), impCounts.get(4), impCounts.get(3), impCounts.get(2), impCounts.get(1)]

}
