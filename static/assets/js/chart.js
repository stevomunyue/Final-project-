// script.js

document.addEventListener("DOMContentLoaded", () => {
    const moodSelect = document.getElementById("mood");
    const addMoodButton = document.getElementById("addMood");
    const moodLog = document.getElementById("moodLog");
    const moodChartCanvas = document.getElementById("moodChart");

    const moodData = {};

    // Function to add a mood
    const addMood = () => {
        const selectedMood = moodSelect.value;
        const timestamp = new Date().toLocaleString();
        
        // Add mood to the log
        const moodEntry = document.createElement("li");
        moodEntry.textContent = `${timestamp}: ${selectedMood}`;
        moodLog.appendChild(moodEntry);
        
        // Update mood count
        moodData[selectedMood] = (moodData[selectedMood] || 0) + 1;
        updateChart();
    };

    // Event listener for the add mood button
    addMoodButton.addEventListener("click", addMood);

    // Chart.js for visualization
    let moodChart = new Chart(moodChartCanvas, {
        type: "doughnut",
        data: {
            labels: [],
            datasets: [{
                data: [],
                backgroundColor: [
                    "#ffcd56", "#ff6384", "#36a2eb", "#cc65fe", "#ff9f40", "#4bc0c0"
                ],
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "bottom",
                }
            }
        }
    });

    // Update the chart with the latest mood data
    const updateChart = () => {
        moodChart.data.labels = Object.keys(moodData);
        moodChart.data.datasets[0].data = Object.values(moodData);
        moodChart.update();
    };
});
