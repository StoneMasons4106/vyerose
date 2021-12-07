# VyeRose

This project is meant to provide an online store for the small local business, VyeRose.

VyeRose is a small singularly owned jewelry business based in Tonawanda, NY. This project gives VyeRose an online platform to advertise their products, and for customers to purchase them, create accounts, edit delivery information, and provide quick contact with the business owner.

[Feel free to view the live project here](https://vyerose.herokuapp.com)!

## UX

This site is designed to give the user a visually pleasing way to browse products for the VyeRose online store.

For inspiration, I looked at a number of [Bootstrap Templates](https://bootstrapmade.com/) to get a beautiful front end design. In the end, I settled on using the [MeFamily](https://bootstrapmade.com/demo/MeFamily/).

#### User Stories:

* First Time Visitor Goals:
    * Easily understand the purpose of the site.
    * Quickly learn how to navigate the site and make sure it is intuitively accessible for first time users.
    * Visually appealing to have a pleasant first experience.
    * Be able to quickly browse products to quickly determine interest.
    * Be able to contact the owner of the store if I have any questions.

* Returning Visitor Goals:
    * Be able to login/register so information can be saved, and chekout is expedient.
    * Be able to login with my Google account so creating an account is painless.
    * Have items that I my have in my cart still be there when I return.

* Frequent User Goals:
    * Be able to save my delivery information so that I don't have to re-enter every time I order.
    * See my order history to see what I have already bought.
    * Have the option to custom order if I want to change something to a particular product.

#### Design Features Include:

* **Mobile Menu** - Consolidating the menu down for mobile devices lets it be flexible for device size.

* **Flexible Footer** - Custom JS was written to measure the window and content and intelligently place the footer either fixed at the bottom, or at the bottom of the content.

* **Breadcrumbs** - Breadcrumb headers are included on each page for a beautiful and uniform appearance.

* **Google Maps Embed** - Google Maps embed link was used on the Contact page and is changeable so the shop owner can show where they are located and update as needed.

* **Homepage Carousel** - Attractive images of jewelry cycle through on the home page for a pleasing experience.

* **Color Scheme** - Primary colors used derived from the Bootstrap template are white, 2 shades of blue, and pastels from the logo to complement.

### Wireframes

* **Desktop** - [View](vyerose_desktop.pdf)

* **Tablet** - [View](vyerose_tablet.pdf)

* **Mobile** - [View](vyerose_mobile.pdf)

## Features

* **User Registration** - Allows user to store their delivery information, their default email, name, phone number, and view their order history.

* **Google Sheets Integration** - When an order is created, the order information from the Order Model gets pushed to a Google Sheet for the owner of the store to keep track of.

* **Google SSO** - Allauth supports signing in and creating an account through your own Google account.

* **Contact Page** - Allows end users to send emails and questions to the store owner for easy correspondence.

* **Cart Model** - Allows users that are registered with the site to have their cart data stored for easy access if they leave the site and log back in.

* **Responsiveness** - Site responds to all device sizes and looks natural on Desktop, Mobile, and Tablet views.

* **Customizable Store** - Flexible product design allows the owner to add products, edit products, and delete them as their store changes.

* **Checkout** - Integration with Stripe allows people to shop and buy products, complete with confirmation emails for both the consumer, and the store owner.

## Technologies Used

**Languages Used**

* HTML5
* CSS3
* JavaScript
* Python
* Jinja

**Frameworks, Libraries & Programs Used**

1. [Bootstrap 4.5.0](https://getbootstrap.com/)
    * Bootstrap was used to assist with the responsiveness and styling of the website.

2. [Font Awesome](https://fontawesome.com/)
    * Font Awesome was used on most pages throughout the website to add icons for aesthetic purposes.

3. [Git](https://git-scm.com/)
    * Git was used for version control by utilizing VS Code to commit to Git and Push to GitHub.

4. [GitHub](https://github.com/)
    * GitHub is used to store the project's code after being pushed from Git.

5. [Balsamiq](https://balsamiq.com/)
    * Balsamiq was used to create the wireframes during the design process.

6. [JQuery](https://jquery.com/)
    * JQuery was used to write shorter, simpler Javascript.

7. [Hover.css](https://ianlunn.github.io/Hover/)
    * Hover.css is used to change the text and background color of buttons and links upon hovering over them.

8. [Django](https://www.djangoproject.com/)
    * Django is the Python framework that this project was built on.

9. [Allauth](https://django-allauth.readthedocs.io/en/latest/)
    * Allauth is used for the authentication models, and SSO for this project.

10. [Django-GSheets](https://github.com/olliebreeden/django-gsheets/tree/patch-1)
    * A forked branch of django-gsheets was used for Google Sheet integration which coerces all data in a model to a string so it can be passed to the sheet.

11. [Postgres SQL](https://www.postgresql.org/)
    * Django uses a relational database system by default, and Heroku has a free Postgres extension to add on to any app.

## Testing

I used the W3C Markup Validator, W3C CSS Validator Services, and JSHint to validate every page of the project, and all JS code to ensure there were no major syntax errors in the project.

[W3C Markup Validator](https://validator.w3.org/)
[W3C CSS Validator](http://jigsaw.w3.org/css-validator/)
[JSHint](https://jshint.com/)

### Testing User Stories from UX Section

* First Time Visitor Goals:
    * Easily understand the purpose of the site.
        * Result: The home page, sections at the top of the page, and the about section make it easy for the user to understand the premise of the site.
    * Quickly learn how to navigate the site and make sure it is intuitively accessible for first time users.
        * Result: Intuitive design of the header with dropdowns make it very easy for users to peruse the entire site with ease.
    * Visually appealing to have a pleasant first experience.
        * Result: Bootstrap template styling with uniform colors and carousel images make it pleasing to the eye.
    * Be able to quickly browse products to quickly determine interest.
        * Result: The products section is easily available, users can scroll through, and filter queries to find what they'd like. 
    * Be able to contact the owner of the store if I have any questions.
        * Result: The contact page is fully operational with an email form and the owner's business line.

* Returning Visitor Goals:
    * Be able to login/register so information can be saved, and chekout is expedient.
        * Result: Users can login and edit their information so that information can be pulled at checkout.
    * Be able to login with my Google account so creating an account is painless.
        * Result: Google SSO is enabled through django-allauth.
    * Have items that I my have in my cart still be there when I return.
        * Result: Cart model is created such that if a user is logged in while shopping, it saves in the database so they can return later. If not logged in, it defaults to storing in the session data.

* Frequent User Goals:
    * Be able to save my delivery information so that I don't have to re-enter every time I order.
        * Result: Delivery information can be saved at checkout or in their profile so checkout is expedient.
    * See my order history to see what I have already bought.
        * Result: Order history is visible on the profile page, users can click into them to see what they've bought.
    * Have the option to custom order if I want to change something to a particular product.
        * Result: Custom notes are built into the order page if the user wants to customize any part of their order.

### Further Testing

* The site was tested on a variety of devices from desktop to mobile to tablet. Other devices were simulated through Chrome dev tools.
    * Custom JS was written to ensure proper positioning of the footer for all devices and window sizes.

* Lighthouse was used to test the pages of this site.
    * The weak point is mobile performance, which hovers between 55 and 59. However desktop performance sits above 80.
    * Every other category consistently tests above 70, and best practices and SEO rank 85 or higher in any platform or page.

* Browsers used to test include Chrome, Edge, Safari, Opera, and Firefox.
    * A slight change to my CSS had to be made due to Firefox not supporting the zoom attribute.
        * Transform was used in its place, and tested.

* Home Page:
    * The home page's design was taken from the MeFamily home page, and altered for this site.
    * The site's logo is changed to VyeRose's, and the headers are intuitive so as to facilitate ease of user navigation.
    * The carousel's images are pulled from the AWS S3 bucket. Replacing the pictures is as easy as getting rid of one picture, and naming the new file the same as the old.
    * The home page text is actually done through a basic model which is just labeled Home Text Fields.
        * This allows the owner to change the text without changing base code.
        * If left blank, the view returns an empty string, avoiding an error and breaking the site if nothing is found.

* Contact Page:
    * The contact page's design was taken from the MeFamily contact page, and altered for this site.
    * The contact model allows the owner of the site to be able to edit the Google embed, the street address, contact email, and phone number.
        * This allows the owner of the site to change the content without editing base code.
    * The contact email process was tested and verified, it uses EmailMessage, from the django.core.mail module to send emails.

* Product Page(s):
    * The product page templates, basic layout, and logic were mainly repurposed from the Boutique Ado sample project, with some minor changes.
        * Sizing due to the type of products being sold on this site was irrelevant, so it was removed from all models and templates.
    * Reading through Django's documentation, I build a basic template tag that would return all Categories of Products to each page.
        * This allows for dynamic product menus and quick filtering for specific types of products.
    * Adding a product, editing products, and deleting products have all been tested and verified working.
    * Minor style change to make sure a line doesn't show up at the bottom of the page if a Category only has 4 items.

* Profile Page(s):


* Cart:


* Checkout:


* Authentication Page(s):

### Known Bugs

* Upon changing the email address in the profile, a confirmation email is sent. If the user attempts to change the email again, an error message is returned saying the user needs to confirm the prior email first.
    * On the profile page when this happens, the email address is the one the user just entered, not the one that needs verified.
    * Upon reloading the page, this corrects itself with the proper data.
    
## Deployment

### Heroku

This project was deployed to Heroku using the steps below:

1. Log into GitHub and locate the [GitHub Repository](https://github.com/StoneMasons4106/vyerose).
2. Log into Heroku and create a new Python app.
3. Under deploy, find Deployment method, and select Github.
4. Select the appropriate repository as shown in step one, and select deploy from master.
5. Enable automatic deploys so when a change is pushed to Github, Heroku automatically adopts the new changes.

### Forking the Repository

You can fork the repository and create a copy for yourself in your own account.

1. Log into GitHub and locate the [GitHub Repository](https://github.com/StoneMasons4106/vyerose).
2. Locate the Fork button, next to the repository settings button.
3. Go to your repositories, and you should see a copy made for you to edit as you please.

### Local Clone

If you'd like to have a copy on your local machine, follow the steps below:

1. Log into GitHub and locate the [GitHub Repository](https://github.com/StoneMasons4106/vyerose).
2. Under the name of the repository, click 'Clone or Download'.
3. Click 'Clone with HTTPS', and copy the link.
4. Open Git Bash on your local computer.
5. Change the directory to where you want the clone located.
6. Type ```git clone``` and paste the URL from step 3.
7. Hit enter. A local clone was now created in the directory you specified.

## Credits

#### Media

* Much of the media was provided by [Pixabay](https://pixabay.com/).

* Favicons were generated using [this Generator](https://www.favicon-generator.org/).

#### Content

* All content was written by the developer.

#### Code

* Some of the Python and HTML templating was taken from the Boutique Ado Project because the premise of an online store is the same.

* Code for sending an email manually in Django was taken from this [Stack Overflow post](https://stackoverflow.com/questions/6367014/how-to-send-email-via-django).

* Documentation for implementing signing in with Google was provided by the [Django Allauth docs](https://django-allauth.readthedocs.io/en/latest/providers.html#google).

* HTML and CSS for Google sign in button found in this [Codepen post](https://codepen.io/jimjammc/pen/PMOVZB).

#### Acknowledgments

* My mentor for continuous and helpful support/design suggestions.