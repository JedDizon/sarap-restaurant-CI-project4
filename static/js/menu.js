function openTab(tabId) {
    const triggerTab = document.getElementById(tabId);
    if (triggerTab) {
        new bootstrap.Tab(triggerTab).show();

        // Scroll to the tab section instead of just the nav
        const tabSection = document.getElementById('menuTabSection');
        if (tabSection) {
            tabSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const hash = window.location.hash;
    if (hash.startsWith('#tab')) {
        const tabButton = document.querySelector(`button${hash}`);
        if (tabButton) {
            new bootstrap.Tab(tabButton).show();

            // Scroll to tabs section
            const tabSection = document.getElementById('menuTabSection');
            if (tabSection) {
                tabSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    }
});