.. _installation:

************
Installation
************

Installing Dungeon Crawl Stone Soup
===================================


Building on Docker
------------------

The docker that is available for download can be built using the dockerfile in `webserver_docker/`::

    cd ~/dcss-ai-wrapper/webserver_docker/

    docker build .


Compiling from Source on Ubuntu
-------------------------------

Note that these instructions were adapted from https://github.com/crawl/crawl/blob/master/crawl-ref/INSTALL.md ::

1. Install system packages:

    sudo apt install build-essential libncursesw5-dev bison flex liblua5.1-0-dev libsqlite3-dev \
    libz-dev pkg-config python3-yaml binutils-gold python-is-python3 python2 make \
    libsdl2-image-dev libsdl2-mixer-dev libsdl2-dev libfreetype6-dev libpng-dev \
    fonts-dejavu-core advancecomp pngcrush git python3.8-venv

2. Clone the repository including submodules::

    git clone --recurse-submodules -j8 https://github.com/crawl/crawl.git crawl/


3. Compile crawl::

    cd crawl/crawl-ref/source/
    make install prefix=/usr/local WEBTILES=y

4. Create an RCS directory that's used to hold player data::

    mkdir /dcss/crawl/crawl-ref/source/rcs/

5.

Old Instructions
----------------
**NOTE** These instructions have not been tested for a while. I have included these instructions in case it helps you to use the terminal version of the game. The current best way to use the API is using the pre-made docker container - see :ref:`quickstart`.

While this API is likely to work with the current dcss master branch, it has been tested with the 23.1 version, which
is the recommended version of crawl to use with this API. We recommend installing a local version of crawl inside this
project's folder.

1. Make sure you have cloned this repository (dcss-ai-wrapper)

2. Grab a copy of the 23.1 version of crawl, by cloning the repo and then resetting to the 23.1 version::

   cd ~/dcss-ai-wrapper/    # assuming this is the directory where you cloned this project - dcss-ai-wrapper)

   git clone https://github.com/crawl/crawl.git

   cd ~/dcss-ai-wrapper/crawl/

   git reset --hard d6e21ad81dcba7f7f8c15336e0e985f070ce85fb

   git submodule update --init

3. Compile crawl with the following flags::

    cd ~/dcss-ai-wrapper/crawl/crawl-ref/source/

    sudo make install prefix=/usr/local/ WEBTILES=y

    __Note for installing on Ubuntu 20.04:__

    If you get an error saying "/usr/bin/env cannot find python", then one possible fix is to the do the following (but beware this may change the default python on your system)

    `sudo ln --symbolic /usr/bin/python2.7 /usr/bin/python`

    Note that Python2.7 is needed to compile crawl.

4. Check that the `crawl/crawl-ref/source/rcs' folder exists, if not create it::

    mkdir crawl/crawl-ref/source/rcs


How to Run a simple agent in the terminal
=========================================

1. Open a new terminal, cd into **dcss-ai-wrapper/** and run:

    First time running the following script may require::

    chmod +x start_crawl_terminal_dungeon.sh

    otherwise

    ./start_crawl_terminal_dungeon.sh

   Note that nothing will happen until an agent connects.

   The terminal that runs this command must be a minimum width and height, so try enlarging the terminal if it doesn't work and you are using a small monitor/screen. (Only try changing the width if the next step fails).

2. Open a new terminal, cd into dcss-ai-wrapper/ and run::

    python3 main.py

3. You should now be able to watch the agent in the terminal as this script is running, as shown in the demo gif at the top of this readme.




