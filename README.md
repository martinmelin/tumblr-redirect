Redirecting a Tumblr custom domain to a new URL
===============================================

If you have a [Tumblr](http://tumblr.com) blog on a custom domain and want to
migrate the content and inbound links somewhere else, this small script is
for you.

You'll need a [Heroku](http://heroku.com/) account to set up the app, and all
of your Tumblr posts hosted somewhere else with the same slugs as on Tumblr.

Quickstart
----------

1. Clone this repository:

       ```
   git clone git@github.com:martinmelin/tumblr-redirect.git
       ```

1. Create a new Heroku app from this repository:

       ```
   cd tumblr-redirect
   heroku create
       ```

       If you get an error when running the second command, you need to make sure
       you have the Heroku toolbelt set up correctly on your machine.

1. Configure the URL you want to redirect to:

       ```
   heroku config set TUMBLR_REDIRECT_BASE_URL=http://example.com/blog/
       ```

1. Push the app to Heroku:

       ```
   git push heroku master
       ```

1. Add your Tumblr custom domain as a [domain in Heroku](https://devcenter.heroku.com/articles/custom-domains):

       ```
    heroku domains:add blog.example.com
       ```


1. Visit your Heroku app and make sure it is redirecting to the correct place

       All paths in this format:
       /post/123456/**slug**

       will redirect to your TUMBLR_REDIRECT_BASE_URL with only the **slug** appended.

       All other paths are redirected to the TUMBLR_REDIRECT_BASE_URL itself.

       An easy way to check that redirection works correctly is to get a path
       to one of your blog posts on Tumblr, like /post/123456/slug, then:

       ```
   curl -I -H 'Host: blog.example.com' http://your.herokuapp.com/post/123456/slug
       ```

       and make sure you get a 302 FOUND response with the Location header
       leading to the right place on your new blog.

1. When the redirection is working correctly, set the app to do permanent
   redirects:

       ```
   heroku config set TUMBLR_REDIRECT_CODE=301
       ```

1. Point your Tumblr custom domain away from Tumblr and to the new Heroku app
   by updating the CNAME record to point to your.herokuapp.com instead of
   domains.tumblr.com

1. You're done! When the DNS change has propagated, any requests to your old 
   Tumblr custom domain blog will now be redirected to your
   TUMBLR_REDIRECT_BASE_URL, without it costing you anything as long as you run
   the Heroku app with the single free dyno they provide.
