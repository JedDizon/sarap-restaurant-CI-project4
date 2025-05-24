function sendMail(contactForm) {
    emailjs.send("service_c8ydk5f_sarap","template_jjsojjq", {
        "name": contactForm.name.value,
        "subject": contactForm.subject.value,
        "message": contactForm.message.value,
        "email": contactForm.email.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            alert("Your message has been sent successfully!");
            contactForm.reset();
        },
        function(error) {
            console.log("FAILED", error);
            alert("Failed to send the message. Please try again later.");
        }
    );
    
    return false;
}