Setting Up Corobo
=================

The following documentation illustrates the process to install corobo and interface it with the gitter(or any other backend) API.

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
     
     
Configuring the backend
------------------------

#. Clone the err-backend-gitter repository in your "corobo" folder.
   ::
     git clone https://github.com/errbotio/errbot@a0f35732484c8c0692e123c48653517cffa21a42
          

#. To make the bot interact with the gitter API you will need a github account(this account can be used to login to gitter) to generate the gitter access token.
   **Remember it is recommended to use a separate account(other than the admin account) for the bot.** 
   Once the account is setup, run the following script.
   ::
     ./oauth.py
   This will guide you with the gitter token generation process.

#. Keep this token safe. It will be used later to set the environment variables.
     
#. Also to configure the bot with access to your github and gitlab repositories, you will need personal access tokens.
   The following links may guide you through this:
     https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
     https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html

#. You can also create github organisations and gitlab groups to manage your repositories.
   Under a organisation, you can make teams to organize the workforce.

#. To configure the bot to join rooms, it is required to first manually join those rooms via the bot gitter account. Once this is done, the bot would automatically find these rooms(if mentioned in ROOMS env variable) and establish connection with them.

#. After completing the above steps, it is time to setup the environment variables with the above gathered information.
   ::
     export BOT_PREFIX="any_name"          ----> This will be used to address the bot along with any command
     export BACKEND="Gitter"               ----> Set the backend(other options are "Text","Zulip",etc.)
     export BOT_TOKEN="your_gitter_token"
     export GH_TOKEN="your_github_token"
     export GL_TOKEN="your_gitlab_token"
     export GH_ORG_NAME="your_github_organisation_name"
     export GL_ORG_NAME="your_gitlab_organisation_name"
     export ROOMS="rooms_to_join"
     export BOT_ADMINS="your_gitter_username"
   (**Note:** The admin user account should be different than the bot account.)

#. Hurrah!!! the bot is now ready to rock. To run the corobo instance use:
   ::
     errbot

   (**Note:** You can use the --DEBUG flag to run the bot in debug mode.)

Your corobo instance should now be running. You can chat with the bot by logging in through the admin gitter account and 
searching its username in the contacts section. You can send it commands via chat.
::
  bot_prefix help    ----> Lists the set of commands available with the bot
  bot_prefix history ----> Lists the command history
  

**Note:** To avoid setting the env variables on every new run of shell instance, you can use a .env file to store the vars and run it before running the bot.
Refer this `link <https://pybit.es/persistent-environment-variables.html>`_ for more info.

To know more about the list of available commands and other features of corobo checkout the other `docs <https://github.com/coala/corobo/tree/master/docs>`_.
