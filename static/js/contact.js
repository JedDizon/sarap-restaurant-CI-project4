function sendMail(contactForm) {
    // Check if any areas in the form are empty
    for (let i = 0; i < contactForm.elements.length; i++) {
        const field = contactForm.elements[i];
        if (field.hasAttribute('required') && !field.value.trim()) {
            alert(`Please fill out the required field: ${field.name}`);
            field.focus();
            return false;
        }
    }

    // Check the overall form validity
    if (!contactForm.checkValidity()) {
        return false;
    }

    // Proceed with EmailJS submission if form is valid
    emailjs.send("service_c8ydk5f_sarap", "template_jjsojjq", {
        "name": contactForm.name.value,
        "subject": contactForm.subject.value,
        "message": contactForm.message.value,
        "email": contactForm.email.value
    })
        .then(
            function (response) {
                console.log("SUCCESS", response);
                alert("Your message has been sent successfully!");
                contactForm.reset();
            },
            function (error) {
                console.log("FAILED", error);
                alert("Failed to send the message. Please try again later.");
            }
        );

    return false;
}

document.getElementById('contactForm').addEventListener('submit', function (event) {
    var phoneField = document.getElementById('phone');
    if (!phoneField.validity.valid) {
        event.preventDefault();

        if (phoneField.validity.valueMissing) {
            phoneField.setCustomValidity('Please enter your phone number.');
        } else if (phoneField.validity.patternMismatch) {
            phoneField.setCustomValidity('Please enter only numbers (no letters or special characters).');
        } else if (phoneField.validity.tooLong) {
            phoneField.setCustomValidity('Phone number cannot be longer than 15 digits.');
        }

        phoneField.reportValidity();
    }
});

// clear previous validation message when user starts typing
document.getElementById('phone').addEventListener('input', function() {
    var phoneField = document.getElementById('phone');
    phoneField.setCustomValidity(''); 
});