# caribbean-recipes
A django app for users to record caribbean recipes
This app celebrates the recipes of the caribbean.  Users can add interesting caribbean recipes.

## Goal
Technology has meant that people can now access recipes online in a variety of apps.  There is also a need for people to record recipes that they enjoy making and eating quickly.  Some people might want to store important recipes that have been passed down in  their families.  I have a mixed heritage background and for a long time have wanted to create a caribbean recipe app to record some of the recipes that my late father who was from the island of Grenada in the Caribbean, used to cook for me and my siblings and my mother.  He was a very good cook and would spend hours perfecting these wonderful recipes.  So the idea for this app was always in my head for many years.  I had created a previous app in flask but this one was intended to be so much better than that.   Users can create their own account and add their recipes, and the option is there to edit or delete them as well.  All users can see all recipes on the home page.  I aim to provide search funtionality for different types of recipes in the future as well.


### The Database Design
The database was designed to allow CRUD functionality to be available to registered users, when signed in. The user model plays a crucial role in handling authentication, provided by Django using the allauth django library.

The entity relationship diagram was created using a spreadsheet environment and shows the schemas for each of the models and how they are related.

![Relational DB](./readme_assets/images/relational_db.png)

### Wireframing

The initial homepage was designed as follows-

![Wireframing](./readme_assets/images/Home_Page.png)

The related Resources had an alternated layout, however, a grid was instead implemented, trying to familiarize with the CSS framework tailwind

![Wireframing](./readme_assets/images/Movies.png)
![Wireframing](./readme_assets/images/news.png)
![Wireframing](./readme_assets/images/Readings.png)

## Tech
In the tech section, we provide information about the technology stack, dependencies, and any technical details related to the project.

### Tech Stack

For the development of Rainbow warriors we made use of the following stack of technologies:

- Front-End
 - HTML3
 - CSS5
 - bootstrap5

- Back-End
 - Python
 - Django
 - Postgres

### Dependencies

- Railway app
- Cloudinary


## Credits
I would like to give credit to the following individuals, organizations, and resources that have contributed to the project or provided inspiration:


### Media
- All images in Caribbean Recipes were sourced and taken from 🌐 [Unsplash.com](https://unsplash.com/) and 🌐 [Pexels.com](https://www.pexels.com/).
- The logo was created ## Goal
Technology and the uprising of AI has provided people with online tools and resources to better navigate our daily lifes and struggles. However, technology is not yet at the point to completely replace the human interaction, but rather empoweres it . Members of the LGBTQ+ community encounter upsetting situations daily and frequently, specific to their cohort and look for help in their peers. The main objective of this project is to demonstrate the use of technology to target and facilitate this interaction. While search engines and other apps using AI can advice on specific subjects, this platform offers a more direct and efficient tool where technology and human feelings will work together to provide the best user experience and results.
This project will not only provide sources of emotional support by directing people to right resources to comfort but will enhence the sense of community within the LGTB+ cohort.


### The Database Design
The database was designed to allow CRUD functionality to be available to registered users, when signed in. The user model plays a crucial role in handling authentication, provided by Django. Enhanced user permissions were designed based on the user.is_staff and user.is_superuser boolean fields. Further information about this model can be found on Django.



The entity relationship diagram was created using a spreadsheet environment and shows the schemas for each of the models and how they are related.

![Relational DB](./readme_assets/images/relational_db.png)

### Wireframing

The initial homepage was designed as follows-

![Wireframing](./readme_assets/images/Home_Page.png)

The related Resources had an alternated layout, however, a grid was instead implemented, trying to familiarize with the CSS framework tailwind

![Wireframing](./readme_assets/images/Movies.png)
![Wireframing](./readme_assets/images/news.png)
![Wireframing](./readme_assets/images/Readings.png)

## Tech
In the tech section, we provide information about the technology stack, dependencies, and any technical details related to the project.

### Tech Stack

For the development of Rainbow warriors we made use of the following stack of technologies:

- Front-End
 - HTML3
 - CSS5
 - Tailwind CSS

- Back-End
 - Python
 - Django
 - Postgres

### Dependencies

- Heroku
- Cloudinary


## Credits
We would like to give credit to the following individuals, organizations, and resources that have contributed to the project or provided inspiration:


### Media
- All images in Rainbow Warriors were sourced and taken from 
- The original logo used as a base for the  logo was sourced from 
- The logo was turned into a Favicon by using 🌐 [Real favicon generator](https://realfavicongenerator.net/)
