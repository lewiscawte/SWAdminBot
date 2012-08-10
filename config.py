# If true, !log <project> <message>
# If false, !log <message>
enable_projects=False

# Relative DN of where the projects live
project_rdn="ou=projects"

# Log messages to identica
enable_identica=False

# Channels to join
targets=("", "")

# Name of nickserv user
nickserv="nickserv"

# Nick to use when joining
nick=""

# Password to identify with
nick_password=""

# Network to join (ex: irc.freenode.net)
network=""

# Port to use when joining network (ex: 6667)
port=

# Map irc nick to real name
author_map={ "example": "Example User" }

# Map irc nick to title of the user (how the bot addresses the user)
title_map={ "example": "your exampleness" }

# Scheme and wiki hostname to connect to
wiki_connection=("https","example.org")

# Url path
wiki_path="/w/"

# Username of wiki bot user
wiki_user=""

# Password of wiki bot user
wiki_pass=""

# LDAP domain to use, if needed
wiki_domain=""

# Page to write to; if you have projects enabled, the project is
# substituted by using "%s". For example:
#     wiki_page="Nova_Resource:%s/SAL"
# If projects are disabled, this is just a normal page name.
wiki_page=""

# Header depth for dates written
wiki_header_depth=3

# Category the articles should be given
wiki_category=""

# username used for connecting with identica
identica_username=""

# password used for connecting with identica
identica_password=""
