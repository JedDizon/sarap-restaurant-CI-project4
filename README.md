# Sarap Talaga! RestoBar

![Image of site on different devices](/docs/features/sarap_mockup.png)

**Developer: Jehdil Dizon**

💻 [Visit live website](https://sarap-restobar-project4-ci-1e69f1c375a6.herokuapp.com/ )  
(Ctrl + click to open in new tab)



## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Device Testing & Browser compatibility](#device-testing--browser-compatibility)
  - [Bugs](#bugs)
  - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

### About

Welcome to Sarap Talaga! RestoBar — a fictional Filipino restaurant.

Guests can easily log in to book a seat online or contact us directly if they prefer us to arrange a booking for them. Visitors can also explore what Sarap Talaga! is all about, view our lunch, dinner, and drinks menus, and find us easily using the interactive map on the site. 

<hr>

### User Goals

- Book a table (choose how many people, date, time)
- Can view, update, delete booking
- View menus, blog, contact restaurant via contact form

### Site Owner Goals

- Allow users to book a table
- Get people to come to the restaurant
- Provide a website that is responsive, accessible, and intuitive to use

## User Experience

### Target Audience

- People who want to reserve a table for a couple, family, or friends
- Repeat customers 
- New customers (people new and visiting the area, locals, anyone looking to sample Filipino food)

### User Requirements and Expectations

- Intuitive & easy to use/navigate
- accessible
- welcoming and sleek themed design
- contact information & form
- location, opening hours

##### Back to [top](#table-of-contents)<hr>


## User Stories

### Users

1. As a site user I can open a menu so that I know what to order.

2. As a user I can go to the nav bar so that I can easily go to any section I want.

3. As a user I can go to about us section so that I can decide if i want to order here.

4. As a user I can go to the footer so that I can see any other useful info.


5. As a user I can book-a-table so that I can decide when I can go to the restaurant.


6. As a user I can contact the restaurant directly so that I can get my questions answered.


7. As a user I can open the site on different devices so that I can use whatever device is most convenient to me.


8. As a user I can login if I have an account so that I can make a booking.


9. As a user I can register for an account so that I can make a booking.


10. As a user I can know if I am logged in so that I know if I can order or if I need to register / login first.


11. As a user I can register so that I can make a booking.


12. As a user I can not book past dates so that my booking is valid.


13. As a user I can make changes so that i can update my booking.


14. As a user I can read my booking so that check the details on when it's booked, what time, and for how many seats.


15. As a user I can create a booking so that I can book seats for when i come.


16. As a user I can send a message on the contact form so that get the site admin to make the changes or if I have any questions.


17. As a user I can get more information about the restaurant so that i can make an informed decision.


18. As a user I can clearly see which bookings are relevant to me so that I don't get mixed up.


### Admin / Authorised User

1. As a site admin I can update the menu so that I can sell new items / remove dishes that aren't selling well / if there is a deal.

2. As a site admin I can filter for bookings so that i can make edits to specific bookings if needed.

3. As a site admin I can add bookings manually if someone calls so that the customer can come and dine.

4. As an admin / a user with authorization I can enter the site in admin mode so that make edits, approve bookings, etc.

5. As a site admin I can use the search bar so that I can search for specific bookings if I know the name.

6. As a Site admin I can accept / reject so that double bookings are avoided.


### Site Owner / Developer
1. As a Site developer I can create wireframes so that I have an idea what I want the finished site to look like.

2. As a site owner I can decide what type of restaurant so that I can decide on the themes & look of the page.

3. As a site developer I can create a base.html file so that creating new pages will be easily done using template inheritance.

4. As a site developer I can deploy the project so that I can determine if there are any issues early on.

5. As a site developer I can view READMe so that I can see the development of the site, verify testing, etc.

6. As a site developer I can create home page so that users get directed here when clicking on the restaurant link.

7. As a site developer I can create a logo so that there is a symbol that users can see to link back to the restaurant.

8. As a site developer I can view the relevant and code so that see how it is done.


### Kanban & Epics 
- User stories were tracked on Github Kanban feature 
- Epics were created using the milestones feature [Visit milestones](https://github.com/JedDizon/sarap-restaurant-project4/milestones)

<details><summary>Epics</summary>

![Epics](/docs/userstories/epics_overall.png)
![Epic 1](/docs/userstories/epic1.png)
![Epic 2](/docs/userstories/epic2.png)
![Epic 3](/docs/userstories/epic3.png)
![Epic 4](/docs/userstories/epic4.png)
![Epic 5](/docs/userstories/epic5.png)
</details>

<details><summary>Kanban</summary>

![Kanban mid](/docs/userstories/userstories_kanban_board2.png)
![Kanban end](/docs/userstories/userstories_kanban_board.png)

</details>


##### Back to [top](#table-of-contents)<hr>


## Design

### Colours

The color palette was carefully selected to reflect the essence of Filipino hospitality, heritage, and cuisine. The primary colors — Banana Leaf Green (#5B8C5A), Adobo Brown (#4E3629), and Coconut Husk (#A47149) — evoke a natural, grounded feeling reminiscent of tropical landscapes, traditional materials, and home-cooked meals. 

To complement this earthy foundation, vibrant accent colors like Mango Yellow (#FFB84C) and Chili Red (#C44536) were added to inject energy and highlight the vibrancy of Filipino culture. Taro Purple (#9D7CBF) offers a subtle nod to beloved local ingredients like ube, while Rice White (#FAF7F0) ensures a clean, welcoming canvas that enhances readability and warmth. Together, these colors create a palette that is rich, inviting, and deeply tied to Filipino identity.

### Structure

#### Website pages

The website was designed with user familiarity in mind, featuring a navigation bar at the top of each page and a hamburger menu for easy access on smaller screens.

The footer includes links to all relevant social media platforms, allowing users to easily follow the business online, helping to grow its digital presence. It also provides quick access to key pages such as About Us, Book a Table, Menus, Contact Information (phone, email, address), and Opening Hours.

- The site consists of the following pages:
 - Home
    - Links to Menu & Book a Table
    - Links to Menus
    - Link to About Us
 - Book Table
   - Link to Menu
   - Links to register / login to allow user to book
   - Book a Table functionality for registered users allowing them to book the number of seats, time, and date needed. Users can only book within opening hour times & cannot book past dates.
   - Logged in users can view current bookings & can update and cancel the booking details as needed.
 - Menu
    - Link to Book a Table
    - Display of Menus & all available food & drinks
 - About
    - Links to Menu & Book a Table
    - Blog about the restaurant, type of food, etc.
 - Location
    - Links to Menu & Book a Table
    - Address and interactive map showing how to find the restaurant
 - Contact Us
    - Links to Menu & Book a Table
    - Form for the user to fill out to send a direct message to the restaurant if they want admins to create/update/cancel a booking for them or if they have general questions
 -  Signup
    - Form for the user to register an account
 -  Login
    - Form for the user to login 
 - Logout
    - Form for the user to logout


#### Database

- Built with Python, Django & Postgres & deployed on Heroku.
- Diagrams.net was used to create the ERDs. 
- See below database models:

<details><summary>Show ERD</summary>

![Model ERDs](docs/features/sarap_erds.png)

</details>


##### About Model
The About model contains the following:
- title
- updated_on
- content


##### Post Model
The Post Model contains the following:
- title
- slug
- author
- content
- created_on
- status
- excerpt
- updated_on
- is_active
- Meta: ordering


##### Comment Model
The Comment Model contains the following:
- post (ForeignKey)
- author
- body
- approved
- created_on
- Meta: ordering


##### Book Model
The Book model contains the following:
- title
- updated_on
- content


##### Reservation Model
The Reservation model contains the following:
- user
- guest_name
- guest_phone
- created_date
- requested_date
- requested_time
- seats
- status
- updated_on


##### Contact Model
The Contact model contains the following:
- title
- updated_on
- content


##### Location Model
The About model contains the following:
- title
- updated_on
- content


##### Menu Model
The Menu model contains the following:
- title
- updated_on
- content

##### MenuItem Model
The Menu model contains the following:
- name
- description
- cost
- category
- is_active
- menu (ForeignKey)



### Wireframes

Wireframes created using Balsamiq

<details><summary>Home</summary>

![Home Desktop](/docs/wireframes/wireframe_home_desktop.png)
![Home Tablet](/docs/wireframes/wireframe_home_tablet.png)
![Home Phone](/docs/wireframes/wireframe_home_phone.png)

</details>

<details><summary>Booking</summary>

![Booking Desktop](/docs/wireframes/wireframe_book_desktop.png)

</details>

<details><summary>Menus</summary>

![Menus Desktop](/docs/wireframes/wireframe_menus_desktop.png)

</details>

<details><summary>About Us</summary>

![About us Desktop](/docs/wireframes/wireframe_about_desktop.png)

</details>

<details><summary>Location</summary>

![Location Desktop](/docs/wireframes/wireframe_location_desktop.png)

</details>

<details><summary>Contact Us</summary>

![Contact us Desktop](/docs/wireframes/wireframe_contact_desktop.png)

</details>

<details><summary>Register/Login/Logout</summary>

![Register/Login/Logout Desktop](/docs/wireframes/wireframe_reg_login_out_desktop.png)

</details>


## Technologies Used

### Languages & Frameworks

- CSS
- Django
- HTML
- Javascript
- Python



### Libraries & Tools

- [Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap v5.2](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Favicon.io](https://favicon.io)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [Postgres](https://www.postgresql.org/)
- [Start Bootstrap](https://startbootstrap.com)
- [Summernote](https://summernote.org/)
- [jQuery](https://jquery.com)
- [BrowserStack](https://www.browserstack.com/)
- [Diagrams.net](https://app.diagrams.net/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [CI Python Linter (PEP8)](https://pep8ci.herokuapp.com/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)



##### Back to [top](#table-of-contents)


## Features

### Logo & Nav Bar
- Custom logo
- Navbar links to other pages
- Navbar is responsive by switching to a burger-style menu 
- displayed on all pages
- if user is logged in, a message is displayed above the nav bar to let users know if their login status.

<details><summary>See feature images</summary>

![Nav and logo](docs/features/sarap_nav_and_logo.png)
![User login status](docs/features/sarap_user_loggedin.png)

</details>


### Footer
- Contains contact details (phone, email, address), quick links to about us, book table, menu pages, opening hours, links to social links
- displayed across all pages

<details><summary>See feature images</summary>

![Footer](docs/features/sarap_footer.png)

</details>

### Reminder links
- Below the nav bar on most pages have reminder links to bring users to the menu & book a table pages
- also exists above the footer on most pages

<details><summary>See feature images</summary>

![Remidner links section 1](docs/features/sarap_reminderlinks.png)
![Remidner links section 2](docs/features/sarap_reminderlinks2.png)

</details>

### Signup
- Users can input details to create an account

<details><summary>See feature images</summary>

![Signup page](docs/features/sarap_signup.png)

</details>

### Login
- Users can login to allow them to create, read, update, or delete their bookings.

<details><summary>See feature images</summary>

![Login page](docs/features/sarap_login.png)

</details>


### Logout
- Lets users logout
- Users must confirm if they want to logout

<details><summary>See feature images</summary>

![Logout page](docs/features/sarap_logout.png)

</details>


### Book
- Book form allows users to book a table by specifying a requested date, time, seats, guest name, phone.
- site prompts users if input is not accepted i.e. time outside opening hours. 
- Booking form does not show us if user is not authenticated. Instead, a message is shown with links to register an account or login. 

<details><summary>See feature images</summary>

![Booking form](docs/features/sarap_booking_form.png)
![Check if user is signed in](docs/features/sarap_register_login_prompt.png)

</details>


### Your Reservations
- When logged in, users can view their current reservations below the booking form.
- States the choices users picked when booking, and status of the booking.
- users can edit & cancel their booking.
- declined bookings auto delete after 5 days, & approved bookings auto delete 5 days after the requested date. 
- bookings are ordered by updated date.


<details><summary>See feature images</summary>

![Your reservations section](docs/features/sarap_reservations.png)

</details>



### Menus
- Menus are split into an accordion style selection box.
- Users can choose between the Main, Desserts, Drinks menus.
- Menu items can be created, updated, deleted through the admin panel by the staff or someone with access.
  
<details><summary>See feature images</summary>

![Menu section](docs/features/sarap_menus.png)

</details>


### About us
- Read more link on the home page redirects users to the about-us page.
- On about about-us page, 3 small blogs can be read by the user to find out more about the story of the restaurant & what is filipino food.
- there is a small image gallery above the footer to showcase Filipino culture.

  
<details><summary>See feature images</summary>

![Link to About us page](docs/features/sarap_link_to_about.png)
![About us page](docs/features/sarap_about_blogs.png)

</details>


### Location
- shows the address & interactive map showing where the restaurant can be found.
- shows an updating opening hours table is below the map to allow users to make clearer decisions on when the restaurant is open

<details><summary>See feature images</summary>

![Interactive map](docs/features/sarap_interactive_map.png)

</details>

### Contact Us
- Users can input their details (name, email, phone, message) to contact restaurant admins.
- Submitting a message sends a message to the user’s input email address telling them that the restaurant will get back to the users when they can.
  
<details><summary>See feature images</summary>

![Contact Us form](docs/features/sarap_contact_form.png)

</details>


##### Back to [top](#table-of-contents)<hr>


## Validation

### Nu HTML Checker

<details><summary>Home</summary>
<img src="docs/validation/sarap_vldtn_home.png" alt="Nu HTML Checker - Home">
</details>

<details><summary>Table Booking</summary>
<img src="docs/validation/sarap_vldtn_book.png" alt="Nu HTML Checker - Home">
</details>

<details><summary>Menus</summary>
<img src="docs/validation/sarap_vldtn_menu.png" alt="Nu HTML Checker - menus">
</details>

<details><summary>About Us</summary>
<img src="docs/validation/sarap_vldtn_about.png" alt="Nu HTML Checker - about us">
</details>

<details><summary>Location</summary>
<img src="docs/validation/sarap_vldtn_location.png" alt="Nu HTML Checker - location">
</details>

<details><summary>Contact Us</summary>
<img src="docs/validation/sarap_vldtn_contact.png" alt="Nu HTML Checker - contact us">
</details>

<details><summary>Register</summary>
<img src="docs/validation/sarap_vldtn_signup.png" alt="Nu HTML Checker - register">
</details>

<details><summary>Login</summary>
<img src="docs/validation/sarap_vldtn_login.png" alt="Nu HTML Checker - login">
</details>

<details><summary>Logout</summary>
<img src="docs/validation/sarap_vldtn_logout.png" alt="Nu HTML Checker - logout">
</details>


### CSS Validation

Only 1 error found. No concern. CSS from startbootstrap.

<details><summary>Style.css</summary>
<img src="docs/validation/sarap_vldtn_css.png" alt="W3C CSS Validation - CSS">
</details><hr>


### JavaScript Validation

Tested using JSHint.
Contact: OK. "emailjs" & "sendMail" variables being used.
Location: OK. "marker" used.
Menu: OK. "openTab" used.

<details><summary>booking.js</summary>
<img src="docs/validation/sarap_js_booking.png" alt="jshint of booking js">
</details>

<details><summary>contact.js</summary>
<img src="docs/validation/sarap_js_contact.png" alt="jshint of contact js">
</details>

<details><summary>location.js</summary>
<img src="docs/validation/sarap_js_location.png" alt="jshint of location js">
</details>

<details><summary>menu.js</summary>
<img src="docs/validation/sarap_js_menu.png" alt="jshint of menu js">
</details>

<details><summary>script.js</summary>
<img src="docs/validation/sarap_js_script.png" alt="jshint of script js">
</details>


### PEP8 Validation

CI Python Linter was used to test code for PEP8 compliance. 

<hr><summary>About</summary><hr>

<details><summary>Admin.py</summary>
<img src="docs/pep8/pep8_about_admin.png">
</details>

<details><summary>models.py</summary>
<img src="docs/pep8/pep8_about_models.png">
</details>

<details><summary>urls.py</summary>
<img src="docs/pep8/pep8_about_urls.png">
</details>

<details><summary>views.py</summary>
<img src="docs/pep8/pep8_about_views.png">
</details>

<hr><summary>Blog</summary><hr>

<details><summary>Admin.py</summary>
<img src="docs/pep8/pep8_blog_admin.png">
</details>

<details><summary>models.py</summary>
<img src="docs/pep8/pep8_blog_models.png">
</details>

<details><summary>urls.py</summary>
<img src="docs/pep8/pep8_blog_urls.png">
</details>

<details><summary>views.py</summary>
<img src="docs/pep8/pep8_blog_views.png">
</details>

<details><summary>tests.py</summary>
<img src="docs/testing/test_blog_pep8.png">
</details>

<hr><summary>Book</summary><hr>

<details><summary>Admin.py</summary>
<img src="docs/pep8/pep8_book_admin.png">
</details>

<details><summary>models.py</summary>
<img src="docs/pep8/pep8_book_models.png">
</details>

<details><summary>urls.py</summary>
<img src="docs/pep8/pep8_book_urls.png">
</details>

<details><summary>views.py</summary>
<img src="docs/pep8/pep8_book_views.png">
</details>

<details><summary>forms.py</summary>
<img src="docs/pep8/pep8_book_forms.png">
</details>

<details><summary>tests.py</summary>
<img src="docs/testing/test_book_pep8.png">
</details>

<hr><summary>Contact</summary><hr>

<details><summary>Admin.py</summary>
<img src="docs/pep8/pep8_contact_admin.png">
</details>

<details><summary>models.py</summary>
<img src="docs/pep8/pep8_contact_models.png">
</details>

<details><summary>urls.py</summary>
<img src="docs/pep8/pep8_book_urls.png">
</details>

<details><summary>views.py</summary>
<img src="docs/pep8/pep8_contact_views.png">
</details>

<hr><summary>Location</summary><hr>

<details><summary>Admin.py</summary>
<img src="docs/pep8/pep8_location_admin.png">
</details>

<details><summary>models.py</summary>
<img src="docs/pep8/pep8_location_models.png">
</details>

<details><summary>urls.py</summary>
<img src="docs/pep8/pep8_location_urls.png">
</details>

<details><summary>views.py</summary>
<img src="docs/pep8/pep8_location_views.png">
</details>

<hr><summary>Menu</summary><hr>

<details><summary>Admin.py</summary>
<img src="docs/pep8/pep8_menu_admin.png">
</details>

<details><summary>models.py</summary>
<img src="docs/pep8/pep8_menu_models.png">
</details>

<details><summary>urls.py</summary>
<img src="docs/pep8/pep8_menu_urls.png">
</details>

<details><summary>views.py</summary>
<img src="docs/pep8/pep8_menu_views.png">
</details>

<details><summary>tests.py</summary>
<img src="docs/testing/test_menu_pep8.png">
</details>

### Lighthouse

Lighthouse used to test performance, accessibility, best practices, and SEO. Main issue is low score for location page on phone. Likely due to the map. 

#### Desktop

<details><summary>Home</summary>
<img src="docs/validation/lh_home_desktop.png">
</details>

<details><summary>Book</summary>
<img src="docs/validation/lh_book_desktop.png">
</details>

<details><summary>Menu</summary>
<img src="docs/validation/lh_menu_desktop.png">
</details>

<details><summary>About</summary>
<img src="docs/validation/lh_about_desktop.png">
</details>

<details><summary>Location</summary>
<img src="docs/validation/lh_location_desktop.png">
</details>

<details><summary>Contact</summary>
<img src="docs/validation/lh_contact_desktop.png">
</details>

<details><summary>Register</summary>
<img src="docs/validation/lh_register_desktop.png">
</details>

<details><summary>Login</summary>
<img src="docs/validation/lh_login_desktop.png">
</details>

<details><summary>Logout</summary>
<img src="docs/validation/lh_logout_desktop.png">
</details>

#### Mobile

<details><summary>Home</summary>
<img src="docs/validation/lh_home_phone.png">
</details>

<details><summary>Book</summary>
<img src="docs/validation/lh_book_phone.png">
</details>

<details><summary>Menu</summary>
<img src="docs/validation/lh_menu_phone.png">
</details>

<details><summary>About</summary>
<img src="docs/validation/lh_about_phone.png">
</details>

<details><summary>Location</summary>
<img src="docs/validation/lh_location_phone.png">
</details>

<details><summary>Contact</summary>
<img src="docs/validation/lh_contact_phone.png">
</details>

<details><summary>Register</summary>
<img src="docs/validation/lh_register_phone.png">
</details>

<details><summary>Login</summary>
<img src="docs/validation/lh_login_phone.png">
</details>

<details><summary>Logout</summary>
<img src="docs/validation/lh_logout_phone.png">
</details>

### Wave

Wave was used to test website accessability.
Only page of note was the Contact Us page with contrast errors. 
Deemed ok via Color Contrast Checker ([Coolors](https://coolors.co/contrast-checker/faf7f0-4e3629)). 

<details><summary>Home</summary>
<img src="docs/validation/wave_home_summary.png">
<img src="docs/validation/wave_home_details.png">
</details>

<details><summary>Book</summary>
<img src="docs/validation/wave_booking_summary.png">
<img src="docs/validation/wave_booking_details.png">
</details>

<details><summary>Menus</summary>
<img src="docs/validation/wave_menus_summary.png">
<img src="docs/validation/wave_menus_details.png">
</details>

<details><summary>About</summary>
<img src="docs/validation/wave_about_summary.png">
<img src="docs/validation/wave_about_details.png">
</details>

<details><summary>Location</summary>
<img src="docs/validation/wave_location_summary.png">
<img src="docs/validation/wave_location_details.png">
</details>

<details><summary>Contact</summary>
<img src="docs/validation/wave_contact_summary.png">
<img src="docs/validation/wave_contact_details.png">
</details>

<details><summary>Register</summary>
<img src="docs/validation/wave_register_summary.png">
<img src="docs/validation/wave_register_details.png">
</details>

<details><summary>Login</summary>
<img src="docs/validation/wave_login_summary.png">
<img src="docs/validation/wave_login_details.png">
</details>

##### Back to [top](#table-of-contents)<hr>


## Testing

### Manual testing

1. Home page
    - As a user I can open the site on different devices so that I can use whatever device is most convenient to me.

    - As a site developer I can create home page so that users get directed here when clicking on the restaurant link.

    - As a site developer I can create a logo so that there is a symbol that users can see to link back to the restaurant.


| TEST                   | ACTION                                | EXPECTATION                              | RESULT    |
|------------------------|---------------------------------------|------------------------------------------|-----------|
| **Homepage loads**   | User opens site link | Site loads | **Success** |
| **Site on different browsers  & devices**   | User opens site link on a tablet, phone, other browser | Site loads and opens | **Success** |
| **Site logo**   | User clicks on logo | Brings user to home page | **Success** |
| **Menu link in hero works**   | User clicks on menu link | Brings user to menu page | **Success** |
| **Book link in hero works**   | User clicks on booklink | Brings user to booking page | **Success** |
| **Menus links bring user to correct menu section**   | User clicks on a menu link (Main/Dessert/Drinks) | Brings user to correct menu section on menu page | **Success** |
| **Shortcut link to about us page works**   | User clicks on about us link to find out more | Brings user to about us page | **Success** |
| **Menu link in reminder section works**   | User clicks on menu link | Brings user to menu page | **Success** |
| **Book link in reminder section works**   | User clicks on booklink | Brings user to booking page | **Success** |

<details><summary></summary>

<img src="docs/testing/website_testing_firefox.png">
<img src="docs/testing/website_testing_ipad9th.png">
<img src="docs/testing/website_testing_samsungs22.png">
<img src="docs/testing/website_testing_samsungs22.png">
<img src="docs/testing/test_logo.png">

</details>

2. Nav bar

    - As a user I can go to the nav bar so that I can easily go to any section I want.

    - As a user I can know if I am logged in so that I know if I can order or if I need to register / login first.

| TEST                   | ACTION                                | EXPECTATION                              | RESULT    |
|------------------------|---------------------------------------|------------------------------------------|-----------|
| **Home link in nav bar**   | User clicks on Home link | Brings user to Home page | **Success** |
| **Logo link**   | User clicks on Logo link | Brings user to Home page | **Success** |
| **Table booking link in nav bar**   | User clicks on Table booking link | Brings user to Table booking page | **Success** |
| **Menus link in nav bar**   | User clicks on Menus link | Brings user to Menus page | **Success** |
| **About us link in nav bar**   | User clicks on About us link | Brings user to About us page | **Success** |
| **Location link in nav bar**   | User clicks on Location link | Brings user to Location page | **Success** |
| **Contact Us link in nav bar**   | User clicks on Contact Us link | Brings user to Contact Us page | **Success** |
| **Register link in nav bar**   | User clicks on Register link | Brings user to Register page | **Success** |
| **Login link in nav bar**   | User clicks on Login link | Brings user to Login page | **Success** |
| **Logout link in nav bar**   | User clicks on Login link | Brings user to Login page | **Success** |
| **Login status**   | User logs in | Message on nav bar displays user login status | **Success** |

<details><summary></summary>

<img src="docs/features/sarap_nav_and_logo.png">
<img src="docs/features/sarap_user_loggedin.png">

</details>

3. Footer

    - As a user I can go to the footer so that I can see any other useful info.

| TEST                   | ACTION                                | EXPECTATION                              | RESULT    |
|------------------------|---------------------------------------|------------------------------------------|-----------|
| **About us link in footer**   | User clicks on About us link | Brings user to About us page | **Success** |
| **Book table link in footer**   | User clicks on Book table link | Brings user to Book table page | **Success** |
| **Menus link in footer**   | User clicks on Menus link | Brings user to Menus page | **Success** |
| **Facebook link in footer**   | User clicks on Facebook logo in Socials section of footer | Facebook link opens in a new tab | **Success** |
| **X link in footer**   | User clicks on X logo in Socials section of footer | X link opens in a new tab | **Success** |
| **Instagram link in footer**   | User clicks on Instagram logo in Socials section of footer | Instagram link opens in a new tab | **Success** |
| **TikTok link in footer**   | User clicks on TikTok logo in Socials section of footer | TikTok link opens in a new tab | **Success** |

<details><summary></summary>

<img src="docs/features/sarap_footer.png">

</details>

4. Table Booking

    - As a user I can book-a-table so that I can decide when I can go to the restaurant.

    - As a user I can not book past dates so that my booking is valid.

    - As a user I can make changes so that i can update my booking.

    - As a user I can read my booking so that check the details on when it's booked, what time, and for how many seats.

    - As a user I can create a booking so that I can book seats for when i come.

    - As a user I can clearly see which bookings are relevant to me so that I don't get mixed up.

    - As a user I can register for an account so that I can make a booking.



| TEST                   | ACTION                                | EXPECTATION                              | RESULT    |
|------------------------|---------------------------------------|------------------------------------------|-----------|
| **Prompt shows if user is not logged in**   | User tries to book without being logged in | Prompt is in place of booking form asking user to login or register | **Success** |
| **Link to register**   | User clicks on register link in prompt | Brings user to register page | **Success** |
| **Link to login**   | User clicks on login link in prompt | Brings user to login page | **Success** |
| **Booking form shows if user is logged in**   | User goes to booking form while logged in | Booking form is visible | **Success** |
| **Old dates can’t be chosen**   | User tries to book a past date | User cannot click on past dates | **Success** |
| **Times outside booking hours can’t be chosen**   | User tries to book a time outside opening hours  | Message prompts user to choose a valid time & they can’t submit | **Success** |
| **User must add how many seats to book**   | User must add how many people the booking is for | User cannot submit if seats not specified | **Success** |
| **User can view their bookings**   | User views their bookings| User can view their bookings | **Success** |
| **User can update their bookings**   | User clicks on Edit to update their bookings| User can Edit their bookings | **Success** |
| **Edit form works same as initial booking form**   | User updates their booking  | Edit booking form have same validation (No old dates, must choose within opening hours, must choose seats) | **Success** |
| **Cancel booking confirmation**   | User clicks on Delete booking  | Confirmation pops up for user to confirm first | **Success** |
| **User can delete booking**   | User deleted booking  | Booking is deleted | **Success** |
| **Approved Booking clean up**   | Approved booking exists 5 days after requested date  | Booking is auto removed from reservations list | **Success** |
| **Declined Booking clean up**   | Declined booking exists 5 days after being declined  | Booking is auto removed from reservations list | **Success** |

<details><summary></summary>

<img src="docs/testing/test_book_correct_dates.png">
<img src="docs/testing/test_book_within_hours.png">
<img src="docs/testing/test_book_update_delete.png">
<img src="docs/testing/test_user_must_be_loggedin.png">

</details>

5. Menus

    - As a site user I can open a menu so that I know what to order.

| TEST                   | ACTION                                | EXPECTATION                              | RESULT    |
|------------------------|---------------------------------------|------------------------------------------|-----------|
| **Menus links bring user to correct menu section**   | User clicks on a menu link (Main/Dessert/Drinks) | Brings user to correct menu section on menu page | **Success** |
| **User can manually choose a menu in menu section**   | User clicks on a menu header | Relevant menu opens | **Success** |

<details><summary></summary>

<img src="docs/features/sarap_menus.png">

</details>

6. About Us

    - As a user I can go to about us section so that I can decide if i want to order here.


| TEST                   | ACTION                                | EXPECTATION                              | RESULT    |
|------------------------|---------------------------------------|------------------------------------------|-----------|
| **Blogs Load**   | User goes to About us page to find out more about the restaurant | User can read blogs | **Success** |
| **Image gallery**   | User goes to gallery section | User can view the images | **Success** |

<details><summary></summary>

<img src="docs/features/sarap_about_blogs.png">

</details>

7. Location

    - As a user I can get more information about the restaurant so that i can make an informed decision.

| TEST                   | ACTION                                | EXPECTATION                              | RESULT    |
|------------------------|---------------------------------------|------------------------------------------|-----------|
| **Google maps restaurant location**   | User moves the map | User can interact with the map | **Success** |
| **Map functionality on phone**   | User moves the map on mobile | User can interact with the map | **Success** |
| **Opening hours update**   | User can check when is opening hours on the day | Opening hours table update to showcase opening hours of a specific day | **Success** |

<details><summary></summary>

<img src="docs/testing/test_restaurant_details.png">

</details>

8. Contact Us

    - As a user I can contact the restaurant directly so that I can get my questions answered.

    - As a user I can send a message on the contact form so that get the site admin to make the changes or if I have any questions.


| TEST                   | ACTION                                | EXPECTATION                              | RESULT    |
|------------------------|---------------------------------------|------------------------------------------|-----------|
| **Contact form**   | User sends a direct message to restaurant admins to ask questions | User sends a direct message to restaurant email | **Success** |
| **User submits an incomplete empty form**   | User attempts to send an empty/incomplete form form | Fails. Form does not submit | **Success** |
| **User phone number**   | User submits a form that has a phone number with letters or really long | Form does not submit | **Success** |
| **Email confimation**   | User submits a complete form | Input email gets sent a notification email of the recieved message | **Success** |

<details><summary></summary>

<img src="docs/testing/test_send_contact_form.png">

</details>

9. Register / Login / Logout

    - As a user I can login if I have an account so that I can make a booking.

    - As a user I can register so that I can make a booking.

| TEST                   | ACTION                                | EXPECTATION                              | RESULT    |
|------------------------|---------------------------------------|------------------------------------------|-----------|
| **Register**   | User clicks on register link | User is brought to a registration form | **Success** |
| **Registration form validation**   | User fills out form  | User must fill out the form with a username and password  | **Success** |
| **Unique username**   | User fills out form with a used username  | Registration fails with a message to select a unique username  | **Success** |
| **User login**   | User enters username and password  | User logs in | **Success** |
| **Logout confirmation**   | User clicks on logout link in navbar | User is brought to a confirmation page if they want to logout | **Success** |
| **Logout function**   | User confirms that they want to logout | User is logged out | **Success** |

<details><summary></summary>

<img src="docs/testing/test_register.png">
<img src="docs/features/sarap_login.png">

</details>

10. Admin

    - As a site admin I can update the menu so that I can sell new items / remove dishes that aren't selling well / if there is a deal.

    - As a site admin I can filter for bookings so that i can make edits to specific bookings if needed.

    - As a site admin I can add bookings manually if someone calls so that the customer can come and dine.

    - As an admin / a user with authorization I can enter the site in admin mode so that make edits, approve bookings, etc.

    - As a site admin I can use the search bar so that I can search for specific bookings if I know the name.

    - As a Site admin I can accept / reject so that double bookings are avoided.


| TEST                   | ACTION                                | EXPECTATION                              | RESULT    |
|------------------------|---------------------------------------|------------------------------------------|-----------|
| **Create blog**   | Admin can creates a blog | Blog is created | **Success** |
| **Update blog**   | Admin can update a blog | Blog is updated | **Success** |
| **Read blog**   | Admin can Read a blog | Blog is read| **Success** |
| **Active blog**   | Admin makes a blog inactive | Blog does not show on about us page| **Success** |
| **Delete blog**   | Admin can Delete a blog | Blog is Deleted| **Success** |
| **Create menu item**   | Admin can create a menu item | Menu item is created | **Success** |
| **Read menu item**   | Admin can Read a menu item | Menu item is Read| **Success** |
| **Update menu item**   | Admin can Update a menu item (name, price, description) | Menu item is updated| **Success** |
| **Delete menu item**   | Admin can Delete a menu item | Menu item is Deleted| **Success** |
| **Menu Item activation**   | Admin selects a menu item to be active | Menu item shows on menus| **Success** |
| **Booking approval**   | Admin approves booking | Booking is approved | **Success** |
| **Booking decline**   | Admin declines booking | Booking is declined| **Success** |
| **Manual booking creation**   | Admin creates booking manually for customer | Booking is created| **Success** |
| **Manual booking update**   | Admin updates booking manually for customer | Booking is updated| **Success** |


<details><summary>Overall Admin Page 1</summary>
<img src="docs/features/sarap_admin_overall1.png">
</details>

<details><summary>Overall Admin Page 2</summary>
<img src="docs/features/sarap_admin_overall2.png">
</details>

<details><summary>Blogs</summary>
<img src="docs/features/sarap_about_blogs.png">
</details>

<details><summary>Blog Creation</summary>
<img src="docs/features/sarap_about_blogs_posts.png">
</details>

<details><summary>Menu Items</summary>
<img src="docs/features/sarap_admin_menu_items.png">
</details>

<details><summary>Menu Creation</summary>
<img src="docs/features/sarap_admin_menu_items_manual.png">
</details>

<details><summary>Reservations</summary>
<img src="docs/features/sarap_admin_reservations.png">
</details>

<details><summary>Manual Reservations</summary>
<img src="docs/features/sarap_admin_reservations_manual.png">
</details>

### Automated testing

#### Blog

- As a user I can go to about us section so that I can decide if i want to order here.

**Test** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Inactive posts | Inactive posts not in the list | **Success** |
| Draft post | Not showing | **Success** |

<details><summary></summary>
<img src="docs/testing/test_blog.png">
</details>

#### Book

- As a site admin I can add bookings manually if someone calls so that the customer can come and dine.

- As an admin / a user with authorization I can enter the site in admin mode so that make edits, approve bookings, etc.

**Test** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Create reservation | Reservation is created | **Success** |
| Delete reservation | Reservation is deleted | **Success** |
| Edit reservation | Reservation can be edited | **Success** |

<details><summary></summary>
<img src="docs/testing/test_book.png">
</details>

#### Menu

- As a site admin I can update the menu so that I can sell new items / remove dishes that aren't selling well / if there is a deal.

**Test** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Menu item categories | Menu items correctly categorized | **Success** |

<details><summary></summary>
<img src="docs/testing/test_menu.png">
</details>

### Device Testing & Browser compatibility

Browserstack was used to emulate different sites and devices. Sarap Talaga app was developed using Chrome and Edge browsers.

<details><summary>Edge (v136)</summary>
<img src="/docs/testing/website_testing_edge.png">
</details>

<details><summary>Firefox (v138)</summary>
<img src="/docs/testing/website_testing_firefox.png">
</details>

<details><summary>Opera (v119)</summary>
<img src="/docs/testing/website_testing_opera.png">
</details>

<details><summary>Safari (v18.4)</summary>
<img src="/docs/testing/website_testing_safari.png">
</details>

<details><summary>iPad 9th</summary>
<img src="/docs/testing/website_testing_ipad9th.png">
</details>

<details><summary>iPhone 13</summary>
<img src="/docs/testing/website_testing_iphone13.png">
</details>

<details><summary>Pixel 7</summary>
<img src="/docs/testing/website_testing_pixel7.png">
</details>

<details><summary>Samsung S22</summary>
<img src="/docs/testing/website_testing_samsungs22.png">
</details>

##### Back to [top](#table-of-contents)<hr>


## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
| CSS not loading properly | Bootstrap CSS not properly connected via Jinja template |
| Footer items not stacking on smaller screen sizes | col-3 class doesn't wrap properly on smaller screens, switched to col-12 |
| Logo & title not spacing correctly | Incorrect use of bootstrap cols |
| Can't reload the page after making an update or deletion or create a form | Use redirect after processing POST to prevent form resubmission |
| Message “Update successful” keeps showing | Changed to use alert message instead |
| Could not load blogs on about app | Did not update jinja template load view name |
| User can submit an empty contact form| Added validation to contact js to check and enforce users filling the form fully out before it can be sent |
| User can input non numbers for phone number section on contact form | Added validation ot contact js to not accept phone numbers that include letters and limited the phone length with min and max |
| User can't submit contact form if initial submission was incorrect| Added js to clear previous validation message when user starts typing |
| New blogs override current blogs| Added toggle for admins to choose which blogs are active |
| Deployment loading timeout error preventing site from opening properly after deploying on Heroku | Added timeout to procfile & added database to vars |


##### Back to [top](#table-of-contents)<hr>


### Heroku Deployment

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)

This application has been deployed from Github using Heroku. Steps to deploy were folowed from CI "I think therefore I blog" module:

1. Create an account at heroku.com

<details>
<img src="docs/deployment/heroku_signup.png">
</details>

2. On the Heroku dashboard, create an app, give it a name, and select a region

<details>
<img src="docs/deployment/heroku_newapp.png">
<img src="docs/deployment/heroku_createapp.png">
</details>

3. In the app settings, set Config Var <strong>DISABLE_COLLECSTATIC</strong> with a value of <strong>1</strong>

<details>
<img src="docs/deployment/heroku_config_vars.png">
</details>

4. Use <strong>pip3</strong> to install "gunicorn~=20.1" and freeze it to the <strong>requirements.txt</strong> file.

5. Create a new file called "Procfile" in the <strong>root directory</strong>

<details>
<img src="docs/deployment/heroku_procfile.png">
</details>

6. In the <strong>Procfile</strong>, add a command using <strong>gunicorn</strong> and <strong>codestar wsgi</strong> file to start the webserver

<details>
<img src="docs/deployment/heroku_procfile_gunicorn.png">
</details>

7.In the PROJECTAPPNAME/settings.py file, set the DEBUG constant to False and append the '.herokuapp.com' hostname to the ALLOWED_HOSTS list.

<details>
<img src="docs/deployment/heroku_debug.png">
</details>

8. On the new app on Heroku, go to the <strong>Deploy</strong> tab & connect it to the GitHub repository

<details>
<img src="docs/deployment/heroku_githubconnect.png">
</details>

9. Manually deploy the main branch of this GitHub repo.

<details>
<img src="docs/deployment/heroku_deploy.png">
</details>

10. In your new app’s resources tab, ensure you are using an eco dyno and delete any Postgres database Add-on

<details>
<img src="docs/deployment/heroku_eco_dynos.png">
</details>

### Fork Repository
Follow the below steps to fork the repository:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner
<hr>

### Clone Repository
Follow the below steps to clone the repository:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7.Press Enter to create your local clone.

##### Back to [top](#table-of-contents)<hr>


## Credits

### Images

Images used were sourced from Pexels.com, Wikimedia Commons and AI image generator (pyxl.pro) was used for logo & favicon with the permission from OpenAI.

### Code

StartBootstrap template “Business Casual used for the site: (https://startbootstrap.com/theme/business-casual)

Google maps API for locations:
(https://www.youtube.com/watch?v=6Tl3ROOgvgw) 

CI projects:
- Resume
  - Using emailjs API
- Flask Dwarves
  - Using StartBootstrap 
- Blog App
  - Creating a django app
  - Using fixtures
  - Creating a blog with comments
  - Authentication
  - How to deploy to Heroku

##### Back to [top](#table-of-contents)<hr>

## Acknowledgements

### Special thanks to the following:
- Code Institute
- Mo Shami (Mentor)

