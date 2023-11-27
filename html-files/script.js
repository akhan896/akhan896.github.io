function searchJobs() {
    // Get values from the form
    var jobTitle = document.getElementById('job-title').value;
    var location = document.getElementById('location').value;

    // In a real-world scenario, you would send these values to a server for processing and retrieval of job results.
    // For simplicity, we'll just simulate some results here.

    var jobResults = [
        { title: 'Software Developer', company: 'Tech Co.', location: 'City A' },
        { title: 'Web Designer', company: 'Design Studio', location: 'City B' },
        { title: 'Marketing Specialist', company: 'Marketing Inc.', location: 'City C' },
    ];

    displayResults(jobResults);
}

function displayResults(results) {
    var resultsList = document.getElementById('job-results');
    resultsList.innerHTML = ''; // Clear previous results

    results.forEach(function (job) {
        var li = document.createElement('li');
        li.innerHTML = <strong>${job.title}</strong> - ${job.company}, ${job.location};
        resultsList.appendChild(li);
    });
}