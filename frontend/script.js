// Replace with your actual API URL
fetch('https://ba082eti6d.execute-api.us-east-2.amazonaws.com/prod')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('visitor-count').textContent = data.count;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('visitor-count').textContent = '?';
    });