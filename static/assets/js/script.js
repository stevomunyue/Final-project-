// JavaScript to dynamically update announcements (optional)
document.addEventListener('DOMContentLoaded', () => {
    const announcements = document.querySelector('#announcements ul');

    const newAnnouncement = document.createElement('li');
    newAnnouncement.textContent = '🌟 Workshop: Mindfulness Practices - January 15, 2025';
    
    announcements.appendChild(newAnnouncement);
});
document.querySelectorAll('.dropdown-toggle').forEach((dropdown) => {
    dropdown.addEventListener('click', function (e) {
        e.preventDefault();
        const content = this.nextElementSibling;

        // Close other open dropdowns
        document.querySelectorAll('.dropdown-content').forEach((menu) => {
            if (menu !== content) {
                menu.style.display = 'none';
            }
        });

        // Toggle current dropdown
        content.style.display = content.style.display === 'block' ? 'none' : 'block';
    });
});

// Close dropdowns when clicking outside
document.addEventListener('click', function (e) {
    if (!e.target.closest('.dropdown')) {
        document.querySelectorAll('.dropdown-content').forEach((menu) => {
            menu.style.display = 'none';
        });
    }
});
// Function to handle tab switching
function openTab(event, tabId) {
    // Hide all tab contents
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });

    // Deactivate all tab links
    document.querySelectorAll('.tab-link').forEach(tab => {
        tab.classList.remove('active');
    });

    // Show the selected tab content
    document.getElementById(tabId).classList.add('active');

    // Activate the selected tab link
    event.currentTarget.classList.add('active');
}
// Form validation and submission
document.querySelector('.booking-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const date = document.getElementById('date').value;
    const sessionType = document.getElementById('session-type').value;
    const notes = document.getElementById('notes').value;

    if (!name || !email || !phone || !date || !sessionType) {
        alert('Please fill in all required fields.');
        return;
    }

    alert(`Appointment Confirmed!\n\nName: ${name}\nEmail: ${email}\nPhone: ${phone}\nDate: ${date}\nSession Type: ${sessionType}\nNotes: ${notes || 'None'}`);
});

/// Script for toggling login dialog
document.addEventListener('DOMContentLoaded', () => {
    const dialog = document.querySelector('.dialog-background');
    const openButton = document.querySelector('.open-login');
    const closeButton = document.querySelector('.close-login');

    openButton.addEventListener('click', () => dialog.style.display = 'flex');
    closeButton.addEventListener('click', () => dialog.style.display = 'none');
});
document.querySelector('.booking-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const successMessage = document.getElementById('success-message');
    successMessage.style.display = 'block';
    this.reset(); // Reset the form
});
