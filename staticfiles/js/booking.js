document.addEventListener("DOMContentLoaded", function () {
        const dateInput = document.querySelector('input[name="requested_date"]');
        const timeInput = document.querySelector('input[name="requested_time"]');
        const warning = document.getElementById("time-warning");

        function validateTime() {
            const dateValue = dateInput.value;
            const timeValue = timeInput.value;

            if (!dateValue || !timeValue) {
                warning.style.display = "none";
                return;
            }

            const selectedDate = new Date(dateValue);
            const day = selectedDate.getDay(); // 0 = Sunday
            let minTime, maxTime;

            if ([1, 2, 3, 4].includes(day)) {
                // Mon–Thu
                minTime = "12:00";
                maxTime = "19:30";
            } else {
                // Fri–Sun
                minTime = "14:00";
                maxTime = "21:30";
            }

            timeInput.min = minTime;
            timeInput.max = maxTime;

            if (timeValue < minTime || timeValue > maxTime) {
                warning.style.display = "block";
            } else {
                warning.style.display = "none";
            }
        }

        const today = new Date().toISOString().split('T')[0];
        if (dateInput) {
            dateInput.min = today;
            dateInput.addEventListener("change", validateTime);
        }
        if (timeInput) {
            timeInput.addEventListener("change", validateTime);
        }

        // Cancel Edit Button
        document.querySelectorAll(".cancel-edit-btn").forEach(button => {
            button.addEventListener("click", function () {
                const id = this.getAttribute("data-reservation-id");
                const form = document.getElementById(`edit-form-${id}`);
                if (form) form.remove(); 
            });
        });
    });