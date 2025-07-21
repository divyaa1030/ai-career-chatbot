function saveDaily() {
    fetch('/save_daily', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            date: document.getElementById('date').value,
            month: document.getElementById('month').value,
            year: document.getElementById('year').value,
            hours: document.getElementById('hours').value,
            learned: document.getElementById('learned').value
        })
    }).then(res => res.json()).then(data => {
        alert('Daily update saved!');
    });
}
