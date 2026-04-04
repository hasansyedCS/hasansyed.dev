// ========== VISITOR COUNTER ==========
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

// ========== STARS EFFECT ==========
function createStars() {
    const container = document.querySelector('.stars-container');
    if (!container) return;
    
    const starCount = 150;
    
    for (let i = 0; i < starCount; i++) {
        const star = document.createElement('div');
        star.classList.add('star');
        
        star.style.left = Math.random() * 100 + '%';
        star.style.top = Math.random() * 100 + '%';
        
        const size = Math.random() * 4 + 1;
        star.style.width = size + 'px';
        star.style.height = size + 'px';
        
        star.style.opacity = Math.random() * 0.7 + 0.3;
        
        container.appendChild(star);
    }
}

createStars();