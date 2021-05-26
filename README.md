# django-custom-users

There are two ways to extend users in Django: the "profile" method and a custom user. We've already used the profile method for our first project, so now we'll cover the custom user.

This project is simply about implementing a custom user from the ground up so that you can use it in the next assignment.

#### **Your Task**

Extend your custom user field so that it has the following _nullable_ field:

* Displayname (Charfield)

Implement your own 

* Signup page
* Login page (do NOT use Django's built-in login view)
* Homepage that is only accessible when logged in

The homepage should show:

*   the username of the person who is logged in
*   the displayname of the person who is logged in
*   the output the value of `settings.AUTH_USER_MODEL`

NOTE: DO NOT name any part of your app "user" -- it will have conflict with the built-in user model and give you all sorts of errors that are really difficult to debug if you don't know what you're looking for. Use "custom_user", "myuser", "dudewheresmyuser"... literally anything but "user" will work.

**Extra Credit (2 points)**

Extend your custom user field so that it has the following _nullable_ fields:

*   Homepage (URLField)
*   Age (IntegerField)

**Extra Credit (1 point)**

(this is the hard part) Make the custom fields appear on the admin panel and available for editing.

**Extra Credit (1 point)**

1 additional bonus point if you make the superuser command ask for their age.

#### **Submission**
 - Push to the **main** branch
 - Submit the link to your repo
<pre>https://github.com/kenzie-se-q4/django-custom-users-&ltgithub_username&gt</pre>
