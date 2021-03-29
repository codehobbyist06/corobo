Setting Up Corobo
=================

The following documentation illustrates the process to install Corobo and interface it with the gitter API.

Installation
------------

*  To install corobo, first you need to setup a virtual environment(it is not mandatory but highly recommended). This can be done as follows:
   ::
     pip3 install virtualenv
     virtualenv venv -p python
     cd venv
     source bin/activate ---->  For Linux
     \Scripts\activate   ---->  For Windows
*  Next, you can clone the corobo package via git and install the requirements(dependent packages).
   ::
     git clone https://github.com/coala/corobo.git
     pip install -r requirements.txt

Configuration of Environment variables(In text mode)
--------------------------------------------------

*  The following environment variables are required to setup corobo in text mode:
   ::
     export BOT_PREFIX="any_name"
     export BACKEND="Text"
     export BOT_USERNAME="@any_other_name"
   (**Note:** The BOT_USERNAME always starts with a @ for a person and # for a room)

Testing Corobo
---------------------------

*  To run the bot use:
   ::
     errbot
*  You can test the bot using the following commands:
   ::
     bot_prefix help    ----> Lists the set of commands available with the bot
     bot_prefix history ----> Lists the command history
     
     
Setting up Corobo with gitter backend
=====================================

#. Clone the err-backend-gitter repository in your "corobo" folder.
   ::
     git clone https://github.com/errbotio/err-backend-gitter.git
     
#. Configure the environment variables(for gitter-backend).
   ::
     export BACKEND="Gitter"
     export BOT_EXTRA_BACKEND_DIR="/path_to/err-backend-gitter"
#. To make the bot interact with the gitter API you will need a github account(this account can be used to login to gitter) to generate the gitter access token.
   **Remember it is recommended to use a separate account(other than the admin account) for the bot.** 
   Once the account is setup, run the following script.
   ::
     ./oauth.py
   This will guide you with the gitter token generation process.
#. Now you can assign the above generated token to the BOT_TOKEN environment variable.
   ::
     export BOT_TOKEN="your_gitter_token"
#. Also to configure the bot with access to your github and gitlab repositories, you will need personal access tokens.
   The following links may guide you through this:
     https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
     https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html
#. You can also create github organisations and gitlab groups to manage your repositories.
   Under a organisation you can make teams to organize the workforce.
#. After completing the above steps, it is time to setup the remaining environment variables with the above gathered information.
   ::
     export GH_TOKEN="your_github_token"
     export GL_TOKEN="your_gitlab_token"
     export GH_ORG_NAME="your_github_organisation_name"
     export GL_ORG_NAME="your_gitlab_organisation_name"
     export ROOMS="rooms_to_join"
     export BOT_ADMINS="your_gitter_username"
   (**Note:** The admin user account should be different than the bot account.)
#. Hurrah!!! the bot is now ready to be deployed. To run the corobo instance use:
   ::
     errbot

Your corobo instance should now be running. You can chat with the bot by logging in through the admin gitter account and 
searching its username in the contacts section. You can send it commands via chat.
::
  bot_prefix help
  bot_prefix history
  
**Note:** Every time you run a new instance of the bot, it is required to set the environment variables(steps 2 and 7).

To know more about the list of available commands and other features of corobo checkout the other `docs <https://github.com/coala/corobo/tree/master/docs>`_.
