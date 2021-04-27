Setting Up Corobo
=================

The following documentation illustrates the process to
install corobo and interface it with the Gitter 
(or any other backend) API.

Installation
------------
- To install corobo, first you need to install 
  python (version 3.6 or more) and set up a virtual environment. 
  This can be done as follows:
  ::
    python3 -m venv env
    cd env
    source bin/activate ---->  For Linux
    \Scripts\activate   ---->  For Windows

- Next, you can clone the corobo package via git and 
  install the requirements (dependent packages).
  ::
    git clone https://github.com/coala/corobo.git
    cd corobo
    pip install -r requirements.txt

Configuring the backend
-----------------------

- Clone the err-backend-gitter repository in your "corobo" folder.
  ::
    pip3 install git+https://github.com/errbotio/\
    err-backend-gitter@14a428bdd0597b473605264c822855da979bd916  

- To make the bot interact with the Gitter API, you need to login to 
  Gitter using your GitHub, GitLab, Twitter, or any other available 
  account. Remember, it is recommended to use a separate account 
  (other than the admin account) for the bot. The bot will now use 
  this account as its Gitter identity. 

- Also, you need to get your Gitter personal access token. It can be 
  found by logging in `here <https://developer.gitter.im/apps>`_ with 
  the above-created account.

- To configure the bot with access to your 
  `GitHub <https://docs.github.com/en/github \
  /authenticating-to-github/creating-a-personal-access-token>`_ 
  and `GitLab <https://docs.gitlab.com/ \
  ee/user/profile/personal_access_tokens.html>`_
  repositories, you will again need access tokens. 
  The given hyperlinks would guide you with the process.

- You can also create GitHub organizations and GitLab groups to 
  manage your repositories.
  Under any organization, you can make teams to organize the workforce.

- To configure the bot to join rooms, it must first 
  manually enter those rooms via the bot Gitter account. Once this
  is done, the bot would automatically find these rooms (if mentioned
  in the ROOMS env variable) and establish a connection with them.

- After completing the above steps, it is finally time to set up the
  environment variables with the above-gathered information. You
  can create a .env file with the following variables and source it
  before running the bot.
  ::
    BOT_PREFIX="any_name" ----> This will be used to address the bot
                                 along with any command
    BACKEND="Gitter"      ----> Set the backend (other options are
                                 "Text","Zulip",etc.)
    BOT_TOKEN="your_gitter_token"
    GH_TOKEN="your_github_token"
    GL_TOKEN="your_gitlab_token"
    GH_ORG_NAME="your_github_organisation_name"
    GL_ORG_NAME="your_gitlab_organisation_name"
    ROOMS="rooms_to_join"
    BOT_ADMINS="your_gitter_username"
  (**Note:** The admin user account should be different than the
  bot account.)

- Hurrah!!! The bot is now ready to rock. To run the corobo instance, use:
  ::
    errbot
  (**Note:** You can use the --DEBUG flag to run the bot in debug mode.)

Your corobo instance should now be running. You can chat with the bot by
logging in through the admin Gitter account and searching it's username in
the conversations tab.
You can send it commands via chat.
::
  bot_prefix help    ----> Lists the set of commands available with the bot
  bot_prefix history ----> Lists the command history

To know more about the list of available commands and other features 
of corobo, check out the other 
`docs <https://github.com/coala/corobo/tree/master/docs>`_.
